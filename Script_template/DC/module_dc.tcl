

#=======================================================
# Step 1 : Read & elaborate the RTL file list & check
#=======================================================
set TOP_MODULE top
analyze -format verilog [list xxx.v top.v]
elaborate 		$TOP_MODULE -architecture verilog
current_design	$TOP_MODULE

if{[link] == 0} {
	echo "Link with error!";
	exit;
}

if{[check_design] == 0} {
	echo "Check design with error!";
	exit;
}

#=======================================================
# Step 2 : Reset the design first
#=======================================================
reset_design

#=======================================================
# Setp 3 : Write the unmapped ddc file
#=======================================================
uniquify
set uniquify_naming_style "%s %d"
write -f ddc -hierarchy -output ${UNMAPPED_PATH}/{TOP_MODULE}.ddc

#=======================================================
# Step 4.0 : Define clock
#=======================================================
set 	CLK_NAME										clk_i
set 	CLK_PERIOD 										10
set 	CLK_SKEW										[expr SCLK_PERIOD*0.05]
set 	CLK_TRAN										[expr SCLK_PERIOD*0.01]
set 	CLK_SRC_LATENCY									[expr SCLK_PERIOD*0.1 ]
set 	CLK_LATNENCY									[expr SCLK_PERIOD*0.1 ]

create_clock		 	-period $CLK_PERIOD 			[get_ports $CLK_NAME]
set_ideal_network 										[get_ports $CLK_NAME]
set_dont_touch_network									[get_ports $CLK_NAME]
set_driver 				0								[get_ports $CLK_NAME]
set_clock_uncertainty 	-setup	$CLK_SKEW 				[get_clocks $CLK_NAME] 
set_clock_transition 	-max	$CLK_SKEW 				[get_clocks $CLK_NAME] 
set_clock_latency 		-source -max $CLK_SRC_LATENCY 	[get_clocks $CLK_NAME] 
set_clock_latency 		-max	$CLK_LATENCY 			[get_clocks $CLK_NAME] 


#=======================================================
# Step 4.1 : Define Reset
#=======================================================
set 	RST_NAME										rst_1_i
set_ideal_network 										[get_ports $RST_NAME]
set_dont_touch_network									[get_ports $RST_NAME]
set_driver 				0								[get_ports $RST_NAME]

#=======================================================
# Step 5 : Set input delay (Using timing budget)
# 	Assume a week cell to drive the input pins
#=======================================================
set 	LIB_NAME			scx_csm_18ic_ss_lp62v_125c
set 	WIRE_LOAD_MODULE 	csm18_wl10
set 	DRIVE_CELL			INVX1
set 	DRIVE_PIN			Y
set		OPERA_CONDITION		ss_lp62v_125c
set		ALL_IN_EXCEPT_CLK	[remove_from_collection [all_inputs] [get_ports "$CLK_NAME"]]
set 	INPUT_DELAY			[expr $CLK_PERIOD*0.6]
set_input_delay $INPUT_DELAY -clock $CLK1_NAME $ALL_IN_EXCEPT_CLK
# set_input_delay -min 0 -clock $CLK1_NAME $ALL_IN_EXCEPT_CLK
set_driving_cell -lib_cell ${DRIVE_CELL} -pin {$DRIVE_PIN} $ALL_IN_EXCEPT_CLK


#=======================================================
# Step 6 : Set output delay
#=======================================================
set		OUTPUT_DELAY		[expr $CLK_PERIOD*0.6]
set		MAX_LOAD			[expr [load of $LIB_NAME/INVX8/A] * 10]
set_output_delay $OUTPUT_DELAY -clock $CLK_NAME [all_outputs]
set_load 					[expr $MAX_LOAD * 3] [all_outputs]
set_isolate_ports -type buffer 					[all_outputs]


#=======================================================
# Step 7 : Set max delay for comb logic
#=======================================================
# set_input_delay [expr $CLK_PERIOD*0.1]	-clock $CLK1_NAME -add_delay [get_ports a_i]
# set_output_delay [expr $CLK_PERIOD*0.1]	-clock $CLK1_NAME -add_delay [get_ports y_o]

#=======================================================
# Step 8 : Set operating condition & wire load model
#=======================================================
set_operating_conditions -max $OPERA_CONDITION	\
						 -max_library $LIB_NAME
						 
set auto_wire_load_selection false

set_wire_load_mode top

set_wire_load_model		-name $WIRE_LOAD_MODEL	\
						-library	$LIB_NAME

#=======================================================
# Step 9 : Set area constraint (Let's DC try its best)
#=======================================================
set_max_area 0


#=======================================================
# Step 10 : Set DRC constraint
#=======================================================
set MAX_CAPACIATNCE [expr [load of $LIB_NAME/NAND4x2/Y] *0.5]
set_max_capacitance $MAX_CAPACIATNCE $ALL_IN_EXCEPT_CLK


#=======================================================
# Step 11 : Set group path
# Avoid getting stack on one path
#=======================================================
group_path -name $CLK_NAME 	-weight 5		\
							-critical_range	[expr $CLK_PERIOD * 0.1]

group_path -name INPUTS 	-from [all_inputs]		\
							-critical_range	[expr $CLK_PERIOD * 0.1]
					
group_path -name OUTPUTS 	-to [all_outputs]		\
							-critical_range	[expr $CLK_PERIOD * 0.1]
						   
group_path -name COMB 		-from [all_inputs]		\
							-to   [all_outputs]		\
							-critical_range	[expr $CLK_PERIOD * 0.1]
							
report_path_group
						   
#=======================================================
# Step 12 : Elimate the multiple-port inter-conncect &
# 			define name style
#=======================================================

set_app_var		verilogout_no_tri					true
set_app_var		verilogout_show_unconnected_pins	true
set_app_var		bus_naming_style					{%s[%d]}
simplify_constants -boundary_optimization
# set_fix_multiple_port_nets -all - buffer_constants


#=======================================================
# Step 13 : Timing exception define
#=======================================================
# set_false_path -from [get_clocks clk1_i] -to [get_clocks clk2_i]
# set ALL_CLOCKS [all_clocks]
# foreach_in_collection CUR_CLK_SALL_CLOCKS{
	# set OTHER_CLKS [remove_from_collection [all_clocks] $CUR_CLK]
	# set_false_path -from $CUR_CLK $OTHER_CLKS
# }

set_false_path -from [get_clocks $CLK1_NAME] -to [get_clocks $CLK2_NAME]
set_false_path -from [get_clocks $CLK2_NAME] -to [get_clocks $CLK1_NAME]


# set_disable_timing TOP/U1 -from a -to y
# set_case_analysis 0 [get_ports sel_i]

# set multicycle_path -setup 	6 -from FFA/CP -through ADD/out -to FFB/D
# set multicycle_path -hold 	5 -from FFA/CP -through ADD/out -to FFB/D
# set multicycle_path -setup 	2 -to [get_pins q_lac*/D]
# set multicycle_path -hold 	1 -to [get_pins q_lac*/D]

#=======================================================
# Step 14 : Compile file
#=======================================================
# ungroup -fatten -all

# lst-pass compile
complie -map_effort high -area_effort medium
# compile -map_effort medium -area_effort high -boundary_optimization

# simplify_constants - boundary_optimization
# set_fix_multiple_port_nets -all buffer_constants

# compile -map_effort high -area_effort high -incremental_mapping -scan

# 2nd-pass compile
# compile -map_effort high -area_effort high -boundary_optimization -incremental_mapping
# compile_ultra -incr


#=======================================================
# Step 15 : Write post-process files
#=======================================================
change_names -rules verilog -hierarchy
remove_unconnected [get_cells -hier *] -blast_buses

# Write the mapped files
write -f ddc 		-hierarchy -output 	$MAPPED_PATH/${TOP_MODULE}.ddc
write -f verilog 	-hierarchy -output 	$MAPPED_PATH/${TOP_MODULE}.v
write_sdc -version 1.7 					$MAPPED_PATH/${TOP_MODULE}.sdc
write_sdf -version 2.1					$MAPPED_PATH/${TOP_MODULE}.sdf

#=======================================================
# Step 16 : Generate report files
#=======================================================
# Get report file
# redirect -tee -file ${REPORT_PATH}/check_design.txt 		{check_design						}
# redirect -tee -file ${REPORT_PATH}/check_timing.txt 		{check_timing						}
# redirect -tee -file ${REPORT_PATH}/report_constraint.txt 	{report_constraint -all_violators	}
# redirect -tee -file ${REPORT_PATH}/check_setup.txt 		{report_timing -delay_type max		}
# redirect -tee -file ${REPORT_PATH}/check_hold.txt 		{report_timing -delay_type min		}
# redirect -tee -file ${REPORT_PATH}/check_area.txt 		{report_area						}

#=======================================================
# Step 17 : At the end
#=======================================================


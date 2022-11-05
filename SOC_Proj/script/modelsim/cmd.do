## part 1: new lib
vlib work
vmap work work

## part 2: load design
vlog -sv -novopt -incr -work work "../lib/prim_sim.v"
vlog -sv -novopt +incdir+../tb -work work "../tb/*.v"
vlog -sv -novopt +incdir+../src/define/ -incr -work work "../module/*.v"


## part 3: sim design
vsim -L work -novopt work.tb

## part 4: add signals
add wave -group "tb" {sim:/tb/*}
add wave -group "adc_event_ctrl" {sim:/tb/adc_event_ctrl_inst/*}

## part 5: show ui 
view wave
view structure
view signals

## part 6: run 
run 10us

## quit sim
# quit -f


# source the module_dc.tcl and print the process to terminal & compile.log
redirect -tee -file ${WORK_PATH}/compile.log {source -echo -verbose module_dc.tcl}
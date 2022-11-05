wire      [ 2 : 0 ] 	 d              ; 
wire      [ 2 : 0 ] 	 q              ; 


 /*############# 	 top1 module start 	 ###############*/ 

top1  top1_inst ( 
	 .clk             ( clk             	), 
	 .rst_n           ( rst_n           	), 
	 .d               ( d               	), 
	 .q               ( q               	) 
); 

 /*############# 	 top1 module end 	 ###############*/ 

 /*############# 	 top2 module start 	 ###############*/ 

top2  top2_inst ( 
	 .clk             ( clk             	), 
	 .rst_n           ( rst_n           	), 
	 .d               ( q               	), 
	 .q               ( d               	) 
); 

 /*############# 	 top2 module end 	 ###############*/ 

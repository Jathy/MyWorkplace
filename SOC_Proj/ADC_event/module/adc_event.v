/****************************/
/*Author:XXX*/
/****************************/

module adc_even(
    clk,
    rstn,
    
    adc_data,
    adc_event,
    adc_event_seq,
    adc_event_intr
);

// --- parameter ---//
// --- Voltage parameter
    parameter   VOLTAGE_LOW      = 10'd1;
    parameter   VOLTAGE_LOW_ON   = 10'd2;
    parameter   VOLTAGE_LOW_OFF  = 10'd3;
    parameter   VOLTAGE_HIGH_ON  = 10'd4;
    parameter   VOLTAGE_HIGH_OFF = 10'd5;

// --- State 
    localparam  STATE0 = 4‘h0;
    localparam  STATE1 = 4‘h1;
    localparam  STATE2 = 4‘h2;
    localparam  STATE3 = 4‘h3;
    localparam  STATE4 = 4‘h4;
    localparam  STATE5 = 4‘h5;
    localparam  STATE6 = 4‘h6;
    localparam  STATE7 = 4‘h7;
    localparam  STATE8 = 4‘h8;
    localparam  STATE9 = 4‘h9;
    localparam  STATE10 = 4‘ha;

// --- I/O interface ---//
    input           clk;
    input           rstn;
    input [9:0]     adc_data;

    output [9:0]    adc_event;
    output [5:0]    adc_event_seq;
    output          adc_event_intr;

// --- Internal interface
    reg [3:0] nstate;
    reg [3:0] cstate;

    reg [9:0] adc_date_pre;

// --- main code ---//
    always @(posedge clk or negedge rstn) begin
        if(!rstn) begin
            cstate <= STATE0;
        end
        else begin
            cstate <= nstate;
        end
    end

    always @(*) begin
        nstate = cstate;
        case(cstate)
            STATE0: begin
                if((adc_data > adc_data_pre) && (adc_data >= VOLTAGE_LOW) && (adc_data < VOLTAGE_LOW_ON))
                    nstate = STATE1;
                else if((adc_data > adc_data_pre) && (adc_data >= VOLTAGE_LOW_ON)) 
                    nstate = STATE2;
                else 
                    nstate = STATE0;
            end
            STATE1: begin
                if((adc_data > adc_data_pre) && (adc_data >= VOLTAGE_LOW_ON ) && (adc_data < VOLTAGE_HIGH_OFF))
                    nstate = STATE2;
                else if((adc_data > adc_data_pre) && (adc_data >= VOLTAGE_HIGH_OFF))
                    nstate = STATE3;
                else 
                    nstate = STATE1;
            end
            STATE2: begin
                if((adc_data > adc_data_pre) && (adc_data >= VOLTAGE_HIGH_OFF) && (adc_data < VOLTAGE_HIGH))
                    nstate = STATE3;
                else if((adc_data > adc_data_pre) && (adc_data >= VOLTAGE_HIGH))
                    nstate = STATE4;
                else if((adc_data < adc_data_pre) && (adc_data <= VOLTAGE_LOW_OFF) && (adc_data > VOLTAGE_LOW))
                    nstate = STATE7;
                else if((adc_data < adc_data_pre) && (adc_data <= VOLTAGE_LOW))
                    nstate = STATE8;
                else 
                    nstate = STATE2;
            end
            STATE3: begin
                if((adc_data > adc_data_pre) && (adc_data >= VOLTAGE_HIGH)) 
                    nstate = STATE4;
                else if((adc_data < adc_data_pre) && (adc_data <= VOLTAGE_HIGH_ON) && (adc_data > VOLTAGE_LOW_OFF))
                    nstate = STATE6;
                else if((adc_data < adc_data_pre) && (adc_data <= VOLTAGE_LOW_OFF))
                    nstate = STATE7;
                else 
                    nstate = STATE3;
            end
            STATE4: begin

            end
            STATE5: begin

            end
            STATE6: begin

            end
            STATE7: begin

            end
            STATE8: begin

            end
            STATE9: begin

            end
            STATE10: begin

            end
            default: begin

            end
        endcase
    end

    always @(posedge clk or negedge rstn) begin
        if(!rstn) begin
            adc_data_pre <= 0;
        end
        else begin
            adc_data_pre <= adc_data;
        end
    end

    assign adc_event_intr = (nstate == cstate)? 1'b0:1'b1;
    



endmodule

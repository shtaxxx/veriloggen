from __future__ import absolute_import
from __future__ import print_function
import veriloggen
import thread_to_multibank_ram

expected_verilog = """
module test;

  reg CLK;
  reg RST;
  wire [32-1:0] myaxi_awaddr;
  wire [8-1:0] myaxi_awlen;
  wire myaxi_awvalid;
  reg myaxi_awready;
  wire [128-1:0] myaxi_wdata;
  wire [16-1:0] myaxi_wstrb;
  wire myaxi_wlast;
  wire myaxi_wvalid;
  reg myaxi_wready;
  wire [32-1:0] myaxi_araddr;
  wire [8-1:0] myaxi_arlen;
  wire myaxi_arvalid;
  reg myaxi_arready;
  reg [128-1:0] myaxi_rdata;
  reg myaxi_rlast;
  reg myaxi_rvalid;
  wire myaxi_rready;
  wire [32-1:0] memory_awaddr;
  wire [8-1:0] memory_awlen;
  wire memory_awvalid;
  reg memory_awready;
  wire [128-1:0] memory_wdata;
  wire [16-1:0] memory_wstrb;
  wire memory_wlast;
  wire memory_wvalid;
  reg memory_wready;
  wire [32-1:0] memory_araddr;
  wire [8-1:0] memory_arlen;
  wire memory_arvalid;
  reg memory_arready;
  reg [128-1:0] memory_rdata;
  reg memory_rlast;
  reg memory_rvalid;
  wire memory_rready;
  reg [8-1:0] _memory_mem [0:2**20-1];

  initial begin
    $readmemh("_memory_memimg_.out", _memory_mem);
  end

  reg [32-1:0] _memory_fsm;
  localparam _memory_fsm_init = 0;
  reg [33-1:0] _write_count;
  reg [32-1:0] _write_addr;
  reg [33-1:0] _read_count;
  reg [32-1:0] _read_addr;
  reg [33-1:0] _sleep_count;
  reg [32-1:0] _d1__memory_fsm;
  reg __memory_fsm_cond_100_0_1;
  reg __memory_fsm_cond_200_1_1;
  reg __memory_fsm_cond_211_2_1;
  assign memory_awaddr = myaxi_awaddr;
  assign memory_awlen = myaxi_awlen;
  assign memory_awvalid = myaxi_awvalid;
  wire _tmp_0;
  assign _tmp_0 = memory_awready;

  always @(*) begin
    myaxi_awready = _tmp_0;
  end

  assign memory_wdata = myaxi_wdata;
  assign memory_wstrb = myaxi_wstrb;
  assign memory_wlast = myaxi_wlast;
  assign memory_wvalid = myaxi_wvalid;
  wire _tmp_1;
  assign _tmp_1 = memory_wready;

  always @(*) begin
    myaxi_wready = _tmp_1;
  end

  assign memory_araddr = myaxi_araddr;
  assign memory_arlen = myaxi_arlen;
  assign memory_arvalid = myaxi_arvalid;
  wire _tmp_2;
  assign _tmp_2 = memory_arready;

  always @(*) begin
    myaxi_arready = _tmp_2;
  end


  always @(*) begin
    myaxi_rdata <= memory_rdata;
  end

  wire _tmp_3;
  assign _tmp_3 = memory_rlast;

  always @(*) begin
    myaxi_rlast = _tmp_3;
  end

  wire _tmp_4;
  assign _tmp_4 = memory_rvalid;

  always @(*) begin
    myaxi_rvalid = _tmp_4;
  end

  assign memory_rready = myaxi_rready;

  blinkled
  uut
  (
    .CLK(CLK),
    .RST(RST),
    .myaxi_awaddr(myaxi_awaddr),
    .myaxi_awlen(myaxi_awlen),
    .myaxi_awvalid(myaxi_awvalid),
    .myaxi_awready(myaxi_awready),
    .myaxi_wdata(myaxi_wdata),
    .myaxi_wstrb(myaxi_wstrb),
    .myaxi_wlast(myaxi_wlast),
    .myaxi_wvalid(myaxi_wvalid),
    .myaxi_wready(myaxi_wready),
    .myaxi_araddr(myaxi_araddr),
    .myaxi_arlen(myaxi_arlen),
    .myaxi_arvalid(myaxi_arvalid),
    .myaxi_arready(myaxi_arready),
    .myaxi_rdata(myaxi_rdata),
    .myaxi_rlast(myaxi_rlast),
    .myaxi_rvalid(myaxi_rvalid),
    .myaxi_rready(myaxi_rready)
  );


  initial begin
    $dumpfile("uut.vcd");
    $dumpvars(0, uut);
  end


  initial begin
    CLK = 0;
    forever begin
      #5 CLK = !CLK;
    end
  end


  initial begin
    RST = 0;
    memory_awready = 0;
    memory_wready = 0;
    memory_arready = 0;
    memory_rdata = 0;
    memory_rlast = 0;
    memory_rvalid = 0;
    _memory_fsm = _memory_fsm_init;
    _write_count = 0;
    _write_addr = 0;
    _read_count = 0;
    _read_addr = 0;
    _sleep_count = 0;
    _d1__memory_fsm = _memory_fsm_init;
    __memory_fsm_cond_100_0_1 = 0;
    __memory_fsm_cond_200_1_1 = 0;
    __memory_fsm_cond_211_2_1 = 0;
    #100;
    RST = 1;
    #100;
    RST = 0;
    #100000;
    $finish;
  end

  localparam _memory_fsm_200 = 200;
  localparam _memory_fsm_201 = 201;
  localparam _memory_fsm_202 = 202;
  localparam _memory_fsm_203 = 203;
  localparam _memory_fsm_204 = 204;
  localparam _memory_fsm_205 = 205;
  localparam _memory_fsm_206 = 206;
  localparam _memory_fsm_207 = 207;
  localparam _memory_fsm_208 = 208;
  localparam _memory_fsm_209 = 209;
  localparam _memory_fsm_210 = 210;
  localparam _memory_fsm_211 = 211;
  localparam _memory_fsm_100 = 100;
  localparam _memory_fsm_101 = 101;
  localparam _memory_fsm_102 = 102;
  localparam _memory_fsm_103 = 103;
  localparam _memory_fsm_104 = 104;
  localparam _memory_fsm_105 = 105;
  localparam _memory_fsm_106 = 106;
  localparam _memory_fsm_107 = 107;
  localparam _memory_fsm_108 = 108;
  localparam _memory_fsm_109 = 109;
  localparam _memory_fsm_110 = 110;
  localparam _memory_fsm_111 = 111;
  localparam _memory_fsm_112 = 112;

  always @(posedge CLK) begin
    if(RST) begin
      _memory_fsm <= _memory_fsm_init;
      _d1__memory_fsm <= _memory_fsm_init;
      memory_awready <= 0;
      _write_addr <= 0;
      _write_count <= 0;
      __memory_fsm_cond_100_0_1 <= 0;
      memory_wready <= 0;
      memory_arready <= 0;
      _read_addr <= 0;
      _read_count <= 0;
      __memory_fsm_cond_200_1_1 <= 0;
      memory_rdata[7:0] <= (0 >> 0) & { 8{ 1'd1 } };
      memory_rdata[15:8] <= (0 >> 8) & { 8{ 1'd1 } };
      memory_rdata[23:16] <= (0 >> 16) & { 8{ 1'd1 } };
      memory_rdata[31:24] <= (0 >> 24) & { 8{ 1'd1 } };
      memory_rdata[39:32] <= (0 >> 32) & { 8{ 1'd1 } };
      memory_rdata[47:40] <= (0 >> 40) & { 8{ 1'd1 } };
      memory_rdata[55:48] <= (0 >> 48) & { 8{ 1'd1 } };
      memory_rdata[63:56] <= (0 >> 56) & { 8{ 1'd1 } };
      memory_rdata[71:64] <= (0 >> 64) & { 8{ 1'd1 } };
      memory_rdata[79:72] <= (0 >> 72) & { 8{ 1'd1 } };
      memory_rdata[87:80] <= (0 >> 80) & { 8{ 1'd1 } };
      memory_rdata[95:88] <= (0 >> 88) & { 8{ 1'd1 } };
      memory_rdata[103:96] <= (0 >> 96) & { 8{ 1'd1 } };
      memory_rdata[111:104] <= (0 >> 104) & { 8{ 1'd1 } };
      memory_rdata[119:112] <= (0 >> 112) & { 8{ 1'd1 } };
      memory_rdata[127:120] <= (0 >> 120) & { 8{ 1'd1 } };
      memory_rvalid <= 0;
      memory_rlast <= 0;
      __memory_fsm_cond_211_2_1 <= 0;
      memory_rdata <= 0;
      _sleep_count <= 0;
    end else begin
      _sleep_count <= _sleep_count + 1;
      if(_sleep_count == 3) begin
        _sleep_count <= 0;
      end 
      _d1__memory_fsm <= _memory_fsm;
      case(_d1__memory_fsm)
        _memory_fsm_100: begin
          if(__memory_fsm_cond_100_0_1) begin
            memory_awready <= 0;
          end 
        end
        _memory_fsm_200: begin
          if(__memory_fsm_cond_200_1_1) begin
            memory_arready <= 0;
          end 
        end
        _memory_fsm_211: begin
          if(__memory_fsm_cond_211_2_1) begin
            memory_rvalid <= 0;
            memory_rlast <= 0;
          end 
        end
      endcase
      case(_memory_fsm)
        _memory_fsm_init: begin
          if(memory_awvalid) begin
            _memory_fsm <= _memory_fsm_100;
          end 
          if(memory_arvalid) begin
            _memory_fsm <= _memory_fsm_200;
          end 
        end
        _memory_fsm_100: begin
          if(memory_awvalid) begin
            memory_awready <= 1;
            _write_addr <= memory_awaddr;
            _write_count <= memory_awlen + 1;
          end 
          __memory_fsm_cond_100_0_1 <= 1;
          if(!memory_awvalid) begin
            _memory_fsm <= _memory_fsm_init;
          end 
          if(memory_awvalid) begin
            _memory_fsm <= _memory_fsm_101;
          end 
        end
        _memory_fsm_101: begin
          _memory_fsm <= _memory_fsm_102;
        end
        _memory_fsm_102: begin
          _memory_fsm <= _memory_fsm_103;
        end
        _memory_fsm_103: begin
          _memory_fsm <= _memory_fsm_104;
        end
        _memory_fsm_104: begin
          _memory_fsm <= _memory_fsm_105;
        end
        _memory_fsm_105: begin
          _memory_fsm <= _memory_fsm_106;
        end
        _memory_fsm_106: begin
          _memory_fsm <= _memory_fsm_107;
        end
        _memory_fsm_107: begin
          _memory_fsm <= _memory_fsm_108;
        end
        _memory_fsm_108: begin
          _memory_fsm <= _memory_fsm_109;
        end
        _memory_fsm_109: begin
          _memory_fsm <= _memory_fsm_110;
        end
        _memory_fsm_110: begin
          _memory_fsm <= _memory_fsm_111;
        end
        _memory_fsm_111: begin
          memory_wready <= 1;
          _memory_fsm <= _memory_fsm_112;
        end
        _memory_fsm_112: begin
          if(memory_wvalid && memory_wstrb[0]) begin
            _memory_mem[_write_addr + 0] <= memory_wdata[7:0];
          end 
          if(memory_wvalid && memory_wstrb[1]) begin
            _memory_mem[_write_addr + 1] <= memory_wdata[15:8];
          end 
          if(memory_wvalid && memory_wstrb[2]) begin
            _memory_mem[_write_addr + 2] <= memory_wdata[23:16];
          end 
          if(memory_wvalid && memory_wstrb[3]) begin
            _memory_mem[_write_addr + 3] <= memory_wdata[31:24];
          end 
          if(memory_wvalid && memory_wstrb[4]) begin
            _memory_mem[_write_addr + 4] <= memory_wdata[39:32];
          end 
          if(memory_wvalid && memory_wstrb[5]) begin
            _memory_mem[_write_addr + 5] <= memory_wdata[47:40];
          end 
          if(memory_wvalid && memory_wstrb[6]) begin
            _memory_mem[_write_addr + 6] <= memory_wdata[55:48];
          end 
          if(memory_wvalid && memory_wstrb[7]) begin
            _memory_mem[_write_addr + 7] <= memory_wdata[63:56];
          end 
          if(memory_wvalid && memory_wstrb[8]) begin
            _memory_mem[_write_addr + 8] <= memory_wdata[71:64];
          end 
          if(memory_wvalid && memory_wstrb[9]) begin
            _memory_mem[_write_addr + 9] <= memory_wdata[79:72];
          end 
          if(memory_wvalid && memory_wstrb[10]) begin
            _memory_mem[_write_addr + 10] <= memory_wdata[87:80];
          end 
          if(memory_wvalid && memory_wstrb[11]) begin
            _memory_mem[_write_addr + 11] <= memory_wdata[95:88];
          end 
          if(memory_wvalid && memory_wstrb[12]) begin
            _memory_mem[_write_addr + 12] <= memory_wdata[103:96];
          end 
          if(memory_wvalid && memory_wstrb[13]) begin
            _memory_mem[_write_addr + 13] <= memory_wdata[111:104];
          end 
          if(memory_wvalid && memory_wstrb[14]) begin
            _memory_mem[_write_addr + 14] <= memory_wdata[119:112];
          end 
          if(memory_wvalid && memory_wstrb[15]) begin
            _memory_mem[_write_addr + 15] <= memory_wdata[127:120];
          end 
          if(memory_wvalid && memory_wready) begin
            _write_addr <= _write_addr + 16;
            _write_count <= _write_count - 1;
          end 
          if(_sleep_count == 3) begin
            memory_wready <= 0;
          end else begin
            memory_wready <= 1;
          end
          if(memory_wvalid && memory_wready && (_write_count == 1)) begin
            memory_wready <= 0;
          end 
          if(memory_wvalid && memory_wready && (_write_count == 1)) begin
            _memory_fsm <= _memory_fsm_init;
          end 
        end
        _memory_fsm_200: begin
          if(memory_arvalid) begin
            memory_arready <= 1;
            _read_addr <= memory_araddr;
            _read_count <= memory_arlen + 1;
          end 
          __memory_fsm_cond_200_1_1 <= 1;
          if(!memory_arvalid) begin
            _memory_fsm <= _memory_fsm_init;
          end 
          if(memory_arvalid) begin
            _memory_fsm <= _memory_fsm_201;
          end 
        end
        _memory_fsm_201: begin
          _memory_fsm <= _memory_fsm_202;
        end
        _memory_fsm_202: begin
          _memory_fsm <= _memory_fsm_203;
        end
        _memory_fsm_203: begin
          _memory_fsm <= _memory_fsm_204;
        end
        _memory_fsm_204: begin
          _memory_fsm <= _memory_fsm_205;
        end
        _memory_fsm_205: begin
          _memory_fsm <= _memory_fsm_206;
        end
        _memory_fsm_206: begin
          _memory_fsm <= _memory_fsm_207;
        end
        _memory_fsm_207: begin
          _memory_fsm <= _memory_fsm_208;
        end
        _memory_fsm_208: begin
          _memory_fsm <= _memory_fsm_209;
        end
        _memory_fsm_209: begin
          _memory_fsm <= _memory_fsm_210;
        end
        _memory_fsm_210: begin
          _memory_fsm <= _memory_fsm_211;
        end
        _memory_fsm_211: begin
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[7:0] <= _memory_mem[_read_addr + 0];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[15:8] <= _memory_mem[_read_addr + 1];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[23:16] <= _memory_mem[_read_addr + 2];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[31:24] <= _memory_mem[_read_addr + 3];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[39:32] <= _memory_mem[_read_addr + 4];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[47:40] <= _memory_mem[_read_addr + 5];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[55:48] <= _memory_mem[_read_addr + 6];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[63:56] <= _memory_mem[_read_addr + 7];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[71:64] <= _memory_mem[_read_addr + 8];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[79:72] <= _memory_mem[_read_addr + 9];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[87:80] <= _memory_mem[_read_addr + 10];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[95:88] <= _memory_mem[_read_addr + 11];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[103:96] <= _memory_mem[_read_addr + 12];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[111:104] <= _memory_mem[_read_addr + 13];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[119:112] <= _memory_mem[_read_addr + 14];
          end 
          if(memory_rready | !memory_rvalid) begin
            memory_rdata[127:120] <= _memory_mem[_read_addr + 15];
          end 
          if((_sleep_count < 3) && (_read_count > 0) && memory_rready | !memory_rvalid) begin
            memory_rvalid <= 1;
            _read_addr <= _read_addr + 16;
            _read_count <= _read_count - 1;
          end 
          if((_sleep_count < 3) && (_read_count == 1) && memory_rready | !memory_rvalid) begin
            memory_rlast <= 1;
          end 
          __memory_fsm_cond_211_2_1 <= 1;
          if(memory_rvalid && !memory_rready) begin
            memory_rvalid <= memory_rvalid;
            memory_rdata <= memory_rdata;
            memory_rlast <= memory_rlast;
          end 
          if(memory_rvalid && memory_rready && (_read_count == 0)) begin
            _memory_fsm <= _memory_fsm_init;
          end 
        end
      endcase
    end
  end


endmodule



module blinkled
(
  input CLK,
  input RST,
  output reg [32-1:0] myaxi_awaddr,
  output reg [8-1:0] myaxi_awlen,
  output reg myaxi_awvalid,
  input myaxi_awready,
  output reg [128-1:0] myaxi_wdata,
  output reg [16-1:0] myaxi_wstrb,
  output reg myaxi_wlast,
  output reg myaxi_wvalid,
  input myaxi_wready,
  output reg [32-1:0] myaxi_araddr,
  output reg [8-1:0] myaxi_arlen,
  output reg myaxi_arvalid,
  input myaxi_arready,
  input [128-1:0] myaxi_rdata,
  input myaxi_rlast,
  input myaxi_rvalid,
  output myaxi_rready
);

  reg _myaxi_read_start;
  reg [8-1:0] _myaxi_read_op_sel;
  reg [32-1:0] _myaxi_read_local_addr;
  reg [32-1:0] _myaxi_read_global_addr;
  reg [33-1:0] _myaxi_read_size;
  reg [32-1:0] _myaxi_read_local_stride;
  reg _myaxi_read_idle;
  reg _myaxi_write_start;
  reg [8-1:0] _myaxi_write_op_sel;
  reg [32-1:0] _myaxi_write_local_addr;
  reg [32-1:0] _myaxi_write_global_addr;
  reg [33-1:0] _myaxi_write_size;
  reg [32-1:0] _myaxi_write_local_stride;
  reg _myaxi_write_idle;
  wire _myaxi_write_data_done;
  reg [10-1:0] myram_0_0_addr;
  wire [32-1:0] myram_0_0_rdata;
  reg [32-1:0] myram_0_0_wdata;
  reg myram_0_0_wenable;

  myram_0
  inst_myram_0
  (
    .CLK(CLK),
    .myram_0_0_addr(myram_0_0_addr),
    .myram_0_0_rdata(myram_0_0_rdata),
    .myram_0_0_wdata(myram_0_0_wdata),
    .myram_0_0_wenable(myram_0_0_wenable)
  );

  reg [10-1:0] myram_1_0_addr;
  wire [32-1:0] myram_1_0_rdata;
  reg [32-1:0] myram_1_0_wdata;
  reg myram_1_0_wenable;

  myram_1
  inst_myram_1
  (
    .CLK(CLK),
    .myram_1_0_addr(myram_1_0_addr),
    .myram_1_0_rdata(myram_1_0_rdata),
    .myram_1_0_wdata(myram_1_0_wdata),
    .myram_1_0_wenable(myram_1_0_wenable)
  );

  reg [10-1:0] myram_2_0_addr;
  wire [32-1:0] myram_2_0_rdata;
  reg [32-1:0] myram_2_0_wdata;
  reg myram_2_0_wenable;

  myram_2
  inst_myram_2
  (
    .CLK(CLK),
    .myram_2_0_addr(myram_2_0_addr),
    .myram_2_0_rdata(myram_2_0_rdata),
    .myram_2_0_wdata(myram_2_0_wdata),
    .myram_2_0_wenable(myram_2_0_wenable)
  );

  reg [10-1:0] myram_3_0_addr;
  wire [32-1:0] myram_3_0_rdata;
  reg [32-1:0] myram_3_0_wdata;
  reg myram_3_0_wenable;

  myram_3
  inst_myram_3
  (
    .CLK(CLK),
    .myram_3_0_addr(myram_3_0_addr),
    .myram_3_0_rdata(myram_3_0_rdata),
    .myram_3_0_wdata(myram_3_0_wdata),
    .myram_3_0_wenable(myram_3_0_wenable)
  );

  reg _tmp_0;
  reg [32-1:0] th_blink;
  localparam th_blink_init = 0;
  reg signed [32-1:0] _th_blink_size_0;
  reg signed [32-1:0] _th_blink_i_1;
  reg signed [32-1:0] _th_blink_offset_2;
  reg signed [32-1:0] _th_blink_size_3;
  reg signed [32-1:0] _th_blink_offset_4;
  reg signed [32-1:0] _th_blink_bank_5;
  reg signed [32-1:0] _th_blink_i_6;
  reg signed [32-1:0] _th_blink_wdata_7;
  reg _myram_0_cond_0_1;
  reg _myram_1_cond_0_1;
  reg _myram_2_cond_0_1;
  reg _myram_3_cond_0_1;
  reg signed [32-1:0] _th_blink_laddr_8;
  reg signed [32-1:0] _th_blink_gaddr_9;
  reg axim_flag_1;
  reg [32-1:0] _d1_th_blink;
  reg _th_blink_cond_17_0_1;
  reg _myaxi_myram_0_write_start;
  reg [8-1:0] _myaxi_myram_0_write_op_sel;
  reg [32-1:0] _myaxi_myram_0_write_local_addr;
  reg [32-1:0] _myaxi_myram_0_write_global_addr;
  reg [33-1:0] _myaxi_myram_0_write_size;
  reg [32-1:0] _myaxi_myram_0_write_local_stride;
  reg [32-1:0] _myaxi_write_fsm;
  localparam _myaxi_write_fsm_init = 0;
  reg [32-1:0] _myaxi_write_cur_global_addr;
  reg [33-1:0] _myaxi_write_cur_size;
  reg [33-1:0] _myaxi_write_rest_size;
  reg _tmp_2;
  reg _tmp_3;
  wire _tmp_4;
  wire _tmp_5;
  assign _tmp_5 = 1;
  localparam _tmp_6 = 1;
  wire [_tmp_6-1:0] _tmp_7;
  assign _tmp_7 = (_tmp_4 || !_tmp_2) && (_tmp_5 || !_tmp_3);
  reg [_tmp_6-1:0] __tmp_7_1;
  wire signed [32-1:0] _tmp_8;
  reg signed [32-1:0] __tmp_8_1;
  assign _tmp_8 = (__tmp_7_1)? myram_0_0_rdata : __tmp_8_1;
  reg _tmp_9;
  reg _tmp_10;
  reg _tmp_11;
  reg _tmp_12;
  reg [34-1:0] _tmp_13;
  reg _tmp_14;
  reg _tmp_15;
  wire _tmp_16;
  wire _tmp_17;
  assign _tmp_17 = 1;
  localparam _tmp_18 = 1;
  wire [_tmp_18-1:0] _tmp_19;
  assign _tmp_19 = (_tmp_16 || !_tmp_14) && (_tmp_17 || !_tmp_15);
  reg [_tmp_18-1:0] __tmp_19_1;
  wire signed [32-1:0] _tmp_20;
  reg signed [32-1:0] __tmp_20_1;
  assign _tmp_20 = (__tmp_19_1)? myram_1_0_rdata : __tmp_20_1;
  reg _tmp_21;
  reg _tmp_22;
  reg _tmp_23;
  reg _tmp_24;
  reg [34-1:0] _tmp_25;
  reg _tmp_26;
  reg _tmp_27;
  wire _tmp_28;
  wire _tmp_29;
  assign _tmp_29 = 1;
  localparam _tmp_30 = 1;
  wire [_tmp_30-1:0] _tmp_31;
  assign _tmp_31 = (_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27);
  reg [_tmp_30-1:0] __tmp_31_1;
  wire signed [32-1:0] _tmp_32;
  reg signed [32-1:0] __tmp_32_1;
  assign _tmp_32 = (__tmp_31_1)? myram_2_0_rdata : __tmp_32_1;
  reg _tmp_33;
  reg _tmp_34;
  reg _tmp_35;
  reg _tmp_36;
  reg [34-1:0] _tmp_37;
  reg _tmp_38;
  reg _tmp_39;
  wire _tmp_40;
  wire _tmp_41;
  assign _tmp_41 = 1;
  localparam _tmp_42 = 1;
  wire [_tmp_42-1:0] _tmp_43;
  assign _tmp_43 = (_tmp_40 || !_tmp_38) && (_tmp_41 || !_tmp_39);
  reg [_tmp_42-1:0] __tmp_43_1;
  wire signed [32-1:0] _tmp_44;
  reg signed [32-1:0] __tmp_44_1;
  assign _tmp_44 = (__tmp_43_1)? myram_3_0_rdata : __tmp_44_1;
  reg _tmp_45;
  reg _tmp_46;
  reg _tmp_47;
  reg _tmp_48;
  reg [34-1:0] _tmp_49;
  reg [9-1:0] _tmp_50;
  reg _myaxi_cond_0_1;
  reg _tmp_51;
  wire [128-1:0] _cat_data_52;
  wire _cat_valid_52;
  wire _cat_ready_52;
  assign _cat_ready_52 = (_myaxi_write_fsm == 3) && (_myaxi_write_op_sel == 1) && ((_tmp_50 > 0) && (myaxi_wready || !myaxi_wvalid));
  reg _myaxi_cond_1_1;
  assign _myaxi_write_data_done = (_tmp_51 && myaxi_wvalid && myaxi_wready)? 1 : 0;
  reg axim_flag_53;
  reg [32-1:0] _d1__myaxi_write_fsm;
  reg __myaxi_write_fsm_cond_4_0_1;
  reg _myram_0_cond_1_1;
  reg _myram_1_cond_1_1;
  reg _myram_2_cond_1_1;
  reg _myram_3_cond_1_1;
  reg axim_flag_54;
  reg _th_blink_cond_32_1_1;
  reg axim_flag_55;
  reg _th_blink_cond_39_2_1;
  reg _myaxi_myram_0_read_start;
  reg [8-1:0] _myaxi_myram_0_read_op_sel;
  reg [32-1:0] _myaxi_myram_0_read_local_addr;
  reg [32-1:0] _myaxi_myram_0_read_global_addr;
  reg [33-1:0] _myaxi_myram_0_read_size;
  reg [32-1:0] _myaxi_myram_0_read_local_stride;
  reg [32-1:0] _myaxi_read_fsm;
  localparam _myaxi_read_fsm_init = 0;
  reg [32-1:0] _myaxi_read_cur_global_addr;
  reg [33-1:0] _myaxi_read_cur_size;
  reg [33-1:0] _myaxi_read_rest_size;
  reg [128-1:0] _wdata_56;
  reg _wvalid_57;
  reg [34-1:0] _tmp_58;
  reg _tmp_59;
  wire [32-1:0] _slice_data_60;
  wire _slice_valid_60;
  wire _slice_ready_60;
  assign _slice_ready_60 = (_tmp_58 > 0) && !_tmp_59;
  reg _myram_0_cond_2_1;
  reg [34-1:0] _tmp_61;
  reg _tmp_62;
  wire [32-1:0] _slice_data_63;
  wire _slice_valid_63;
  wire _slice_ready_63;
  assign _slice_ready_63 = (_tmp_61 > 0) && !_tmp_62;
  reg _myram_1_cond_2_1;
  reg [34-1:0] _tmp_64;
  reg _tmp_65;
  wire [32-1:0] _slice_data_66;
  wire _slice_valid_66;
  wire _slice_ready_66;
  assign _slice_ready_66 = (_tmp_64 > 0) && !_tmp_65;
  reg _myram_2_cond_2_1;
  reg [34-1:0] _tmp_67;
  reg _tmp_68;
  wire [32-1:0] _slice_data_69;
  wire _slice_valid_69;
  wire _slice_ready_69;
  assign _slice_ready_69 = (_tmp_67 > 0) && !_tmp_68;
  reg _myram_3_cond_2_1;
  reg [9-1:0] _tmp_70;
  reg _myaxi_cond_2_1;
  assign myaxi_rready = _myaxi_read_fsm == 3;
  reg [32-1:0] _d1__myaxi_read_fsm;
  reg __myaxi_read_fsm_cond_3_0_1;
  reg axim_flag_71;
  reg __myaxi_read_fsm_cond_4_1_1;
  reg _tmp_72;
  reg _myram_0_cond_3_1;
  reg _myram_0_cond_4_1;
  reg _myram_0_cond_4_2;
  reg _tmp_73;
  reg _myram_1_cond_3_1;
  reg _myram_1_cond_4_1;
  reg _myram_1_cond_4_2;
  reg _tmp_74;
  reg _myram_2_cond_3_1;
  reg _myram_2_cond_4_1;
  reg _myram_2_cond_4_2;
  reg _tmp_75;
  reg _myram_3_cond_3_1;
  reg _myram_3_cond_4_1;
  reg _myram_3_cond_4_2;
  reg signed [32-1:0] _tmp_76;
  reg signed [32-1:0] _th_blink_rdata_10;
  reg axim_flag_77;
  reg _th_blink_cond_57_3_1;
  reg _tmp_78;
  reg _myram_0_cond_5_1;
  reg _myram_0_cond_6_1;
  reg _myram_0_cond_6_2;
  reg _tmp_79;
  reg _myram_1_cond_5_1;
  reg _myram_1_cond_6_1;
  reg _myram_1_cond_6_2;
  reg _tmp_80;
  reg _myram_2_cond_5_1;
  reg _myram_2_cond_6_1;
  reg _myram_2_cond_6_2;
  reg _tmp_81;
  reg _myram_3_cond_5_1;
  reg _myram_3_cond_6_1;
  reg _myram_3_cond_6_2;
  reg signed [32-1:0] _tmp_82;

  always @(posedge CLK) begin
    if(RST) begin
      _myaxi_read_start <= 0;
      _myaxi_write_start <= 0;
      _myaxi_myram_0_write_start <= 0;
      _myaxi_myram_0_write_op_sel <= 0;
      _myaxi_myram_0_write_local_addr <= 0;
      _myaxi_myram_0_write_global_addr <= 0;
      _myaxi_myram_0_write_size <= 0;
      _myaxi_myram_0_write_local_stride <= 0;
      _myaxi_write_idle <= 1;
      _myaxi_write_op_sel <= 0;
      _myaxi_write_local_addr <= 0;
      _myaxi_write_global_addr <= 0;
      _myaxi_write_size <= 0;
      _myaxi_write_local_stride <= 0;
      myaxi_awaddr <= 0;
      myaxi_awlen <= 0;
      myaxi_awvalid <= 0;
      _tmp_50 <= 0;
      _myaxi_cond_0_1 <= 0;
      myaxi_wdata <= 0;
      myaxi_wvalid <= 0;
      myaxi_wlast <= 0;
      myaxi_wstrb <= 0;
      _tmp_51 <= 0;
      _myaxi_cond_1_1 <= 0;
      _myaxi_myram_0_read_start <= 0;
      _myaxi_myram_0_read_op_sel <= 0;
      _myaxi_myram_0_read_local_addr <= 0;
      _myaxi_myram_0_read_global_addr <= 0;
      _myaxi_myram_0_read_size <= 0;
      _myaxi_myram_0_read_local_stride <= 0;
      _myaxi_read_idle <= 1;
      _myaxi_read_op_sel <= 0;
      _myaxi_read_local_addr <= 0;
      _myaxi_read_global_addr <= 0;
      _myaxi_read_size <= 0;
      _myaxi_read_local_stride <= 0;
      myaxi_araddr <= 0;
      myaxi_arlen <= 0;
      myaxi_arvalid <= 0;
      _tmp_70 <= 0;
      _myaxi_cond_2_1 <= 0;
    end else begin
      if(_myaxi_cond_0_1) begin
        myaxi_awvalid <= 0;
      end 
      if(_myaxi_cond_1_1) begin
        myaxi_wvalid <= 0;
        myaxi_wlast <= 0;
        _tmp_51 <= 0;
      end 
      if(_myaxi_cond_2_1) begin
        myaxi_arvalid <= 0;
      end 
      _myaxi_read_start <= 0;
      _myaxi_write_start <= 0;
      _myaxi_myram_0_write_start <= 0;
      if(axim_flag_1) begin
        _myaxi_myram_0_write_start <= 1;
        _myaxi_myram_0_write_op_sel <= 1;
        _myaxi_myram_0_write_local_addr <= _th_blink_laddr_8;
        _myaxi_myram_0_write_global_addr <= _th_blink_gaddr_9;
        _myaxi_myram_0_write_size <= _th_blink_size_3;
        _myaxi_myram_0_write_local_stride <= 1;
      end 
      if(_myaxi_myram_0_write_start) begin
        _myaxi_write_idle <= 0;
      end 
      if(_myaxi_myram_0_write_start) begin
        _myaxi_write_start <= 1;
        _myaxi_write_op_sel <= _myaxi_myram_0_write_op_sel;
        _myaxi_write_local_addr <= _myaxi_myram_0_write_local_addr;
        _myaxi_write_global_addr <= _myaxi_myram_0_write_global_addr;
        _myaxi_write_size <= _myaxi_myram_0_write_size;
        _myaxi_write_local_stride <= _myaxi_myram_0_write_local_stride;
      end 
      if((_myaxi_write_fsm == 2) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_50 == 0))) begin
        myaxi_awaddr <= _myaxi_write_cur_global_addr;
        myaxi_awlen <= _myaxi_write_cur_size - 1;
        myaxi_awvalid <= 1;
        _tmp_50 <= _myaxi_write_cur_size;
      end 
      if((_myaxi_write_fsm == 2) && ((myaxi_awready || !myaxi_awvalid) && (_tmp_50 == 0)) && (_myaxi_write_cur_size == 0)) begin
        myaxi_awvalid <= 0;
      end 
      _myaxi_cond_0_1 <= 1;
      if(myaxi_awvalid && !myaxi_awready) begin
        myaxi_awvalid <= myaxi_awvalid;
      end 
      if(_cat_valid_52 && ((_myaxi_write_fsm == 3) && (_myaxi_write_op_sel == 1) && ((_tmp_50 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_50 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_50 > 0))) begin
        myaxi_wdata <= _cat_data_52;
        myaxi_wvalid <= 1;
        myaxi_wlast <= 0;
        myaxi_wstrb <= { 16{ 1'd1 } };
        _tmp_50 <= _tmp_50 - 1;
      end 
      if(_cat_valid_52 && ((_myaxi_write_fsm == 3) && (_myaxi_write_op_sel == 1) && ((_tmp_50 > 0) && (myaxi_wready || !myaxi_wvalid))) && ((_tmp_50 > 0) && (myaxi_wready || !myaxi_wvalid) && (_tmp_50 > 0)) && (_tmp_50 == 1)) begin
        myaxi_wlast <= 1;
        _tmp_51 <= 1;
      end 
      _myaxi_cond_1_1 <= 1;
      if(myaxi_wvalid && !myaxi_wready) begin
        myaxi_wvalid <= myaxi_wvalid;
        myaxi_wlast <= myaxi_wlast;
        _tmp_51 <= _tmp_51;
      end 
      if(axim_flag_53) begin
        _myaxi_write_idle <= 1;
      end 
      if(axim_flag_54) begin
        _myaxi_myram_0_write_start <= 1;
        _myaxi_myram_0_write_op_sel <= 1;
        _myaxi_myram_0_write_local_addr <= _th_blink_laddr_8;
        _myaxi_myram_0_write_global_addr <= _th_blink_gaddr_9;
        _myaxi_myram_0_write_size <= _th_blink_size_3;
        _myaxi_myram_0_write_local_stride <= 1;
      end 
      _myaxi_myram_0_read_start <= 0;
      if(axim_flag_55) begin
        _myaxi_myram_0_read_start <= 1;
        _myaxi_myram_0_read_op_sel <= 1;
        _myaxi_myram_0_read_local_addr <= _th_blink_laddr_8;
        _myaxi_myram_0_read_global_addr <= _th_blink_gaddr_9;
        _myaxi_myram_0_read_size <= _th_blink_size_3;
        _myaxi_myram_0_read_local_stride <= 1;
      end 
      if(_myaxi_myram_0_read_start) begin
        _myaxi_read_idle <= 0;
      end 
      if(_myaxi_myram_0_read_start) begin
        _myaxi_read_start <= 1;
        _myaxi_read_op_sel <= _myaxi_myram_0_read_op_sel;
        _myaxi_read_local_addr <= _myaxi_myram_0_read_local_addr;
        _myaxi_read_global_addr <= _myaxi_myram_0_read_global_addr;
        _myaxi_read_size <= _myaxi_myram_0_read_size;
        _myaxi_read_local_stride <= _myaxi_myram_0_read_local_stride;
      end 
      if((_myaxi_read_fsm == 2) && ((myaxi_arready || !myaxi_arvalid) && (_tmp_70 == 0))) begin
        myaxi_araddr <= _myaxi_read_cur_global_addr;
        myaxi_arlen <= _myaxi_read_cur_size - 1;
        myaxi_arvalid <= 1;
        _tmp_70 <= _myaxi_read_cur_size;
      end 
      _myaxi_cond_2_1 <= 1;
      if(myaxi_arvalid && !myaxi_arready) begin
        myaxi_arvalid <= myaxi_arvalid;
      end 
      if(myaxi_rready && myaxi_rvalid && (_tmp_70 > 0)) begin
        _tmp_70 <= _tmp_70 - 1;
      end 
      if(axim_flag_71) begin
        _myaxi_read_idle <= 1;
      end 
      if(axim_flag_77) begin
        _myaxi_myram_0_read_start <= 1;
        _myaxi_myram_0_read_op_sel <= 1;
        _myaxi_myram_0_read_local_addr <= _th_blink_laddr_8;
        _myaxi_myram_0_read_global_addr <= _th_blink_gaddr_9;
        _myaxi_myram_0_read_size <= _th_blink_size_3;
        _myaxi_myram_0_read_local_stride <= 1;
      end 
    end
  end

  reg [32-1:0] _slice_data_83;
  reg _slice_valid_83;
  wire _slice_ready_83;
  reg [32-1:0] _slice_data_84;
  reg _slice_valid_84;
  wire _slice_ready_84;
  reg [32-1:0] _slice_data_85;
  reg _slice_valid_85;
  wire _slice_ready_85;
  reg [32-1:0] _slice_data_86;
  reg _slice_valid_86;
  wire _slice_ready_86;
  assign _slice_data_60 = _slice_data_83;
  assign _slice_valid_60 = _slice_valid_83;
  assign _slice_ready_83 = _slice_ready_60;
  assign _slice_data_63 = _slice_data_84;
  assign _slice_valid_63 = _slice_valid_84;
  assign _slice_ready_84 = _slice_ready_63;
  assign _slice_data_66 = _slice_data_85;
  assign _slice_valid_66 = _slice_valid_85;
  assign _slice_ready_85 = _slice_ready_66;
  assign _slice_data_69 = _slice_data_86;
  assign _slice_valid_69 = _slice_valid_86;
  assign _slice_ready_86 = _slice_ready_69;

  always @(posedge CLK) begin
    if(RST) begin
      _slice_data_83 <= 0;
      _slice_valid_83 <= 0;
      _slice_data_84 <= 0;
      _slice_valid_84 <= 0;
      _slice_data_85 <= 0;
      _slice_valid_85 <= 0;
      _slice_data_86 <= 0;
      _slice_valid_86 <= 0;
    end else begin
      if((_slice_ready_83 || !_slice_valid_83) && 1 && _wvalid_57) begin
        _slice_data_83 <= _wdata_56[6'd31:1'd0];
      end 
      if(_slice_valid_83 && _slice_ready_83) begin
        _slice_valid_83 <= 0;
      end 
      if((_slice_ready_83 || !_slice_valid_83) && 1) begin
        _slice_valid_83 <= _wvalid_57;
      end 
      if((_slice_ready_84 || !_slice_valid_84) && 1 && _wvalid_57) begin
        _slice_data_84 <= _wdata_56[7'd63:7'd32];
      end 
      if(_slice_valid_84 && _slice_ready_84) begin
        _slice_valid_84 <= 0;
      end 
      if((_slice_ready_84 || !_slice_valid_84) && 1) begin
        _slice_valid_84 <= _wvalid_57;
      end 
      if((_slice_ready_85 || !_slice_valid_85) && 1 && _wvalid_57) begin
        _slice_data_85 <= _wdata_56[8'd95:8'd64];
      end 
      if(_slice_valid_85 && _slice_ready_85) begin
        _slice_valid_85 <= 0;
      end 
      if((_slice_ready_85 || !_slice_valid_85) && 1) begin
        _slice_valid_85 <= _wvalid_57;
      end 
      if((_slice_ready_86 || !_slice_valid_86) && 1 && _wvalid_57) begin
        _slice_data_86 <= _wdata_56[8'd127:8'd96];
      end 
      if(_slice_valid_86 && _slice_ready_86) begin
        _slice_valid_86 <= 0;
      end 
      if((_slice_ready_86 || !_slice_valid_86) && 1) begin
        _slice_valid_86 <= _wvalid_57;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram_0_0_addr <= 0;
      myram_0_0_wdata <= 0;
      myram_0_0_wenable <= 0;
      _myram_0_cond_0_1 <= 0;
      __tmp_7_1 <= 0;
      __tmp_8_1 <= 0;
      _tmp_12 <= 0;
      _tmp_2 <= 0;
      _tmp_3 <= 0;
      _tmp_10 <= 0;
      _tmp_11 <= 0;
      _tmp_9 <= 0;
      _tmp_13 <= 0;
      _myram_0_cond_1_1 <= 0;
      _tmp_58 <= 0;
      _tmp_59 <= 0;
      _myram_0_cond_2_1 <= 0;
      _myram_0_cond_3_1 <= 0;
      _tmp_72 <= 0;
      _myram_0_cond_4_1 <= 0;
      _myram_0_cond_4_2 <= 0;
      _myram_0_cond_5_1 <= 0;
      _tmp_78 <= 0;
      _myram_0_cond_6_1 <= 0;
      _myram_0_cond_6_2 <= 0;
    end else begin
      if(_myram_0_cond_4_2) begin
        _tmp_72 <= 0;
      end 
      if(_myram_0_cond_6_2) begin
        _tmp_78 <= 0;
      end 
      if(_myram_0_cond_0_1) begin
        myram_0_0_wenable <= 0;
      end 
      if(_myram_0_cond_1_1) begin
        myram_0_0_wenable <= 0;
      end 
      if(_myram_0_cond_2_1) begin
        myram_0_0_wenable <= 0;
        _tmp_59 <= 0;
      end 
      if(_myram_0_cond_3_1) begin
        _tmp_72 <= 1;
      end 
      _myram_0_cond_4_2 <= _myram_0_cond_4_1;
      if(_myram_0_cond_5_1) begin
        _tmp_78 <= 1;
      end 
      _myram_0_cond_6_2 <= _myram_0_cond_6_1;
      if((th_blink == 12) && (_th_blink_bank_5 == 0)) begin
        myram_0_0_addr <= _th_blink_i_6;
        myram_0_0_wdata <= _th_blink_wdata_7;
        myram_0_0_wenable <= 1;
      end 
      _myram_0_cond_0_1 <= (th_blink == 12) && (_th_blink_bank_5 == 0);
      __tmp_7_1 <= _tmp_7;
      __tmp_8_1 <= _tmp_8;
      if((_tmp_4 || !_tmp_2) && (_tmp_5 || !_tmp_3) && _tmp_10) begin
        _tmp_12 <= 0;
        _tmp_2 <= 0;
        _tmp_3 <= 0;
        _tmp_10 <= 0;
      end 
      if((_tmp_4 || !_tmp_2) && (_tmp_5 || !_tmp_3) && _tmp_9) begin
        _tmp_2 <= 1;
        _tmp_3 <= 1;
        _tmp_12 <= _tmp_11;
        _tmp_11 <= 0;
        _tmp_9 <= 0;
        _tmp_10 <= 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_13 == 0) && !_tmp_11 && !_tmp_12) begin
        myram_0_0_addr <= _myaxi_write_local_addr;
        _tmp_13 <= _myaxi_write_size - 1;
        _tmp_9 <= 1;
        _tmp_11 <= _myaxi_write_size == 1;
      end 
      if((_tmp_4 || !_tmp_2) && (_tmp_5 || !_tmp_3) && (_tmp_13 > 0)) begin
        myram_0_0_addr <= myram_0_0_addr + _myaxi_write_local_stride;
        _tmp_13 <= _tmp_13 - 1;
        _tmp_9 <= 1;
        _tmp_11 <= 0;
      end 
      if((_tmp_4 || !_tmp_2) && (_tmp_5 || !_tmp_3) && (_tmp_13 == 1)) begin
        _tmp_11 <= 1;
      end 
      if((th_blink == 27) && (_th_blink_bank_5 == 0)) begin
        myram_0_0_addr <= _th_blink_i_6;
        myram_0_0_wdata <= _th_blink_wdata_7;
        myram_0_0_wenable <= 1;
      end 
      _myram_0_cond_1_1 <= (th_blink == 27) && (_th_blink_bank_5 == 0);
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_58 == 0)) begin
        myram_0_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_58 <= _myaxi_read_size;
      end 
      if(_slice_valid_60 && ((_tmp_58 > 0) && !_tmp_59) && (_tmp_58 > 0)) begin
        myram_0_0_addr <= myram_0_0_addr + _myaxi_read_local_stride;
        myram_0_0_wdata <= _slice_data_60;
        myram_0_0_wenable <= 1;
        _tmp_58 <= _tmp_58 - 1;
      end 
      if(_slice_valid_60 && ((_tmp_58 > 0) && !_tmp_59) && (_tmp_58 == 1)) begin
        _tmp_59 <= 1;
      end 
      _myram_0_cond_2_1 <= 1;
      if(th_blink == 48) begin
        myram_0_0_addr <= _th_blink_i_6;
      end 
      _myram_0_cond_3_1 <= th_blink == 48;
      _myram_0_cond_4_1 <= th_blink == 48;
      if(th_blink == 66) begin
        myram_0_0_addr <= _th_blink_i_6;
      end 
      _myram_0_cond_5_1 <= th_blink == 66;
      _myram_0_cond_6_1 <= th_blink == 66;
    end
  end

  reg [128-1:0] _cat_data_87;
  reg _cat_valid_87;
  wire _cat_ready_87;
  assign _tmp_40 = 1 && ((_cat_ready_87 || !_cat_valid_87) && (_tmp_38 && _tmp_26 && _tmp_14 && _tmp_2));
  assign _tmp_28 = 1 && ((_cat_ready_87 || !_cat_valid_87) && (_tmp_38 && _tmp_26 && _tmp_14 && _tmp_2));
  assign _tmp_16 = 1 && ((_cat_ready_87 || !_cat_valid_87) && (_tmp_38 && _tmp_26 && _tmp_14 && _tmp_2));
  assign _tmp_4 = 1 && ((_cat_ready_87 || !_cat_valid_87) && (_tmp_38 && _tmp_26 && _tmp_14 && _tmp_2));
  assign _cat_data_52 = _cat_data_87;
  assign _cat_valid_52 = _cat_valid_87;
  assign _cat_ready_87 = _cat_ready_52;

  always @(posedge CLK) begin
    if(RST) begin
      _cat_data_87 <= 0;
      _cat_valid_87 <= 0;
    end else begin
      if((_cat_ready_87 || !_cat_valid_87) && (_tmp_40 && _tmp_28 && _tmp_16 && _tmp_4) && (_tmp_38 && _tmp_26 && _tmp_14 && _tmp_2)) begin
        _cat_data_87 <= { _tmp_44, _tmp_32, _tmp_20, _tmp_8 };
      end 
      if(_cat_valid_87 && _cat_ready_87) begin
        _cat_valid_87 <= 0;
      end 
      if((_cat_ready_87 || !_cat_valid_87) && (_tmp_40 && _tmp_28 && _tmp_16 && _tmp_4)) begin
        _cat_valid_87 <= _tmp_38 && _tmp_26 && _tmp_14 && _tmp_2;
      end 
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram_1_0_addr <= 0;
      myram_1_0_wdata <= 0;
      myram_1_0_wenable <= 0;
      _myram_1_cond_0_1 <= 0;
      __tmp_19_1 <= 0;
      __tmp_20_1 <= 0;
      _tmp_24 <= 0;
      _tmp_14 <= 0;
      _tmp_15 <= 0;
      _tmp_22 <= 0;
      _tmp_23 <= 0;
      _tmp_21 <= 0;
      _tmp_25 <= 0;
      _myram_1_cond_1_1 <= 0;
      _tmp_61 <= 0;
      _tmp_62 <= 0;
      _myram_1_cond_2_1 <= 0;
      _myram_1_cond_3_1 <= 0;
      _tmp_73 <= 0;
      _myram_1_cond_4_1 <= 0;
      _myram_1_cond_4_2 <= 0;
      _myram_1_cond_5_1 <= 0;
      _tmp_79 <= 0;
      _myram_1_cond_6_1 <= 0;
      _myram_1_cond_6_2 <= 0;
    end else begin
      if(_myram_1_cond_4_2) begin
        _tmp_73 <= 0;
      end 
      if(_myram_1_cond_6_2) begin
        _tmp_79 <= 0;
      end 
      if(_myram_1_cond_0_1) begin
        myram_1_0_wenable <= 0;
      end 
      if(_myram_1_cond_1_1) begin
        myram_1_0_wenable <= 0;
      end 
      if(_myram_1_cond_2_1) begin
        myram_1_0_wenable <= 0;
        _tmp_62 <= 0;
      end 
      if(_myram_1_cond_3_1) begin
        _tmp_73 <= 1;
      end 
      _myram_1_cond_4_2 <= _myram_1_cond_4_1;
      if(_myram_1_cond_5_1) begin
        _tmp_79 <= 1;
      end 
      _myram_1_cond_6_2 <= _myram_1_cond_6_1;
      if((th_blink == 12) && (_th_blink_bank_5 == 1)) begin
        myram_1_0_addr <= _th_blink_i_6;
        myram_1_0_wdata <= _th_blink_wdata_7;
        myram_1_0_wenable <= 1;
      end 
      _myram_1_cond_0_1 <= (th_blink == 12) && (_th_blink_bank_5 == 1);
      __tmp_19_1 <= _tmp_19;
      __tmp_20_1 <= _tmp_20;
      if((_tmp_16 || !_tmp_14) && (_tmp_17 || !_tmp_15) && _tmp_22) begin
        _tmp_24 <= 0;
        _tmp_14 <= 0;
        _tmp_15 <= 0;
        _tmp_22 <= 0;
      end 
      if((_tmp_16 || !_tmp_14) && (_tmp_17 || !_tmp_15) && _tmp_21) begin
        _tmp_14 <= 1;
        _tmp_15 <= 1;
        _tmp_24 <= _tmp_23;
        _tmp_23 <= 0;
        _tmp_21 <= 0;
        _tmp_22 <= 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_25 == 0) && !_tmp_23 && !_tmp_24) begin
        myram_1_0_addr <= _myaxi_write_local_addr;
        _tmp_25 <= _myaxi_write_size - 1;
        _tmp_21 <= 1;
        _tmp_23 <= _myaxi_write_size == 1;
      end 
      if((_tmp_16 || !_tmp_14) && (_tmp_17 || !_tmp_15) && (_tmp_25 > 0)) begin
        myram_1_0_addr <= myram_1_0_addr + _myaxi_write_local_stride;
        _tmp_25 <= _tmp_25 - 1;
        _tmp_21 <= 1;
        _tmp_23 <= 0;
      end 
      if((_tmp_16 || !_tmp_14) && (_tmp_17 || !_tmp_15) && (_tmp_25 == 1)) begin
        _tmp_23 <= 1;
      end 
      if((th_blink == 27) && (_th_blink_bank_5 == 1)) begin
        myram_1_0_addr <= _th_blink_i_6;
        myram_1_0_wdata <= _th_blink_wdata_7;
        myram_1_0_wenable <= 1;
      end 
      _myram_1_cond_1_1 <= (th_blink == 27) && (_th_blink_bank_5 == 1);
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_61 == 0)) begin
        myram_1_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_61 <= _myaxi_read_size;
      end 
      if(_slice_valid_63 && ((_tmp_61 > 0) && !_tmp_62) && (_tmp_61 > 0)) begin
        myram_1_0_addr <= myram_1_0_addr + _myaxi_read_local_stride;
        myram_1_0_wdata <= _slice_data_63;
        myram_1_0_wenable <= 1;
        _tmp_61 <= _tmp_61 - 1;
      end 
      if(_slice_valid_63 && ((_tmp_61 > 0) && !_tmp_62) && (_tmp_61 == 1)) begin
        _tmp_62 <= 1;
      end 
      _myram_1_cond_2_1 <= 1;
      if(th_blink == 48) begin
        myram_1_0_addr <= _th_blink_i_6;
      end 
      _myram_1_cond_3_1 <= th_blink == 48;
      _myram_1_cond_4_1 <= th_blink == 48;
      if(th_blink == 66) begin
        myram_1_0_addr <= _th_blink_i_6;
      end 
      _myram_1_cond_5_1 <= th_blink == 66;
      _myram_1_cond_6_1 <= th_blink == 66;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram_2_0_addr <= 0;
      myram_2_0_wdata <= 0;
      myram_2_0_wenable <= 0;
      _myram_2_cond_0_1 <= 0;
      __tmp_31_1 <= 0;
      __tmp_32_1 <= 0;
      _tmp_36 <= 0;
      _tmp_26 <= 0;
      _tmp_27 <= 0;
      _tmp_34 <= 0;
      _tmp_35 <= 0;
      _tmp_33 <= 0;
      _tmp_37 <= 0;
      _myram_2_cond_1_1 <= 0;
      _tmp_64 <= 0;
      _tmp_65 <= 0;
      _myram_2_cond_2_1 <= 0;
      _myram_2_cond_3_1 <= 0;
      _tmp_74 <= 0;
      _myram_2_cond_4_1 <= 0;
      _myram_2_cond_4_2 <= 0;
      _myram_2_cond_5_1 <= 0;
      _tmp_80 <= 0;
      _myram_2_cond_6_1 <= 0;
      _myram_2_cond_6_2 <= 0;
    end else begin
      if(_myram_2_cond_4_2) begin
        _tmp_74 <= 0;
      end 
      if(_myram_2_cond_6_2) begin
        _tmp_80 <= 0;
      end 
      if(_myram_2_cond_0_1) begin
        myram_2_0_wenable <= 0;
      end 
      if(_myram_2_cond_1_1) begin
        myram_2_0_wenable <= 0;
      end 
      if(_myram_2_cond_2_1) begin
        myram_2_0_wenable <= 0;
        _tmp_65 <= 0;
      end 
      if(_myram_2_cond_3_1) begin
        _tmp_74 <= 1;
      end 
      _myram_2_cond_4_2 <= _myram_2_cond_4_1;
      if(_myram_2_cond_5_1) begin
        _tmp_80 <= 1;
      end 
      _myram_2_cond_6_2 <= _myram_2_cond_6_1;
      if((th_blink == 12) && (_th_blink_bank_5 == 2)) begin
        myram_2_0_addr <= _th_blink_i_6;
        myram_2_0_wdata <= _th_blink_wdata_7;
        myram_2_0_wenable <= 1;
      end 
      _myram_2_cond_0_1 <= (th_blink == 12) && (_th_blink_bank_5 == 2);
      __tmp_31_1 <= _tmp_31;
      __tmp_32_1 <= _tmp_32;
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && _tmp_34) begin
        _tmp_36 <= 0;
        _tmp_26 <= 0;
        _tmp_27 <= 0;
        _tmp_34 <= 0;
      end 
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && _tmp_33) begin
        _tmp_26 <= 1;
        _tmp_27 <= 1;
        _tmp_36 <= _tmp_35;
        _tmp_35 <= 0;
        _tmp_33 <= 0;
        _tmp_34 <= 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_37 == 0) && !_tmp_35 && !_tmp_36) begin
        myram_2_0_addr <= _myaxi_write_local_addr;
        _tmp_37 <= _myaxi_write_size - 1;
        _tmp_33 <= 1;
        _tmp_35 <= _myaxi_write_size == 1;
      end 
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && (_tmp_37 > 0)) begin
        myram_2_0_addr <= myram_2_0_addr + _myaxi_write_local_stride;
        _tmp_37 <= _tmp_37 - 1;
        _tmp_33 <= 1;
        _tmp_35 <= 0;
      end 
      if((_tmp_28 || !_tmp_26) && (_tmp_29 || !_tmp_27) && (_tmp_37 == 1)) begin
        _tmp_35 <= 1;
      end 
      if((th_blink == 27) && (_th_blink_bank_5 == 2)) begin
        myram_2_0_addr <= _th_blink_i_6;
        myram_2_0_wdata <= _th_blink_wdata_7;
        myram_2_0_wenable <= 1;
      end 
      _myram_2_cond_1_1 <= (th_blink == 27) && (_th_blink_bank_5 == 2);
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_64 == 0)) begin
        myram_2_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_64 <= _myaxi_read_size;
      end 
      if(_slice_valid_66 && ((_tmp_64 > 0) && !_tmp_65) && (_tmp_64 > 0)) begin
        myram_2_0_addr <= myram_2_0_addr + _myaxi_read_local_stride;
        myram_2_0_wdata <= _slice_data_66;
        myram_2_0_wenable <= 1;
        _tmp_64 <= _tmp_64 - 1;
      end 
      if(_slice_valid_66 && ((_tmp_64 > 0) && !_tmp_65) && (_tmp_64 == 1)) begin
        _tmp_65 <= 1;
      end 
      _myram_2_cond_2_1 <= 1;
      if(th_blink == 48) begin
        myram_2_0_addr <= _th_blink_i_6;
      end 
      _myram_2_cond_3_1 <= th_blink == 48;
      _myram_2_cond_4_1 <= th_blink == 48;
      if(th_blink == 66) begin
        myram_2_0_addr <= _th_blink_i_6;
      end 
      _myram_2_cond_5_1 <= th_blink == 66;
      _myram_2_cond_6_1 <= th_blink == 66;
    end
  end


  always @(posedge CLK) begin
    if(RST) begin
      myram_3_0_addr <= 0;
      myram_3_0_wdata <= 0;
      myram_3_0_wenable <= 0;
      _myram_3_cond_0_1 <= 0;
      __tmp_43_1 <= 0;
      __tmp_44_1 <= 0;
      _tmp_48 <= 0;
      _tmp_38 <= 0;
      _tmp_39 <= 0;
      _tmp_46 <= 0;
      _tmp_47 <= 0;
      _tmp_45 <= 0;
      _tmp_49 <= 0;
      _myram_3_cond_1_1 <= 0;
      _tmp_67 <= 0;
      _tmp_68 <= 0;
      _myram_3_cond_2_1 <= 0;
      _myram_3_cond_3_1 <= 0;
      _tmp_75 <= 0;
      _myram_3_cond_4_1 <= 0;
      _myram_3_cond_4_2 <= 0;
      _myram_3_cond_5_1 <= 0;
      _tmp_81 <= 0;
      _myram_3_cond_6_1 <= 0;
      _myram_3_cond_6_2 <= 0;
    end else begin
      if(_myram_3_cond_4_2) begin
        _tmp_75 <= 0;
      end 
      if(_myram_3_cond_6_2) begin
        _tmp_81 <= 0;
      end 
      if(_myram_3_cond_0_1) begin
        myram_3_0_wenable <= 0;
      end 
      if(_myram_3_cond_1_1) begin
        myram_3_0_wenable <= 0;
      end 
      if(_myram_3_cond_2_1) begin
        myram_3_0_wenable <= 0;
        _tmp_68 <= 0;
      end 
      if(_myram_3_cond_3_1) begin
        _tmp_75 <= 1;
      end 
      _myram_3_cond_4_2 <= _myram_3_cond_4_1;
      if(_myram_3_cond_5_1) begin
        _tmp_81 <= 1;
      end 
      _myram_3_cond_6_2 <= _myram_3_cond_6_1;
      if((th_blink == 12) && (_th_blink_bank_5 == 3)) begin
        myram_3_0_addr <= _th_blink_i_6;
        myram_3_0_wdata <= _th_blink_wdata_7;
        myram_3_0_wenable <= 1;
      end 
      _myram_3_cond_0_1 <= (th_blink == 12) && (_th_blink_bank_5 == 3);
      __tmp_43_1 <= _tmp_43;
      __tmp_44_1 <= _tmp_44;
      if((_tmp_40 || !_tmp_38) && (_tmp_41 || !_tmp_39) && _tmp_46) begin
        _tmp_48 <= 0;
        _tmp_38 <= 0;
        _tmp_39 <= 0;
        _tmp_46 <= 0;
      end 
      if((_tmp_40 || !_tmp_38) && (_tmp_41 || !_tmp_39) && _tmp_45) begin
        _tmp_38 <= 1;
        _tmp_39 <= 1;
        _tmp_48 <= _tmp_47;
        _tmp_47 <= 0;
        _tmp_45 <= 0;
        _tmp_46 <= 1;
      end 
      if(_myaxi_write_start && (_myaxi_write_op_sel == 1) && (_tmp_49 == 0) && !_tmp_47 && !_tmp_48) begin
        myram_3_0_addr <= _myaxi_write_local_addr;
        _tmp_49 <= _myaxi_write_size - 1;
        _tmp_45 <= 1;
        _tmp_47 <= _myaxi_write_size == 1;
      end 
      if((_tmp_40 || !_tmp_38) && (_tmp_41 || !_tmp_39) && (_tmp_49 > 0)) begin
        myram_3_0_addr <= myram_3_0_addr + _myaxi_write_local_stride;
        _tmp_49 <= _tmp_49 - 1;
        _tmp_45 <= 1;
        _tmp_47 <= 0;
      end 
      if((_tmp_40 || !_tmp_38) && (_tmp_41 || !_tmp_39) && (_tmp_49 == 1)) begin
        _tmp_47 <= 1;
      end 
      if((th_blink == 27) && (_th_blink_bank_5 == 3)) begin
        myram_3_0_addr <= _th_blink_i_6;
        myram_3_0_wdata <= _th_blink_wdata_7;
        myram_3_0_wenable <= 1;
      end 
      _myram_3_cond_1_1 <= (th_blink == 27) && (_th_blink_bank_5 == 3);
      if(_myaxi_read_start && (_myaxi_read_op_sel == 1) && (_tmp_67 == 0)) begin
        myram_3_0_addr <= _myaxi_read_local_addr - _myaxi_read_local_stride;
        _tmp_67 <= _myaxi_read_size;
      end 
      if(_slice_valid_69 && ((_tmp_67 > 0) && !_tmp_68) && (_tmp_67 > 0)) begin
        myram_3_0_addr <= myram_3_0_addr + _myaxi_read_local_stride;
        myram_3_0_wdata <= _slice_data_69;
        myram_3_0_wenable <= 1;
        _tmp_67 <= _tmp_67 - 1;
      end 
      if(_slice_valid_69 && ((_tmp_67 > 0) && !_tmp_68) && (_tmp_67 == 1)) begin
        _tmp_68 <= 1;
      end 
      _myram_3_cond_2_1 <= 1;
      if(th_blink == 48) begin
        myram_3_0_addr <= _th_blink_i_6;
      end 
      _myram_3_cond_3_1 <= th_blink == 48;
      _myram_3_cond_4_1 <= th_blink == 48;
      if(th_blink == 66) begin
        myram_3_0_addr <= _th_blink_i_6;
      end 
      _myram_3_cond_5_1 <= th_blink == 66;
      _myram_3_cond_6_1 <= th_blink == 66;
    end
  end

  localparam th_blink_1 = 1;
  localparam th_blink_2 = 2;
  localparam th_blink_3 = 3;
  localparam th_blink_4 = 4;
  localparam th_blink_5 = 5;
  localparam th_blink_6 = 6;
  localparam th_blink_7 = 7;
  localparam th_blink_8 = 8;
  localparam th_blink_9 = 9;
  localparam th_blink_10 = 10;
  localparam th_blink_11 = 11;
  localparam th_blink_12 = 12;
  localparam th_blink_13 = 13;
  localparam th_blink_14 = 14;
  localparam th_blink_15 = 15;
  localparam th_blink_16 = 16;
  localparam th_blink_17 = 17;
  localparam th_blink_18 = 18;
  localparam th_blink_19 = 19;
  localparam th_blink_20 = 20;
  localparam th_blink_21 = 21;
  localparam th_blink_22 = 22;
  localparam th_blink_23 = 23;
  localparam th_blink_24 = 24;
  localparam th_blink_25 = 25;
  localparam th_blink_26 = 26;
  localparam th_blink_27 = 27;
  localparam th_blink_28 = 28;
  localparam th_blink_29 = 29;
  localparam th_blink_30 = 30;
  localparam th_blink_31 = 31;
  localparam th_blink_32 = 32;
  localparam th_blink_33 = 33;
  localparam th_blink_34 = 34;
  localparam th_blink_35 = 35;
  localparam th_blink_36 = 36;
  localparam th_blink_37 = 37;
  localparam th_blink_38 = 38;
  localparam th_blink_39 = 39;
  localparam th_blink_40 = 40;
  localparam th_blink_41 = 41;
  localparam th_blink_42 = 42;
  localparam th_blink_43 = 43;
  localparam th_blink_44 = 44;
  localparam th_blink_45 = 45;
  localparam th_blink_46 = 46;
  localparam th_blink_47 = 47;
  localparam th_blink_48 = 48;
  localparam th_blink_49 = 49;
  localparam th_blink_50 = 50;
  localparam th_blink_51 = 51;
  localparam th_blink_52 = 52;
  localparam th_blink_53 = 53;
  localparam th_blink_54 = 54;
  localparam th_blink_55 = 55;
  localparam th_blink_56 = 56;
  localparam th_blink_57 = 57;
  localparam th_blink_58 = 58;
  localparam th_blink_59 = 59;
  localparam th_blink_60 = 60;
  localparam th_blink_61 = 61;
  localparam th_blink_62 = 62;
  localparam th_blink_63 = 63;
  localparam th_blink_64 = 64;
  localparam th_blink_65 = 65;
  localparam th_blink_66 = 66;
  localparam th_blink_67 = 67;
  localparam th_blink_68 = 68;
  localparam th_blink_69 = 69;
  localparam th_blink_70 = 70;
  localparam th_blink_71 = 71;
  localparam th_blink_72 = 72;
  localparam th_blink_73 = 73;
  localparam th_blink_74 = 74;
  localparam th_blink_75 = 75;
  localparam th_blink_76 = 76;
  localparam th_blink_77 = 77;

  always @(posedge CLK) begin
    if(RST) begin
      th_blink <= th_blink_init;
      _d1_th_blink <= th_blink_init;
      _th_blink_size_0 <= 0;
      _tmp_0 <= 0;
      _th_blink_i_1 <= 0;
      _th_blink_offset_2 <= 0;
      _th_blink_size_3 <= 0;
      _th_blink_offset_4 <= 0;
      _th_blink_bank_5 <= 0;
      _th_blink_i_6 <= 0;
      _th_blink_wdata_7 <= 0;
      _th_blink_laddr_8 <= 0;
      _th_blink_gaddr_9 <= 0;
      axim_flag_1 <= 0;
      _th_blink_cond_17_0_1 <= 0;
      axim_flag_54 <= 0;
      _th_blink_cond_32_1_1 <= 0;
      axim_flag_55 <= 0;
      _th_blink_cond_39_2_1 <= 0;
      _tmp_76 <= 0;
      _th_blink_rdata_10 <= 0;
      axim_flag_77 <= 0;
      _th_blink_cond_57_3_1 <= 0;
      _tmp_82 <= 0;
    end else begin
      _d1_th_blink <= th_blink;
      case(_d1_th_blink)
        th_blink_17: begin
          if(_th_blink_cond_17_0_1) begin
            axim_flag_1 <= 0;
          end 
        end
        th_blink_32: begin
          if(_th_blink_cond_32_1_1) begin
            axim_flag_54 <= 0;
          end 
        end
        th_blink_39: begin
          if(_th_blink_cond_39_2_1) begin
            axim_flag_55 <= 0;
          end 
        end
        th_blink_57: begin
          if(_th_blink_cond_57_3_1) begin
            axim_flag_77 <= 0;
          end 
        end
      endcase
      case(th_blink)
        th_blink_init: begin
          _th_blink_size_0 <= 16;
          th_blink <= th_blink_1;
        end
        th_blink_1: begin
          _tmp_0 <= 1;
          th_blink <= th_blink_2;
        end
        th_blink_2: begin
          _th_blink_i_1 <= 0;
          th_blink <= th_blink_3;
        end
        th_blink_3: begin
          if(_th_blink_i_1 < 4) begin
            th_blink <= th_blink_4;
          end else begin
            th_blink <= th_blink_75;
          end
        end
        th_blink_4: begin
          $display("# iter %d start", _th_blink_i_1);
          th_blink <= th_blink_5;
        end
        th_blink_5: begin
          _th_blink_offset_2 <= ((_th_blink_i_1 << 10) << 4) + 4092;
          th_blink <= th_blink_6;
        end
        th_blink_6: begin
          _th_blink_size_3 <= _th_blink_size_0;
          _th_blink_offset_4 <= _th_blink_offset_2;
          th_blink <= th_blink_7;
        end
        th_blink_7: begin
          _th_blink_bank_5 <= 0;
          th_blink <= th_blink_8;
        end
        th_blink_8: begin
          if(_th_blink_bank_5 < 4) begin
            th_blink <= th_blink_9;
          end else begin
            th_blink <= th_blink_15;
          end
        end
        th_blink_9: begin
          _th_blink_i_6 <= 0;
          th_blink <= th_blink_10;
        end
        th_blink_10: begin
          if(_th_blink_i_6 < _th_blink_size_3) begin
            th_blink <= th_blink_11;
          end else begin
            th_blink <= th_blink_14;
          end
        end
        th_blink_11: begin
          _th_blink_wdata_7 <= _th_blink_i_6 + 100 + _th_blink_bank_5;
          th_blink <= th_blink_12;
        end
        th_blink_12: begin
          th_blink <= th_blink_13;
        end
        th_blink_13: begin
          _th_blink_i_6 <= _th_blink_i_6 + 1;
          th_blink <= th_blink_10;
        end
        th_blink_14: begin
          _th_blink_bank_5 <= _th_blink_bank_5 + 1;
          th_blink <= th_blink_8;
        end
        th_blink_15: begin
          _th_blink_laddr_8 <= 0;
          th_blink <= th_blink_16;
        end
        th_blink_16: begin
          _th_blink_gaddr_9 <= _th_blink_offset_4;
          th_blink <= th_blink_17;
        end
        th_blink_17: begin
          axim_flag_1 <= 1;
          _th_blink_cond_17_0_1 <= 1;
          th_blink <= th_blink_18;
        end
        th_blink_18: begin
          th_blink <= th_blink_19;
        end
        th_blink_19: begin
          th_blink <= th_blink_20;
        end
        th_blink_20: begin
          if(_myaxi_write_idle) begin
            th_blink <= th_blink_21;
          end 
        end
        th_blink_21: begin
          $display("dma_write: [%d] -> [%d]", _th_blink_laddr_8, _th_blink_gaddr_9);
          th_blink <= th_blink_22;
        end
        th_blink_22: begin
          _th_blink_bank_5 <= 0;
          th_blink <= th_blink_23;
        end
        th_blink_23: begin
          if(_th_blink_bank_5 < 4) begin
            th_blink <= th_blink_24;
          end else begin
            th_blink <= th_blink_30;
          end
        end
        th_blink_24: begin
          _th_blink_i_6 <= 0;
          th_blink <= th_blink_25;
        end
        th_blink_25: begin
          if(_th_blink_i_6 < _th_blink_size_3) begin
            th_blink <= th_blink_26;
          end else begin
            th_blink <= th_blink_29;
          end
        end
        th_blink_26: begin
          _th_blink_wdata_7 <= _th_blink_i_6 + 1000 + _th_blink_bank_5;
          th_blink <= th_blink_27;
        end
        th_blink_27: begin
          th_blink <= th_blink_28;
        end
        th_blink_28: begin
          _th_blink_i_6 <= _th_blink_i_6 + 1;
          th_blink <= th_blink_25;
        end
        th_blink_29: begin
          _th_blink_bank_5 <= _th_blink_bank_5 + 1;
          th_blink <= th_blink_23;
        end
        th_blink_30: begin
          _th_blink_laddr_8 <= 0;
          th_blink <= th_blink_31;
        end
        th_blink_31: begin
          _th_blink_gaddr_9 <= 512 + _th_blink_offset_4;
          th_blink <= th_blink_32;
        end
        th_blink_32: begin
          axim_flag_54 <= 1;
          _th_blink_cond_32_1_1 <= 1;
          th_blink <= th_blink_33;
        end
        th_blink_33: begin
          th_blink <= th_blink_34;
        end
        th_blink_34: begin
          th_blink <= th_blink_35;
        end
        th_blink_35: begin
          if(_myaxi_write_idle) begin
            th_blink <= th_blink_36;
          end 
        end
        th_blink_36: begin
          $display("dma_write: [%d] -> [%d]", _th_blink_laddr_8, _th_blink_gaddr_9);
          th_blink <= th_blink_37;
        end
        th_blink_37: begin
          _th_blink_laddr_8 <= 0;
          th_blink <= th_blink_38;
        end
        th_blink_38: begin
          _th_blink_gaddr_9 <= _th_blink_offset_4;
          th_blink <= th_blink_39;
        end
        th_blink_39: begin
          axim_flag_55 <= 1;
          _th_blink_cond_39_2_1 <= 1;
          th_blink <= th_blink_40;
        end
        th_blink_40: begin
          th_blink <= th_blink_41;
        end
        th_blink_41: begin
          th_blink <= th_blink_42;
        end
        th_blink_42: begin
          if(_myaxi_read_idle) begin
            th_blink <= th_blink_43;
          end 
        end
        th_blink_43: begin
          $display("dma_read:  [%d] <- [%d]", _th_blink_laddr_8, _th_blink_gaddr_9);
          th_blink <= th_blink_44;
        end
        th_blink_44: begin
          _th_blink_bank_5 <= 0;
          th_blink <= th_blink_45;
        end
        th_blink_45: begin
          if(_th_blink_bank_5 < 4) begin
            th_blink <= th_blink_46;
          end else begin
            th_blink <= th_blink_55;
          end
        end
        th_blink_46: begin
          _th_blink_i_6 <= 0;
          th_blink <= th_blink_47;
        end
        th_blink_47: begin
          if(_th_blink_i_6 < _th_blink_size_3) begin
            th_blink <= th_blink_48;
          end else begin
            th_blink <= th_blink_54;
          end
        end
        th_blink_48: begin
          if(_tmp_72 && (_th_blink_bank_5 == 0)) begin
            _tmp_76 <= myram_0_0_rdata;
          end 
          if(_tmp_73 && (_th_blink_bank_5 == 1)) begin
            _tmp_76 <= myram_1_0_rdata;
          end 
          if(_tmp_74 && (_th_blink_bank_5 == 2)) begin
            _tmp_76 <= myram_2_0_rdata;
          end 
          if(_tmp_75 && (_th_blink_bank_5 == 3)) begin
            _tmp_76 <= myram_3_0_rdata;
          end 
          if(_tmp_72) begin
            th_blink <= th_blink_49;
          end 
        end
        th_blink_49: begin
          _th_blink_rdata_10 <= _tmp_76;
          th_blink <= th_blink_50;
        end
        th_blink_50: begin
          if(_th_blink_rdata_10 !== _th_blink_i_6 + 100 + _th_blink_bank_5) begin
            th_blink <= th_blink_51;
          end else begin
            th_blink <= th_blink_53;
          end
        end
        th_blink_51: begin
          $display("rdata[%d] = %d", _th_blink_i_6, _th_blink_rdata_10);
          th_blink <= th_blink_52;
        end
        th_blink_52: begin
          _tmp_0 <= 0;
          th_blink <= th_blink_53;
        end
        th_blink_53: begin
          _th_blink_i_6 <= _th_blink_i_6 + 1;
          th_blink <= th_blink_47;
        end
        th_blink_54: begin
          _th_blink_bank_5 <= _th_blink_bank_5 + 1;
          th_blink <= th_blink_45;
        end
        th_blink_55: begin
          _th_blink_laddr_8 <= 0;
          th_blink <= th_blink_56;
        end
        th_blink_56: begin
          _th_blink_gaddr_9 <= 512 + _th_blink_offset_4;
          th_blink <= th_blink_57;
        end
        th_blink_57: begin
          axim_flag_77 <= 1;
          _th_blink_cond_57_3_1 <= 1;
          th_blink <= th_blink_58;
        end
        th_blink_58: begin
          th_blink <= th_blink_59;
        end
        th_blink_59: begin
          th_blink <= th_blink_60;
        end
        th_blink_60: begin
          if(_myaxi_read_idle) begin
            th_blink <= th_blink_61;
          end 
        end
        th_blink_61: begin
          $display("dma_read:  [%d] <- [%d]", _th_blink_laddr_8, _th_blink_gaddr_9);
          th_blink <= th_blink_62;
        end
        th_blink_62: begin
          _th_blink_bank_5 <= 0;
          th_blink <= th_blink_63;
        end
        th_blink_63: begin
          if(_th_blink_bank_5 < 4) begin
            th_blink <= th_blink_64;
          end else begin
            th_blink <= th_blink_73;
          end
        end
        th_blink_64: begin
          _th_blink_i_6 <= 0;
          th_blink <= th_blink_65;
        end
        th_blink_65: begin
          if(_th_blink_i_6 < _th_blink_size_3) begin
            th_blink <= th_blink_66;
          end else begin
            th_blink <= th_blink_72;
          end
        end
        th_blink_66: begin
          if(_tmp_78 && (_th_blink_bank_5 == 0)) begin
            _tmp_82 <= myram_0_0_rdata;
          end 
          if(_tmp_79 && (_th_blink_bank_5 == 1)) begin
            _tmp_82 <= myram_1_0_rdata;
          end 
          if(_tmp_80 && (_th_blink_bank_5 == 2)) begin
            _tmp_82 <= myram_2_0_rdata;
          end 
          if(_tmp_81 && (_th_blink_bank_5 == 3)) begin
            _tmp_82 <= myram_3_0_rdata;
          end 
          if(_tmp_78) begin
            th_blink <= th_blink_67;
          end 
        end
        th_blink_67: begin
          _th_blink_rdata_10 <= _tmp_82;
          th_blink <= th_blink_68;
        end
        th_blink_68: begin
          if(_th_blink_rdata_10 !== _th_blink_i_6 + 1000 + _th_blink_bank_5) begin
            th_blink <= th_blink_69;
          end else begin
            th_blink <= th_blink_71;
          end
        end
        th_blink_69: begin
          $display("rdata[%d] = %d", _th_blink_i_6, _th_blink_rdata_10);
          th_blink <= th_blink_70;
        end
        th_blink_70: begin
          _tmp_0 <= 0;
          th_blink <= th_blink_71;
        end
        th_blink_71: begin
          _th_blink_i_6 <= _th_blink_i_6 + 1;
          th_blink <= th_blink_65;
        end
        th_blink_72: begin
          _th_blink_bank_5 <= _th_blink_bank_5 + 1;
          th_blink <= th_blink_63;
        end
        th_blink_73: begin
          $display("# iter %d end", _th_blink_i_1);
          th_blink <= th_blink_74;
        end
        th_blink_74: begin
          _th_blink_i_1 <= _th_blink_i_1 + 1;
          th_blink <= th_blink_3;
        end
        th_blink_75: begin
          if(_tmp_0) begin
            th_blink <= th_blink_76;
          end else begin
            th_blink <= th_blink_77;
          end
        end
        th_blink_76: begin
          $display("ALL OK");
          th_blink <= th_blink_77;
        end
      endcase
    end
  end

  localparam _myaxi_write_fsm_1 = 1;
  localparam _myaxi_write_fsm_2 = 2;
  localparam _myaxi_write_fsm_3 = 3;
  localparam _myaxi_write_fsm_4 = 4;
  localparam _myaxi_write_fsm_5 = 5;

  always @(posedge CLK) begin
    if(RST) begin
      _myaxi_write_fsm <= _myaxi_write_fsm_init;
      _d1__myaxi_write_fsm <= _myaxi_write_fsm_init;
      _myaxi_write_cur_global_addr <= 0;
      _myaxi_write_rest_size <= 0;
      _myaxi_write_cur_size <= 0;
      axim_flag_53 <= 0;
      __myaxi_write_fsm_cond_4_0_1 <= 0;
    end else begin
      _d1__myaxi_write_fsm <= _myaxi_write_fsm;
      case(_d1__myaxi_write_fsm)
        _myaxi_write_fsm_4: begin
          if(__myaxi_write_fsm_cond_4_0_1) begin
            axim_flag_53 <= 0;
          end 
        end
      endcase
      case(_myaxi_write_fsm)
        _myaxi_write_fsm_init: begin
          if(_myaxi_write_start) begin
            _myaxi_write_cur_global_addr <= (_myaxi_write_global_addr >> 4) << 4;
            _myaxi_write_rest_size <= _myaxi_write_size;
          end 
          if(_myaxi_write_start && (_myaxi_write_op_sel == 1)) begin
            _myaxi_write_fsm <= _myaxi_write_fsm_1;
          end 
        end
        _myaxi_write_fsm_1: begin
          if((_myaxi_write_rest_size <= 256) && ((_myaxi_write_cur_global_addr & 4095) + (_myaxi_write_rest_size << 4) >= 4096)) begin
            _myaxi_write_cur_size <= 4096 - (_myaxi_write_cur_global_addr & 4095) >> 4;
            _myaxi_write_rest_size <= _myaxi_write_rest_size - (4096 - (_myaxi_write_cur_global_addr & 4095) >> 4);
          end else if(_myaxi_write_rest_size <= 256) begin
            _myaxi_write_cur_size <= _myaxi_write_rest_size;
            _myaxi_write_rest_size <= 0;
          end else if((_myaxi_write_cur_global_addr & 4095) + 4096 >= 4096) begin
            _myaxi_write_cur_size <= 4096 - (_myaxi_write_cur_global_addr & 4095) >> 4;
            _myaxi_write_rest_size <= _myaxi_write_rest_size - (4096 - (_myaxi_write_cur_global_addr & 4095) >> 4);
          end else begin
            _myaxi_write_cur_size <= 256;
            _myaxi_write_rest_size <= _myaxi_write_rest_size - 256;
          end
          _myaxi_write_fsm <= _myaxi_write_fsm_2;
        end
        _myaxi_write_fsm_2: begin
          if(myaxi_awready || !myaxi_awvalid) begin
            _myaxi_write_fsm <= _myaxi_write_fsm_3;
          end 
        end
        _myaxi_write_fsm_3: begin
          if(_myaxi_write_data_done) begin
            _myaxi_write_cur_global_addr <= _myaxi_write_cur_global_addr + (_myaxi_write_cur_size << 4);
          end 
          if(_myaxi_write_data_done && (_myaxi_write_rest_size > 0)) begin
            _myaxi_write_fsm <= _myaxi_write_fsm_1;
          end 
          if(_myaxi_write_data_done && (_myaxi_write_rest_size == 0)) begin
            _myaxi_write_fsm <= _myaxi_write_fsm_4;
          end 
        end
        _myaxi_write_fsm_4: begin
          axim_flag_53 <= 1;
          __myaxi_write_fsm_cond_4_0_1 <= 1;
          _myaxi_write_fsm <= _myaxi_write_fsm_5;
        end
        _myaxi_write_fsm_5: begin
          _myaxi_write_fsm <= _myaxi_write_fsm_init;
        end
      endcase
    end
  end

  localparam _myaxi_read_fsm_1 = 1;
  localparam _myaxi_read_fsm_2 = 2;
  localparam _myaxi_read_fsm_3 = 3;
  localparam _myaxi_read_fsm_4 = 4;
  localparam _myaxi_read_fsm_5 = 5;

  always @(posedge CLK) begin
    if(RST) begin
      _myaxi_read_fsm <= _myaxi_read_fsm_init;
      _d1__myaxi_read_fsm <= _myaxi_read_fsm_init;
      _myaxi_read_cur_global_addr <= 0;
      _myaxi_read_rest_size <= 0;
      _myaxi_read_cur_size <= 0;
      __myaxi_read_fsm_cond_3_0_1 <= 0;
      _wvalid_57 <= 0;
      _wdata_56 <= 0;
      axim_flag_71 <= 0;
      __myaxi_read_fsm_cond_4_1_1 <= 0;
    end else begin
      _d1__myaxi_read_fsm <= _myaxi_read_fsm;
      case(_d1__myaxi_read_fsm)
        _myaxi_read_fsm_3: begin
          if(__myaxi_read_fsm_cond_3_0_1) begin
            _wvalid_57 <= 0;
          end 
        end
        _myaxi_read_fsm_4: begin
          if(__myaxi_read_fsm_cond_4_1_1) begin
            axim_flag_71 <= 0;
          end 
        end
      endcase
      case(_myaxi_read_fsm)
        _myaxi_read_fsm_init: begin
          if(_myaxi_read_start) begin
            _myaxi_read_cur_global_addr <= (_myaxi_read_global_addr >> 4) << 4;
            _myaxi_read_rest_size <= _myaxi_read_size;
          end 
          if(_myaxi_read_start && (_myaxi_read_op_sel == 1)) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_1;
          end 
        end
        _myaxi_read_fsm_1: begin
          if((_myaxi_read_rest_size <= 256) && ((_myaxi_read_cur_global_addr & 4095) + (_myaxi_read_rest_size << 4) >= 4096)) begin
            _myaxi_read_cur_size <= 4096 - (_myaxi_read_cur_global_addr & 4095) >> 4;
            _myaxi_read_rest_size <= _myaxi_read_rest_size - (4096 - (_myaxi_read_cur_global_addr & 4095) >> 4);
          end else if(_myaxi_read_rest_size <= 256) begin
            _myaxi_read_cur_size <= _myaxi_read_rest_size;
            _myaxi_read_rest_size <= 0;
          end else if((_myaxi_read_cur_global_addr & 4095) + 4096 >= 4096) begin
            _myaxi_read_cur_size <= 4096 - (_myaxi_read_cur_global_addr & 4095) >> 4;
            _myaxi_read_rest_size <= _myaxi_read_rest_size - (4096 - (_myaxi_read_cur_global_addr & 4095) >> 4);
          end else begin
            _myaxi_read_cur_size <= 256;
            _myaxi_read_rest_size <= _myaxi_read_rest_size - 256;
          end
          _myaxi_read_fsm <= _myaxi_read_fsm_2;
        end
        _myaxi_read_fsm_2: begin
          if(myaxi_arready || !myaxi_arvalid) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_3;
          end 
        end
        _myaxi_read_fsm_3: begin
          __myaxi_read_fsm_cond_3_0_1 <= 1;
          if(myaxi_rready && myaxi_rvalid && (_myaxi_read_op_sel == 1)) begin
            _wdata_56 <= myaxi_rdata;
            _wvalid_57 <= 1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast) begin
            _myaxi_read_cur_global_addr <= _myaxi_read_cur_global_addr + (_myaxi_read_cur_size << 4);
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_myaxi_read_rest_size > 0)) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_1;
          end 
          if(myaxi_rready && myaxi_rvalid && myaxi_rlast && (_myaxi_read_rest_size == 0)) begin
            _myaxi_read_fsm <= _myaxi_read_fsm_4;
          end 
        end
        _myaxi_read_fsm_4: begin
          axim_flag_71 <= 1;
          __myaxi_read_fsm_cond_4_1_1 <= 1;
          _myaxi_read_fsm <= _myaxi_read_fsm_5;
        end
        _myaxi_read_fsm_5: begin
          _myaxi_read_fsm <= _myaxi_read_fsm_init;
        end
      endcase
    end
  end


endmodule



module myram_0
(
  input CLK,
  input [10-1:0] myram_0_0_addr,
  output [32-1:0] myram_0_0_rdata,
  input [32-1:0] myram_0_0_wdata,
  input myram_0_0_wenable
);

  reg [10-1:0] myram_0_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram_0_0_wenable) begin
      mem[myram_0_0_addr] <= myram_0_0_wdata;
    end 
    myram_0_0_daddr <= myram_0_0_addr;
  end

  assign myram_0_0_rdata = mem[myram_0_0_daddr];

endmodule



module myram_1
(
  input CLK,
  input [10-1:0] myram_1_0_addr,
  output [32-1:0] myram_1_0_rdata,
  input [32-1:0] myram_1_0_wdata,
  input myram_1_0_wenable
);

  reg [10-1:0] myram_1_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram_1_0_wenable) begin
      mem[myram_1_0_addr] <= myram_1_0_wdata;
    end 
    myram_1_0_daddr <= myram_1_0_addr;
  end

  assign myram_1_0_rdata = mem[myram_1_0_daddr];

endmodule



module myram_2
(
  input CLK,
  input [10-1:0] myram_2_0_addr,
  output [32-1:0] myram_2_0_rdata,
  input [32-1:0] myram_2_0_wdata,
  input myram_2_0_wenable
);

  reg [10-1:0] myram_2_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram_2_0_wenable) begin
      mem[myram_2_0_addr] <= myram_2_0_wdata;
    end 
    myram_2_0_daddr <= myram_2_0_addr;
  end

  assign myram_2_0_rdata = mem[myram_2_0_daddr];

endmodule



module myram_3
(
  input CLK,
  input [10-1:0] myram_3_0_addr,
  output [32-1:0] myram_3_0_rdata,
  input [32-1:0] myram_3_0_wdata,
  input myram_3_0_wenable
);

  reg [10-1:0] myram_3_0_daddr;
  reg [32-1:0] mem [0:1024-1];

  always @(posedge CLK) begin
    if(myram_3_0_wenable) begin
      mem[myram_3_0_addr] <= myram_3_0_wdata;
    end 
    myram_3_0_daddr <= myram_3_0_addr;
  end

  assign myram_3_0_rdata = mem[myram_3_0_daddr];

endmodule
"""


def test():
    veriloggen.reset()
    test_module = thread_to_multibank_ram.mkTest()
    code = test_module.to_verilog()

    from pyverilog.vparser.parser import VerilogParser
    from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
    parser = VerilogParser()
    expected_ast = parser.parse(expected_verilog)
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)

    assert(expected_code == code)

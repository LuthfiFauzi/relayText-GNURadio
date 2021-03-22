#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Relay Block
# Generated: Wed Jun 17 15:46:26 2020
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx


class relay_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Relay Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2000000
        self.gainTx = gainTx = 15
        self.gainRx = gainRx = 45

        ##################################################
        # Blocks
        ##################################################
        _gainTx_sizer = wx.BoxSizer(wx.VERTICAL)
        self._gainTx_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_gainTx_sizer,
        	value=self.gainTx,
        	callback=self.set_gainTx,
        	label='gainTx',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._gainTx_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_gainTx_sizer,
        	value=self.gainTx,
        	callback=self.set_gainTx,
        	minimum=0,
        	maximum=70,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_gainTx_sizer)
        _gainRx_sizer = wx.BoxSizer(wx.VERTICAL)
        self._gainRx_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_gainRx_sizer,
        	value=self.gainRx,
        	callback=self.set_gainRx,
        	label='gainRx',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._gainRx_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_gainRx_sizer,
        	value=self.gainRx,
        	callback=self.set_gainRx,
        	minimum=0,
        	maximum=90,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_gainRx_sizer)
        self.wxgui_scopesink2_0_0 = scopesink2.scope_sink_c(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0_0.win)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "serial=3188130")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(825e6, 0)
        self.uhd_usrp_source_0.set_gain(gainRx, 0)
        self.uhd_usrp_source_0.set_antenna("RX2", 0)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "serial=318A028")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(845e6, 0)
        self.uhd_usrp_sink_0.set_gain(gainTx, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.digital_gmsk_mod_0_0 = digital.gmsk_mod(
        	samples_per_symbol=2,
        	bt=0.35,
        	verbose=False,
        	log=False,
        )
        self.digital_gmsk_demod_0 = digital.gmsk_demod(
        	samples_per_symbol=2,
        	gain_mu=0.175,
        	mu=0.5,
        	omega_relative_limit=0.005,
        	freq_error=0.0,
        	verbose=False,
        	log=False,
        )
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vcc((1, ))
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, "/home/luthfi/Desktop/Relay/TextRelay.txt", False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blks2_packet_encoder_0_0 = grc_blks2.packet_mod_f(grc_blks2.packet_encoder(
        		samples_per_symbol=5,
        		bits_per_symbol=2,
        		preamble="",
        		access_code="",
        		pad_for_usrp=False,
        	),
        	payload_length=200,
        )
        self.blks2_packet_decoder_0 = grc_blks2.packet_demod_f(grc_blks2.packet_decoder(
        		access_code="",
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0.recv_pkt(ok, payload),
        	),
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blks2_packet_decoder_0, 0), (self.blks2_packet_encoder_0_0, 0))    
        self.connect((self.blks2_packet_decoder_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.blks2_packet_encoder_0_0, 0), (self.digital_gmsk_mod_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.uhd_usrp_sink_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.wxgui_scopesink2_0_0, 0))    
        self.connect((self.blocks_throttle_1, 0), (self.digital_gmsk_demod_0, 0))    
        self.connect((self.digital_gmsk_demod_0, 0), (self.blks2_packet_decoder_0, 0))    
        self.connect((self.digital_gmsk_mod_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_throttle_1, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.wxgui_scopesink2_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_1.set_sample_rate(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0_0.set_sample_rate(self.samp_rate)

    def get_gainTx(self):
        return self.gainTx

    def set_gainTx(self, gainTx):
        self.gainTx = gainTx
        self.uhd_usrp_sink_0.set_gain(self.gainTx, 0)
        	
        self._gainTx_slider.set_value(self.gainTx)
        self._gainTx_text_box.set_value(self.gainTx)

    def get_gainRx(self):
        return self.gainRx

    def set_gainRx(self, gainRx):
        self.gainRx = gainRx
        self.uhd_usrp_source_0.set_gain(self.gainRx, 0)
        	
        self._gainRx_slider.set_value(self.gainRx)
        self._gainRx_text_box.set_value(self.gainRx)


def main(top_block_cls=relay_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()

#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "Algorithm of speex codec"

def get_licence():
	return "BSD-3"

def get_compagny_type():
	return "org"

def get_compagny_name():
	return "Xiph"

def get_version():
	return [1,2,"rc2"]

def configure(target, my_module):
	# add extra compilation flags:
	my_module.add_extra_flags()
	# add the file to compile:
	my_module.add_src_file([
		'speex/libspeex/bits.c',
		'speex/libspeex/exc_5_256_table.c',
		'speex/libspeex/gain_table_lbr.c',
		'speex/libspeex/kiss_fftr.c',
		'speex/libspeex/modes.c',
		'speex/libspeex/smallft.c',
		'speex/libspeex/vq.c',
		'speex/libspeex/cb_search.c',
		'speex/libspeex/exc_5_64_table.c',
		'speex/libspeex/hexc_10_32_table.c',
		'speex/libspeex/lpc.c',
		'speex/libspeex/modes_wb.c',
		'speex/libspeex/speex.c',
		'speex/libspeex/window.c',
		'speex/libspeex/exc_10_16_table.c',
		'speex/libspeex/exc_8_128_table.c',
		'speex/libspeex/hexc_table.c',
		'speex/libspeex/lsp.c',
		'speex/libspeex/nb_celp.c',
		'speex/libspeex/speex_callbacks.c',
		'speex/libspeex/exc_10_32_table.c',
		'speex/libspeex/filters.c',
		'speex/libspeex/high_lsp_tables.c',
		'speex/libspeex/lsp_tables_nb.c',
		'speex/libspeex/quant_lsp.c',
		'speex/libspeex/speex_header.c',
		'speex/libspeex/vbr.c',
		'speex/libspeex/exc_20_32_table.c',
		'speex/libspeex/gain_table.c',
		'speex/libspeex/kiss_fft.c',
		'speex/libspeex/ltp.c',
		'speex/libspeex/sb_celp.c',
		'speex/libspeex/stereo.c',
		'speex/libspeex/vorbis_psy.c'
		])
	my_module.add_header_file([
		'speex/include/speex/speex_header.h',
		'speex/include/speex/speex_config_types.h',
		'speex/include/speex/speex_callbacks.h',
		'speex/include/speex/speex_types.h',
		'speex/include/speex/speex.h',
		'speex/include/speex/speex_stereo.h',
		'speex/include/speex/speex_bits.h'
		],
		destination_path="speex")
	

	my_module.compile_version("c", 1989, gnu=True)
	my_module.add_depend(['m'])
	my_module.add_path("speex/include")
	# configure library :
	
	# Make use of ARM4 assembly optimizations
	#my_module.add_flag_CC("-DARM4_ASM=1")
	# Make use of ARM5E assembly optimizations
	#my_module.add_flag_CC("-DARM5E_ASM=1")
	# Make use of Blackfin assembly optimizations
	#my_module.add_flag_CC("-DBFIN_ASM=1")
	# Disable all parts of the API that are using floats
	#my_module.add_flag_CC("-DDISABLE_FLOAT_API=1")
	# Enable valgrind extra checks
	#my_module.add_flag_CC("-DENABLE_VALGRIND=1")
	# Symbol visibility prefix */
	#define EXPORT __attribute__((visibility("default")))
	my_module.add_flag('c', "-DEXPORT=''")
	# Debug fixed-point implementation */
	#my_module.add_flag_CC("-DFIXED_DEBUG=1")
	# Compile as fixed-point / floating-point
	if True:
		my_module.add_flag('c', "-DFIXED_POINT")
	else:
		my_module.add_flag('c', "-DFLOATING_POINT")
		# Enable NEON support */
		#my_module.add_flag('c', "-D_USE_NEON=1")
		# Enable SSE support */
		my_module.add_flag('c', "-D_USE_SSE=1")
		# Enable SSE2 support */
		my_module.add_flag('c', "-D_USE_SSE2=1")
	# Define to 1 if you have the <alloca.h> header file.
	my_module.add_flag('c', "-DHAVE_ALLOCA_H=1")
	# Use FFT from OggVorbis */
	my_module.add_flag('c', "-DUSE_SMALLFT=1")
	# Use C99 variable-size arrays */
	my_module.add_flag('c', "-DVAR_ARRAYS=1")
	
	my_module.add_depend([
		    'c'
		    ])
	return True



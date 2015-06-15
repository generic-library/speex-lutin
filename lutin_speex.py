#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools

def get_desc():
	return "Algorithm of speex codec"


def create(target):
	myModule = module.Module(__file__, 'speex', 'LIBRARY')
	# add extra compilation flags :
	myModule.add_extra_compile_flags()
	# add the file to compile:
	myModule.add_src_file([
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
	
	# name of the dependency
	#myModule.add_module_depend('speexdsp')
	
	myModule.compile_version_CC(1989, gnu=True)
	myModule.add_export_path(tools.get_current_path(__file__) + "/speex/include")
	# configure library :
	
	# Make use of ARM4 assembly optimizations
	#myModule.compile_flags_CC("-DARM4_ASM=1")
	# Make use of ARM5E assembly optimizations
	#myModule.compile_flags_CC("-DARM5E_ASM=1")
	# Make use of Blackfin assembly optimizations
	#myModule.compile_flags_CC("-DBFIN_ASM=1")
	# Disable all parts of the API that are using floats
	#myModule.compile_flags_CC("-DDISABLE_FLOAT_API=1")
	# Enable valgrind extra checks
	#myModule.compile_flags_CC("-DENABLE_VALGRIND=1")
	# Symbol visibility prefix */
	#define EXPORT __attribute__((visibility("default")))
	myModule.compile_flags('c', "-DEXPORT=''")
	# Debug fixed-point implementation */
	#myModule.compile_flags_CC("-DFIXED_DEBUG=1")
	# Compile as fixed-point / floating-point
	if True:
		myModule.compile_flags('c', "-DFIXED_POINT")
	else:
		myModule.compile_flags('c', "-DFLOATING_POINT")
		# Enable NEON support */
		#myModule.compile_flags('c', "-D_USE_NEON=1")
		# Enable SSE support */
		myModule.compile_flags('c', "-D_USE_SSE=1")
		# Enable SSE2 support */
		myModule.compile_flags('c', "-D_USE_SSE2=1")
	# Define to 1 if you have the <alloca.h> header file.
	myModule.compile_flags('c', "-DHAVE_ALLOCA_H=1")
	# Use FFT from OggVorbis */
	myModule.compile_flags('c', "-DUSE_SMALLFT=1")
	# Use C99 variable-size arrays */
	myModule.compile_flags('c', "-DVAR_ARRAYS=1")
	
	return myModule



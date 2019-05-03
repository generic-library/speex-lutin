#!/usr/bin/python
import realog.debug as debug
import lutin.tools as tools


def get_type():
	return "BINARY"

def get_sub_type():
	return "TEST"

def get_desc():
	return "Encode wide band"

def get_licence():
	return "BSD-3"

def get_compagny_type():
	return "org"

def get_compagny_name():
	return "Xiph"

def configure(target, my_module):
	my_module.add_extra_flags()
	my_module.add_src_file([
		'speex/libspeex/testenc_wb.c'
		])
	
	my_module.compile_version('c', 1989, gnu=True)
	my_module.add_depend('speex')
	return True



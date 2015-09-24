#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools

def get_desc():
	return "test: Encode wide band"


def create(target):
	my_module = module.Module(__file__, 'speextestencwb', 'BINARY')
	# add extra compilation flags :
	my_module.add_extra_compile_flags()
	# add the file to compile:
	my_module.add_src_file([
		'speex/libspeex/testenc_wb.c'
		])
	
	my_module.compile_version_CC(1989, gnu=True)
	# name of the dependency
	my_module.add_module_depend('speex')
	
	# add the currrent module at the 
	return my_module



#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools

def get_desc():
	return "Encode test"


def create(target):
	my_module = module.Module(__file__, 'speextestenc', 'BINARY')
	# add extra compilation flags :
	my_module.add_extra_compile_flags()
	# add the file to compile:
	my_module.add_src_file([
		'speex/libspeex/testenc.c'
		])
	
	my_module.compile_version_CC(1989, gnu=True)
	# name of the dependency
	my_module.add_module_depend('speex')
	
	# add the currrent module at the 
	return my_module



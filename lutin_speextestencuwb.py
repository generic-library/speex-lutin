#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools

def get_desc():
	return "test: Encode U wide band"


def create(target):
	myModule = module.Module(__file__, 'speextestencuwb', 'BINARY')
	# add extra compilation flags :
	myModule.add_extra_compile_flags()
	# add the file to compile:
	myModule.add_src_file([
		'speex/libspeex/testenc_uwb.c'
		])
	
	myModule.compile_version_CC(1989, gnu=True)
	# name of the dependency
	myModule.add_module_depend('speex')
	
	# add the currrent module at the 
	return myModule



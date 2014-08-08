#!/usr/bin/env python3

import sys
import inspect
import getopt

def represents_int(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

def represents_float(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

def represents_bool(s):
	if s == 'True' or s == 'False':
		return True
	else:
		return False

def parse_bool(s):
	if s == 'True':
		return True
	elif s == 'False':
		return False
	else:
		return bool(s)

def represents_none(s):
	if s == 'None':
		return True
	else:
		return False
 
def try_to_parse(s):
	if represents_int(s):
		return int(s)
	elif represents_float(s):
		return float(s)
	elif represents_bool(s):
		return parse_bool(s)
	elif represents_none(s):
		return None
	else: 
		return s

def print_opt_arg_error():
    print('For help use --help')
    return(2)

def commander_line(func, print_done=True, squash_return_value=True, argv=None):
	'''
	commander_line(func, print_done=True, squash_return_value=True, argv=None)

	Q: Officer, state your name and rank!
	A: Commander Line reporting for duty, Sir!
	Q: What is the most sacred code that we honor?
	A: Convention over configuration, Sir!

	Commander Line converts any python function to a full-fledged command line tool.
	It will take any function as an parameter and use the function's parameter names to parse (long) command line arguments (i.e., --param_name) with those same names.
	It will attempt to parse argument values in the following order:
		1. int
		2. float
		3. bool (True or False)
		4. None
		5. leave as string (default)
	Commander Line respects default values defined by your function and will use them when needed (i.e., when arguments are missing).
	By default, it will return 0 and print 'Done' when you function has finished. This behaviour can be controlled with the print_done and squash_return_value parameters.
	Your function's __doc__ string will be printed when either of the -h and --help arguments are provided.

	To enable, just include the following in your code (and replace 'function_name' with your function):

	import commanderline.commander_line as cl
	if __name__ == '__main__':
		cl.commander_line(function_name)

	'''

	if argv is None:
		argv = sys.argv

	spec = inspect.getargspec(func)

	help_options = {'short':'h', 'long':'help'}
	loop_options_help = ('-'+help_options['short'], '--'+help_options['long'])

    # Prepare options for getopt()
	getopt_options_default = [help_options['long']]

	getopt_options_user = spec[0].copy()
	getopt_options_user = [o+'=' for o in getopt_options_user]

	getopt_options = getopt_options_default.copy()
	getopt_options.extend(getopt_options_user)

	# Prepare opts for lookup in loop
	loop_options = spec[0].copy()
	loop_options = {'--'+o for o in loop_options}

	# Prepare opts and values for function call
	unwrap_options = {}

	# Fill in defaults
	num_defaults = len(spec[3])
	if num_defaults > 0:
		diff = len(spec[0]) - num_defaults
		for i in range(0, num_defaults):
			unwrap_options[spec[0][diff+i]] = spec[3][i]

	# Get options
	try:
	    opts, args = getopt.getopt(argv[1:], help_options['short'], getopt_options)
	except getopt.error as msg:
	    print(msg)
	    return print_opt_arg_error()

	
	# Process options
	for o, a in opts:
	    if o in loop_options_help:
	        print(func.__doc__)
	        return 0
	    elif o in loop_options:
	    	unwrap_options[o.lstrip('-')] = try_to_parse(a)
	    else:
	        print('Error: Unkown option '+o)
	        return print_opt_arg_error()

	# # process arguments
	# for arg in args:
	#     #process(arg) # process() is defined elsewhere 
	#     print("Error: Unkown argument: "+arg)
	#     return print_opt_arg_error() 

	# verification
	for k in spec[0]:
	    if k not in unwrap_options:
	        print('Error: Missing flag: '+k)
	        return print_opt_arg_error()

	return_value = func(**unwrap_options)

	if print_done:
		print('Done')

	if squash_return_value:
		return 0
	else:
		return return_value

if __name__ == '__main__':
	commander_line(commander_line)

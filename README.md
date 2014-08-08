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


P.S. Adding: 

	#!/usr/bin/env python3

as your shebang line will provide a nice and portable run environment for your new command-line tool
	

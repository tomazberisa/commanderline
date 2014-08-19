# Commander Line
	commander_line(funcs, print_done=True, squash_return_value=True, argv=None, print_argv_to_output=True, help_prints_args=True)

Commander Line converts any python function to a full-fledged command line tool.

It will take any function as a parameter and use the function's parameter names to parse (long) command line arguments (i.e., --param_name) with those same names.

To enable, just include the following in your code (and replace 'function_name' with your function):

	import commanderline.commander_line as cl
	if __name__ == '__main__':
		cl.commander_line(function_name)

It will attempt to parse argument values in the following order:

1. int
2. float
3. bool (True or False)
4. None
5. leave as string (default)

Commander Line respects default values defined by your function and will use them when needed (i.e., when arguments are missing).

By default, it will print out the command line arguments, return 0, and print 'Done' when your function has finished. This behaviour can be controlled with the print_argv_to_output, squash_return_value, and print_done parameters (respectively).

Your function's __doc__ string will be printed when either of the -h and --help arguments are provided. A summary of its parameters and defaults will also be printed (existence of summary can be controlled with help_prints_args).

If you provide a list or tuple of functions instead of a single function, you can specify which one to call from the command line with the -f <func_name> argument. If none is specified, the first element in the tuple/list is taken as default.

List functions that are exported (and their command line arguments) with -l

P.S. Adding: 

	#!/usr/bin/env python3

as your shebang line will provide a nice and portable run environment for your new command-line tool
	

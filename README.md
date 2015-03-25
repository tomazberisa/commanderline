# Commander Line (for Python 3)
	commander_line(funcs, print_done=True, squash_return_value=True, argv=None, print_argv_to_output=True, help_prints_args=True)

Commander Line makes any python function accessible from the command-line with just 2 lines of code.

It will take any function (from the current scope) as a parameter and expose the function's parameters to the command line as long arguments (i.e., --param_name).

Best-effort parsing of the parameters is performed. Currently supported data types are:

	1.  int
	2.  float
	3.  complex
	4.  bool
	5.  None
	6.  dict
	7.  list
	8.  set
	9.  tuple
	10. str

# Installation
	
	$ pip install commanderline

# Usage

Just import Commander Line as follows:

	import commanderline.commander_line as cl

...and include the following line at the end of your .py file (replace 'function_name' with your function):

	cl.commander_line(function_name) if __name__ == '__main__' else None

# Example

## test.py 

	#!/usr/bin/env python3
	
	import commanderline.commander_line as cl

	def add(v1, v2):
	  '''Add two values v1 and v2 '''
	  print(str(v1)+' + '+str(v2)+' = '+str(v1+v2))

	def subtract(v1, v2):
	  '''Subtract v2 from v1 '''
	  print(str(v1)+' - '+str(v2)+' = '+str(v1-v2))

	cl.commander_line([add, subtract]) if __name__ == '__main__' else None	

## run / output

	$ ./test.py --v1 5 --v2 4
	Run parameters: ./test.py --v1 5 --v2 4
	5 + 4 = 9
	Done

	$ ./test.py -f subtract --v1 5 --v2 4
	Run parameters: ./test.py -f subtract --v1 5 --v2 4
	5 - 4 = 1
	Done

	$ ./test.py -h
	Run parameters: ./test.py -h
	Add two values v1 and v2
	add arguments (and defaults if defined):
	  --v1
	  --v2

	$ ./test.py -f subtract -h
	Run parameters: ./test.py -f subtract -h
	Subtract v2 from v2
	subtract arguments (and defaults if defined):
	  --v1
	  --v2

	$ ./test.py -l
	Run parameters: ./test.py -l
	Exported functions:
	add [default]
	  --v1
	  --v2
	subtract
	  --v1
	  --v2

# Details

Commander Line will attempt to parse argument values in the following order:

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
	

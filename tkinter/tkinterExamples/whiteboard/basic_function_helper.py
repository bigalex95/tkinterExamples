"""
Define the C-variables and functions from the C-files that are needed in Python
"""
from ctypes import *
import sys
print(sys.platform)
lib_path = 'example_dll.dll'
print(lib_path)
basic_function_lib = CDLL(lib_path)
print(basic_function_lib)
# try:
#     basic_function_lib = CDLL(lib_path)
# except:
#     print('OS %s not recognized' % (sys.platform))

# python_c_square = basic_function_lib.c_square
# python_c_square.restype = None

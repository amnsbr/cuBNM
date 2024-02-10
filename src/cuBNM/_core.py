"""
This imports run_simulations extension while
handling some known issues that may occur during import
in addition to initializing the extension
"""
import sys

try:
    from cuBNM.core import run_simulations
except ImportError as e:
    error_msg = str(e)
    if "GLIBC_2.29" in error_msg:
        print("To fix this error either update `ldd` or build cuBNM from source (https://github.com/amnsbr/cuBNM)")
    elif "undefined symbol" in error_msg:
        print("To fix this error try building cuBNM from source (https://github.com/amnsbr/cuBNM)")
    raise
else:
    from cuBNM.core import init, set_const, set_conf, get_conf
    init()
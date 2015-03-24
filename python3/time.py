"""Stub file for the 'time' module."""
# This is an autogenerated file. It serves as a starting point
# for a more percise manual annotation of this module.
# Feel free to edit the source below, but remove this header when you do.

def asctime(*args, **kwargs) -> unicode: pass

def clock() -> float: pass

def clock_getres(a: int) -> float:
    raise IOError()

def clock_gettime(a: int) -> float:
    raise IOError()

def clock_settime(a: int, b) -> NoneType:
    raise IOError()

def ctime(*args, **kwargs) -> unicode: pass

def get_clock_info(a: str) -> object:
    raise ValueError()

def gmtime(*args, **kwargs) -> tuple:
    raise OSError()

def localtime(*args, **kwargs) -> tuple: pass

def mktime(*args, **kwargs) -> float:
    raise OverflowError()

def monotonic() -> float: pass

def perf_counter() -> float: pass

def process_time() -> float: pass

def sleep(a: float) -> NoneType:
    raise ValueError()

def strftime(a: str, *args, **kwargs) -> unicode:
    raise MemoryError()

def strptime(*args, **kwargs) -> object: pass

def time() -> float: pass

def tzset() -> NoneType: pass

"""Stub file for the 'cStringIO' module."""
# This is an autogenerated file. It serves as a starting point
# for a more percise manual annotation of this module.
# Feel free to edit the source below, but remove this header when you do.

InputType = Undefined(StringI)
OutputType = Undefined(StringO)
cStringIO_CAPI = Undefined(object)

def StringIO(*args, **kwargs) -> object: pass


class StringI(object):
    def close() -> NoneType: pass
    def flush() -> NoneType: pass
    def getvalue(*args, **kwargs) -> str: pass
    def isatty() -> bool: pass
    def read(*args, **kwargs) -> str: pass
    def readline(*args, **kwargs) -> str: pass
    def readlines(*args, **kwargs) -> List[str]: pass
    def reset() -> NoneType: pass
    def seek(a: int, *args, **kwargs) -> NoneType: pass
    def tell() -> int: pass
    def truncate(*args, **kwargs) -> NoneType:
        raise IOError()

class StringO(object):
    def close() -> NoneType: pass
    def flush() -> NoneType: pass
    def getvalue(*args, **kwargs) -> str: pass
    def isatty() -> bool: pass
    def read(*args, **kwargs) -> str: pass
    def readline(*args, **kwargs) -> str: pass
    def readlines(*args, **kwargs) -> List[str]: pass
    def reset() -> NoneType: pass
    def seek(a: int, *args, **kwargs) -> NoneType: pass
    def tell() -> int: pass
    def truncate(*args, **kwargs) -> NoneType:
        raise IOError()
    def write(a) -> NoneType: pass
    def writelines(*args, **kwargs) -> NoneType: pass

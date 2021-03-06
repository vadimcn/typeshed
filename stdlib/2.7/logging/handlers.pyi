# Stubs for logging.handlers (Python 2.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Union, Tuple
from . import LogRecord
import logging
import socket

threading = ...  # type: Any
DEFAULT_TCP_LOGGING_PORT = ...  # type: Any
DEFAULT_UDP_LOGGING_PORT = ...  # type: Any
DEFAULT_HTTP_LOGGING_PORT = ...  # type: Any
DEFAULT_SOAP_LOGGING_PORT = ...  # type: Any
SYSLOG_UDP_PORT = ...  # type: Any
SYSLOG_TCP_PORT = ...  # type: Any

class BaseRotatingHandler(logging.FileHandler):
    mode = ...  # type: Any
    encoding = ...  # type: Any
    namer = ...  # type: Any
    rotator = ...  # type: Any
    def __init__(self, filename: unicode, mode: unicode, encoding: unicode =..., delay: int =...) -> None: ...
    def emit(self, record: LogRecord) -> None: ...
    def rotation_filename(self, default_name: unicode): ...
    def rotate(self, source, dest): ...

class RotatingFileHandler(BaseRotatingHandler):
    maxBytes = ...  # type: Any
    backupCount = ...  # type: Any
    def __init__(self, filename: unicode, mode: unicode = ..., maxBytes: int = ..., backupCount:int = ...,
                 encoding: str = ..., delay: int = ...) -> None: ...
    stream = ...  # type: Any
    def doRollover(self) -> None: ...
    def shouldRollover(self, record: LogRecord) -> int: ...

class TimedRotatingFileHandler(BaseRotatingHandler):
    when = ...  # type: Any
    backupCount = ...  # type: Any
    utc = ...  # type: Any
    atTime = ...  # type: Any
    interval = ...  # type: Any
    suffix = ...  # type: Any
    extMatch = ...  # type: Any
    dayOfWeek = ...  # type: Any
    rolloverAt = ...  # type: Any
    def __init__(self, filename: unicode, when: unicode =..., interval: int =..., backupCount: int =...,
                 encoding: unicode =..., delay: bool =..., utc: bool =..., atTime=...) -> None: ...
    def computeRollover(self, currentTime: int) -> int: ...
    def shouldRollover(self, record: LogRecord) -> int: ...
    def getFilesToDelete(self) -> list[str]: ...
    stream = ...  # type: Any
    def doRollover(self) -> None: ...

class WatchedFileHandler(logging.FileHandler):
    def __init__(self, filename: str, mode: str = ..., encoding: str = ..., delay: int = ...) -> None: ...
    stream = ...  # type: Any
    def emit(self, record: LogRecord) -> None: ...

class SocketHandler(logging.Handler):
    host = ...  # type: Any
    port = ...  # type: Any
    address = ...  # type: Any
    sock = ...  # type: Any
    closeOnError = ...  # type: Any
    retryTime = ...  # type: Any
    retryStart = ...  # type: Any
    retryMax = ...  # type: Any
    retryFactor = ...  # type: Any
    def __init__(self, host, port) -> None: ...
    def makeSocket(self, timeout: int =...): ...
    retryPeriod = ...  # type: Any
    def createSocket(self) -> None: ...
    def send(self, s: str) -> None: ...
    def makePickle(self, record: LogRecord) -> str: ...
    def handleError(self, record: LogRecord) -> None: ...
    def emit(self, record: LogRecord) -> None: ...
    def close(self) -> None: ...

class DatagramHandler(SocketHandler):
    closeOnError = ...  # type: Any
    def __init__(self, host, port) -> None: ...
    def makeSocket(self, timeout: int =...) -> None: ...
    def send(self, s: str) -> None: ...

class SysLogHandler(logging.Handler):
    LOG_EMERG = ...  # type: Any
    LOG_ALERT = ...  # type: Any
    LOG_CRIT = ...  # type: Any
    LOG_ERR = ...  # type: Any
    LOG_WARNING = ...  # type: Any
    LOG_NOTICE = ...  # type: Any
    LOG_INFO = ...  # type: Any
    LOG_DEBUG = ...  # type: Any
    LOG_KERN = ...  # type: Any
    LOG_USER = ...  # type: Any
    LOG_MAIL = ...  # type: Any
    LOG_DAEMON = ...  # type: Any
    LOG_AUTH = ...  # type: Any
    LOG_SYSLOG = ...  # type: Any
    LOG_LPR = ...  # type: Any
    LOG_NEWS = ...  # type: Any
    LOG_UUCP = ...  # type: Any
    LOG_CRON = ...  # type: Any
    LOG_AUTHPRIV = ...  # type: Any
    LOG_FTP = ...  # type: Any
    LOG_LOCAL0 = ...  # type: Any
    LOG_LOCAL1 = ...  # type: Any
    LOG_LOCAL2 = ...  # type: Any
    LOG_LOCAL3 = ...  # type: Any
    LOG_LOCAL4 = ...  # type: Any
    LOG_LOCAL5 = ...  # type: Any
    LOG_LOCAL6 = ...  # type: Any
    LOG_LOCAL7 = ...  # type: Any
    priority_names = ...  # type: Any
    facility_names = ...  # type: Any
    priority_map = ...  # type: Any
    address = ...  # type: Any
    facility = ...  # type: Any
    socktype = ...  # type: Any
    unixsocket = ...  # type: Any
    socket = ...  # type: Any
    formatter = ...  # type: Any
    def __init__(self, address: tuple[str,int] =..., facility: int =..., socktype: int =...) -> None: ...
    def encodePriority(self, facility: int, priority: Union[basestring,int]) -> int: ...
    def close(self) -> None: ...
    def mapPriority(self, levelName: str) -> str: ...
    ident = ...  # type: Any
    append_nul = ...  # type: Any
    def emit(self, record: LogRecord) -> None: ...

class SMTPHandler(logging.Handler):
    username = ...  # type: Any
    fromaddr = ...  # type: Any
    toaddrs = ...  # type: Any
    subject = ...  # type: Any
    secure = ...  # type: Any
    timeout = ...  # type: Any
    def __init__(self, mailhost, fromaddr, toaddrs, subject: unicode, credentials: Tuple[Any,Any]=...,
                 secure=...) -> None: ...
    def getSubject(self, record: LogRecord) -> unicode: ...
    def emit(self, record: LogRecord) -> None: ...

class NTEventLogHandler(logging.Handler):
    appname = ...  # type: Any
    dllname = ...  # type: Any
    logtype = ...  # type: Any
    deftype = ...  # type: Any
    typemap = ...  # type: Any
    def __init__(self, appname, dllname=..., logtype: str =...) -> None: ...
    def getMessageID(self, record: LogRecord) -> int: ...
    def getEventCategory(self, record: LogRecord) -> int: ...
    def getEventType(self, record: LogRecord): ...
    def emit(self, record: LogRecord) -> None: ...
    def close(self) -> None: ...

class HTTPHandler(logging.Handler):
    host = ...  # type: Any
    url = ...  # type: Any
    method = ...  # type: Any
    secure = ...  # type: Any
    credentials = ...  # type: Any
    def __init__(self, host, url, method: str =..., secure=..., credentials=...) -> None: ...
    def mapLogRecord(self, record: LogRecord) -> dict[Any,Any]: ...
    def emit(self, record: LogRecord) -> None: ...

class BufferingHandler(logging.Handler):
    capacity = ...  # type: Any
    buffer = ...  # type: Any
    def __init__(self, capacity: int) -> None: ...
    def shouldFlush(self, record: LogRecord) -> bool: ...
    def emit(self, record: LogRecord) -> None: ...
    def flush(self) -> None: ...
    def close(self) -> None: ...

class MemoryHandler(BufferingHandler):
    flushLevel = ...  # type: Any
    target = ...  # type: Any
    def __init__(self, capacity: int, flushLevel: int =..., target=...) -> None: ...
    def shouldFlush(self, record: LogRecord) -> bool: ...
    def setTarget(self, target) -> None: ...
    buffer = ...  # type: Any
    def flush(self) -> None: ...
    def close(self) -> None: ...

class QueueHandler(logging.Handler):
    queue = ...  # type: Any
    def __init__(self, queue) -> None: ...
    def enqueue(self, record: LogRecord): ...
    def prepare(self, record: LogRecord): ...
    def emit(self, record: LogRecord) -> None: ...

class QueueListener:
    queue = ...  # type: Any
    handlers = ...  # type: Any
    def __init__(self, queue, *handlers) -> None: ...
    def dequeue(self, block): ...
    def start(self) -> None: ...
    def prepare(self, record: LogRecord): ...
    def handle(self, record: LogRecord): ...
    def enqueue_sentinel(self): ...
    def stop(self) -> None: ...

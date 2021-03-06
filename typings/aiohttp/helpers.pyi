"""
This type stub file was generated by pyright.
"""

import asyncio
import datetime
import functools
import netrc
import os
import re
import sys
import async_timeout
import attr
from collections import namedtuple
from types import TracebackType
from typing import Any, Callable, Dict, Iterable, Iterator, Mapping, Optional, Pattern, Set, Tuple, Type, TypeVar, Union
from yarl import URL

"""Various helper functions"""
__all__ = ('BasicAuth', 'ChainMapProxy')
PY_36 = sys.version_info >= (3, 6)
PY_37 = sys.version_info >= (3, 7)
PY_38 = sys.version_info >= (3, 8)
if not PY_37:
    ...
def all_tasks(loop: Optional[asyncio.AbstractEventLoop] = ...) -> Set[asyncio.Task[Any]]:
    ...

if PY_37:
    all_tasks = getattr(asyncio, 'all_tasks')
_T = TypeVar('_T')
sentinel = object()
NO_EXTENSIONS = bool(os.environ.get('AIOHTTP_NO_EXTENSIONS'))
DEBUG = getattr(sys.flags, 'dev_mode', False) or not sys.flags.ignore_environment and bool(os.environ.get('PYTHONASYNCIODEBUG'))
CHAR = set(chr(i) for i in range(0, 128))
CTL = set(chr(i) for i in range(0, 32)) | chr(127)
SEPARATORS = '(', ')', '<', '>', '@', ',', ';', ':', '\\', '"', '/', '[', ']', '?', '=', '{', '}', ' ', chr(9)
TOKEN = CHAR ^ CTL ^ SEPARATORS
coroutines = asyncio.coroutines
old_debug = coroutines._DEBUG
@asyncio.coroutine
def noop(*args, **kwargs):
    ...

async def noop2(*args: Any, **kwargs: Any) -> None:
    ...

class BasicAuth(namedtuple('BasicAuth', ['login', 'password', 'encoding'])):
    """Http basic authentication helper."""
    def __new__(cls, login: str, password: str = ..., encoding: str = ...) -> BasicAuth:
        ...
    
    @classmethod
    def decode(cls, auth_header: str, encoding: str = ...) -> BasicAuth:
        """Create a BasicAuth object from an Authorization HTTP header."""
        ...
    
    @classmethod
    def from_url(cls, url: URL, *, encoding: str = ...) -> Optional[BasicAuth]:
        """Create BasicAuth from url."""
        ...
    
    def encode(self) -> str:
        """Encode credentials."""
        ...
    


def strip_auth_from_url(url: URL) -> Tuple[URL, Optional[BasicAuth]]:
    ...

def netrc_from_env() -> Optional[netrc.netrc]:
    """Attempt to load the netrc file from the path specified by the env-var
    NETRC or in the default location in the user's home directory.

    Returns None if it couldn't be found or fails to parse.
    """
    ...

@attr.s(frozen=True, slots=True)
class ProxyInfo:
    proxy = ...
    proxy_auth = ...


def proxies_from_env() -> Dict[str, ProxyInfo]:
    ...

def current_task(loop: Optional[asyncio.AbstractEventLoop] = ...) -> asyncio.Task:
    ...

def get_running_loop(loop: Optional[asyncio.AbstractEventLoop] = ...) -> asyncio.AbstractEventLoop:
    ...

def isasyncgenfunction(obj: Any) -> bool:
    ...

@attr.s(frozen=True, slots=True)
class MimeType:
    type = ...
    subtype = ...
    suffix = ...
    parameters = ...


@functools.lru_cache(maxsize=56)
def parse_mimetype(mimetype: str) -> MimeType:
    """Parses a MIME type into its components.

    mimetype is a MIME type string.

    Returns a MimeType object.

    Example:

    >>> parse_mimetype('text/html; charset=utf-8')
    MimeType(type='text', subtype='html', suffix='',
             parameters={'charset': 'utf-8'})

    """
    ...

def guess_filename(obj: Any, default: Optional[str] = ...) -> Optional[str]:
    ...

def content_disposition_header(disptype: str, quote_fields: bool = ..., **params: str) -> str:
    """Sets ``Content-Disposition`` header.

    disptype is a disposition type: inline, attachment, form-data.
    Should be valid extension token (see RFC 2183)

    params is a dict with disposition params.
    """
    ...

class reify:
    """Use as a class method decorator.  It operates almost exactly like
    the Python `@property` decorator, but it puts the result of the
    method it decorates into the instance dict after the first call,
    effectively replacing the function it decorates with an instance
    variable.  It is, in Python parlance, a data descriptor.

    """
    def __init__(self, wrapped: Callable[..., Any]) -> None:
        self.wrapped = ...
        self.name = ...
    
    def __get__(self, inst: Any, owner: Any) -> Any:
        ...
    
    def __set__(self, inst: Any, value: Any) -> None:
        ...
    


reify_py = reify
_ipv4_pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}' r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
_ipv6_pattern = r'^(?:(?:(?:[A-F0-9]{1,4}:){6}|(?=(?:[A-F0-9]{0,4}:){0,6}' r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}$)(([0-9A-F]{1,4}:){0,5}|:)' r'((:[0-9A-F]{1,4}){1,5}:|:)|::(?:[A-F0-9]{1,4}:){5})' r'(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}' r'(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])|(?:[A-F0-9]{1,4}:){7}' r'[A-F0-9]{1,4}|(?=(?:[A-F0-9]{0,4}:){0,7}[A-F0-9]{0,4}$)' r'(([0-9A-F]{1,4}:){1,7}|:)((:[0-9A-F]{1,4}){1,7}|:)|(?:[A-F0-9]{1,4}:){7}' r':|:(:[A-F0-9]{1,4}){7})$'
_ipv4_regex = re.compile(_ipv4_pattern)
_ipv6_regex = re.compile(_ipv6_pattern, flags=re.IGNORECASE)
_ipv4_regexb = re.compile(_ipv4_pattern.encode('ascii'))
_ipv6_regexb = re.compile(_ipv6_pattern.encode('ascii'), flags=re.IGNORECASE)
def _is_ip_address(regex: Pattern[str], regexb: Pattern[bytes], host: Optional[Union[str, bytes]]) -> bool:
    ...

is_ipv4_address = functools.partial(_is_ip_address, _ipv4_regex, _ipv4_regexb)
is_ipv6_address = functools.partial(_is_ip_address, _ipv6_regex, _ipv6_regexb)
def is_ip_address(host: Optional[Union[str, bytes, bytearray, memoryview]]) -> bool:
    ...

def next_whole_second() -> datetime.datetime:
    """Return current time rounded up to the next whole second."""
    ...

_cached_current_datetime = None
_cached_formatted_datetime = ""
def rfc822_formatted_time() -> str:
    ...

def _weakref_handle(info):
    ...

def weakref_handle(ob, name, timeout, loop, ceil_timeout: bool = ...):
    ...

def call_later(cb, timeout, loop):
    ...

class TimeoutHandle:
    """ Timeout handle """
    def __init__(self, loop: asyncio.AbstractEventLoop, timeout: Optional[float]) -> None:
        ...
    
    def register(self, callback: Callable[..., None], *args: Any, **kwargs: Any) -> None:
        ...
    
    def close(self) -> None:
        ...
    
    def start(self) -> Optional[asyncio.Handle]:
        ...
    
    def timer(self) -> BaseTimerContext:
        ...
    
    def __call__(self) -> None:
        ...
    


class BaseTimerContext(ContextManager['BaseTimerContext']):
    ...


class TimerNoop(BaseTimerContext):
    def __enter__(self) -> BaseTimerContext:
        ...
    
    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[TracebackType]) -> Optional[bool]:
        ...
    


class TimerContext(BaseTimerContext):
    """ Low resolution timeout context manager """
    def __init__(self, loop: asyncio.AbstractEventLoop) -> None:
        ...
    
    def __enter__(self) -> BaseTimerContext:
        ...
    
    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[TracebackType]) -> Optional[bool]:
        ...
    
    def timeout(self) -> None:
        ...
    


class CeilTimeout(async_timeout.timeout):
    def __enter__(self) -> async_timeout.timeout:
        ...
    


class HeadersMixin:
    ATTRS = ...
    _content_type = ...
    _content_dict = ...
    _stored_content_type = ...
    def _parse_content_type(self, raw: str) -> None:
        ...
    
    @property
    def content_type(self) -> str:
        """The value of content part for Content-Type HTTP header."""
        ...
    
    @property
    def charset(self) -> Optional[str]:
        """The value of charset part for Content-Type HTTP header."""
        ...
    
    @property
    def content_length(self) -> Optional[int]:
        """The value of Content-Length HTTP header."""
        ...
    


def set_result(fut: asyncio.Future[_T], result: _T) -> None:
    ...

def set_exception(fut: asyncio.Future[_T], exc: BaseException) -> None:
    ...

class ChainMapProxy(Mapping[str, Any]):
    __slots__ = ...
    def __init__(self, maps: Iterable[Mapping[str, Any]]) -> None:
        ...
    
    def __init_subclass__(cls) -> None:
        ...
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default: Any = ...) -> Any:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __iter__(self) -> Iterator[str]:
        ...
    
    def __contains__(self, key: object) -> bool:
        ...
    
    def __bool__(self) -> bool:
        ...
    
    def __repr__(self) -> str:
        ...
    



"""
This type stub file was generated by pyright.
"""

import attr
from types import SimpleNamespace
from typing import Awaitable, Callable, TYPE_CHECKING, Type, Union
from multidict import CIMultiDict
from yarl import URL
from .client_reqrep import ClientResponse
from .signals import Signal
from .client import ClientSession

if TYPE_CHECKING:
    _SignalArgs = Union['TraceRequestStartParams', 'TraceRequestEndParams', 'TraceRequestExceptionParams', 'TraceConnectionQueuedStartParams', 'TraceConnectionQueuedEndParams', 'TraceConnectionCreateStartParams', 'TraceConnectionCreateEndParams', 'TraceConnectionReuseconnParams', 'TraceDnsResolveHostStartParams', 'TraceDnsResolveHostEndParams', 'TraceDnsCacheHitParams', 'TraceDnsCacheMissParams', 'TraceRequestRedirectParams', 'TraceRequestChunkSentParams', 'TraceResponseChunkReceivedParams']
    _Signal = Signal[Callable[[ClientSession, SimpleNamespace, _SignalArgs], Awaitable[None]]]
else:
    _Signal = Signal
__all__ = ('TraceConfig', 'TraceRequestStartParams', 'TraceRequestEndParams', 'TraceRequestExceptionParams', 'TraceConnectionQueuedStartParams', 'TraceConnectionQueuedEndParams', 'TraceConnectionCreateStartParams', 'TraceConnectionCreateEndParams', 'TraceConnectionReuseconnParams', 'TraceDnsResolveHostStartParams', 'TraceDnsResolveHostEndParams', 'TraceDnsCacheHitParams', 'TraceDnsCacheMissParams', 'TraceRequestRedirectParams', 'TraceRequestChunkSentParams', 'TraceResponseChunkReceivedParams')
class TraceConfig:
    """First-class used to trace requests launched via ClientSession
    objects."""
    def __init__(self, trace_config_ctx_factory: Type[SimpleNamespace] = ...) -> None:
        ...
    
    def trace_config_ctx(self, trace_request_ctx: SimpleNamespace = ...) -> SimpleNamespace:
        """ Return a new trace_config_ctx instance """
        ...
    
    def freeze(self) -> None:
        ...
    
    @property
    def on_request_start(self) -> _Signal:
        ...
    
    @property
    def on_request_chunk_sent(self) -> _Signal:
        ...
    
    @property
    def on_response_chunk_received(self) -> _Signal:
        ...
    
    @property
    def on_request_end(self) -> _Signal:
        ...
    
    @property
    def on_request_exception(self) -> _Signal:
        ...
    
    @property
    def on_request_redirect(self) -> _Signal:
        ...
    
    @property
    def on_connection_queued_start(self) -> _Signal:
        ...
    
    @property
    def on_connection_queued_end(self) -> _Signal:
        ...
    
    @property
    def on_connection_create_start(self) -> _Signal:
        ...
    
    @property
    def on_connection_create_end(self) -> _Signal:
        ...
    
    @property
    def on_connection_reuseconn(self) -> _Signal:
        ...
    
    @property
    def on_dns_resolvehost_start(self) -> _Signal:
        ...
    
    @property
    def on_dns_resolvehost_end(self) -> _Signal:
        ...
    
    @property
    def on_dns_cache_hit(self) -> _Signal:
        ...
    
    @property
    def on_dns_cache_miss(self) -> _Signal:
        ...
    


@attr.s(frozen=True, slots=True)
class TraceRequestStartParams:
    """ Parameters sent by the `on_request_start` signal"""
    method = ...
    url = ...
    headers = ...


@attr.s(frozen=True, slots=True)
class TraceRequestChunkSentParams:
    """ Parameters sent by the `on_request_chunk_sent` signal"""
    chunk = ...


@attr.s(frozen=True, slots=True)
class TraceResponseChunkReceivedParams:
    """ Parameters sent by the `on_response_chunk_received` signal"""
    chunk = ...


@attr.s(frozen=True, slots=True)
class TraceRequestEndParams:
    """ Parameters sent by the `on_request_end` signal"""
    method = ...
    url = ...
    headers = ...
    response = ...


@attr.s(frozen=True, slots=True)
class TraceRequestExceptionParams:
    """ Parameters sent by the `on_request_exception` signal"""
    method = ...
    url = ...
    headers = ...
    exception = ...


@attr.s(frozen=True, slots=True)
class TraceRequestRedirectParams:
    """ Parameters sent by the `on_request_redirect` signal"""
    method = ...
    url = ...
    headers = ...
    response = ...


@attr.s(frozen=True, slots=True)
class TraceConnectionQueuedStartParams:
    """ Parameters sent by the `on_connection_queued_start` signal"""
    ...


@attr.s(frozen=True, slots=True)
class TraceConnectionQueuedEndParams:
    """ Parameters sent by the `on_connection_queued_end` signal"""
    ...


@attr.s(frozen=True, slots=True)
class TraceConnectionCreateStartParams:
    """ Parameters sent by the `on_connection_create_start` signal"""
    ...


@attr.s(frozen=True, slots=True)
class TraceConnectionCreateEndParams:
    """ Parameters sent by the `on_connection_create_end` signal"""
    ...


@attr.s(frozen=True, slots=True)
class TraceConnectionReuseconnParams:
    """ Parameters sent by the `on_connection_reuseconn` signal"""
    ...


@attr.s(frozen=True, slots=True)
class TraceDnsResolveHostStartParams:
    """ Parameters sent by the `on_dns_resolvehost_start` signal"""
    host = ...


@attr.s(frozen=True, slots=True)
class TraceDnsResolveHostEndParams:
    """ Parameters sent by the `on_dns_resolvehost_end` signal"""
    host = ...


@attr.s(frozen=True, slots=True)
class TraceDnsCacheHitParams:
    """ Parameters sent by the `on_dns_cache_hit` signal"""
    host = ...


@attr.s(frozen=True, slots=True)
class TraceDnsCacheMissParams:
    """ Parameters sent by the `on_dns_cache_miss` signal"""
    host = ...


class Trace:
    """ Internal class used to keep together the main dependencies used
    at the moment of send a signal."""
    def __init__(self, session: ClientSession, trace_config: TraceConfig, trace_config_ctx: SimpleNamespace) -> None:
        ...
    
    async def send_request_start(self, method: str, url: URL, headers: CIMultiDict[str]) -> None:
        ...
    
    async def send_request_chunk_sent(self, chunk: bytes) -> None:
        ...
    
    async def send_response_chunk_received(self, chunk: bytes) -> None:
        ...
    
    async def send_request_end(self, method: str, url: URL, headers: CIMultiDict[str], response: ClientResponse) -> None:
        ...
    
    async def send_request_exception(self, method: str, url: URL, headers: CIMultiDict[str], exception: BaseException) -> None:
        ...
    
    async def send_request_redirect(self, method: str, url: URL, headers: CIMultiDict[str], response: ClientResponse) -> None:
        ...
    
    async def send_connection_queued_start(self) -> None:
        ...
    
    async def send_connection_queued_end(self) -> None:
        ...
    
    async def send_connection_create_start(self) -> None:
        ...
    
    async def send_connection_create_end(self) -> None:
        ...
    
    async def send_connection_reuseconn(self) -> None:
        ...
    
    async def send_dns_resolvehost_start(self, host: str) -> None:
        ...
    
    async def send_dns_resolvehost_end(self, host: str) -> None:
        ...
    
    async def send_dns_cache_hit(self, host: str) -> None:
        ...
    
    async def send_dns_cache_miss(self, host: str) -> None:
        ...
    



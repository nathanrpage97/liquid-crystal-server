"""
This type stub file was generated by pyright.
"""

import collections
from typing import Any, Optional

"""Resource CORS options class definition.
"""
__all__ = ("ResourceOptions", )
def _is_proper_sequence(seq):
    """Returns is seq is sequence and not string."""
    ...

class ResourceOptions(collections.namedtuple("Base", ("allow_credentials", "expose_headers", "allow_headers", "max_age", "allow_methods"))):
    """Resource CORS options."""
    __slots__ = ...
    def __init__(self, *, allow_credentials: bool = ..., expose_headers=..., allow_headers=..., max_age: Optional[Any] = ..., allow_methods: Optional[Any] = ...):
        """Construct resource CORS options.

        Options will be normalized.

        :param allow_credentials:
            Is passing client credentials to the resource from other origin
            is allowed.
            See <http://www.w3.org/TR/cors/#user-credentials> for
            the definition.
        :type allow_credentials: bool
            Is passing client credentials to the resource from other origin
            is allowed.

        :param expose_headers:
            Server headers that are allowed to be exposed to the client.
            Simple response headers are excluded from this set, see
            <http://www.w3.org/TR/cors/#list-of-exposed-headers>.
        :type expose_headers: sequence of strings or ``*`` string.

        :param allow_headers:
            Client headers that are allowed to be passed to the resource.
            See <http://www.w3.org/TR/cors/#list-of-headers>.
        :type allow_headers: sequence of strings or ``*`` string.

        :param max_age:
            How long the results of a preflight request can be cached in a
            preflight result cache (in seconds).
            See <http://www.w3.org/TR/cors/#http-access-control-max-age>.

        :param allow_methods:
            List of allowed methods or ``*``string. Can be used in resource or
            global defaults, but not in specific route.

            It's not required to specify all allowed methods for specific
            resource, routes that have explicit CORS configuration will be
            treated as if their methods are allowed.
        """
        ...
    
    def __new__(cls, *, allow_credentials: bool = ..., expose_headers=..., allow_headers=..., max_age: Optional[Any] = ..., allow_methods: Optional[Any] = ...):
        """Normalize source parameters and store them in namedtuple."""
        ...
    
    def is_method_allowed(self, method):
        ...
    


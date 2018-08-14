from typing import Any, Callable, Optional, Set, Tuple, Type, Union

from django.contrib.auth.mixins import AccessMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.middleware.cache import CacheMiddleware
from django.test.testcases import LiveServerTestCase
from django.utils.deprecation import MiddlewareMixin
from django.views.generic.base import TemplateResponseMixin, View


class classonlymethod(classmethod):
    def __get__(
        self,
        instance: Optional[View],
        cls: Type[
            Union[AccessMixin, SuccessMessageMixin, TemplateResponseMixin, View]
        ] = ...,
    ) -> Callable: ...

def method_decorator(
    decorator: Union[Callable, Set[Callable], Tuple[Callable, Callable]],
    name: str = ...,
) -> Callable: ...
def decorator_from_middleware_with_args(
    middleware_class: Type[CacheMiddleware]
) -> Callable: ...
def decorator_from_middleware(
    middleware_class: Type[MiddlewareMixin]
) -> Callable: ...
def available_attrs(fn: Any): ...
def make_middleware_decorator(
    middleware_class: Type[MiddlewareMixin]
) -> Callable: ...

class classproperty:
    fget: Optional[Callable] = ...
    def __init__(self, method: Optional[Callable] = ...) -> None: ...
    def __get__(
        self,
        instance: Optional[LiveServerTestCase],
        cls: Type[LiveServerTestCase] = ...,
    ) -> str: ...
    def getter(self, method: Callable) -> classproperty: ...

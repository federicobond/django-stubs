from contextlib import ContextDecorator
from datetime import date, datetime, timedelta, tzinfo
from typing import Any, Optional, Union


class FixedOffset(tzinfo):
    def __init__(
        self, offset: Optional[float] = ..., name: Optional[str] = ...
    ) -> None: ...
    def utcoffset(self, dt: Union[datetime, str]) -> timedelta: ...
    def tzname(self, dt: Optional[Union[datetime, str]]) -> str: ...
    def dst(self, dt: datetime) -> timedelta: ...

utc: Any

def get_fixed_timezone(offset: Union[timedelta, int]) -> FixedOffset: ...
def get_default_timezone(): ...
def get_default_timezone_name() -> str: ...
def get_current_timezone() -> FixedOffset: ...
def get_current_timezone_name() -> str: ...
def activate(timezone: Optional[Union[FixedOffset, str]]) -> None: ...
def deactivate() -> None: ...

class override(ContextDecorator):
    timezone: Optional[Union[django.utils.timezone.FixedOffset, str]] = ...
    def __init__(self, timezone: Optional[Union[FixedOffset, str]]) -> None: ...
    old_timezone: Optional[django.utils.timezone.FixedOffset] = ...
    def __enter__(self) -> None: ...
    def __exit__(
        self, exc_type: None, exc_value: None, traceback: None
    ) -> None: ...

def localtime(
    value: Optional[datetime] = ..., timezone: Optional[FixedOffset] = ...
) -> datetime: ...
def now() -> datetime: ...
def is_aware(value: datetime) -> bool: ...
def is_naive(value: datetime) -> bool: ...
def make_aware(
    value: datetime,
    timezone: Optional[FixedOffset] = ...,
    is_dst: Optional[bool] = ...,
) -> datetime: ...
def make_naive(
    value: datetime, timezone: Optional[FixedOffset] = ...
) -> datetime: ...

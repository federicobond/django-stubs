from typing import Any, Callable, Dict, List, Optional, Type, Union

from django.core.handlers.wsgi import WSGIRequest
from django.http.request import QueryDict
from django.http.response import Http404, HttpResponse
from django.utils.safestring import SafeText

DEBUG_ENGINE: Any
HIDDEN_SETTINGS: Any
CLEANSED_SUBSTITUTE: str
CURRENT_DIR: Any

class CallableSettingWrapper:
    def __init__(
        self, callable_setting: Union[Callable, Type[Any]]
    ) -> None: ...

def cleanse_setting(key: Union[int, str], value: Any) -> Any: ...
def get_safe_settings() -> Dict[str, Any]: ...
def technical_500_response(
    request: Any, exc_type: Any, exc_value: Any, tb: Any, status_code: int = ...
): ...
def get_default_exception_reporter_filter() -> SafeExceptionReporterFilter: ...
def get_exception_reporter_filter(
    request: Optional[WSGIRequest]
) -> SafeExceptionReporterFilter: ...

class ExceptionReporterFilter:
    def get_post_parameters(self, request: Any): ...
    def get_traceback_frame_variables(self, request: Any, tb_frame: Any): ...

class SafeExceptionReporterFilter(ExceptionReporterFilter):
    def is_active(self, request: Optional[WSGIRequest]) -> bool: ...
    def get_cleansed_multivaluedict(
        self, request: WSGIRequest, multivaluedict: QueryDict
    ) -> QueryDict: ...
    def get_post_parameters(
        self, request: Optional[WSGIRequest]
    ) -> Union[Dict[Any, Any], QueryDict]: ...
    def cleanse_special_types(
        self, request: Optional[WSGIRequest], value: Any
    ) -> Any: ...
    def get_traceback_frame_variables(self, request: Any, tb_frame: Any): ...

class ExceptionReporter:
    request: Optional[django.core.handlers.wsgi.WSGIRequest] = ...
    filter: django.views.debug.SafeExceptionReporterFilter = ...
    exc_type: None = ...
    exc_value: Optional[str] = ...
    tb: None = ...
    is_email: bool = ...
    template_info: None = ...
    template_does_not_exist: bool = ...
    postmortem: None = ...
    def __init__(
        self,
        request: Optional[WSGIRequest],
        exc_type: None,
        exc_value: Optional[str],
        tb: None,
        is_email: bool = ...,
    ) -> None: ...
    def get_traceback_data(self) -> Dict[str, Any]: ...
    def get_traceback_html(self) -> SafeText: ...
    def get_traceback_text(self) -> SafeText: ...
    def get_traceback_frames(self) -> List[Any]: ...

def technical_404_response(
    request: WSGIRequest, exception: Http404
) -> HttpResponse: ...
def default_urlconf(request: WSGIRequest) -> HttpResponse: ...

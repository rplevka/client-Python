from reportportal_client.core.rp_file import RPFile as RPFile
from reportportal_client.core.rp_issues import Issue as Issue
from reportportal_client.core.rp_responses import RPResponse as RPResponse
from reportportal_client.static.abstract import AbstractBaseClass
from reportportal_client.static.defines import Priority as Priority
from typing import Any, Callable, ByteString, Dict, IO, List, Optional, Text, Union

class HttpRequest:
    session_method: Callable = ...
    url: Text = ...
    data = Optional[Union[Dict, List[Union[tuple, ByteString]], IO]] = ...
    json = Optional[Dict] = ...
    def __init__(self,
                 session_method: Callable,
                 url: Text,
                 data = Optional[Union[Dict, List[Union[tuple, ByteString, IO]]]],
                 json = Optional[Dict]) -> None: ...
    def make(self) -> RPResponse: ...


class RPRequestBase(metaclass=AbstractBaseClass):
    __metaclass__: AbstractBaseClass = ...
    _http_request: Optional[HttpRequest] = ...
    _priority: Priority = ...
    _response: Optional[RPResponse] = ...
    def __init__(self) -> None: ...
    def __ge__(self, other: RPRequestBase) -> bool: ...
    @property
    def http_request(self) -> HttpRequest: ...
    @http_request.setter
    def http_request(self, value: HttpRequest) -> None: ...
    @property
    def priority(self) -> Priority: ...
    @priority.setter
    def priority(self, value: Priority) -> None: ...
    @property
    def response(self) -> Optional[RPResponse]: ...
    @response.setter
    def response(self, value: RPResponse) -> None: ...
    def payload(self) -> Dict: ...

class LaunchStartRequest(RPRequestBase):
    attributes: List = ...
    description: Text = ...
    mode: Text = ...
    name: Text = ...
    rerun: bool = ...
    rerun_of: Text = ...
    start_time: Text = ...
    uuid: Text = ...
    def __init__(self,
                 name: Text,
                 start_time: Text,
                 attributes: Optional[List] = ...,
                 description: Optional[Text] = ...,
                 mode: Text = ...,
                 rerun: bool = ...,
                 rerun_of: Optional[Text] = ...,
                 uuid: Optional[Text] = ...) -> None: ...
    @property
    def payload(self) -> Dict: ...

class LaunchFinishRequest(RPRequestBase):
    attributes: List = ...
    description: Text = ...
    end_time: Text = ...
    status: Text = ...
    def __init__(self,
                 end_time: Text,
                 status: Optional[Text] = ...,
                 attributes: Optional[List] = ...,
                 description: Optional[Text] = ...) -> None: ...
    @property
    def payload(self) -> Dict: ...

class ItemStartRequest(RPRequestBase):
    attributes: List = ...
    code_ref: Text = ...
    description: Text = ...
    has_stats: bool = ...
    launch_uuid: Text = ...
    name: Text = ...
    parameters: List = ...
    retry: bool = ...
    start_time: Text = ...
    type_: Text = ...
    uuid: Text = ...
    unique_id: Text = ...
    def __init__(self,
                 name: Text,
                 start_time: Text,
                 type_: Text,
                 launch_uuid: Text,
                 attributes: Optional[List] = ...,
                 code_ref: Optional[Text] = ...,
                 description: Optional[Text] = ...,
                 has_stats: bool = ...,
                 parameters: Optional[List] = ...,
                 retry: bool = ...,
                 uuid: Optional[Any] = ...,
                 unique_id: Optional[Any] = ...) -> None: ...
    @property
    def payload(self) -> Dict: ...

class ItemFinishRequest(RPRequestBase):
    attributes: List = ...
    description: Text = ...
    end_time: Text = ...
    issue: Issue = ...
    launch_uuid: Text = ...
    status: Text = ...
    retry: bool = ...
    def __init__(self,
                 end_time: Text,
                 launch_uuid: Text,
                 status: Text,
                 attributes: Optional[List] = ...,
                 description: Optional[Any] = ...,
                 issue: Optional[Issue] = ...,
                 retry: bool = ...) -> None: ...
    @property
    def payload(self) -> Dict: ...

class RPRequestLog(RPRequestBase):
    file: RPFile = ...
    launch_uuid: Text = ...
    level: Text = ...
    message: Text = ...
    time: Text = ...
    item_uuid: Text = ...
    def __init__(self,
                 launch_uuid: Text,
                 time: Text,
                 file: Optional[RPFile] = ...,
                 item_uuid: Optional[Text] = ...,
                 level: Text = ...,
                 message: Optional[Text] = ...) -> None: ...
    def __file(self) -> Dict: ...
    @property
    def payload(self) -> Dict: ...

class RPLogBatch(RPRequestBase):
    default_content: Text = ...
    log_reqs: List[RPRequestLog] = ...
    def __init__(self, log_reqs: List[RPRequestLog]) -> None: ...
    def __get_file(self, rp_file: RPFile) -> tuple: ...
    def __get_files(self) -> List: ...
    def __get_request_part(self) -> Dict: ...
    @property
    def payload(self) -> Dict: ...

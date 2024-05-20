"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import error_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.wrappers_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _View:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ViewEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_View.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    LEFT: _View.ValueType  # 0
    RIGHT: _View.ValueType  # 1

class View(_View, metaclass=_ViewEnumTypeWrapper): ...

LEFT: View.ValueType  # 0
RIGHT: View.ValueType  # 1
global___View = View

@typing.final
class VideoAck(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    @property
    def success(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def error(self) -> error_pb2.Error: ...
    def __init__(
        self,
        *,
        success: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        error: error_pb2.Error | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["error", b"error", "success", b"success"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["error", b"error", "success", b"success"]) -> None: ...

global___VideoAck = VideoAck

@typing.final
class CameraInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MXID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    STEREO_FIELD_NUMBER: builtins.int
    DEPTH_FIELD_NUMBER: builtins.int
    mxid: builtins.str
    name: builtins.str
    stereo: builtins.bool
    depth: builtins.bool
    def __init__(
        self,
        *,
        mxid: builtins.str = ...,
        name: builtins.str = ...,
        stereo: builtins.bool = ...,
        depth: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["depth", b"depth", "mxid", b"mxid", "name", b"name", "stereo", b"stereo"]) -> None: ...

global___CameraInfo = CameraInfo

@typing.final
class ListOfCameraInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CAMERA_INFO_FIELD_NUMBER: builtins.int
    @property
    def camera_info(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CameraInfo]: ...
    def __init__(
        self,
        *,
        camera_info: collections.abc.Iterable[global___CameraInfo] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["camera_info", b"camera_info"]) -> None: ...

global___ListOfCameraInfo = ListOfCameraInfo

@typing.final
class Frame(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    data: builtins.bytes
    def __init__(
        self,
        *,
        data: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["data", b"data"]) -> None: ...

global___Frame = Frame

@typing.final
class IntrinsicMatrix(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    K_FIELD_NUMBER: builtins.int
    K: builtins.bytes
    def __init__(
        self,
        *,
        K: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["K", b"K"]) -> None: ...

global___IntrinsicMatrix = IntrinsicMatrix

@typing.final
class ViewRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CAMERA_INFO_FIELD_NUMBER: builtins.int
    VIEW_FIELD_NUMBER: builtins.int
    view: global___View.ValueType
    @property
    def camera_info(self) -> global___CameraInfo: ...
    def __init__(
        self,
        *,
        camera_info: global___CameraInfo | None = ...,
        view: global___View.ValueType | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_view", b"_view", "camera_info", b"camera_info", "view", b"view"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_view", b"_view", "camera_info", b"camera_info", "view", b"view"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_view", b"_view"]) -> typing.Literal["view"] | None: ...

global___ViewRequest = ViewRequest

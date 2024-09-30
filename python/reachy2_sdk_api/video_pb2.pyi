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
import google.protobuf.timestamp_pb2
import google.protobuf.wrappers_pb2
import kinematics_pb2
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
    DEPTH: _View.ValueType  # 2

class View(_View, metaclass=_ViewEnumTypeWrapper): ...

LEFT: View.ValueType  # 0
RIGHT: View.ValueType  # 1
DEPTH: View.ValueType  # 2
global___View = View

@typing_extensions.final
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
    def HasField(self, field_name: typing_extensions.Literal["error", b"error", "success", b"success"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["error", b"error", "success", b"success"]) -> None: ...

global___VideoAck = VideoAck

@typing_extensions.final
class CameraFeatures(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    STEREO_FIELD_NUMBER: builtins.int
    DEPTH_FIELD_NUMBER: builtins.int
    name: builtins.str
    stereo: builtins.bool
    depth: builtins.bool
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        stereo: builtins.bool = ...,
        depth: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["depth", b"depth", "name", b"name", "stereo", b"stereo"]) -> None: ...

global___CameraFeatures = CameraFeatures

@typing_extensions.final
class CameraParameters(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEIGHT_FIELD_NUMBER: builtins.int
    WIDTH_FIELD_NUMBER: builtins.int
    DISTORTION_MODEL_FIELD_NUMBER: builtins.int
    D_FIELD_NUMBER: builtins.int
    K_FIELD_NUMBER: builtins.int
    R_FIELD_NUMBER: builtins.int
    P_FIELD_NUMBER: builtins.int
    height: builtins.int
    width: builtins.int
    distortion_model: builtins.str
    @property
    def D(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    @property
    def K(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    @property
    def R(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    @property
    def P(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    def __init__(
        self,
        *,
        height: builtins.int = ...,
        width: builtins.int = ...,
        distortion_model: builtins.str = ...,
        D: collections.abc.Iterable[builtins.float] | None = ...,
        K: collections.abc.Iterable[builtins.float] | None = ...,
        R: collections.abc.Iterable[builtins.float] | None = ...,
        P: collections.abc.Iterable[builtins.float] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["D", b"D", "K", b"K", "P", b"P", "R", b"R", "distortion_model", b"distortion_model", "height", b"height", "width", b"width"]) -> None: ...

global___CameraParameters = CameraParameters

@typing_extensions.final
class CameraExtrinsics(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EXTRINCICS_FIELD_NUMBER: builtins.int
    @property
    def extrincics(self) -> kinematics_pb2.Matrix4x4: ...
    def __init__(
        self,
        *,
        extrincics: kinematics_pb2.Matrix4x4 | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["extrincics", b"extrincics"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["extrincics", b"extrincics"]) -> None: ...

global___CameraExtrinsics = CameraExtrinsics

@typing_extensions.final
class ListOfCameraFeatures(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CAMERA_FEAT_FIELD_NUMBER: builtins.int
    @property
    def camera_feat(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CameraFeatures]: ...
    def __init__(
        self,
        *,
        camera_feat: collections.abc.Iterable[global___CameraFeatures] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["camera_feat", b"camera_feat"]) -> None: ...

global___ListOfCameraFeatures = ListOfCameraFeatures

@typing_extensions.final
class Frame(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIMESTAMP_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    data: builtins.bytes
    def __init__(
        self,
        *,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        data: builtins.bytes = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["timestamp", b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data", "timestamp", b"timestamp"]) -> None: ...

global___Frame = Frame

@typing_extensions.final
class FrameRaw(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIMESTAMP_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    WIDTH_FIELD_NUMBER: builtins.int
    ENCODING_FIELD_NUMBER: builtins.int
    STEP_FIELD_NUMBER: builtins.int
    ISBIGENDIAN_FIELD_NUMBER: builtins.int
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    data: builtins.bytes
    height: builtins.int
    width: builtins.int
    encoding: builtins.str
    step: builtins.int
    isbigendian: builtins.bool
    def __init__(
        self,
        *,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        data: builtins.bytes = ...,
        height: builtins.int = ...,
        width: builtins.int = ...,
        encoding: builtins.str = ...,
        step: builtins.int = ...,
        isbigendian: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["timestamp", b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data", "encoding", b"encoding", "height", b"height", "isbigendian", b"isbigendian", "step", b"step", "timestamp", b"timestamp", "width", b"width"]) -> None: ...

global___FrameRaw = FrameRaw

@typing_extensions.final
class ViewRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CAMERA_FEAT_FIELD_NUMBER: builtins.int
    VIEW_FIELD_NUMBER: builtins.int
    @property
    def camera_feat(self) -> global___CameraFeatures: ...
    view: global___View.ValueType
    def __init__(
        self,
        *,
        camera_feat: global___CameraFeatures | None = ...,
        view: global___View.ValueType | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_view", b"_view", "camera_feat", b"camera_feat", "view", b"view"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_view", b"_view", "camera_feat", b"camera_feat", "view", b"view"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_view", b"_view"]) -> typing_extensions.Literal["view"] | None: ...

global___ViewRequest = ViewRequest

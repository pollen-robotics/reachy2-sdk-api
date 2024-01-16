"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.wrappers_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Matrix4x4(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    @property
    def data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    def __init__(
        self,
        *,
        data: collections.abc.Iterable[builtins.float] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data"]) -> None: ...

global___Matrix4x4 = Matrix4x4

@typing_extensions.final
class Matrix3x3(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    @property
    def data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    def __init__(
        self,
        *,
        data: collections.abc.Iterable[builtins.float] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data"]) -> None: ...

global___Matrix3x3 = Matrix3x3

@typing_extensions.final
class Quaternion(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    W_FIELD_NUMBER: builtins.int
    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    Z_FIELD_NUMBER: builtins.int
    w: builtins.float
    x: builtins.float
    y: builtins.float
    z: builtins.float
    def __init__(
        self,
        *,
        w: builtins.float = ...,
        x: builtins.float = ...,
        y: builtins.float = ...,
        z: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["w", b"w", "x", b"x", "y", b"y", "z", b"z"]) -> None: ...

global___Quaternion = Quaternion

@typing_extensions.final
class Rotation3d(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    Q_FIELD_NUMBER: builtins.int
    RPY_FIELD_NUMBER: builtins.int
    MATRIX_FIELD_NUMBER: builtins.int
    @property
    def q(self) -> global___Quaternion: ...
    @property
    def rpy(self) -> global___ExtEulerAngles: ...
    @property
    def matrix(self) -> global___Matrix3x3: ...
    def __init__(
        self,
        *,
        q: global___Quaternion | None = ...,
        rpy: global___ExtEulerAngles | None = ...,
        matrix: global___Matrix3x3 | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["matrix", b"matrix", "q", b"q", "rotation", b"rotation", "rpy", b"rpy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["matrix", b"matrix", "q", b"q", "rotation", b"rotation", "rpy", b"rpy"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["rotation", b"rotation"]) -> typing_extensions.Literal["q", "rpy", "matrix"] | None: ...

global___Rotation3d = Rotation3d

@typing_extensions.final
class Point(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    Z_FIELD_NUMBER: builtins.int
    x: builtins.float
    y: builtins.float
    z: builtins.float
    def __init__(
        self,
        *,
        x: builtins.float = ...,
        y: builtins.float = ...,
        z: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["x", b"x", "y", b"y", "z", b"z"]) -> None: ...

global___Point = Point

@typing_extensions.final
class ExtEulerAngles(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROLL_FIELD_NUMBER: builtins.int
    PITCH_FIELD_NUMBER: builtins.int
    YAW_FIELD_NUMBER: builtins.int
    @property
    def roll(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def pitch(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def yaw(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    def __init__(
        self,
        *,
        roll: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        pitch: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        yaw: google.protobuf.wrappers_pb2.FloatValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pitch", b"pitch", "roll", b"roll", "yaw", b"yaw"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["pitch", b"pitch", "roll", b"roll", "yaw", b"yaw"]) -> None: ...

global___ExtEulerAngles = ExtEulerAngles

@typing_extensions.final
class PointDistanceTolerances(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    X_TOL_FIELD_NUMBER: builtins.int
    Y_TOL_FIELD_NUMBER: builtins.int
    Z_TOL_FIELD_NUMBER: builtins.int
    x_tol: builtins.float
    y_tol: builtins.float
    z_tol: builtins.float
    def __init__(
        self,
        *,
        x_tol: builtins.float = ...,
        y_tol: builtins.float = ...,
        z_tol: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["x_tol", b"x_tol", "y_tol", b"y_tol", "z_tol", b"z_tol"]) -> None: ...

global___PointDistanceTolerances = PointDistanceTolerances

@typing_extensions.final
class ExtEulerAnglesTolerances(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROLL_TOL_FIELD_NUMBER: builtins.int
    PITCH_TOL_FIELD_NUMBER: builtins.int
    YAW_TOL_FIELD_NUMBER: builtins.int
    roll_tol: builtins.float
    pitch_tol: builtins.float
    yaw_tol: builtins.float
    def __init__(
        self,
        *,
        roll_tol: builtins.float = ...,
        pitch_tol: builtins.float = ...,
        yaw_tol: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pitch_tol", b"pitch_tol", "roll_tol", b"roll_tol", "yaw_tol", b"yaw_tol"]) -> None: ...

global___ExtEulerAnglesTolerances = ExtEulerAnglesTolerances

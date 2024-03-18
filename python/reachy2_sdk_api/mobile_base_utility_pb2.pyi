"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.wrappers_pb2
import mobile_base_lidar_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ControlModePossiblities:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ControlModePossiblitiesEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ControlModePossiblities.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NONE_CONTROL_MODE: _ControlModePossiblities.ValueType  # 0
    OPEN_LOOP: _ControlModePossiblities.ValueType  # 1
    PID: _ControlModePossiblities.ValueType  # 2

class ControlModePossiblities(_ControlModePossiblities, metaclass=_ControlModePossiblitiesEnumTypeWrapper): ...

NONE_CONTROL_MODE: ControlModePossiblities.ValueType  # 0
OPEN_LOOP: ControlModePossiblities.ValueType  # 1
PID: ControlModePossiblities.ValueType  # 2
global___ControlModePossiblities = ControlModePossiblities

class _ZuuuModePossiblities:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ZuuuModePossiblitiesEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ZuuuModePossiblities.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NONE_ZUUU_MODE: _ZuuuModePossiblities.ValueType  # 0
    CMD_VEL: _ZuuuModePossiblities.ValueType  # 1
    BRAKE: _ZuuuModePossiblities.ValueType  # 2
    FREE_WHEEL: _ZuuuModePossiblities.ValueType  # 3
    SPEED: _ZuuuModePossiblities.ValueType  # 4
    GOTO: _ZuuuModePossiblities.ValueType  # 5
    EMERGENCY_STOP: _ZuuuModePossiblities.ValueType  # 6

class ZuuuModePossiblities(_ZuuuModePossiblities, metaclass=_ZuuuModePossiblitiesEnumTypeWrapper): ...

NONE_ZUUU_MODE: ZuuuModePossiblities.ValueType  # 0
CMD_VEL: ZuuuModePossiblities.ValueType  # 1
BRAKE: ZuuuModePossiblities.ValueType  # 2
FREE_WHEEL: ZuuuModePossiblities.ValueType  # 3
SPEED: ZuuuModePossiblities.ValueType  # 4
GOTO: ZuuuModePossiblities.ValueType  # 5
EMERGENCY_STOP: ZuuuModePossiblities.ValueType  # 6
global___ZuuuModePossiblities = ZuuuModePossiblities

@typing_extensions.final
class MobileBaseInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIAL_NUMBER_FIELD_NUMBER: builtins.int
    VERSION_HARD_FIELD_NUMBER: builtins.int
    VERSION_SOFT_FIELD_NUMBER: builtins.int
    serial_number: builtins.str
    version_hard: builtins.str
    version_soft: builtins.str
    def __init__(
        self,
        *,
        serial_number: builtins.str = ...,
        version_hard: builtins.str = ...,
        version_soft: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["serial_number", b"serial_number", "version_hard", b"version_hard", "version_soft", b"version_soft"]) -> None: ...

global___MobileBaseInfo = MobileBaseInfo

@typing_extensions.final
class MobileBase(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INFO_FIELD_NUMBER: builtins.int
    @property
    def info(self) -> global___MobileBaseInfo: ...
    def __init__(
        self,
        *,
        info: global___MobileBaseInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["info", b"info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["info", b"info"]) -> None: ...

global___MobileBase = MobileBase

@typing_extensions.final
class MobileBaseState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BATTERY_LEVEL_FIELD_NUMBER: builtins.int
    LIDAR_OBSTACLE_DETECTION_STATUS_FIELD_NUMBER: builtins.int
    @property
    def battery_level(self) -> global___BatteryLevel: ...
    @property
    def lidar_obstacle_detection_status(self) -> mobile_base_lidar_pb2.LidarObstacleDetectionStatus: ...
    def __init__(
        self,
        *,
        battery_level: global___BatteryLevel | None = ...,
        lidar_obstacle_detection_status: mobile_base_lidar_pb2.LidarObstacleDetectionStatus | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["battery_level", b"battery_level", "lidar_obstacle_detection_status", b"lidar_obstacle_detection_status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["battery_level", b"battery_level", "lidar_obstacle_detection_status", b"lidar_obstacle_detection_status"]) -> None: ...

global___MobileBaseState = MobileBaseState

@typing_extensions.final
class OdometryVector(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    THETA_FIELD_NUMBER: builtins.int
    @property
    def x(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def y(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def theta(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    def __init__(
        self,
        *,
        x: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        y: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        theta: google.protobuf.wrappers_pb2.FloatValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["theta", b"theta", "x", b"x", "y", b"y"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["theta", b"theta", "x", b"x", "y", b"y"]) -> None: ...

global___OdometryVector = OdometryVector

@typing_extensions.final
class ControlModeCommand(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODE_FIELD_NUMBER: builtins.int
    mode: global___ControlModePossiblities.ValueType
    def __init__(
        self,
        *,
        mode: global___ControlModePossiblities.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["mode", b"mode"]) -> None: ...

global___ControlModeCommand = ControlModeCommand

@typing_extensions.final
class ZuuuModeCommand(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODE_FIELD_NUMBER: builtins.int
    mode: global___ZuuuModePossiblities.ValueType
    def __init__(
        self,
        *,
        mode: global___ZuuuModePossiblities.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["mode", b"mode"]) -> None: ...

global___ZuuuModeCommand = ZuuuModeCommand

@typing_extensions.final
class BatteryLevel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LEVEL_FIELD_NUMBER: builtins.int
    @property
    def level(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    def __init__(
        self,
        *,
        level: google.protobuf.wrappers_pb2.FloatValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["level", b"level"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["level", b"level"]) -> None: ...

global___BatteryLevel = BatteryLevel

@typing_extensions.final
class MobileBaseVersion(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODEL_VERSION_FIELD_NUMBER: builtins.int
    @property
    def model_version(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    def __init__(
        self,
        *,
        model_version: google.protobuf.wrappers_pb2.FloatValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["model_version", b"model_version"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["model_version", b"model_version"]) -> None: ...

global___MobileBaseVersion = MobileBaseVersion
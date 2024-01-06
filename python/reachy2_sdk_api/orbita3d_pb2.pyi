"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import component_pb2
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

class _Orbita3dField:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _Orbita3dFieldEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Orbita3dField.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NONE: _Orbita3dField.ValueType  # 0
    NAME: _Orbita3dField.ValueType  # 1
    ID: _Orbita3dField.ValueType  # 2
    PRESENT_POSITION: _Orbita3dField.ValueType  # 3
    PRESENT_SPEED: _Orbita3dField.ValueType  # 4
    PRESENT_LOAD: _Orbita3dField.ValueType  # 5
    TEMPERATURE: _Orbita3dField.ValueType  # 6
    JOINT_LIMIT: _Orbita3dField.ValueType  # 7
    COMPLIANT: _Orbita3dField.ValueType  # 8
    GOAL_POSITION: _Orbita3dField.ValueType  # 9
    SPEED_LIMIT: _Orbita3dField.ValueType  # 10
    TORQUE_LIMIT: _Orbita3dField.ValueType  # 11
    PID: _Orbita3dField.ValueType  # 12
    ALL: _Orbita3dField.ValueType  # 15

class Orbita3dField(_Orbita3dField, metaclass=_Orbita3dFieldEnumTypeWrapper): ...

NONE: Orbita3dField.ValueType  # 0
NAME: Orbita3dField.ValueType  # 1
ID: Orbita3dField.ValueType  # 2
PRESENT_POSITION: Orbita3dField.ValueType  # 3
PRESENT_SPEED: Orbita3dField.ValueType  # 4
PRESENT_LOAD: Orbita3dField.ValueType  # 5
TEMPERATURE: Orbita3dField.ValueType  # 6
JOINT_LIMIT: Orbita3dField.ValueType  # 7
COMPLIANT: Orbita3dField.ValueType  # 8
GOAL_POSITION: Orbita3dField.ValueType  # 9
SPEED_LIMIT: Orbita3dField.ValueType  # 10
TORQUE_LIMIT: Orbita3dField.ValueType  # 11
PID: Orbita3dField.ValueType  # 12
ALL: Orbita3dField.ValueType  # 15
global___Orbita3dField = Orbita3dField

@typing_extensions.final
class Orbita3dState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIMESTAMP_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    PRESENT_POSITION_FIELD_NUMBER: builtins.int
    PRESENT_SPEED_FIELD_NUMBER: builtins.int
    PRESENT_LOAD_FIELD_NUMBER: builtins.int
    TEMPERATURE_FIELD_NUMBER: builtins.int
    JOINT_LIMIT_FIELD_NUMBER: builtins.int
    COMPLIANT_FIELD_NUMBER: builtins.int
    GOAL_POSITION_FIELD_NUMBER: builtins.int
    SPEED_LIMIT_FIELD_NUMBER: builtins.int
    TORQUE_LIMIT_FIELD_NUMBER: builtins.int
    PID_FIELD_NUMBER: builtins.int
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def id(self) -> component_pb2.ComponentId: ...
    @property
    def present_position(self) -> kinematics_pb2.Rotation3d: ...
    @property
    def present_speed(self) -> global___Vector3d: ...
    @property
    def present_load(self) -> global___Vector3d: ...
    @property
    def temperature(self) -> global___Float3d: ...
    @property
    def joint_limit(self) -> global___Limits3d: ...
    @property
    def compliant(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def goal_position(self) -> kinematics_pb2.Rotation3d: ...
    @property
    def speed_limit(self) -> global___Float3d: ...
    @property
    def torque_limit(self) -> global___Float3d: ...
    @property
    def pid(self) -> global___PID3d: ...
    def __init__(
        self,
        *,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        id: component_pb2.ComponentId | None = ...,
        present_position: kinematics_pb2.Rotation3d | None = ...,
        present_speed: global___Vector3d | None = ...,
        present_load: global___Vector3d | None = ...,
        temperature: global___Float3d | None = ...,
        joint_limit: global___Limits3d | None = ...,
        compliant: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        goal_position: kinematics_pb2.Rotation3d | None = ...,
        speed_limit: global___Float3d | None = ...,
        torque_limit: global___Float3d | None = ...,
        pid: global___PID3d | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["compliant", b"compliant", "goal_position", b"goal_position", "id", b"id", "joint_limit", b"joint_limit", "pid", b"pid", "present_load", b"present_load", "present_position", b"present_position", "present_speed", b"present_speed", "speed_limit", b"speed_limit", "temperature", b"temperature", "timestamp", b"timestamp", "torque_limit", b"torque_limit"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["compliant", b"compliant", "goal_position", b"goal_position", "id", b"id", "joint_limit", b"joint_limit", "pid", b"pid", "present_load", b"present_load", "present_position", b"present_position", "present_speed", b"present_speed", "speed_limit", b"speed_limit", "temperature", b"temperature", "timestamp", b"timestamp", "torque_limit", b"torque_limit"]) -> None: ...

global___Orbita3dState = Orbita3dState

@typing_extensions.final
class Orbita3dStateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FIELDS_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    @property
    def fields(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___Orbita3dField.ValueType]: ...
    @property
    def id(self) -> component_pb2.ComponentId: ...
    def __init__(
        self,
        *,
        fields: collections.abc.Iterable[global___Orbita3dField.ValueType] | None = ...,
        id: component_pb2.ComponentId | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["id", b"id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["fields", b"fields", "id", b"id"]) -> None: ...

global___Orbita3dStateRequest = Orbita3dStateRequest

@typing_extensions.final
class Orbita3dStreamStateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQ_FIELD_NUMBER: builtins.int
    FREQ_FIELD_NUMBER: builtins.int
    @property
    def req(self) -> global___Orbita3dStateRequest: ...
    freq: builtins.float
    def __init__(
        self,
        *,
        req: global___Orbita3dStateRequest | None = ...,
        freq: builtins.float = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["req", b"req"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["freq", b"freq", "req", b"req"]) -> None: ...

global___Orbita3dStreamStateRequest = Orbita3dStreamStateRequest

@typing_extensions.final
class PID3d(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MOTOR_1_FIELD_NUMBER: builtins.int
    MOTOR_2_FIELD_NUMBER: builtins.int
    MOTOR_3_FIELD_NUMBER: builtins.int
    @property
    def motor_1(self) -> component_pb2.PIDGains: ...
    @property
    def motor_2(self) -> component_pb2.PIDGains: ...
    @property
    def motor_3(self) -> component_pb2.PIDGains: ...
    def __init__(
        self,
        *,
        motor_1: component_pb2.PIDGains | None = ...,
        motor_2: component_pb2.PIDGains | None = ...,
        motor_3: component_pb2.PIDGains | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["motor_1", b"motor_1", "motor_2", b"motor_2", "motor_3", b"motor_3"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["motor_1", b"motor_1", "motor_2", b"motor_2", "motor_3", b"motor_3"]) -> None: ...

global___PID3d = PID3d

@typing_extensions.final
class Limits3d(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROLL_FIELD_NUMBER: builtins.int
    PITCH_FIELD_NUMBER: builtins.int
    YAW_FIELD_NUMBER: builtins.int
    @property
    def roll(self) -> component_pb2.JointLimits: ...
    @property
    def pitch(self) -> component_pb2.JointLimits: ...
    @property
    def yaw(self) -> component_pb2.JointLimits: ...
    def __init__(
        self,
        *,
        roll: component_pb2.JointLimits | None = ...,
        pitch: component_pb2.JointLimits | None = ...,
        yaw: component_pb2.JointLimits | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pitch", b"pitch", "roll", b"roll", "yaw", b"yaw"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["pitch", b"pitch", "roll", b"roll", "yaw", b"yaw"]) -> None: ...

global___Limits3d = Limits3d

@typing_extensions.final
class Float3d(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MOTOR_1_FIELD_NUMBER: builtins.int
    MOTOR_2_FIELD_NUMBER: builtins.int
    MOTOR_3_FIELD_NUMBER: builtins.int
    @property
    def motor_1(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def motor_2(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def motor_3(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    def __init__(
        self,
        *,
        motor_1: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        motor_2: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        motor_3: google.protobuf.wrappers_pb2.FloatValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["motor_1", b"motor_1", "motor_2", b"motor_2", "motor_3", b"motor_3"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["motor_1", b"motor_1", "motor_2", b"motor_2", "motor_3", b"motor_3"]) -> None: ...

global___Float3d = Float3d

@typing_extensions.final
class Vector3d(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    Z_FIELD_NUMBER: builtins.int
    @property
    def x(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def y(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def z(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    def __init__(
        self,
        *,
        x: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        y: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        z: google.protobuf.wrappers_pb2.FloatValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["x", b"x", "y", b"y", "z", b"z"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["x", b"x", "y", b"y", "z", b"z"]) -> None: ...

global___Vector3d = Vector3d

@typing_extensions.final
class Orbita3dCommand(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    COMPLIANT_FIELD_NUMBER: builtins.int
    GOAL_POSITION_FIELD_NUMBER: builtins.int
    SPEED_LIMIT_FIELD_NUMBER: builtins.int
    TORQUE_LIMIT_FIELD_NUMBER: builtins.int
    PID_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> component_pb2.ComponentId: ...
    @property
    def compliant(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def goal_position(self) -> kinematics_pb2.Rotation3d: ...
    @property
    def speed_limit(self) -> global___Float3d: ...
    @property
    def torque_limit(self) -> global___Float3d: ...
    @property
    def pid(self) -> global___PID3d: ...
    def __init__(
        self,
        *,
        id: component_pb2.ComponentId | None = ...,
        compliant: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        goal_position: kinematics_pb2.Rotation3d | None = ...,
        speed_limit: global___Float3d | None = ...,
        torque_limit: global___Float3d | None = ...,
        pid: global___PID3d | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["compliant", b"compliant", "goal_position", b"goal_position", "id", b"id", "pid", b"pid", "speed_limit", b"speed_limit", "torque_limit", b"torque_limit"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["compliant", b"compliant", "goal_position", b"goal_position", "id", b"id", "pid", b"pid", "speed_limit", b"speed_limit", "torque_limit", b"torque_limit"]) -> None: ...

global___Orbita3dCommand = Orbita3dCommand

@typing_extensions.final
class Orbita3dsCommand(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CMD_FIELD_NUMBER: builtins.int
    @property
    def cmd(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Orbita3dCommand]: ...
    def __init__(
        self,
        *,
        cmd: collections.abc.Iterable[global___Orbita3dCommand] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cmd", b"cmd"]) -> None: ...

global___Orbita3dsCommand = Orbita3dsCommand

@typing_extensions.final
class Orbita3dGoal(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    ROTATION_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> component_pb2.ComponentId: ...
    @property
    def rotation(self) -> kinematics_pb2.Rotation3d: ...
    @property
    def duration(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    def __init__(
        self,
        *,
        id: component_pb2.ComponentId | None = ...,
        rotation: kinematics_pb2.Rotation3d | None = ...,
        duration: google.protobuf.wrappers_pb2.FloatValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["duration", b"duration", "id", b"id", "rotation", b"rotation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["duration", b"duration", "id", b"id", "rotation", b"rotation"]) -> None: ...

global___Orbita3dGoal = Orbita3dGoal

@typing_extensions.final
class Orbita3d(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    SERIAL_NUMBER_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> component_pb2.ComponentId: ...
    serial_number: builtins.str
    def __init__(
        self,
        *,
        id: component_pb2.ComponentId | None = ...,
        serial_number: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["id", b"id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "serial_number", b"serial_number"]) -> None: ...

global___Orbita3d = Orbita3d

@typing_extensions.final
class ListOfOrbita3d(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INFO_FIELD_NUMBER: builtins.int
    @property
    def info(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Orbita3d]: ...
    def __init__(
        self,
        *,
        info: collections.abc.Iterable[global___Orbita3d] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["info", b"info"]) -> None: ...

global___ListOfOrbita3d = ListOfOrbita3d

@typing_extensions.final
class Orbita3dStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___Orbita3dStatus = Orbita3dStatus

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
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _DynamixelMotorField:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _DynamixelMotorFieldEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_DynamixelMotorField.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NONE: _DynamixelMotorField.ValueType  # 0
    NAME: _DynamixelMotorField.ValueType  # 1
    ID: _DynamixelMotorField.ValueType  # 2
    PRESENT_POSITION: _DynamixelMotorField.ValueType  # 3
    PRESENT_SPEED: _DynamixelMotorField.ValueType  # 4
    PRESENT_LOAD: _DynamixelMotorField.ValueType  # 5
    TEMPERATURE: _DynamixelMotorField.ValueType  # 6
    JOINT_LIMIT: _DynamixelMotorField.ValueType  # 7
    COMPLIANT: _DynamixelMotorField.ValueType  # 8
    GOAL_POSITION: _DynamixelMotorField.ValueType  # 9
    SPEED_LIMIT: _DynamixelMotorField.ValueType  # 10
    TORQUE_LIMIT: _DynamixelMotorField.ValueType  # 11
    PID: _DynamixelMotorField.ValueType  # 12
    ALL: _DynamixelMotorField.ValueType  # 15

class DynamixelMotorField(_DynamixelMotorField, metaclass=_DynamixelMotorFieldEnumTypeWrapper): ...

NONE: DynamixelMotorField.ValueType  # 0
NAME: DynamixelMotorField.ValueType  # 1
ID: DynamixelMotorField.ValueType  # 2
PRESENT_POSITION: DynamixelMotorField.ValueType  # 3
PRESENT_SPEED: DynamixelMotorField.ValueType  # 4
PRESENT_LOAD: DynamixelMotorField.ValueType  # 5
TEMPERATURE: DynamixelMotorField.ValueType  # 6
JOINT_LIMIT: DynamixelMotorField.ValueType  # 7
COMPLIANT: DynamixelMotorField.ValueType  # 8
GOAL_POSITION: DynamixelMotorField.ValueType  # 9
SPEED_LIMIT: DynamixelMotorField.ValueType  # 10
TORQUE_LIMIT: DynamixelMotorField.ValueType  # 11
PID: DynamixelMotorField.ValueType  # 12
ALL: DynamixelMotorField.ValueType  # 15
global___DynamixelMotorField = DynamixelMotorField

@typing_extensions.final
class DynamixelMotorState(google.protobuf.message.Message):
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
    def present_position(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def present_speed(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def present_load(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def temperature(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def joint_limit(self) -> component_pb2.JointLimits: ...
    @property
    def compliant(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def goal_position(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def speed_limit(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def torque_limit(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def pid(self) -> component_pb2.PIDGains: ...
    def __init__(
        self,
        *,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        id: component_pb2.ComponentId | None = ...,
        present_position: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        present_speed: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        present_load: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        temperature: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        joint_limit: component_pb2.JointLimits | None = ...,
        compliant: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        goal_position: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        speed_limit: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        torque_limit: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        pid: component_pb2.PIDGains | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["compliant", b"compliant", "goal_position", b"goal_position", "id", b"id", "joint_limit", b"joint_limit", "pid", b"pid", "present_load", b"present_load", "present_position", b"present_position", "present_speed", b"present_speed", "speed_limit", b"speed_limit", "temperature", b"temperature", "timestamp", b"timestamp", "torque_limit", b"torque_limit"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["compliant", b"compliant", "goal_position", b"goal_position", "id", b"id", "joint_limit", b"joint_limit", "pid", b"pid", "present_load", b"present_load", "present_position", b"present_position", "present_speed", b"present_speed", "speed_limit", b"speed_limit", "temperature", b"temperature", "timestamp", b"timestamp", "torque_limit", b"torque_limit"]) -> None: ...

global___DynamixelMotorState = DynamixelMotorState

@typing_extensions.final
class DynamixelMotorStateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FIELDS_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    @property
    def fields(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___DynamixelMotorField.ValueType]: ...
    @property
    def id(self) -> component_pb2.ComponentId: ...
    def __init__(
        self,
        *,
        fields: collections.abc.Iterable[global___DynamixelMotorField.ValueType] | None = ...,
        id: component_pb2.ComponentId | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["id", b"id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["fields", b"fields", "id", b"id"]) -> None: ...

global___DynamixelMotorStateRequest = DynamixelMotorStateRequest

@typing_extensions.final
class DynamixelMotorStreamStateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQ_FIELD_NUMBER: builtins.int
    FREQ_FIELD_NUMBER: builtins.int
    @property
    def req(self) -> global___DynamixelMotorStateRequest: ...
    freq: builtins.float
    def __init__(
        self,
        *,
        req: global___DynamixelMotorStateRequest | None = ...,
        freq: builtins.float = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["req", b"req"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["freq", b"freq", "req", b"req"]) -> None: ...

global___DynamixelMotorStreamStateRequest = DynamixelMotorStreamStateRequest

@typing_extensions.final
class DynamixelMotorGoal(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    GOAL_POSITION_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> component_pb2.ComponentId: ...
    @property
    def goal_position(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def duration(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    def __init__(
        self,
        *,
        id: component_pb2.ComponentId | None = ...,
        goal_position: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        duration: google.protobuf.wrappers_pb2.FloatValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["duration", b"duration", "goal_position", b"goal_position", "id", b"id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["duration", b"duration", "goal_position", b"goal_position", "id", b"id"]) -> None: ...

global___DynamixelMotorGoal = DynamixelMotorGoal

@typing_extensions.final
class DynamixelMotorCommand(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    COMPLIANT_FIELD_NUMBER: builtins.int
    GOAL_POSITION_FIELD_NUMBER: builtins.int
    SPEED_LIMIT_FIELD_NUMBER: builtins.int
    TORQUE_LIMIT_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> component_pb2.ComponentId: ...
    @property
    def compliant(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def goal_position(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def speed_limit(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def torque_limit(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    def __init__(
        self,
        *,
        id: component_pb2.ComponentId | None = ...,
        compliant: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        goal_position: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        speed_limit: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        torque_limit: google.protobuf.wrappers_pb2.FloatValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["compliant", b"compliant", "goal_position", b"goal_position", "id", b"id", "speed_limit", b"speed_limit", "torque_limit", b"torque_limit"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["compliant", b"compliant", "goal_position", b"goal_position", "id", b"id", "speed_limit", b"speed_limit", "torque_limit", b"torque_limit"]) -> None: ...

global___DynamixelMotorCommand = DynamixelMotorCommand

@typing_extensions.final
class DynamixelMotorsCommand(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CMD_FIELD_NUMBER: builtins.int
    @property
    def cmd(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DynamixelMotorCommand]: ...
    def __init__(
        self,
        *,
        cmd: collections.abc.Iterable[global___DynamixelMotorCommand] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cmd", b"cmd"]) -> None: ...

global___DynamixelMotorsCommand = DynamixelMotorsCommand

@typing_extensions.final
class DynamixelMotor(google.protobuf.message.Message):
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

global___DynamixelMotor = DynamixelMotor

@typing_extensions.final
class ListOfDynamixelMotor(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INFO_FIELD_NUMBER: builtins.int
    @property
    def info(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DynamixelMotor]: ...
    def __init__(
        self,
        *,
        info: collections.abc.Iterable[global___DynamixelMotor] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["info", b"info"]) -> None: ...

global___ListOfDynamixelMotor = ListOfDynamixelMotor

@typing_extensions.final
class DynamixelMotorStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___DynamixelMotorStatus = DynamixelMotorStatus

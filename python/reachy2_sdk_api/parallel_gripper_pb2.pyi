"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import component_pb2
import error_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ParallelGripperField:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ParallelGripperFieldEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ParallelGripperField.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NONE: _ParallelGripperField.ValueType  # 0
    NAME: _ParallelGripperField.ValueType  # 1
    ID: _ParallelGripperField.ValueType  # 2
    PRESENT_POSITION: _ParallelGripperField.ValueType  # 3
    PRESENT_SPEED: _ParallelGripperField.ValueType  # 4
    PRESENT_LOAD: _ParallelGripperField.ValueType  # 5
    TEMPERATURE: _ParallelGripperField.ValueType  # 6
    FORCE_SENSOR: _ParallelGripperField.ValueType  # 7
    COMPLIANT: _ParallelGripperField.ValueType  # 8
    GOAL_POSITION: _ParallelGripperField.ValueType  # 9
    SPEED_LIMIT: _ParallelGripperField.ValueType  # 10
    TORQUE_LIMIT: _ParallelGripperField.ValueType  # 11
    PID: _ParallelGripperField.ValueType  # 12
    ALL: _ParallelGripperField.ValueType  # 15

class ParallelGripperField(_ParallelGripperField, metaclass=_ParallelGripperFieldEnumTypeWrapper): ...

NONE: ParallelGripperField.ValueType  # 0
NAME: ParallelGripperField.ValueType  # 1
ID: ParallelGripperField.ValueType  # 2
PRESENT_POSITION: ParallelGripperField.ValueType  # 3
PRESENT_SPEED: ParallelGripperField.ValueType  # 4
PRESENT_LOAD: ParallelGripperField.ValueType  # 5
TEMPERATURE: ParallelGripperField.ValueType  # 6
FORCE_SENSOR: ParallelGripperField.ValueType  # 7
COMPLIANT: ParallelGripperField.ValueType  # 8
GOAL_POSITION: ParallelGripperField.ValueType  # 9
SPEED_LIMIT: ParallelGripperField.ValueType  # 10
TORQUE_LIMIT: ParallelGripperField.ValueType  # 11
PID: ParallelGripperField.ValueType  # 12
ALL: ParallelGripperField.ValueType  # 15
global___ParallelGripperField = ParallelGripperField

@typing_extensions.final
class ParallelGripperState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIMESTAMP_FIELD_NUMBER: builtins.int
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["timestamp", b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["timestamp", b"timestamp"]) -> None: ...

global___ParallelGripperState = ParallelGripperState

@typing_extensions.final
class ParallelGripperStateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FIELDS_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    @property
    def fields(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___ParallelGripperField.ValueType]: ...
    @property
    def id(self) -> component_pb2.ComponentId: ...
    def __init__(
        self,
        *,
        fields: collections.abc.Iterable[global___ParallelGripperField.ValueType] | None = ...,
        id: component_pb2.ComponentId | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["id", b"id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["fields", b"fields", "id", b"id"]) -> None: ...

global___ParallelGripperStateRequest = ParallelGripperStateRequest

@typing_extensions.final
class ParallelGripperStreamStateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQ_FIELD_NUMBER: builtins.int
    FREQ_FIELD_NUMBER: builtins.int
    @property
    def req(self) -> global___ParallelGripperStateRequest: ...
    freq: builtins.float
    def __init__(
        self,
        *,
        req: global___ParallelGripperStateRequest | None = ...,
        freq: builtins.float = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["req", b"req"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["freq", b"freq", "req", b"req"]) -> None: ...

global___ParallelGripperStreamStateRequest = ParallelGripperStreamStateRequest

@typing_extensions.final
class ParallelGripperCommand(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ParallelGripperCommand = ParallelGripperCommand

@typing_extensions.final
class ParallelGripperInfo(google.protobuf.message.Message):
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

global___ParallelGripperInfo = ParallelGripperInfo

@typing_extensions.final
class ListOfParallelGripperInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARALLEL_GRIPPER_INFO_FIELD_NUMBER: builtins.int
    @property
    def parallel_gripper_info(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ParallelGripperInfo]: ...
    def __init__(
        self,
        *,
        parallel_gripper_info: collections.abc.Iterable[global___ParallelGripperInfo] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["parallel_gripper_info", b"parallel_gripper_info"]) -> None: ...

global___ListOfParallelGripperInfo = ListOfParallelGripperInfo

@typing_extensions.final
class ParallelGripperStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ERRORS_FIELD_NUMBER: builtins.int
    @property
    def errors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[error_pb2.Error]: ...
    def __init__(
        self,
        *,
        errors: collections.abc.Iterable[error_pb2.Error] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["errors", b"errors"]) -> None: ...

global___ParallelGripperStatus = ParallelGripperStatus

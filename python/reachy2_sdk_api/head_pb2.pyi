"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import component_pb2
import dynamixel_motor_pb2
import error_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import google.protobuf.wrappers_pb2
import kinematics_pb2
import orbita3d_pb2
import part_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _HeadField:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _HeadFieldEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_HeadField.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NONE: _HeadField.ValueType  # 0
    NAME: _HeadField.ValueType  # 1
    ID: _HeadField.ValueType  # 2
    PRESENT_POSITION: _HeadField.ValueType  # 3
    PRESENT_SPEED: _HeadField.ValueType  # 4
    PRESENT_LOAD: _HeadField.ValueType  # 5
    TEMPERATURE: _HeadField.ValueType  # 6
    JOINT_LIMITS: _HeadField.ValueType  # 7
    COMPLIANT: _HeadField.ValueType  # 8
    GOAL_POSITION: _HeadField.ValueType  # 9
    SPEED_LIMIT: _HeadField.ValueType  # 10
    TORQUE_LIMIT: _HeadField.ValueType  # 11
    PID: _HeadField.ValueType  # 12
    ALL: _HeadField.ValueType  # 15

class HeadField(_HeadField, metaclass=_HeadFieldEnumTypeWrapper): ...

NONE: HeadField.ValueType  # 0
NAME: HeadField.ValueType  # 1
ID: HeadField.ValueType  # 2
PRESENT_POSITION: HeadField.ValueType  # 3
PRESENT_SPEED: HeadField.ValueType  # 4
PRESENT_LOAD: HeadField.ValueType  # 5
TEMPERATURE: HeadField.ValueType  # 6
JOINT_LIMITS: HeadField.ValueType  # 7
COMPLIANT: HeadField.ValueType  # 8
GOAL_POSITION: HeadField.ValueType  # 9
SPEED_LIMIT: HeadField.ValueType  # 10
TORQUE_LIMIT: HeadField.ValueType  # 11
PID: HeadField.ValueType  # 12
ALL: HeadField.ValueType  # 15
global___HeadField = HeadField

<<<<<<< HEAD
@typing.final
=======
class _NeckJoints:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _NeckJointsEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_NeckJoints.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ROLL: _NeckJoints.ValueType  # 0
    PITCH: _NeckJoints.ValueType  # 1
    YAW: _NeckJoints.ValueType  # 2

class NeckJoints(_NeckJoints, metaclass=_NeckJointsEnumTypeWrapper): ...

ROLL: NeckJoints.ValueType  # 0
PITCH: NeckJoints.ValueType  # 1
YAW: NeckJoints.ValueType  # 2
global___NeckJoints = NeckJoints

@typing_extensions.final
class CustomNeckJoints(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOINTS_FIELD_NUMBER: builtins.int
    @property
    def joints(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___NeckJoints.ValueType]: ...
    def __init__(
        self,
        *,
        joints: collections.abc.Iterable[global___NeckJoints.ValueType] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["joints", b"joints"]) -> None: ...

global___CustomNeckJoints = CustomNeckJoints

@typing_extensions.final
>>>>>>> v1.0.9
class Head(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PART_ID_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    INFO_FIELD_NUMBER: builtins.int
    @property
    def part_id(self) -> part_pb2.PartId: ...
    @property
    def description(self) -> global___HeadDescription: ...
    @property
    def info(self) -> part_pb2.PartInfo: ...
    def __init__(
        self,
        *,
        part_id: part_pb2.PartId | None = ...,
        description: global___HeadDescription | None = ...,
        info: part_pb2.PartInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["description", b"description", "info", b"info", "part_id", b"part_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "info", b"info", "part_id", b"part_id"]) -> None: ...

global___Head = Head

@typing.final
class HeadDescription(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NECK_FIELD_NUMBER: builtins.int
    L_ANTENNA_FIELD_NUMBER: builtins.int
    R_ANTENNA_FIELD_NUMBER: builtins.int
    @property
    def neck(self) -> orbita3d_pb2.Orbita3d: ...
    @property
    def l_antenna(self) -> dynamixel_motor_pb2.DynamixelMotor: ...
    @property
    def r_antenna(self) -> dynamixel_motor_pb2.DynamixelMotor: ...
    def __init__(
        self,
        *,
        neck: orbita3d_pb2.Orbita3d | None = ...,
        l_antenna: dynamixel_motor_pb2.DynamixelMotor | None = ...,
        r_antenna: dynamixel_motor_pb2.DynamixelMotor | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["l_antenna", b"l_antenna", "neck", b"neck", "r_antenna", b"r_antenna"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["l_antenna", b"l_antenna", "neck", b"neck", "r_antenna", b"r_antenna"]) -> None: ...

global___HeadDescription = HeadDescription

@typing.final
class ListOfHead(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEAD_FIELD_NUMBER: builtins.int
    @property
    def head(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Head]: ...
    def __init__(
        self,
        *,
        head: collections.abc.Iterable[global___Head] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["head", b"head"]) -> None: ...

global___ListOfHead = ListOfHead

@typing.final
class HeadState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIMESTAMP_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    ACTIVATED_FIELD_NUMBER: builtins.int
    NECK_STATE_FIELD_NUMBER: builtins.int
    L_ANTENNA_STATE_FIELD_NUMBER: builtins.int
    R_ANTENNA_STATE_FIELD_NUMBER: builtins.int
    activated: builtins.bool
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def id(self) -> part_pb2.PartId: ...
    @property
    def neck_state(self) -> orbita3d_pb2.Orbita3dState: ...
    @property
    def l_antenna_state(self) -> dynamixel_motor_pb2.DynamixelMotorState: ...
    @property
    def r_antenna_state(self) -> dynamixel_motor_pb2.DynamixelMotorState: ...
    def __init__(
        self,
        *,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        id: part_pb2.PartId | None = ...,
        activated: builtins.bool = ...,
        neck_state: orbita3d_pb2.Orbita3dState | None = ...,
        l_antenna_state: dynamixel_motor_pb2.DynamixelMotorState | None = ...,
        r_antenna_state: dynamixel_motor_pb2.DynamixelMotorState | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["id", b"id", "l_antenna_state", b"l_antenna_state", "neck_state", b"neck_state", "r_antenna_state", b"r_antenna_state", "timestamp", b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["activated", b"activated", "id", b"id", "l_antenna_state", b"l_antenna_state", "neck_state", b"neck_state", "r_antenna_state", b"r_antenna_state", "timestamp", b"timestamp"]) -> None: ...

global___HeadState = HeadState

@typing.final
class HeadPosition(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NECK_POSITION_FIELD_NUMBER: builtins.int
    L_ANTENNA_POSITION_FIELD_NUMBER: builtins.int
    R_ANTENNA_POSITION_FIELD_NUMBER: builtins.int
    @property
    def neck_position(self) -> kinematics_pb2.Rotation3d: ...
    @property
    def l_antenna_position(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def r_antenna_position(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    def __init__(
        self,
        *,
        neck_position: kinematics_pb2.Rotation3d | None = ...,
        l_antenna_position: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        r_antenna_position: google.protobuf.wrappers_pb2.FloatValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["l_antenna_position", b"l_antenna_position", "neck_position", b"neck_position", "r_antenna_position", b"r_antenna_position"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["l_antenna_position", b"l_antenna_position", "neck_position", b"neck_position", "r_antenna_position", b"r_antenna_position"]) -> None: ...

global___HeadPosition = HeadPosition

@typing.final
class NeckCartesianGoal(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    POINT_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> part_pb2.PartId: ...
    @property
    def point(self) -> kinematics_pb2.Point: ...
    @property
    def duration(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    def __init__(
        self,
        *,
        id: part_pb2.PartId | None = ...,
        point: kinematics_pb2.Point | None = ...,
        duration: google.protobuf.wrappers_pb2.FloatValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["duration", b"duration", "id", b"id", "point", b"point"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["duration", b"duration", "id", b"id", "point", b"point"]) -> None: ...

global___NeckCartesianGoal = NeckCartesianGoal

@typing.final
class NeckJointGoal(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    JOINTS_GOAL_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> part_pb2.PartId: ...
    @property
    def joints_goal(self) -> global___NeckOrientation: ...
    @property
    def duration(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    def __init__(
        self,
        *,
        id: part_pb2.PartId | None = ...,
        joints_goal: global___NeckOrientation | None = ...,
        duration: google.protobuf.wrappers_pb2.FloatValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["duration", b"duration", "id", b"id", "joints_goal", b"joints_goal"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["duration", b"duration", "id", b"id", "joints_goal", b"joints_goal"]) -> None: ...

global___NeckJointGoal = NeckJointGoal

@typing.final
class NeckOrientation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROTATION_FIELD_NUMBER: builtins.int
    @property
    def rotation(self) -> kinematics_pb2.Rotation3d: ...
    def __init__(
        self,
        *,
        rotation: kinematics_pb2.Rotation3d | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["rotation", b"rotation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["rotation", b"rotation"]) -> None: ...

global___NeckOrientation = NeckOrientation

@typing.final
class NeckFKRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    POSITION_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> part_pb2.PartId: ...
    @property
    def position(self) -> global___HeadPosition: ...
    def __init__(
        self,
        *,
        id: part_pb2.PartId | None = ...,
        position: global___HeadPosition | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["id", b"id", "position", b"position"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["id", b"id", "position", b"position"]) -> None: ...

global___NeckFKRequest = NeckFKRequest

@typing.final
class NeckFKSolution(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    ORIENTATION_FIELD_NUMBER: builtins.int
    success: builtins.bool
    @property
    def orientation(self) -> global___NeckOrientation: ...
    def __init__(
        self,
        *,
        success: builtins.bool = ...,
        orientation: global___NeckOrientation | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["orientation", b"orientation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["orientation", b"orientation", "success", b"success"]) -> None: ...

global___NeckFKSolution = NeckFKSolution

@typing.final
class NeckIKRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    TARGET_FIELD_NUMBER: builtins.int
    Q0_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> part_pb2.PartId: ...
    @property
    def target(self) -> global___NeckOrientation: ...
    @property
    def q0(self) -> kinematics_pb2.Rotation3d: ...
    def __init__(
        self,
        *,
        id: part_pb2.PartId | None = ...,
        target: global___NeckOrientation | None = ...,
        q0: kinematics_pb2.Rotation3d | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["id", b"id", "q0", b"q0", "target", b"target"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["id", b"id", "q0", b"q0", "target", b"target"]) -> None: ...

global___NeckIKRequest = NeckIKRequest

@typing.final
class NeckIKSolution(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    POSITION_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    success: builtins.bool
    @property
    def position(self) -> kinematics_pb2.Rotation3d: ...
    @property
    def error(self) -> error_pb2.Error: ...
    def __init__(
        self,
        *,
        success: builtins.bool = ...,
        position: kinematics_pb2.Rotation3d | None = ...,
        error: error_pb2.Error | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["error", b"error", "position", b"position"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["error", b"error", "position", b"position", "success", b"success"]) -> None: ...

global___NeckIKSolution = NeckIKSolution

@typing.final
class HeadStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NECK_STATUS_FIELD_NUMBER: builtins.int
    L_ANTENNA_STATUS_FIELD_NUMBER: builtins.int
    R_ANTENNA_STATUS_FIELD_NUMBER: builtins.int
    @property
    def neck_status(self) -> orbita3d_pb2.Orbita3dStatus: ...
    @property
    def l_antenna_status(self) -> dynamixel_motor_pb2.DynamixelMotorStatus: ...
    @property
    def r_antenna_status(self) -> dynamixel_motor_pb2.DynamixelMotorStatus: ...
    def __init__(
        self,
        *,
        neck_status: orbita3d_pb2.Orbita3dStatus | None = ...,
        l_antenna_status: dynamixel_motor_pb2.DynamixelMotorStatus | None = ...,
        r_antenna_status: dynamixel_motor_pb2.DynamixelMotorStatus | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["l_antenna_status", b"l_antenna_status", "neck_status", b"neck_status", "r_antenna_status", b"r_antenna_status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["l_antenna_status", b"l_antenna_status", "neck_status", b"neck_status", "r_antenna_status", b"r_antenna_status"]) -> None: ...

global___HeadStatus = HeadStatus

@typing.final
class SpeedLimitRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    limit: builtins.int
    @property
    def id(self) -> part_pb2.PartId: ...
    def __init__(
        self,
        *,
        id: part_pb2.PartId | None = ...,
        limit: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["id", b"id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["id", b"id", "limit", b"limit"]) -> None: ...

global___SpeedLimitRequest = SpeedLimitRequest

@typing.final
class TorqueLimitRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    limit: builtins.int
    @property
    def id(self) -> part_pb2.PartId: ...
    def __init__(
        self,
        *,
        id: part_pb2.PartId | None = ...,
        limit: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["id", b"id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["id", b"id", "limit", b"limit"]) -> None: ...

global___TorqueLimitRequest = TorqueLimitRequest

@typing.final
class JointsLimits(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NECK_LIMITS_FIELD_NUMBER: builtins.int
    L_ANTENNA_LIMITS_FIELD_NUMBER: builtins.int
    R_ANTENNA_LIMITS_FIELD_NUMBER: builtins.int
    @property
    def neck_limits(self) -> orbita3d_pb2.Limits3d: ...
    @property
    def l_antenna_limits(self) -> component_pb2.JointLimits: ...
    @property
    def r_antenna_limits(self) -> component_pb2.JointLimits: ...
    def __init__(
        self,
        *,
        neck_limits: orbita3d_pb2.Limits3d | None = ...,
        l_antenna_limits: component_pb2.JointLimits | None = ...,
        r_antenna_limits: component_pb2.JointLimits | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["l_antenna_limits", b"l_antenna_limits", "neck_limits", b"neck_limits", "r_antenna_limits", b"r_antenna_limits"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["l_antenna_limits", b"l_antenna_limits", "neck_limits", b"neck_limits", "r_antenna_limits", b"r_antenna_limits"]) -> None: ...

global___JointsLimits = JointsLimits

@typing.final
class HeadTemperatures(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NECK_TEMPERATURE_FIELD_NUMBER: builtins.int
    L_ANTENNA_TEMPERATURE_FIELD_NUMBER: builtins.int
    R_ANTENNA_TEMPERATURE_FIELD_NUMBER: builtins.int
    l_antenna_temperature: builtins.float
    r_antenna_temperature: builtins.float
    @property
    def neck_temperature(self) -> orbita3d_pb2.Float3d: ...
    def __init__(
        self,
        *,
        neck_temperature: orbita3d_pb2.Float3d | None = ...,
        l_antenna_temperature: builtins.float = ...,
        r_antenna_temperature: builtins.float = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["neck_temperature", b"neck_temperature"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["l_antenna_temperature", b"l_antenna_temperature", "neck_temperature", b"neck_temperature", "r_antenna_temperature", b"r_antenna_temperature"]) -> None: ...

global___HeadTemperatures = HeadTemperatures

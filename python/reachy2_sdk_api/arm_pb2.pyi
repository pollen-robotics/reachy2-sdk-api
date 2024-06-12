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
import orbita2d_pb2
import orbita3d_pb2
import part_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ArmField:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ArmFieldEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ArmField.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NONE: _ArmField.ValueType  # 0
    NAME: _ArmField.ValueType  # 1
    ID: _ArmField.ValueType  # 2
    PRESENT_POSITION: _ArmField.ValueType  # 3
    PRESENT_SPEED: _ArmField.ValueType  # 4
    PRESENT_LOAD: _ArmField.ValueType  # 5
    TEMPERATURE: _ArmField.ValueType  # 6
    JOINT_LIMITS: _ArmField.ValueType  # 7
    COMPLIANT: _ArmField.ValueType  # 8
    GOAL_POSITION: _ArmField.ValueType  # 9
    SPEED_LIMIT: _ArmField.ValueType  # 10
    TORQUE_LIMIT: _ArmField.ValueType  # 11
    PID: _ArmField.ValueType  # 12
    ALL: _ArmField.ValueType  # 15

class ArmField(_ArmField, metaclass=_ArmFieldEnumTypeWrapper): ...

NONE: ArmField.ValueType  # 0
NAME: ArmField.ValueType  # 1
ID: ArmField.ValueType  # 2
PRESENT_POSITION: ArmField.ValueType  # 3
PRESENT_SPEED: ArmField.ValueType  # 4
PRESENT_LOAD: ArmField.ValueType  # 5
TEMPERATURE: ArmField.ValueType  # 6
JOINT_LIMITS: ArmField.ValueType  # 7
COMPLIANT: ArmField.ValueType  # 8
GOAL_POSITION: ArmField.ValueType  # 9
SPEED_LIMIT: ArmField.ValueType  # 10
TORQUE_LIMIT: ArmField.ValueType  # 11
PID: ArmField.ValueType  # 12
ALL: ArmField.ValueType  # 15
global___ArmField = ArmField

class _IKMode:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _IKModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_IKMode.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UNCONSTRAINED: _IKMode.ValueType  # 0
    LOW_ELBOW: _IKMode.ValueType  # 1

class IKMode(_IKMode, metaclass=_IKModeEnumTypeWrapper): ...

UNCONSTRAINED: IKMode.ValueType  # 0
LOW_ELBOW: IKMode.ValueType  # 1
global___IKMode = IKMode

@typing_extensions.final
class ArmState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIMESTAMP_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    ACTIVATED_FIELD_NUMBER: builtins.int
    SHOULDER_STATE_FIELD_NUMBER: builtins.int
    ELBOW_STATE_FIELD_NUMBER: builtins.int
    WRIST_STATE_FIELD_NUMBER: builtins.int
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def id(self) -> part_pb2.PartId: ...
    activated: builtins.bool
    @property
    def shoulder_state(self) -> orbita2d_pb2.Orbita2dState: ...
    @property
    def elbow_state(self) -> orbita2d_pb2.Orbita2dState: ...
    @property
    def wrist_state(self) -> orbita3d_pb2.Orbita3dState: ...
    def __init__(
        self,
        *,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        id: part_pb2.PartId | None = ...,
        activated: builtins.bool = ...,
        shoulder_state: orbita2d_pb2.Orbita2dState | None = ...,
        elbow_state: orbita2d_pb2.Orbita2dState | None = ...,
        wrist_state: orbita3d_pb2.Orbita3dState | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["elbow_state", b"elbow_state", "id", b"id", "shoulder_state", b"shoulder_state", "timestamp", b"timestamp", "wrist_state", b"wrist_state"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["activated", b"activated", "elbow_state", b"elbow_state", "id", b"id", "shoulder_state", b"shoulder_state", "timestamp", b"timestamp", "wrist_state", b"wrist_state"]) -> None: ...

global___ArmState = ArmState

@typing_extensions.final
class ArmDescription(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SHOULDER_FIELD_NUMBER: builtins.int
    ELBOW_FIELD_NUMBER: builtins.int
    WRIST_FIELD_NUMBER: builtins.int
    @property
    def shoulder(self) -> orbita2d_pb2.Orbita2d: ...
    @property
    def elbow(self) -> orbita2d_pb2.Orbita2d: ...
    @property
    def wrist(self) -> orbita3d_pb2.Orbita3d: ...
    def __init__(
        self,
        *,
        shoulder: orbita2d_pb2.Orbita2d | None = ...,
        elbow: orbita2d_pb2.Orbita2d | None = ...,
        wrist: orbita3d_pb2.Orbita3d | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["elbow", b"elbow", "shoulder", b"shoulder", "wrist", b"wrist"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["elbow", b"elbow", "shoulder", b"shoulder", "wrist", b"wrist"]) -> None: ...

global___ArmDescription = ArmDescription

@typing_extensions.final
class Arm(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PART_ID_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    INFO_FIELD_NUMBER: builtins.int
    @property
    def part_id(self) -> part_pb2.PartId: ...
    @property
    def description(self) -> global___ArmDescription: ...
    @property
    def info(self) -> part_pb2.PartInfo: ...
    def __init__(
        self,
        *,
        part_id: part_pb2.PartId | None = ...,
        description: global___ArmDescription | None = ...,
        info: part_pb2.PartInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["description", b"description", "info", b"info", "part_id", b"part_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "info", b"info", "part_id", b"part_id"]) -> None: ...

global___Arm = Arm

@typing_extensions.final
class ListOfArm(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ARM_FIELD_NUMBER: builtins.int
    @property
    def arm(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Arm]: ...
    def __init__(
        self,
        *,
        arm: collections.abc.Iterable[global___Arm] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["arm", b"arm"]) -> None: ...

global___ListOfArm = ListOfArm

@typing_extensions.final
class ArmPosition(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SHOULDER_POSITION_FIELD_NUMBER: builtins.int
    ELBOW_POSITION_FIELD_NUMBER: builtins.int
    WRIST_POSITION_FIELD_NUMBER: builtins.int
    @property
    def shoulder_position(self) -> orbita2d_pb2.Pose2d: ...
    @property
    def elbow_position(self) -> orbita2d_pb2.Pose2d: ...
    @property
    def wrist_position(self) -> kinematics_pb2.Rotation3d: ...
    def __init__(
        self,
        *,
        shoulder_position: orbita2d_pb2.Pose2d | None = ...,
        elbow_position: orbita2d_pb2.Pose2d | None = ...,
        wrist_position: kinematics_pb2.Rotation3d | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["elbow_position", b"elbow_position", "shoulder_position", b"shoulder_position", "wrist_position", b"wrist_position"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["elbow_position", b"elbow_position", "shoulder_position", b"shoulder_position", "wrist_position", b"wrist_position"]) -> None: ...

global___ArmPosition = ArmPosition

@typing_extensions.final
class ArmCartesianGoal(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    GOAL_POSE_FIELD_NUMBER: builtins.int
    POSITION_TOLERANCE_FIELD_NUMBER: builtins.int
    ORIENTATION_TOLERANCE_FIELD_NUMBER: builtins.int
    Q0_FIELD_NUMBER: builtins.int
    MODE_FIELD_NUMBER: builtins.int
    PREFERRED_THETA_FIELD_NUMBER: builtins.int
    D_THETA_MAX_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    ORDER_ID_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> part_pb2.PartId: ...
    @property
    def goal_pose(self) -> kinematics_pb2.Matrix4x4: ...
    @property
    def position_tolerance(self) -> kinematics_pb2.PointDistanceTolerances: ...
    @property
    def orientation_tolerance(self) -> kinematics_pb2.ExtEulerAnglesTolerances: ...
    @property
    def q0(self) -> global___ArmPosition: ...
    mode: global___IKMode.ValueType
    @property
    def preferred_theta(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def d_theta_max(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def duration(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def order_id(self) -> google.protobuf.wrappers_pb2.Int32Value: ...
    def __init__(
        self,
        *,
        id: part_pb2.PartId | None = ...,
        goal_pose: kinematics_pb2.Matrix4x4 | None = ...,
        position_tolerance: kinematics_pb2.PointDistanceTolerances | None = ...,
        orientation_tolerance: kinematics_pb2.ExtEulerAnglesTolerances | None = ...,
        q0: global___ArmPosition | None = ...,
        mode: global___IKMode.ValueType = ...,
        preferred_theta: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        d_theta_max: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        duration: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        order_id: google.protobuf.wrappers_pb2.Int32Value | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["d_theta_max", b"d_theta_max", "duration", b"duration", "goal_pose", b"goal_pose", "id", b"id", "order_id", b"order_id", "orientation_tolerance", b"orientation_tolerance", "position_tolerance", b"position_tolerance", "preferred_theta", b"preferred_theta", "q0", b"q0"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["d_theta_max", b"d_theta_max", "duration", b"duration", "goal_pose", b"goal_pose", "id", b"id", "mode", b"mode", "order_id", b"order_id", "orientation_tolerance", b"orientation_tolerance", "position_tolerance", b"position_tolerance", "preferred_theta", b"preferred_theta", "q0", b"q0"]) -> None: ...

global___ArmCartesianGoal = ArmCartesianGoal

@typing_extensions.final
class ArmJointGoal(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    JOINTS_GOAL_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> part_pb2.PartId: ...
    @property
    def joints_goal(self) -> global___ArmPosition: ...
    @property
    def duration(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    def __init__(
        self,
        *,
        id: part_pb2.PartId | None = ...,
        joints_goal: global___ArmPosition | None = ...,
        duration: google.protobuf.wrappers_pb2.FloatValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["duration", b"duration", "id", b"id", "joints_goal", b"joints_goal"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["duration", b"duration", "id", b"id", "joints_goal", b"joints_goal"]) -> None: ...

global___ArmJointGoal = ArmJointGoal

@typing_extensions.final
class ArmEndEffector(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POSE_FIELD_NUMBER: builtins.int
    @property
    def pose(self) -> kinematics_pb2.Matrix4x4: ...
    def __init__(
        self,
        *,
        pose: kinematics_pb2.Matrix4x4 | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pose", b"pose"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["pose", b"pose"]) -> None: ...

global___ArmEndEffector = ArmEndEffector

@typing_extensions.final
class ArmFKRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    POSITION_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> part_pb2.PartId: ...
    @property
    def position(self) -> global___ArmPosition: ...
    def __init__(
        self,
        *,
        id: part_pb2.PartId | None = ...,
        position: global___ArmPosition | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["id", b"id", "position", b"position"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "position", b"position"]) -> None: ...

global___ArmFKRequest = ArmFKRequest

@typing_extensions.final
class ArmFKSolution(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    END_EFFECTOR_FIELD_NUMBER: builtins.int
    success: builtins.bool
    @property
    def end_effector(self) -> global___ArmEndEffector: ...
    def __init__(
        self,
        *,
        success: builtins.bool = ...,
        end_effector: global___ArmEndEffector | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["end_effector", b"end_effector"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["end_effector", b"end_effector", "success", b"success"]) -> None: ...

global___ArmFKSolution = ArmFKSolution

@typing_extensions.final
class ArmIKRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    TARGET_FIELD_NUMBER: builtins.int
    Q0_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> part_pb2.PartId: ...
    @property
    def target(self) -> global___ArmEndEffector: ...
    @property
    def q0(self) -> global___ArmPosition: ...
    def __init__(
        self,
        *,
        id: part_pb2.PartId | None = ...,
        target: global___ArmEndEffector | None = ...,
        q0: global___ArmPosition | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["id", b"id", "q0", b"q0", "target", b"target"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "q0", b"q0", "target", b"target"]) -> None: ...

global___ArmIKRequest = ArmIKRequest

@typing_extensions.final
class ArmIKSolution(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    ARM_POSITION_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    success: builtins.bool
    @property
    def arm_position(self) -> global___ArmPosition: ...
    @property
    def error(self) -> error_pb2.Error: ...
    def __init__(
        self,
        *,
        success: builtins.bool = ...,
        arm_position: global___ArmPosition | None = ...,
        error: error_pb2.Error | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["arm_position", b"arm_position", "error", b"error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["arm_position", b"arm_position", "error", b"error", "success", b"success"]) -> None: ...

global___ArmIKSolution = ArmIKSolution

@typing_extensions.final
class ArmStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SHOULDER_STATUS_FIELD_NUMBER: builtins.int
    ELBOW_STATUS_FIELD_NUMBER: builtins.int
    WRIST_STATUS_FIELD_NUMBER: builtins.int
    @property
    def shoulder_status(self) -> orbita2d_pb2.Orbita2dStatus: ...
    @property
    def elbow_status(self) -> orbita2d_pb2.Orbita2dStatus: ...
    @property
    def wrist_status(self) -> orbita3d_pb2.Orbita3dStatus: ...
    def __init__(
        self,
        *,
        shoulder_status: orbita2d_pb2.Orbita2dStatus | None = ...,
        elbow_status: orbita2d_pb2.Orbita2dStatus | None = ...,
        wrist_status: orbita3d_pb2.Orbita3dStatus | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["elbow_status", b"elbow_status", "shoulder_status", b"shoulder_status", "wrist_status", b"wrist_status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["elbow_status", b"elbow_status", "shoulder_status", b"shoulder_status", "wrist_status", b"wrist_status"]) -> None: ...

global___ArmStatus = ArmStatus

@typing_extensions.final
class SpeedLimitRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> part_pb2.PartId: ...
    limit: builtins.int
    def __init__(
        self,
        *,
        id: part_pb2.PartId | None = ...,
        limit: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["id", b"id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "limit", b"limit"]) -> None: ...

global___SpeedLimitRequest = SpeedLimitRequest

@typing_extensions.final
class TorqueLimitRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> part_pb2.PartId: ...
    limit: builtins.int
    def __init__(
        self,
        *,
        id: part_pb2.PartId | None = ...,
        limit: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["id", b"id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "limit", b"limit"]) -> None: ...

global___TorqueLimitRequest = TorqueLimitRequest

@typing_extensions.final
class ArmLimits(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SHOULDER_LIMITS_FIELD_NUMBER: builtins.int
    ELBOW_LIMITS_FIELD_NUMBER: builtins.int
    WRIST_LIMITS_FIELD_NUMBER: builtins.int
    @property
    def shoulder_limits(self) -> orbita2d_pb2.Limits2d: ...
    @property
    def elbow_limits(self) -> orbita2d_pb2.Limits2d: ...
    @property
    def wrist_limits(self) -> orbita3d_pb2.Limits3d: ...
    def __init__(
        self,
        *,
        shoulder_limits: orbita2d_pb2.Limits2d | None = ...,
        elbow_limits: orbita2d_pb2.Limits2d | None = ...,
        wrist_limits: orbita3d_pb2.Limits3d | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["elbow_limits", b"elbow_limits", "shoulder_limits", b"shoulder_limits", "wrist_limits", b"wrist_limits"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["elbow_limits", b"elbow_limits", "shoulder_limits", b"shoulder_limits", "wrist_limits", b"wrist_limits"]) -> None: ...

global___ArmLimits = ArmLimits

@typing_extensions.final
class ArmTemperatures(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SHOULDER_TEMPERATURE_FIELD_NUMBER: builtins.int
    ELBOW_TEMPERATURE_FIELD_NUMBER: builtins.int
    WRIST_TEMPERATURE_FIELD_NUMBER: builtins.int
    @property
    def shoulder_temperature(self) -> orbita2d_pb2.Float2d: ...
    @property
    def elbow_temperature(self) -> orbita2d_pb2.Float2d: ...
    @property
    def wrist_temperature(self) -> orbita3d_pb2.Float3d: ...
    def __init__(
        self,
        *,
        shoulder_temperature: orbita2d_pb2.Float2d | None = ...,
        elbow_temperature: orbita2d_pb2.Float2d | None = ...,
        wrist_temperature: orbita3d_pb2.Float3d | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["elbow_temperature", b"elbow_temperature", "shoulder_temperature", b"shoulder_temperature", "wrist_temperature", b"wrist_temperature"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["elbow_temperature", b"elbow_temperature", "shoulder_temperature", b"shoulder_temperature", "wrist_temperature", b"wrist_temperature"]) -> None: ...

global___ArmTemperatures = ArmTemperatures

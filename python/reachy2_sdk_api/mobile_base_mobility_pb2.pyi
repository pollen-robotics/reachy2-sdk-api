"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.wrappers_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class DirectionVector(google.protobuf.message.Message):
    """Speed commands in SI units (m/s and rad/s)"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    THETA_FIELD_NUMBER: builtins.int
    @property
    def x(self) -> google.protobuf.wrappers_pb2.FloatValue:
        """use FloatValue instead of double to avoid 0.0 default value being ignored"""
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

global___DirectionVector = DirectionVector

@typing_extensions.final
class TargetDirectionCommand(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DIRECTION_FIELD_NUMBER: builtins.int
    @property
    def direction(self) -> global___DirectionVector: ...
    def __init__(
        self,
        *,
        direction: global___DirectionVector | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["direction", b"direction"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["direction", b"direction"]) -> None: ...

global___TargetDirectionCommand = TargetDirectionCommand

@typing_extensions.final
class GoToVector(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    X_GOAL_FIELD_NUMBER: builtins.int
    Y_GOAL_FIELD_NUMBER: builtins.int
    THETA_GOAL_FIELD_NUMBER: builtins.int
    @property
    def x_goal(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def y_goal(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def theta_goal(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    def __init__(
        self,
        *,
        x_goal: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        y_goal: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        theta_goal: google.protobuf.wrappers_pb2.FloatValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["theta_goal", b"theta_goal", "x_goal", b"x_goal", "y_goal", b"y_goal"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["theta_goal", b"theta_goal", "x_goal", b"x_goal", "y_goal", b"y_goal"]) -> None: ...

global___GoToVector = GoToVector

@typing_extensions.final
class SetSpeedVector(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    X_VEL_FIELD_NUMBER: builtins.int
    Y_VEL_FIELD_NUMBER: builtins.int
    ROT_VEL_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    @property
    def x_vel(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def y_vel(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def rot_vel(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def duration(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    def __init__(
        self,
        *,
        x_vel: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        y_vel: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        rot_vel: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        duration: google.protobuf.wrappers_pb2.FloatValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["duration", b"duration", "rot_vel", b"rot_vel", "x_vel", b"x_vel", "y_vel", b"y_vel"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["duration", b"duration", "rot_vel", b"rot_vel", "x_vel", b"x_vel", "y_vel", b"y_vel"]) -> None: ...

global___SetSpeedVector = SetSpeedVector

@typing_extensions.final
class DistanceToGoalVector(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DELTA_X_FIELD_NUMBER: builtins.int
    DELTA_Y_FIELD_NUMBER: builtins.int
    DELTA_THETA_FIELD_NUMBER: builtins.int
    DISTANCE_FIELD_NUMBER: builtins.int
    @property
    def delta_x(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def delta_y(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def delta_theta(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def distance(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    def __init__(
        self,
        *,
        delta_x: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        delta_y: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        delta_theta: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        distance: google.protobuf.wrappers_pb2.FloatValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["delta_theta", b"delta_theta", "delta_x", b"delta_x", "delta_y", b"delta_y", "distance", b"distance"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["delta_theta", b"delta_theta", "delta_x", b"delta_x", "delta_y", b"delta_y", "distance", b"distance"]) -> None: ...

global___DistanceToGoalVector = DistanceToGoalVector

@typing_extensions.final
class MobilityServiceAck(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    @property
    def success(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    def __init__(
        self,
        *,
        success: google.protobuf.wrappers_pb2.BoolValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["success", b"success"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["success", b"success"]) -> None: ...

global___MobilityServiceAck = MobilityServiceAck
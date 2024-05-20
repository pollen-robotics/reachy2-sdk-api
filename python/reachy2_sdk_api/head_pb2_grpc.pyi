"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import google.protobuf.empty_pb2
import grpc
import grpc.aio
import head_pb2
import kinematics_pb2
import part_pb2
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class HeadServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    GetAllHeads: grpc.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        head_pb2.ListOfHead,
    ]

    GetState: grpc.UnaryUnaryMultiCallable[
        part_pb2.PartId,
        head_pb2.HeadState,
    ]

    ComputeNeckFK: grpc.UnaryUnaryMultiCallable[
        head_pb2.NeckFKRequest,
        head_pb2.NeckFKSolution,
    ]

    ComputeNeckIK: grpc.UnaryUnaryMultiCallable[
        head_pb2.NeckIKRequest,
        head_pb2.NeckIKSolution,
    ]

    GetOrientation: grpc.UnaryUnaryMultiCallable[
        part_pb2.PartId,
        kinematics_pb2.Rotation3d,
    ]

    Audit: grpc.UnaryUnaryMultiCallable[
        part_pb2.PartId,
        head_pb2.HeadStatus,
    ]

    HeartBeat: grpc.UnaryUnaryMultiCallable[
        part_pb2.PartId,
        google.protobuf.empty_pb2.Empty,
    ]

    Restart: grpc.UnaryUnaryMultiCallable[
        part_pb2.PartId,
        google.protobuf.empty_pb2.Empty,
    ]

    ResetDefaultValues: grpc.UnaryUnaryMultiCallable[
        part_pb2.PartId,
        google.protobuf.empty_pb2.Empty,
    ]

    TurnOn: grpc.UnaryUnaryMultiCallable[
        part_pb2.PartId,
        google.protobuf.empty_pb2.Empty,
    ]

    TurnOff: grpc.UnaryUnaryMultiCallable[
        part_pb2.PartId,
        google.protobuf.empty_pb2.Empty,
    ]

    GetJointsLimits: grpc.UnaryUnaryMultiCallable[
        part_pb2.PartId,
        head_pb2.JointsLimits,
    ]

    GetTemperatures: grpc.UnaryUnaryMultiCallable[
        part_pb2.PartId,
        head_pb2.HeadTemperatures,
    ]

    GetJointGoalPosition: grpc.UnaryUnaryMultiCallable[
        part_pb2.PartId,
        kinematics_pb2.Rotation3d,
    ]

    SetSpeedLimit: grpc.UnaryUnaryMultiCallable[
        head_pb2.SpeedLimitRequest,
        google.protobuf.empty_pb2.Empty,
    ]

    SetTorqueLimit: grpc.UnaryUnaryMultiCallable[
        head_pb2.TorqueLimitRequest,
        google.protobuf.empty_pb2.Empty,
    ]

    SendNeckJointGoal: grpc.UnaryUnaryMultiCallable[
        head_pb2.NeckJointGoal,
        google.protobuf.empty_pb2.Empty,
    ]

class HeadServiceAsyncStub:
    GetAllHeads: grpc.aio.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        head_pb2.ListOfHead,
    ]

    GetState: grpc.aio.UnaryUnaryMultiCallable[
        part_pb2.PartId,
        head_pb2.HeadState,
    ]

    ComputeNeckFK: grpc.aio.UnaryUnaryMultiCallable[
        head_pb2.NeckFKRequest,
        head_pb2.NeckFKSolution,
    ]

    ComputeNeckIK: grpc.aio.UnaryUnaryMultiCallable[
        head_pb2.NeckIKRequest,
        head_pb2.NeckIKSolution,
    ]

    GetOrientation: grpc.aio.UnaryUnaryMultiCallable[
        part_pb2.PartId,
        kinematics_pb2.Rotation3d,
    ]

    Audit: grpc.aio.UnaryUnaryMultiCallable[
        part_pb2.PartId,
        head_pb2.HeadStatus,
    ]

    HeartBeat: grpc.aio.UnaryUnaryMultiCallable[
        part_pb2.PartId,
        google.protobuf.empty_pb2.Empty,
    ]

    Restart: grpc.aio.UnaryUnaryMultiCallable[
        part_pb2.PartId,
        google.protobuf.empty_pb2.Empty,
    ]

    ResetDefaultValues: grpc.aio.UnaryUnaryMultiCallable[
        part_pb2.PartId,
        google.protobuf.empty_pb2.Empty,
    ]

    TurnOn: grpc.aio.UnaryUnaryMultiCallable[
        part_pb2.PartId,
        google.protobuf.empty_pb2.Empty,
    ]

    TurnOff: grpc.aio.UnaryUnaryMultiCallable[
        part_pb2.PartId,
        google.protobuf.empty_pb2.Empty,
    ]

    GetJointsLimits: grpc.aio.UnaryUnaryMultiCallable[
        part_pb2.PartId,
        head_pb2.JointsLimits,
    ]

    GetTemperatures: grpc.aio.UnaryUnaryMultiCallable[
        part_pb2.PartId,
        head_pb2.HeadTemperatures,
    ]

    GetJointGoalPosition: grpc.aio.UnaryUnaryMultiCallable[
        part_pb2.PartId,
        kinematics_pb2.Rotation3d,
    ]

    SetSpeedLimit: grpc.aio.UnaryUnaryMultiCallable[
        head_pb2.SpeedLimitRequest,
        google.protobuf.empty_pb2.Empty,
    ]

    SetTorqueLimit: grpc.aio.UnaryUnaryMultiCallable[
        head_pb2.TorqueLimitRequest,
        google.protobuf.empty_pb2.Empty,
    ]

    SendNeckJointGoal: grpc.aio.UnaryUnaryMultiCallable[
        head_pb2.NeckJointGoal,
        google.protobuf.empty_pb2.Empty,
    ]

class HeadServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetAllHeads(
        self,
        request: google.protobuf.empty_pb2.Empty,
        context: _ServicerContext,
    ) -> typing.Union[head_pb2.ListOfHead, collections.abc.Awaitable[head_pb2.ListOfHead]]: ...

    @abc.abstractmethod
    def GetState(
        self,
        request: part_pb2.PartId,
        context: _ServicerContext,
    ) -> typing.Union[head_pb2.HeadState, collections.abc.Awaitable[head_pb2.HeadState]]: ...

    @abc.abstractmethod
    def ComputeNeckFK(
        self,
        request: head_pb2.NeckFKRequest,
        context: _ServicerContext,
    ) -> typing.Union[head_pb2.NeckFKSolution, collections.abc.Awaitable[head_pb2.NeckFKSolution]]: ...

    @abc.abstractmethod
    def ComputeNeckIK(
        self,
        request: head_pb2.NeckIKRequest,
        context: _ServicerContext,
    ) -> typing.Union[head_pb2.NeckIKSolution, collections.abc.Awaitable[head_pb2.NeckIKSolution]]: ...

    @abc.abstractmethod
    def GetOrientation(
        self,
        request: part_pb2.PartId,
        context: _ServicerContext,
    ) -> typing.Union[kinematics_pb2.Rotation3d, collections.abc.Awaitable[kinematics_pb2.Rotation3d]]: ...

    @abc.abstractmethod
    def Audit(
        self,
        request: part_pb2.PartId,
        context: _ServicerContext,
    ) -> typing.Union[head_pb2.HeadStatus, collections.abc.Awaitable[head_pb2.HeadStatus]]: ...

    @abc.abstractmethod
    def HeartBeat(
        self,
        request: part_pb2.PartId,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]: ...

    @abc.abstractmethod
    def Restart(
        self,
        request: part_pb2.PartId,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]: ...

    @abc.abstractmethod
    def ResetDefaultValues(
        self,
        request: part_pb2.PartId,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]: ...

    @abc.abstractmethod
    def TurnOn(
        self,
        request: part_pb2.PartId,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]: ...

    @abc.abstractmethod
    def TurnOff(
        self,
        request: part_pb2.PartId,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]: ...

    @abc.abstractmethod
    def GetJointsLimits(
        self,
        request: part_pb2.PartId,
        context: _ServicerContext,
    ) -> typing.Union[head_pb2.JointsLimits, collections.abc.Awaitable[head_pb2.JointsLimits]]: ...

    @abc.abstractmethod
    def GetTemperatures(
        self,
        request: part_pb2.PartId,
        context: _ServicerContext,
    ) -> typing.Union[head_pb2.HeadTemperatures, collections.abc.Awaitable[head_pb2.HeadTemperatures]]: ...

    @abc.abstractmethod
    def GetJointGoalPosition(
        self,
        request: part_pb2.PartId,
        context: _ServicerContext,
    ) -> typing.Union[kinematics_pb2.Rotation3d, collections.abc.Awaitable[kinematics_pb2.Rotation3d]]: ...

    @abc.abstractmethod
    def SetSpeedLimit(
        self,
        request: head_pb2.SpeedLimitRequest,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]: ...

    @abc.abstractmethod
    def SetTorqueLimit(
        self,
        request: head_pb2.TorqueLimitRequest,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]: ...

    @abc.abstractmethod
    def SendNeckJointGoal(
        self,
        request: head_pb2.NeckJointGoal,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]: ...

def add_HeadServiceServicer_to_server(servicer: HeadServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...

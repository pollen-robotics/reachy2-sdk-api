"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import collections.abc
import component_pb2
import dynamixel_motor_pb2
import google.protobuf.empty_pb2
import grpc
import grpc.aio
import typing

_T = typing.TypeVar('_T')

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta):
    ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore
    ...

class DynamixelMotorServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    GetAllDynamixelMotor: grpc.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        dynamixel_motor_pb2.ListOfDynamixelMotor,
    ]
    GetState: grpc.UnaryUnaryMultiCallable[
        dynamixel_motor_pb2.DynamixelMotorStateRequest,
        dynamixel_motor_pb2.DynamixelMotorState,
    ]
    StreamState: grpc.UnaryStreamMultiCallable[
        dynamixel_motor_pb2.DynamixelMotorStreamStateRequest,
        dynamixel_motor_pb2.DynamixelMotorState,
    ]
    SendCommand: grpc.UnaryUnaryMultiCallable[
        dynamixel_motor_pb2.DynamixelMotorsCommand,
        google.protobuf.empty_pb2.Empty,
    ]
    StreamCommand: grpc.StreamUnaryMultiCallable[
        dynamixel_motor_pb2.DynamixelMotorsCommand,
        google.protobuf.empty_pb2.Empty,
    ]
    SetPosition: grpc.UnaryUnaryMultiCallable[
        dynamixel_motor_pb2.DynamixelMotorGoal,
        google.protobuf.empty_pb2.Empty,
    ]
    Audit: grpc.UnaryUnaryMultiCallable[
        component_pb2.ComponentId,
        dynamixel_motor_pb2.DynamixelMotorStatus,
    ]
    HeartBeat: grpc.UnaryUnaryMultiCallable[
        component_pb2.ComponentId,
        google.protobuf.empty_pb2.Empty,
    ]
    Restart: grpc.UnaryUnaryMultiCallable[
        component_pb2.ComponentId,
        google.protobuf.empty_pb2.Empty,
    ]

class DynamixelMotorServiceAsyncStub:
    GetAllDynamixelMotor: grpc.aio.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        dynamixel_motor_pb2.ListOfDynamixelMotor,
    ]
    GetState: grpc.aio.UnaryUnaryMultiCallable[
        dynamixel_motor_pb2.DynamixelMotorStateRequest,
        dynamixel_motor_pb2.DynamixelMotorState,
    ]
    StreamState: grpc.aio.UnaryStreamMultiCallable[
        dynamixel_motor_pb2.DynamixelMotorStreamStateRequest,
        dynamixel_motor_pb2.DynamixelMotorState,
    ]
    SendCommand: grpc.aio.UnaryUnaryMultiCallable[
        dynamixel_motor_pb2.DynamixelMotorsCommand,
        google.protobuf.empty_pb2.Empty,
    ]
    StreamCommand: grpc.aio.StreamUnaryMultiCallable[
        dynamixel_motor_pb2.DynamixelMotorsCommand,
        google.protobuf.empty_pb2.Empty,
    ]
    SetPosition: grpc.aio.UnaryUnaryMultiCallable[
        dynamixel_motor_pb2.DynamixelMotorGoal,
        google.protobuf.empty_pb2.Empty,
    ]
    Audit: grpc.aio.UnaryUnaryMultiCallable[
        component_pb2.ComponentId,
        dynamixel_motor_pb2.DynamixelMotorStatus,
    ]
    HeartBeat: grpc.aio.UnaryUnaryMultiCallable[
        component_pb2.ComponentId,
        google.protobuf.empty_pb2.Empty,
    ]
    Restart: grpc.aio.UnaryUnaryMultiCallable[
        component_pb2.ComponentId,
        google.protobuf.empty_pb2.Empty,
    ]

class DynamixelMotorServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetAllDynamixelMotor(
        self,
        request: google.protobuf.empty_pb2.Empty,
        context: _ServicerContext,
    ) -> typing.Union[dynamixel_motor_pb2.ListOfDynamixelMotor, collections.abc.Awaitable[dynamixel_motor_pb2.ListOfDynamixelMotor]]: ...
    @abc.abstractmethod
    def GetState(
        self,
        request: dynamixel_motor_pb2.DynamixelMotorStateRequest,
        context: _ServicerContext,
    ) -> typing.Union[dynamixel_motor_pb2.DynamixelMotorState, collections.abc.Awaitable[dynamixel_motor_pb2.DynamixelMotorState]]: ...
    @abc.abstractmethod
    def StreamState(
        self,
        request: dynamixel_motor_pb2.DynamixelMotorStreamStateRequest,
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[dynamixel_motor_pb2.DynamixelMotorState], collections.abc.AsyncIterator[dynamixel_motor_pb2.DynamixelMotorState]]: ...
    @abc.abstractmethod
    def SendCommand(
        self,
        request: dynamixel_motor_pb2.DynamixelMotorsCommand,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]: ...
    @abc.abstractmethod
    def StreamCommand(
        self,
        request_iterator: _MaybeAsyncIterator[dynamixel_motor_pb2.DynamixelMotorsCommand],
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]: ...
    @abc.abstractmethod
    def SetPosition(
        self,
        request: dynamixel_motor_pb2.DynamixelMotorGoal,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]: ...
    @abc.abstractmethod
    def Audit(
        self,
        request: component_pb2.ComponentId,
        context: _ServicerContext,
    ) -> typing.Union[dynamixel_motor_pb2.DynamixelMotorStatus, collections.abc.Awaitable[dynamixel_motor_pb2.DynamixelMotorStatus]]: ...
    @abc.abstractmethod
    def HeartBeat(
        self,
        request: component_pb2.ComponentId,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]: ...
    @abc.abstractmethod
    def Restart(
        self,
        request: component_pb2.ComponentId,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]: ...

def add_DynamixelMotorServiceServicer_to_server(servicer: DynamixelMotorServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...

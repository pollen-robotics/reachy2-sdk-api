"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import collections.abc
import component_pb2
import google.protobuf.empty_pb2
import grpc
import grpc.aio
import parallel_gripper_pb2
import typing

_T = typing.TypeVar('_T')

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta):
    ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore
    ...

class GripperServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    GetAllParallelGripper: grpc.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        parallel_gripper_pb2.ListOfParallelGripperInfo,
    ]
    GetState: grpc.UnaryUnaryMultiCallable[
        parallel_gripper_pb2.ParallelGripperStateRequest,
        parallel_gripper_pb2.ParallelGripperState,
    ]
    StreamState: grpc.UnaryStreamMultiCallable[
        parallel_gripper_pb2.ParallelGripperStreamStateRequest,
        parallel_gripper_pb2.ParallelGripperState,
    ]
    SendCommand: grpc.UnaryUnaryMultiCallable[
        parallel_gripper_pb2.ParallelGripperCommand,
        google.protobuf.empty_pb2.Empty,
    ]
    StreamCommand: grpc.StreamUnaryMultiCallable[
        parallel_gripper_pb2.ParallelGripperCommand,
        google.protobuf.empty_pb2.Empty,
    ]
    Audit: grpc.UnaryUnaryMultiCallable[
        component_pb2.ComponentId,
        parallel_gripper_pb2.ParallelGripperStatus,
    ]
    HeartBeat: grpc.UnaryUnaryMultiCallable[
        component_pb2.ComponentId,
        google.protobuf.empty_pb2.Empty,
    ]
    Restart: grpc.UnaryUnaryMultiCallable[
        component_pb2.ComponentId,
        google.protobuf.empty_pb2.Empty,
    ]

class GripperServiceAsyncStub:
    GetAllParallelGripper: grpc.aio.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        parallel_gripper_pb2.ListOfParallelGripperInfo,
    ]
    GetState: grpc.aio.UnaryUnaryMultiCallable[
        parallel_gripper_pb2.ParallelGripperStateRequest,
        parallel_gripper_pb2.ParallelGripperState,
    ]
    StreamState: grpc.aio.UnaryStreamMultiCallable[
        parallel_gripper_pb2.ParallelGripperStreamStateRequest,
        parallel_gripper_pb2.ParallelGripperState,
    ]
    SendCommand: grpc.aio.UnaryUnaryMultiCallable[
        parallel_gripper_pb2.ParallelGripperCommand,
        google.protobuf.empty_pb2.Empty,
    ]
    StreamCommand: grpc.aio.StreamUnaryMultiCallable[
        parallel_gripper_pb2.ParallelGripperCommand,
        google.protobuf.empty_pb2.Empty,
    ]
    Audit: grpc.aio.UnaryUnaryMultiCallable[
        component_pb2.ComponentId,
        parallel_gripper_pb2.ParallelGripperStatus,
    ]
    HeartBeat: grpc.aio.UnaryUnaryMultiCallable[
        component_pb2.ComponentId,
        google.protobuf.empty_pb2.Empty,
    ]
    Restart: grpc.aio.UnaryUnaryMultiCallable[
        component_pb2.ComponentId,
        google.protobuf.empty_pb2.Empty,
    ]

class GripperServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetAllParallelGripper(
        self,
        request: google.protobuf.empty_pb2.Empty,
        context: _ServicerContext,
    ) -> typing.Union[parallel_gripper_pb2.ListOfParallelGripperInfo, collections.abc.Awaitable[parallel_gripper_pb2.ListOfParallelGripperInfo]]: ...
    @abc.abstractmethod
    def GetState(
        self,
        request: parallel_gripper_pb2.ParallelGripperStateRequest,
        context: _ServicerContext,
    ) -> typing.Union[parallel_gripper_pb2.ParallelGripperState, collections.abc.Awaitable[parallel_gripper_pb2.ParallelGripperState]]: ...
    @abc.abstractmethod
    def StreamState(
        self,
        request: parallel_gripper_pb2.ParallelGripperStreamStateRequest,
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[parallel_gripper_pb2.ParallelGripperState], collections.abc.AsyncIterator[parallel_gripper_pb2.ParallelGripperState]]: ...
    @abc.abstractmethod
    def SendCommand(
        self,
        request: parallel_gripper_pb2.ParallelGripperCommand,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]: ...
    @abc.abstractmethod
    def StreamCommand(
        self,
        request_iterator: _MaybeAsyncIterator[parallel_gripper_pb2.ParallelGripperCommand],
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]: ...
    @abc.abstractmethod
    def Audit(
        self,
        request: component_pb2.ComponentId,
        context: _ServicerContext,
    ) -> typing.Union[parallel_gripper_pb2.ParallelGripperStatus, collections.abc.Awaitable[parallel_gripper_pb2.ParallelGripperStatus]]: ...
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

def add_GripperServiceServicer_to_server(servicer: GripperServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...

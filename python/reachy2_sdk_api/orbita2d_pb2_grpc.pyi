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
import orbita2d_pb2
import typing

_T = typing.TypeVar('_T')

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta):
    ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore
    ...

class Orbita2dServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    GetAllOrbita2d: grpc.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        orbita2d_pb2.ListOfOrbita2d,
    ]
    GetState: grpc.UnaryUnaryMultiCallable[
        orbita2d_pb2.Orbita2dStateRequest,
        orbita2d_pb2.Orbita2dState,
    ]
    StreamState: grpc.UnaryStreamMultiCallable[
        orbita2d_pb2.Orbita2dStreamStateRequest,
        orbita2d_pb2.Orbita2dState,
    ]
    SendCommand: grpc.UnaryUnaryMultiCallable[
        orbita2d_pb2.Orbita2dsCommand,
        google.protobuf.empty_pb2.Empty,
    ]
    StreamCommand: grpc.StreamUnaryMultiCallable[
        orbita2d_pb2.Orbita2dsCommand,
        google.protobuf.empty_pb2.Empty,
    ]
    Audit: grpc.UnaryUnaryMultiCallable[
        component_pb2.ComponentId,
        orbita2d_pb2.Orbita2dStatus,
    ]
    HeartBeat: grpc.UnaryUnaryMultiCallable[
        component_pb2.ComponentId,
        google.protobuf.empty_pb2.Empty,
    ]
    Restart: grpc.UnaryUnaryMultiCallable[
        component_pb2.ComponentId,
        google.protobuf.empty_pb2.Empty,
    ]

class Orbita2dServiceAsyncStub:
    GetAllOrbita2d: grpc.aio.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        orbita2d_pb2.ListOfOrbita2d,
    ]
    GetState: grpc.aio.UnaryUnaryMultiCallable[
        orbita2d_pb2.Orbita2dStateRequest,
        orbita2d_pb2.Orbita2dState,
    ]
    StreamState: grpc.aio.UnaryStreamMultiCallable[
        orbita2d_pb2.Orbita2dStreamStateRequest,
        orbita2d_pb2.Orbita2dState,
    ]
    SendCommand: grpc.aio.UnaryUnaryMultiCallable[
        orbita2d_pb2.Orbita2dsCommand,
        google.protobuf.empty_pb2.Empty,
    ]
    StreamCommand: grpc.aio.StreamUnaryMultiCallable[
        orbita2d_pb2.Orbita2dsCommand,
        google.protobuf.empty_pb2.Empty,
    ]
    Audit: grpc.aio.UnaryUnaryMultiCallable[
        component_pb2.ComponentId,
        orbita2d_pb2.Orbita2dStatus,
    ]
    HeartBeat: grpc.aio.UnaryUnaryMultiCallable[
        component_pb2.ComponentId,
        google.protobuf.empty_pb2.Empty,
    ]
    Restart: grpc.aio.UnaryUnaryMultiCallable[
        component_pb2.ComponentId,
        google.protobuf.empty_pb2.Empty,
    ]

class Orbita2dServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetAllOrbita2d(
        self,
        request: google.protobuf.empty_pb2.Empty,
        context: _ServicerContext,
    ) -> typing.Union[orbita2d_pb2.ListOfOrbita2d, collections.abc.Awaitable[orbita2d_pb2.ListOfOrbita2d]]: ...
    @abc.abstractmethod
    def GetState(
        self,
        request: orbita2d_pb2.Orbita2dStateRequest,
        context: _ServicerContext,
    ) -> typing.Union[orbita2d_pb2.Orbita2dState, collections.abc.Awaitable[orbita2d_pb2.Orbita2dState]]: ...
    @abc.abstractmethod
    def StreamState(
        self,
        request: orbita2d_pb2.Orbita2dStreamStateRequest,
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[orbita2d_pb2.Orbita2dState], collections.abc.AsyncIterator[orbita2d_pb2.Orbita2dState]]: ...
    @abc.abstractmethod
    def SendCommand(
        self,
        request: orbita2d_pb2.Orbita2dsCommand,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]: ...
    @abc.abstractmethod
    def StreamCommand(
        self,
        request_iterator: _MaybeAsyncIterator[orbita2d_pb2.Orbita2dsCommand],
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]: ...
    @abc.abstractmethod
    def Audit(
        self,
        request: component_pb2.ComponentId,
        context: _ServicerContext,
    ) -> typing.Union[orbita2d_pb2.Orbita2dStatus, collections.abc.Awaitable[orbita2d_pb2.Orbita2dStatus]]: ...
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

def add_Orbita2dServiceServicer_to_server(servicer: Orbita2dServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...

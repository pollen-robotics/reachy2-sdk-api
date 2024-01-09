"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import collections.abc
import google.protobuf.empty_pb2
import goto_pb2
import grpc
import grpc.aio
import typing

_T = typing.TypeVar('_T')

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta):
    ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore
    ...

class GoToServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    GoToCartesian: grpc.UnaryUnaryMultiCallable[
        goto_pb2.GoToRequest,
        goto_pb2.GoToId,
    ]
    GoToJoints: grpc.UnaryUnaryMultiCallable[
        goto_pb2.GoToRequest,
        goto_pb2.GoToId,
    ]
    GetGoToState: grpc.UnaryUnaryMultiCallable[
        goto_pb2.GoToId,
        goto_pb2.GoToGoalStatus,
    ]
    CancelGoTo: grpc.UnaryUnaryMultiCallable[
        goto_pb2.GoToId,
        goto_pb2.GoToAck,
    ]
    CancelAllGoTo: grpc.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        goto_pb2.GoToAck,
    ]

class GoToServiceAsyncStub:
    GoToCartesian: grpc.aio.UnaryUnaryMultiCallable[
        goto_pb2.GoToRequest,
        goto_pb2.GoToId,
    ]
    GoToJoints: grpc.aio.UnaryUnaryMultiCallable[
        goto_pb2.GoToRequest,
        goto_pb2.GoToId,
    ]
    GetGoToState: grpc.aio.UnaryUnaryMultiCallable[
        goto_pb2.GoToId,
        goto_pb2.GoToGoalStatus,
    ]
    CancelGoTo: grpc.aio.UnaryUnaryMultiCallable[
        goto_pb2.GoToId,
        goto_pb2.GoToAck,
    ]
    CancelAllGoTo: grpc.aio.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        goto_pb2.GoToAck,
    ]

class GoToServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GoToCartesian(
        self,
        request: goto_pb2.GoToRequest,
        context: _ServicerContext,
    ) -> typing.Union[goto_pb2.GoToId, collections.abc.Awaitable[goto_pb2.GoToId]]: ...
    @abc.abstractmethod
    def GoToJoints(
        self,
        request: goto_pb2.GoToRequest,
        context: _ServicerContext,
    ) -> typing.Union[goto_pb2.GoToId, collections.abc.Awaitable[goto_pb2.GoToId]]: ...
    @abc.abstractmethod
    def GetGoToState(
        self,
        request: goto_pb2.GoToId,
        context: _ServicerContext,
    ) -> typing.Union[goto_pb2.GoToGoalStatus, collections.abc.Awaitable[goto_pb2.GoToGoalStatus]]: ...
    @abc.abstractmethod
    def CancelGoTo(
        self,
        request: goto_pb2.GoToId,
        context: _ServicerContext,
    ) -> typing.Union[goto_pb2.GoToAck, collections.abc.Awaitable[goto_pb2.GoToAck]]: ...
    @abc.abstractmethod
    def CancelAllGoTo(
        self,
        request: google.protobuf.empty_pb2.Empty,
        context: _ServicerContext,
    ) -> typing.Union[goto_pb2.GoToAck, collections.abc.Awaitable[goto_pb2.GoToAck]]: ...

def add_GoToServiceServicer_to_server(servicer: GoToServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...

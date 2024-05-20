"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import google.protobuf.empty_pb2
import grpc
import grpc.aio
import reachy_pb2
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class ReachyServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    GetReachy: grpc.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        reachy_pb2.Reachy,
    ]

    GetReachyState: grpc.UnaryUnaryMultiCallable[
        reachy_pb2.ReachyId,
        reachy_pb2.ReachyState,
    ]

    StreamReachyState: grpc.UnaryStreamMultiCallable[
        reachy_pb2.ReachyStreamStateRequest,
        reachy_pb2.ReachyState,
    ]

class ReachyServiceAsyncStub:
    GetReachy: grpc.aio.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        reachy_pb2.Reachy,
    ]

    GetReachyState: grpc.aio.UnaryUnaryMultiCallable[
        reachy_pb2.ReachyId,
        reachy_pb2.ReachyState,
    ]

    StreamReachyState: grpc.aio.UnaryStreamMultiCallable[
        reachy_pb2.ReachyStreamStateRequest,
        reachy_pb2.ReachyState,
    ]

class ReachyServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def GetReachy(
        self,
        request: google.protobuf.empty_pb2.Empty,
        context: _ServicerContext,
    ) -> typing.Union[reachy_pb2.Reachy, collections.abc.Awaitable[reachy_pb2.Reachy]]: ...

    @abc.abstractmethod
    def GetReachyState(
        self,
        request: reachy_pb2.ReachyId,
        context: _ServicerContext,
    ) -> typing.Union[reachy_pb2.ReachyState, collections.abc.Awaitable[reachy_pb2.ReachyState]]: ...

    @abc.abstractmethod
    def StreamReachyState(
        self,
        request: reachy_pb2.ReachyStreamStateRequest,
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[reachy_pb2.ReachyState], collections.abc.AsyncIterator[reachy_pb2.ReachyState]]: ...

def add_ReachyServiceServicer_to_server(servicer: ReachyServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...

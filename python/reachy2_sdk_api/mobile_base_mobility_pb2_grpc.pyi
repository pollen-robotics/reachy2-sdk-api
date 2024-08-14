"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import collections.abc
import grpc
import grpc.aio
import mobile_base_mobility_pb2
import part_pb2
import typing

_T = typing.TypeVar('_T')

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta):
    ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore
    ...

class MobileBaseMobilityServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    SendDirection: grpc.UnaryUnaryMultiCallable[
        mobile_base_mobility_pb2.TargetDirectionCommand,
        mobile_base_mobility_pb2.MobilityServiceAck,
    ]
    """Mobility commands"""
    SendSetSpeed: grpc.UnaryUnaryMultiCallable[
        mobile_base_mobility_pb2.SetSpeedVector,
        mobile_base_mobility_pb2.MobilityServiceAck,
    ]
    SendGoTo: grpc.UnaryUnaryMultiCallable[
        mobile_base_mobility_pb2.GoToVector,
        mobile_base_mobility_pb2.MobilityServiceAck,
    ]
    DistanceToGoal: grpc.UnaryUnaryMultiCallable[
        part_pb2.PartId,
        mobile_base_mobility_pb2.DistanceToGoalVector,
    ]

class MobileBaseMobilityServiceAsyncStub:
    SendDirection: grpc.aio.UnaryUnaryMultiCallable[
        mobile_base_mobility_pb2.TargetDirectionCommand,
        mobile_base_mobility_pb2.MobilityServiceAck,
    ]
    """Mobility commands"""
    SendSetSpeed: grpc.aio.UnaryUnaryMultiCallable[
        mobile_base_mobility_pb2.SetSpeedVector,
        mobile_base_mobility_pb2.MobilityServiceAck,
    ]
    SendGoTo: grpc.aio.UnaryUnaryMultiCallable[
        mobile_base_mobility_pb2.GoToVector,
        mobile_base_mobility_pb2.MobilityServiceAck,
    ]
    DistanceToGoal: grpc.aio.UnaryUnaryMultiCallable[
        part_pb2.PartId,
        mobile_base_mobility_pb2.DistanceToGoalVector,
    ]

class MobileBaseMobilityServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def SendDirection(
        self,
        request: mobile_base_mobility_pb2.TargetDirectionCommand,
        context: _ServicerContext,
    ) -> typing.Union[mobile_base_mobility_pb2.MobilityServiceAck, collections.abc.Awaitable[mobile_base_mobility_pb2.MobilityServiceAck]]:
        """Mobility commands"""
    @abc.abstractmethod
    def SendSetSpeed(
        self,
        request: mobile_base_mobility_pb2.SetSpeedVector,
        context: _ServicerContext,
    ) -> typing.Union[mobile_base_mobility_pb2.MobilityServiceAck, collections.abc.Awaitable[mobile_base_mobility_pb2.MobilityServiceAck]]: ...
    @abc.abstractmethod
    def SendGoTo(
        self,
        request: mobile_base_mobility_pb2.GoToVector,
        context: _ServicerContext,
    ) -> typing.Union[mobile_base_mobility_pb2.MobilityServiceAck, collections.abc.Awaitable[mobile_base_mobility_pb2.MobilityServiceAck]]: ...
    @abc.abstractmethod
    def DistanceToGoal(
        self,
        request: part_pb2.PartId,
        context: _ServicerContext,
    ) -> typing.Union[mobile_base_mobility_pb2.DistanceToGoalVector, collections.abc.Awaitable[mobile_base_mobility_pb2.DistanceToGoalVector]]: ...

def add_MobileBaseMobilityServiceServicer_to_server(servicer: MobileBaseMobilityServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...

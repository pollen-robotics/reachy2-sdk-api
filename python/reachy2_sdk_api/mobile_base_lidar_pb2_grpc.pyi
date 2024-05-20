"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import google.protobuf.empty_pb2
import grpc
import grpc.aio
import mobile_base_lidar_pb2
import mobile_base_mobility_pb2
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class MobileBaseLidarServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    SetZuuuSafety: grpc.UnaryUnaryMultiCallable[
        mobile_base_lidar_pb2.LidarSafety,
        mobile_base_mobility_pb2.MobilityServiceAck,
    ]

    GetZuuuSafety: grpc.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        mobile_base_lidar_pb2.LidarSafety,
    ]

    GetLidarMap: grpc.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        mobile_base_lidar_pb2.LidarMap,
    ]

    GetLidarObstacleDetectionStatus: grpc.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        mobile_base_lidar_pb2.LidarObstacleDetectionStatus,
    ]

class MobileBaseLidarServiceAsyncStub:
    SetZuuuSafety: grpc.aio.UnaryUnaryMultiCallable[
        mobile_base_lidar_pb2.LidarSafety,
        mobile_base_mobility_pb2.MobilityServiceAck,
    ]

    GetZuuuSafety: grpc.aio.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        mobile_base_lidar_pb2.LidarSafety,
    ]

    GetLidarMap: grpc.aio.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        mobile_base_lidar_pb2.LidarMap,
    ]

    GetLidarObstacleDetectionStatus: grpc.aio.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        mobile_base_lidar_pb2.LidarObstacleDetectionStatus,
    ]

class MobileBaseLidarServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def SetZuuuSafety(
        self,
        request: mobile_base_lidar_pb2.LidarSafety,
        context: _ServicerContext,
    ) -> typing.Union[mobile_base_mobility_pb2.MobilityServiceAck, collections.abc.Awaitable[mobile_base_mobility_pb2.MobilityServiceAck]]: ...

    @abc.abstractmethod
    def GetZuuuSafety(
        self,
        request: google.protobuf.empty_pb2.Empty,
        context: _ServicerContext,
    ) -> typing.Union[mobile_base_lidar_pb2.LidarSafety, collections.abc.Awaitable[mobile_base_lidar_pb2.LidarSafety]]: ...

    @abc.abstractmethod
    def GetLidarMap(
        self,
        request: google.protobuf.empty_pb2.Empty,
        context: _ServicerContext,
    ) -> typing.Union[mobile_base_lidar_pb2.LidarMap, collections.abc.Awaitable[mobile_base_lidar_pb2.LidarMap]]: ...

    @abc.abstractmethod
    def GetLidarObstacleDetectionStatus(
        self,
        request: google.protobuf.empty_pb2.Empty,
        context: _ServicerContext,
    ) -> typing.Union[mobile_base_lidar_pb2.LidarObstacleDetectionStatus, collections.abc.Awaitable[mobile_base_lidar_pb2.LidarObstacleDetectionStatus]]: ...

def add_MobileBaseLidarServiceServicer_to_server(servicer: MobileBaseLidarServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...

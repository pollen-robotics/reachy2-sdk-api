"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import collections.abc
import google.protobuf.empty_pb2
import grpc
import grpc.aio
import mobile_base_mobility_pb2
import mobile_base_utility_pb2
import typing

_T = typing.TypeVar('_T')

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta):
    ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore
    ...

class MobileBaseUtilityServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    SetControlMode: grpc.UnaryUnaryMultiCallable[
        mobile_base_utility_pb2.ControlModeCommand,
        mobile_base_mobility_pb2.MobilityServiceAck,
    ]
    GetControlMode: grpc.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        mobile_base_utility_pb2.ControlModeCommand,
    ]
    SetZuuuMode: grpc.UnaryUnaryMultiCallable[
        mobile_base_utility_pb2.ZuuuModeCommand,
        mobile_base_mobility_pb2.MobilityServiceAck,
    ]
    GetZuuuMode: grpc.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        mobile_base_utility_pb2.ZuuuModeCommand,
    ]
    GetBatteryLevel: grpc.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        mobile_base_utility_pb2.BatteryLevel,
    ]
    GetOdometry: grpc.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        mobile_base_utility_pb2.OdometryVector,
    ]
    ResetOdometry: grpc.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        mobile_base_mobility_pb2.MobilityServiceAck,
    ]
    GetMobileBase: grpc.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        mobile_base_utility_pb2.MobileBase,
    ]
    GetState: grpc.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        mobile_base_utility_pb2.MobileBaseState,
    ]

class MobileBaseUtilityServiceAsyncStub:
    SetControlMode: grpc.aio.UnaryUnaryMultiCallable[
        mobile_base_utility_pb2.ControlModeCommand,
        mobile_base_mobility_pb2.MobilityServiceAck,
    ]
    GetControlMode: grpc.aio.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        mobile_base_utility_pb2.ControlModeCommand,
    ]
    SetZuuuMode: grpc.aio.UnaryUnaryMultiCallable[
        mobile_base_utility_pb2.ZuuuModeCommand,
        mobile_base_mobility_pb2.MobilityServiceAck,
    ]
    GetZuuuMode: grpc.aio.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        mobile_base_utility_pb2.ZuuuModeCommand,
    ]
    GetBatteryLevel: grpc.aio.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        mobile_base_utility_pb2.BatteryLevel,
    ]
    GetOdometry: grpc.aio.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        mobile_base_utility_pb2.OdometryVector,
    ]
    ResetOdometry: grpc.aio.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        mobile_base_mobility_pb2.MobilityServiceAck,
    ]
    GetMobileBase: grpc.aio.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        mobile_base_utility_pb2.MobileBase,
    ]
    GetState: grpc.aio.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        mobile_base_utility_pb2.MobileBaseState,
    ]

class MobileBaseUtilityServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def SetControlMode(
        self,
        request: mobile_base_utility_pb2.ControlModeCommand,
        context: _ServicerContext,
    ) -> typing.Union[mobile_base_mobility_pb2.MobilityServiceAck, collections.abc.Awaitable[mobile_base_mobility_pb2.MobilityServiceAck]]: ...
    @abc.abstractmethod
    def GetControlMode(
        self,
        request: google.protobuf.empty_pb2.Empty,
        context: _ServicerContext,
    ) -> typing.Union[mobile_base_utility_pb2.ControlModeCommand, collections.abc.Awaitable[mobile_base_utility_pb2.ControlModeCommand]]: ...
    @abc.abstractmethod
    def SetZuuuMode(
        self,
        request: mobile_base_utility_pb2.ZuuuModeCommand,
        context: _ServicerContext,
    ) -> typing.Union[mobile_base_mobility_pb2.MobilityServiceAck, collections.abc.Awaitable[mobile_base_mobility_pb2.MobilityServiceAck]]: ...
    @abc.abstractmethod
    def GetZuuuMode(
        self,
        request: google.protobuf.empty_pb2.Empty,
        context: _ServicerContext,
    ) -> typing.Union[mobile_base_utility_pb2.ZuuuModeCommand, collections.abc.Awaitable[mobile_base_utility_pb2.ZuuuModeCommand]]: ...
    @abc.abstractmethod
    def GetBatteryLevel(
        self,
        request: google.protobuf.empty_pb2.Empty,
        context: _ServicerContext,
    ) -> typing.Union[mobile_base_utility_pb2.BatteryLevel, collections.abc.Awaitable[mobile_base_utility_pb2.BatteryLevel]]: ...
    @abc.abstractmethod
    def GetOdometry(
        self,
        request: google.protobuf.empty_pb2.Empty,
        context: _ServicerContext,
    ) -> typing.Union[mobile_base_utility_pb2.OdometryVector, collections.abc.Awaitable[mobile_base_utility_pb2.OdometryVector]]: ...
    @abc.abstractmethod
    def ResetOdometry(
        self,
        request: google.protobuf.empty_pb2.Empty,
        context: _ServicerContext,
    ) -> typing.Union[mobile_base_mobility_pb2.MobilityServiceAck, collections.abc.Awaitable[mobile_base_mobility_pb2.MobilityServiceAck]]: ...
    @abc.abstractmethod
    def GetMobileBase(
        self,
        request: google.protobuf.empty_pb2.Empty,
        context: _ServicerContext,
    ) -> typing.Union[mobile_base_utility_pb2.MobileBase, collections.abc.Awaitable[mobile_base_utility_pb2.MobileBase]]: ...
    @abc.abstractmethod
    def GetState(
        self,
        request: google.protobuf.empty_pb2.Empty,
        context: _ServicerContext,
    ) -> typing.Union[mobile_base_utility_pb2.MobileBaseState, collections.abc.Awaitable[mobile_base_utility_pb2.MobileBaseState]]: ...

def add_MobileBaseUtilityServiceServicer_to_server(servicer: MobileBaseUtilityServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
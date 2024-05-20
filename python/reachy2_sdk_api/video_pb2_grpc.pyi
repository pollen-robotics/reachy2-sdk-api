"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import google.protobuf.empty_pb2
import grpc
import grpc.aio
import typing
import video_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class VideoServiceStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    InitAllCameras: grpc.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        video_pb2.ListOfCameraInfo,
    ]

    GetFrame: grpc.UnaryUnaryMultiCallable[
        video_pb2.ViewRequest,
        video_pb2.Frame,
    ]

    GetDepthFrame: grpc.UnaryUnaryMultiCallable[
        video_pb2.ViewRequest,
        video_pb2.Frame,
    ]

    GetDepthMap: grpc.UnaryUnaryMultiCallable[
        video_pb2.CameraInfo,
        video_pb2.Frame,
    ]

    GetDisparity: grpc.UnaryUnaryMultiCallable[
        video_pb2.CameraInfo,
        video_pb2.Frame,
    ]

    GetIntrinsicMatrix: grpc.UnaryUnaryMultiCallable[
        video_pb2.ViewRequest,
        video_pb2.IntrinsicMatrix,
    ]

    Capture: grpc.UnaryUnaryMultiCallable[
        video_pb2.CameraInfo,
        video_pb2.VideoAck,
    ]

    GoodBye: grpc.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        google.protobuf.empty_pb2.Empty,
    ]

class VideoServiceAsyncStub:
    InitAllCameras: grpc.aio.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        video_pb2.ListOfCameraInfo,
    ]

    GetFrame: grpc.aio.UnaryUnaryMultiCallable[
        video_pb2.ViewRequest,
        video_pb2.Frame,
    ]

    GetDepthFrame: grpc.aio.UnaryUnaryMultiCallable[
        video_pb2.ViewRequest,
        video_pb2.Frame,
    ]

    GetDepthMap: grpc.aio.UnaryUnaryMultiCallable[
        video_pb2.CameraInfo,
        video_pb2.Frame,
    ]

    GetDisparity: grpc.aio.UnaryUnaryMultiCallable[
        video_pb2.CameraInfo,
        video_pb2.Frame,
    ]

    GetIntrinsicMatrix: grpc.aio.UnaryUnaryMultiCallable[
        video_pb2.ViewRequest,
        video_pb2.IntrinsicMatrix,
    ]

    Capture: grpc.aio.UnaryUnaryMultiCallable[
        video_pb2.CameraInfo,
        video_pb2.VideoAck,
    ]

    GoodBye: grpc.aio.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        google.protobuf.empty_pb2.Empty,
    ]

class VideoServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def InitAllCameras(
        self,
        request: google.protobuf.empty_pb2.Empty,
        context: _ServicerContext,
    ) -> typing.Union[video_pb2.ListOfCameraInfo, collections.abc.Awaitable[video_pb2.ListOfCameraInfo]]: ...

    @abc.abstractmethod
    def GetFrame(
        self,
        request: video_pb2.ViewRequest,
        context: _ServicerContext,
    ) -> typing.Union[video_pb2.Frame, collections.abc.Awaitable[video_pb2.Frame]]: ...

    @abc.abstractmethod
    def GetDepthFrame(
        self,
        request: video_pb2.ViewRequest,
        context: _ServicerContext,
    ) -> typing.Union[video_pb2.Frame, collections.abc.Awaitable[video_pb2.Frame]]: ...

    @abc.abstractmethod
    def GetDepthMap(
        self,
        request: video_pb2.CameraInfo,
        context: _ServicerContext,
    ) -> typing.Union[video_pb2.Frame, collections.abc.Awaitable[video_pb2.Frame]]: ...

    @abc.abstractmethod
    def GetDisparity(
        self,
        request: video_pb2.CameraInfo,
        context: _ServicerContext,
    ) -> typing.Union[video_pb2.Frame, collections.abc.Awaitable[video_pb2.Frame]]: ...

    @abc.abstractmethod
    def GetIntrinsicMatrix(
        self,
        request: video_pb2.ViewRequest,
        context: _ServicerContext,
    ) -> typing.Union[video_pb2.IntrinsicMatrix, collections.abc.Awaitable[video_pb2.IntrinsicMatrix]]: ...

    @abc.abstractmethod
    def Capture(
        self,
        request: video_pb2.CameraInfo,
        context: _ServicerContext,
    ) -> typing.Union[video_pb2.VideoAck, collections.abc.Awaitable[video_pb2.VideoAck]]: ...

    @abc.abstractmethod
    def GoodBye(
        self,
        request: google.protobuf.empty_pb2.Empty,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]: ...

def add_VideoServiceServicer_to_server(servicer: VideoServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...

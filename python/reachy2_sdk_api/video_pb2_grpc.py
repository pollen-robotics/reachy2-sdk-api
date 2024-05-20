# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import video_pb2 as video__pb2


class VideoServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.InitAllCameras = channel.unary_unary(
                '/component.video.VideoService/InitAllCameras',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=video__pb2.ListOfCameraInfo.FromString,
                )
        self.GetFrame = channel.unary_unary(
                '/component.video.VideoService/GetFrame',
                request_serializer=video__pb2.ViewRequest.SerializeToString,
                response_deserializer=video__pb2.Frame.FromString,
                )
        self.GetDepthFrame = channel.unary_unary(
                '/component.video.VideoService/GetDepthFrame',
                request_serializer=video__pb2.ViewRequest.SerializeToString,
                response_deserializer=video__pb2.Frame.FromString,
                )
        self.GetDepthMap = channel.unary_unary(
                '/component.video.VideoService/GetDepthMap',
                request_serializer=video__pb2.CameraInfo.SerializeToString,
                response_deserializer=video__pb2.Frame.FromString,
                )
        self.GetDisparity = channel.unary_unary(
                '/component.video.VideoService/GetDisparity',
                request_serializer=video__pb2.CameraInfo.SerializeToString,
                response_deserializer=video__pb2.Frame.FromString,
                )
        self.GetIntrinsicMatrix = channel.unary_unary(
                '/component.video.VideoService/GetIntrinsicMatrix',
                request_serializer=video__pb2.CameraInfo.SerializeToString,
                response_deserializer=video__pb2.IntrinsicMatrix.FromString,
                )
        self.Capture = channel.unary_unary(
                '/component.video.VideoService/Capture',
                request_serializer=video__pb2.CameraInfo.SerializeToString,
                response_deserializer=video__pb2.VideoAck.FromString,
                )
        self.GoodBye = channel.unary_unary(
                '/component.video.VideoService/GoodBye',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class VideoServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def InitAllCameras(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFrame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDepthFrame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDepthMap(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDisparity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIntrinsicMatrix(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Capture(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GoodBye(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VideoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'InitAllCameras': grpc.unary_unary_rpc_method_handler(
                    servicer.InitAllCameras,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=video__pb2.ListOfCameraInfo.SerializeToString,
            ),
            'GetFrame': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFrame,
                    request_deserializer=video__pb2.ViewRequest.FromString,
                    response_serializer=video__pb2.Frame.SerializeToString,
            ),
            'GetDepthFrame': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDepthFrame,
                    request_deserializer=video__pb2.ViewRequest.FromString,
                    response_serializer=video__pb2.Frame.SerializeToString,
            ),
            'GetDepthMap': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDepthMap,
                    request_deserializer=video__pb2.CameraInfo.FromString,
                    response_serializer=video__pb2.Frame.SerializeToString,
            ),
            'GetDisparity': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDisparity,
                    request_deserializer=video__pb2.CameraInfo.FromString,
                    response_serializer=video__pb2.Frame.SerializeToString,
            ),
            'GetIntrinsicMatrix': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIntrinsicMatrix,
                    request_deserializer=video__pb2.CameraInfo.FromString,
                    response_serializer=video__pb2.IntrinsicMatrix.SerializeToString,
            ),
            'Capture': grpc.unary_unary_rpc_method_handler(
                    servicer.Capture,
                    request_deserializer=video__pb2.CameraInfo.FromString,
                    response_serializer=video__pb2.VideoAck.SerializeToString,
            ),
            'GoodBye': grpc.unary_unary_rpc_method_handler(
                    servicer.GoodBye,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'component.video.VideoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VideoService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def InitAllCameras(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/component.video.VideoService/InitAllCameras',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            video__pb2.ListOfCameraInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFrame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/component.video.VideoService/GetFrame',
            video__pb2.ViewRequest.SerializeToString,
            video__pb2.Frame.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDepthFrame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/component.video.VideoService/GetDepthFrame',
            video__pb2.ViewRequest.SerializeToString,
            video__pb2.Frame.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDepthMap(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/component.video.VideoService/GetDepthMap',
            video__pb2.CameraInfo.SerializeToString,
            video__pb2.Frame.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDisparity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/component.video.VideoService/GetDisparity',
            video__pb2.CameraInfo.SerializeToString,
            video__pb2.Frame.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetIntrinsicMatrix(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/component.video.VideoService/GetIntrinsicMatrix',
            video__pb2.CameraInfo.SerializeToString,
            video__pb2.IntrinsicMatrix.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Capture(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/component.video.VideoService/Capture',
            video__pb2.CameraInfo.SerializeToString,
            video__pb2.VideoAck.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GoodBye(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/component.video.VideoService/GoodBye',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

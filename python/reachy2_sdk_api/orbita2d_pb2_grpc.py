# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import component_pb2 as component__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import orbita2d_pb2 as orbita2d__pb2


class Orbita2DServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAllOrbita2D = channel.unary_unary(
                '/component.orbita2d.Orbita2DService/GetAllOrbita2D',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=orbita2d__pb2.ListOfOrbita2D.FromString,
                )
        self.GetState = channel.unary_unary(
                '/component.orbita2d.Orbita2DService/GetState',
                request_serializer=orbita2d__pb2.Orbita2DStateRequest.SerializeToString,
                response_deserializer=orbita2d__pb2.Orbita2DState.FromString,
                )
        self.StreamState = channel.unary_stream(
                '/component.orbita2d.Orbita2DService/StreamState',
                request_serializer=orbita2d__pb2.Orbita2DStreamStateRequest.SerializeToString,
                response_deserializer=orbita2d__pb2.Orbita2DState.FromString,
                )
        self.SendCommand = channel.unary_unary(
                '/component.orbita2d.Orbita2DService/SendCommand',
                request_serializer=orbita2d__pb2.Orbita2DsCommand.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.StreamCommand = channel.stream_unary(
                '/component.orbita2d.Orbita2DService/StreamCommand',
                request_serializer=orbita2d__pb2.Orbita2DsCommand.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Audit = channel.unary_unary(
                '/component.orbita2d.Orbita2DService/Audit',
                request_serializer=component__pb2.ComponentId.SerializeToString,
                response_deserializer=orbita2d__pb2.Orbita2DStatus.FromString,
                )
        self.HeartBeat = channel.unary_unary(
                '/component.orbita2d.Orbita2DService/HeartBeat',
                request_serializer=component__pb2.ComponentId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Restart = channel.unary_unary(
                '/component.orbita2d.Orbita2DService/Restart',
                request_serializer=component__pb2.ComponentId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class Orbita2DServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAllOrbita2D(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendCommand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamCommand(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Audit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HeartBeat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Restart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Orbita2DServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAllOrbita2D': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllOrbita2D,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=orbita2d__pb2.ListOfOrbita2D.SerializeToString,
            ),
            'GetState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetState,
                    request_deserializer=orbita2d__pb2.Orbita2DStateRequest.FromString,
                    response_serializer=orbita2d__pb2.Orbita2DState.SerializeToString,
            ),
            'StreamState': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamState,
                    request_deserializer=orbita2d__pb2.Orbita2DStreamStateRequest.FromString,
                    response_serializer=orbita2d__pb2.Orbita2DState.SerializeToString,
            ),
            'SendCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.SendCommand,
                    request_deserializer=orbita2d__pb2.Orbita2DsCommand.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'StreamCommand': grpc.stream_unary_rpc_method_handler(
                    servicer.StreamCommand,
                    request_deserializer=orbita2d__pb2.Orbita2DsCommand.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Audit': grpc.unary_unary_rpc_method_handler(
                    servicer.Audit,
                    request_deserializer=component__pb2.ComponentId.FromString,
                    response_serializer=orbita2d__pb2.Orbita2DStatus.SerializeToString,
            ),
            'HeartBeat': grpc.unary_unary_rpc_method_handler(
                    servicer.HeartBeat,
                    request_deserializer=component__pb2.ComponentId.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Restart': grpc.unary_unary_rpc_method_handler(
                    servicer.Restart,
                    request_deserializer=component__pb2.ComponentId.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'component.orbita2d.Orbita2DService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Orbita2DService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAllOrbita2D(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/component.orbita2d.Orbita2DService/GetAllOrbita2D',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            orbita2d__pb2.ListOfOrbita2D.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/component.orbita2d.Orbita2DService/GetState',
            orbita2d__pb2.Orbita2DStateRequest.SerializeToString,
            orbita2d__pb2.Orbita2DState.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/component.orbita2d.Orbita2DService/StreamState',
            orbita2d__pb2.Orbita2DStreamStateRequest.SerializeToString,
            orbita2d__pb2.Orbita2DState.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/component.orbita2d.Orbita2DService/SendCommand',
            orbita2d__pb2.Orbita2DsCommand.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamCommand(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/component.orbita2d.Orbita2DService/StreamCommand',
            orbita2d__pb2.Orbita2DsCommand.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Audit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/component.orbita2d.Orbita2DService/Audit',
            component__pb2.ComponentId.SerializeToString,
            orbita2d__pb2.Orbita2DStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HeartBeat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/component.orbita2d.Orbita2DService/HeartBeat',
            component__pb2.ComponentId.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Restart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/component.orbita2d.Orbita2DService/Restart',
            component__pb2.ComponentId.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

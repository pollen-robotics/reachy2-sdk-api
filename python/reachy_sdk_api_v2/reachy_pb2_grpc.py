# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import reachy_pb2 as reachy__pb2


class ReachyServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetReachy = channel.unary_unary(
                '/reachy.ReachyService/GetReachy',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=reachy__pb2.Reachy.FromString,
                )
        self.Echo = channel.unary_unary(
                '/reachy.ReachyService/Echo',
                request_serializer=reachy__pb2.SimpleMessage.SerializeToString,
                response_deserializer=reachy__pb2.SimpleMessage.FromString,
                )
        self.GetReachyState = channel.unary_unary(
                '/reachy.ReachyService/GetReachyState',
                request_serializer=reachy__pb2.ReachyId.SerializeToString,
                response_deserializer=reachy__pb2.ReachyState.FromString,
                )
        self.StreamReachyState = channel.unary_stream(
                '/reachy.ReachyService/StreamReachyState',
                request_serializer=reachy__pb2.ReachyStreamStateRequest.SerializeToString,
                response_deserializer=reachy__pb2.ReachyState.FromString,
                )


class ReachyServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetReachy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Echo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetReachyState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamReachyState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReachyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetReachy': grpc.unary_unary_rpc_method_handler(
                    servicer.GetReachy,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=reachy__pb2.Reachy.SerializeToString,
            ),
            'Echo': grpc.unary_unary_rpc_method_handler(
                    servicer.Echo,
                    request_deserializer=reachy__pb2.SimpleMessage.FromString,
                    response_serializer=reachy__pb2.SimpleMessage.SerializeToString,
            ),
            'GetReachyState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetReachyState,
                    request_deserializer=reachy__pb2.ReachyId.FromString,
                    response_serializer=reachy__pb2.ReachyState.SerializeToString,
            ),
            'StreamReachyState': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamReachyState,
                    request_deserializer=reachy__pb2.ReachyStreamStateRequest.FromString,
                    response_serializer=reachy__pb2.ReachyState.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'reachy.ReachyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ReachyService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetReachy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.ReachyService/GetReachy',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            reachy__pb2.Reachy.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Echo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.ReachyService/Echo',
            reachy__pb2.SimpleMessage.SerializeToString,
            reachy__pb2.SimpleMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetReachyState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.ReachyService/GetReachyState',
            reachy__pb2.ReachyId.SerializeToString,
            reachy__pb2.ReachyState.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamReachyState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/reachy.ReachyService/StreamReachyState',
            reachy__pb2.ReachyStreamStateRequest.SerializeToString,
            reachy__pb2.ReachyState.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

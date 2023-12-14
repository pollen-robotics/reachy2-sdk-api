# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import goto_pb2 as goto__pb2


class GoToServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GoToCartesian = channel.unary_unary(
                '/GoToService/GoToCartesian',
                request_serializer=goto__pb2.CartesianGoal.SerializeToString,
                response_deserializer=goto__pb2.GoToId.FromString,
                )
        self.GoToJoints = channel.unary_unary(
                '/GoToService/GoToJoints',
                request_serializer=goto__pb2.JointsGoal.SerializeToString,
                response_deserializer=goto__pb2.GoToId.FromString,
                )
        self.CancelGoTo = channel.unary_unary(
                '/GoToService/CancelGoTo',
                request_serializer=goto__pb2.GoToId.SerializeToString,
                response_deserializer=goto__pb2.GoToAck.FromString,
                )
        self.CancelAllGoTo = channel.unary_unary(
                '/GoToService/CancelAllGoTo',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=goto__pb2.GoToAck.FromString,
                )


class GoToServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GoToCartesian(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GoToJoints(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelGoTo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelAllGoTo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GoToServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GoToCartesian': grpc.unary_unary_rpc_method_handler(
                    servicer.GoToCartesian,
                    request_deserializer=goto__pb2.CartesianGoal.FromString,
                    response_serializer=goto__pb2.GoToId.SerializeToString,
            ),
            'GoToJoints': grpc.unary_unary_rpc_method_handler(
                    servicer.GoToJoints,
                    request_deserializer=goto__pb2.JointsGoal.FromString,
                    response_serializer=goto__pb2.GoToId.SerializeToString,
            ),
            'CancelGoTo': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelGoTo,
                    request_deserializer=goto__pb2.GoToId.FromString,
                    response_serializer=goto__pb2.GoToAck.SerializeToString,
            ),
            'CancelAllGoTo': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelAllGoTo,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=goto__pb2.GoToAck.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'GoToService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GoToService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GoToCartesian(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GoToService/GoToCartesian',
            goto__pb2.CartesianGoal.SerializeToString,
            goto__pb2.GoToId.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GoToJoints(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GoToService/GoToJoints',
            goto__pb2.JointsGoal.SerializeToString,
            goto__pb2.GoToId.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CancelGoTo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GoToService/CancelGoTo',
            goto__pb2.GoToId.SerializeToString,
            goto__pb2.GoToAck.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CancelAllGoTo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GoToService/CancelAllGoTo',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            goto__pb2.GoToAck.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

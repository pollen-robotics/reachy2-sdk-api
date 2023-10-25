# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import component_pb2 as component__pb2
import dynamixel_motor_pb2 as dynamixel__motor__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class DynamixelMotorServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAllDynamixelMotor = channel.unary_unary(
                '/component.dynamixel_motor.DynamixelMotorService/GetAllDynamixelMotor',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=dynamixel__motor__pb2.ListOfDynamixelMotor.FromString,
                )
        self.GetState = channel.unary_unary(
                '/component.dynamixel_motor.DynamixelMotorService/GetState',
                request_serializer=dynamixel__motor__pb2.DynamixelMotorStateRequest.SerializeToString,
                response_deserializer=dynamixel__motor__pb2.DynamixelMotorState.FromString,
                )
        self.StreamState = channel.unary_stream(
                '/component.dynamixel_motor.DynamixelMotorService/StreamState',
                request_serializer=dynamixel__motor__pb2.DynamixelMotorStreamStateRequest.SerializeToString,
                response_deserializer=dynamixel__motor__pb2.DynamixelMotorState.FromString,
                )
        self.SendCommand = channel.unary_unary(
                '/component.dynamixel_motor.DynamixelMotorService/SendCommand',
                request_serializer=dynamixel__motor__pb2.DynamixelMotorsCommand.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.StreamCommand = channel.stream_unary(
                '/component.dynamixel_motor.DynamixelMotorService/StreamCommand',
                request_serializer=dynamixel__motor__pb2.DynamixelMotorsCommand.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.SetPosition = channel.unary_unary(
                '/component.dynamixel_motor.DynamixelMotorService/SetPosition',
                request_serializer=dynamixel__motor__pb2.DynamixelMotorGoal.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Audit = channel.unary_unary(
                '/component.dynamixel_motor.DynamixelMotorService/Audit',
                request_serializer=component__pb2.ComponentId.SerializeToString,
                response_deserializer=dynamixel__motor__pb2.DynamixelMotorStatus.FromString,
                )
        self.HeartBeat = channel.unary_unary(
                '/component.dynamixel_motor.DynamixelMotorService/HeartBeat',
                request_serializer=component__pb2.ComponentId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Restart = channel.unary_unary(
                '/component.dynamixel_motor.DynamixelMotorService/Restart',
                request_serializer=component__pb2.ComponentId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class DynamixelMotorServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAllDynamixelMotor(self, request, context):
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

    def SetPosition(self, request, context):
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


def add_DynamixelMotorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAllDynamixelMotor': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllDynamixelMotor,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=dynamixel__motor__pb2.ListOfDynamixelMotor.SerializeToString,
            ),
            'GetState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetState,
                    request_deserializer=dynamixel__motor__pb2.DynamixelMotorStateRequest.FromString,
                    response_serializer=dynamixel__motor__pb2.DynamixelMotorState.SerializeToString,
            ),
            'StreamState': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamState,
                    request_deserializer=dynamixel__motor__pb2.DynamixelMotorStreamStateRequest.FromString,
                    response_serializer=dynamixel__motor__pb2.DynamixelMotorState.SerializeToString,
            ),
            'SendCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.SendCommand,
                    request_deserializer=dynamixel__motor__pb2.DynamixelMotorsCommand.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'StreamCommand': grpc.stream_unary_rpc_method_handler(
                    servicer.StreamCommand,
                    request_deserializer=dynamixel__motor__pb2.DynamixelMotorsCommand.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SetPosition': grpc.unary_unary_rpc_method_handler(
                    servicer.SetPosition,
                    request_deserializer=dynamixel__motor__pb2.DynamixelMotorGoal.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Audit': grpc.unary_unary_rpc_method_handler(
                    servicer.Audit,
                    request_deserializer=component__pb2.ComponentId.FromString,
                    response_serializer=dynamixel__motor__pb2.DynamixelMotorStatus.SerializeToString,
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
            'component.dynamixel_motor.DynamixelMotorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DynamixelMotorService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAllDynamixelMotor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/component.dynamixel_motor.DynamixelMotorService/GetAllDynamixelMotor',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            dynamixel__motor__pb2.ListOfDynamixelMotor.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/component.dynamixel_motor.DynamixelMotorService/GetState',
            dynamixel__motor__pb2.DynamixelMotorStateRequest.SerializeToString,
            dynamixel__motor__pb2.DynamixelMotorState.FromString,
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
        return grpc.experimental.unary_stream(request, target, '/component.dynamixel_motor.DynamixelMotorService/StreamState',
            dynamixel__motor__pb2.DynamixelMotorStreamStateRequest.SerializeToString,
            dynamixel__motor__pb2.DynamixelMotorState.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/component.dynamixel_motor.DynamixelMotorService/SendCommand',
            dynamixel__motor__pb2.DynamixelMotorsCommand.SerializeToString,
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
        return grpc.experimental.stream_unary(request_iterator, target, '/component.dynamixel_motor.DynamixelMotorService/StreamCommand',
            dynamixel__motor__pb2.DynamixelMotorsCommand.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetPosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/component.dynamixel_motor.DynamixelMotorService/SetPosition',
            dynamixel__motor__pb2.DynamixelMotorGoal.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/component.dynamixel_motor.DynamixelMotorService/Audit',
            component__pb2.ComponentId.SerializeToString,
            dynamixel__motor__pb2.DynamixelMotorStatus.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/component.dynamixel_motor.DynamixelMotorService/HeartBeat',
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
        return grpc.experimental.unary_unary(request, target, '/component.dynamixel_motor.DynamixelMotorService/Restart',
            component__pb2.ComponentId.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

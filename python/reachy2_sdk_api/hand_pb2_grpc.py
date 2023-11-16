# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import hand_pb2 as hand__pb2
import part_pb2 as part__pb2


class HandServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAllHands = channel.unary_unary(
                '/reachy.part.hand.HandService/GetAllHands',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=hand__pb2.ListOfHand.FromString,
                )
        self.GetHandState = channel.unary_unary(
                '/reachy.part.hand.HandService/GetHandState',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=hand__pb2.HandState.FromString,
                )
        self.OpenHand = channel.unary_unary(
                '/reachy.part.hand.HandService/OpenHand',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.CloseHand = channel.unary_unary(
                '/reachy.part.hand.HandService/CloseHand',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Audit = channel.unary_unary(
                '/reachy.part.hand.HandService/Audit',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=hand__pb2.HandStatus.FromString,
                )
        self.HeartBeat = channel.unary_unary(
                '/reachy.part.hand.HandService/HeartBeat',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Restart = channel.unary_unary(
                '/reachy.part.hand.HandService/Restart',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ResetDefaultValues = channel.unary_unary(
                '/reachy.part.hand.HandService/ResetDefaultValues',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.TurnOn = channel.unary_unary(
                '/reachy.part.hand.HandService/TurnOn',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.TurnOff = channel.unary_unary(
                '/reachy.part.hand.HandService/TurnOff',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetJointLimit = channel.unary_unary(
                '/reachy.part.hand.HandService/GetJointLimit',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=hand__pb2.JointsLimits.FromString,
                )
        self.GetTemperature = channel.unary_unary(
                '/reachy.part.hand.HandService/GetTemperature',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=hand__pb2.HandTemperatures.FromString,
                )
        self.GetHandGoalPosition = channel.unary_unary(
                '/reachy.part.hand.HandService/GetHandGoalPosition',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=hand__pb2.HandPosition.FromString,
                )
        self.SetSpeedLimit = channel.unary_unary(
                '/reachy.part.hand.HandService/SetSpeedLimit',
                request_serializer=hand__pb2.SpeedLimitRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.SetHandPosition = channel.unary_unary(
                '/reachy.part.hand.HandService/SetHandPosition',
                request_serializer=hand__pb2.HandPosition.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetForce = channel.unary_unary(
                '/reachy.part.hand.HandService/GetForce',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=hand__pb2.Force.FromString,
                )


class HandServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAllHands(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetHandState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OpenHand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseHand(self, request, context):
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

    def ResetDefaultValues(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TurnOn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TurnOff(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetJointLimit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTemperature(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetHandGoalPosition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetSpeedLimit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetHandPosition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetForce(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HandServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAllHands': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllHands,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=hand__pb2.ListOfHand.SerializeToString,
            ),
            'GetHandState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHandState,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=hand__pb2.HandState.SerializeToString,
            ),
            'OpenHand': grpc.unary_unary_rpc_method_handler(
                    servicer.OpenHand,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'CloseHand': grpc.unary_unary_rpc_method_handler(
                    servicer.CloseHand,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Audit': grpc.unary_unary_rpc_method_handler(
                    servicer.Audit,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=hand__pb2.HandStatus.SerializeToString,
            ),
            'HeartBeat': grpc.unary_unary_rpc_method_handler(
                    servicer.HeartBeat,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Restart': grpc.unary_unary_rpc_method_handler(
                    servicer.Restart,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ResetDefaultValues': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetDefaultValues,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'TurnOn': grpc.unary_unary_rpc_method_handler(
                    servicer.TurnOn,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'TurnOff': grpc.unary_unary_rpc_method_handler(
                    servicer.TurnOff,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetJointLimit': grpc.unary_unary_rpc_method_handler(
                    servicer.GetJointLimit,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=hand__pb2.JointsLimits.SerializeToString,
            ),
            'GetTemperature': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTemperature,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=hand__pb2.HandTemperatures.SerializeToString,
            ),
            'GetHandGoalPosition': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHandGoalPosition,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=hand__pb2.HandPosition.SerializeToString,
            ),
            'SetSpeedLimit': grpc.unary_unary_rpc_method_handler(
                    servicer.SetSpeedLimit,
                    request_deserializer=hand__pb2.SpeedLimitRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SetHandPosition': grpc.unary_unary_rpc_method_handler(
                    servicer.SetHandPosition,
                    request_deserializer=hand__pb2.HandPosition.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetForce': grpc.unary_unary_rpc_method_handler(
                    servicer.GetForce,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=hand__pb2.Force.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'reachy.part.hand.HandService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HandService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAllHands(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.hand.HandService/GetAllHands',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            hand__pb2.ListOfHand.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetHandState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.hand.HandService/GetHandState',
            part__pb2.PartId.SerializeToString,
            hand__pb2.HandState.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OpenHand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.hand.HandService/OpenHand',
            part__pb2.PartId.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CloseHand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.hand.HandService/CloseHand',
            part__pb2.PartId.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/reachy.part.hand.HandService/Audit',
            part__pb2.PartId.SerializeToString,
            hand__pb2.HandStatus.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/reachy.part.hand.HandService/HeartBeat',
            part__pb2.PartId.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/reachy.part.hand.HandService/Restart',
            part__pb2.PartId.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResetDefaultValues(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.hand.HandService/ResetDefaultValues',
            part__pb2.PartId.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TurnOn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.hand.HandService/TurnOn',
            part__pb2.PartId.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TurnOff(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.hand.HandService/TurnOff',
            part__pb2.PartId.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetJointLimit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.hand.HandService/GetJointLimit',
            part__pb2.PartId.SerializeToString,
            hand__pb2.JointsLimits.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTemperature(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.hand.HandService/GetTemperature',
            part__pb2.PartId.SerializeToString,
            hand__pb2.HandTemperatures.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetHandGoalPosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.hand.HandService/GetHandGoalPosition',
            part__pb2.PartId.SerializeToString,
            hand__pb2.HandPosition.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetSpeedLimit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.hand.HandService/SetSpeedLimit',
            hand__pb2.SpeedLimitRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetHandPosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.hand.HandService/SetHandPosition',
            hand__pb2.HandPosition.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetForce(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.hand.HandService/GetForce',
            part__pb2.PartId.SerializeToString,
            hand__pb2.Force.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import head_pb2 as head__pb2
import kinematics_pb2 as kinematics__pb2
import part_pb2 as part__pb2


class HeadServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAllHeads = channel.unary_unary(
                '/reachy.part.head.HeadService/GetAllHeads',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=head__pb2.ListOfHead.FromString,
                )
        self.ComputeNeckFK = channel.unary_unary(
                '/reachy.part.head.HeadService/ComputeNeckFK',
                request_serializer=head__pb2.NeckFKRequest.SerializeToString,
                response_deserializer=head__pb2.NeckFKSolution.FromString,
                )
        self.ComputeNeckIK = channel.unary_unary(
                '/reachy.part.head.HeadService/ComputeNeckIK',
                request_serializer=head__pb2.NeckIKRequest.SerializeToString,
                response_deserializer=head__pb2.NeckIKSolution.FromString,
                )
        self.GoToOrientation = channel.unary_unary(
                '/reachy.part.head.HeadService/GoToOrientation',
                request_serializer=head__pb2.NeckGoal.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetOrientation = channel.unary_unary(
                '/reachy.part.head.HeadService/GetOrientation',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=kinematics__pb2.Quaternion.FromString,
                )
        self.LookAt = channel.unary_unary(
                '/reachy.part.head.HeadService/LookAt',
                request_serializer=head__pb2.HeadTargetPoint.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Audit = channel.unary_unary(
                '/reachy.part.head.HeadService/Audit',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=head__pb2.HeadStatus.FromString,
                )
        self.HeartBeat = channel.unary_unary(
                '/reachy.part.head.HeadService/HeartBeat',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Restart = channel.unary_unary(
                '/reachy.part.head.HeadService/Restart',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ResetDefaultValues = channel.unary_unary(
                '/reachy.part.head.HeadService/ResetDefaultValues',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.TurnOn = channel.unary_unary(
                '/reachy.part.head.HeadService/TurnOn',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.TurnOff = channel.unary_unary(
                '/reachy.part.head.HeadService/TurnOff',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetJointsLimits = channel.unary_unary(
                '/reachy.part.head.HeadService/GetJointsLimits',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=head__pb2.JointsLimits.FromString,
                )
        self.GetTemperatures = channel.unary_unary(
                '/reachy.part.head.HeadService/GetTemperatures',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=head__pb2.HeadTemperatures.FromString,
                )
        self.GetJointGoalPosition = channel.unary_unary(
                '/reachy.part.head.HeadService/GetJointGoalPosition',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=head__pb2.NeckPosition.FromString,
                )
        self.SetSpeedLimit = channel.unary_unary(
                '/reachy.part.head.HeadService/SetSpeedLimit',
                request_serializer=head__pb2.SpeedLimitRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class HeadServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAllHeads(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ComputeNeckFK(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ComputeNeckIK(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GoToOrientation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrientation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LookAt(self, request, context):
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

    def GetJointsLimits(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTemperatures(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetJointGoalPosition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetSpeedLimit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HeadServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAllHeads': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllHeads,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=head__pb2.ListOfHead.SerializeToString,
            ),
            'ComputeNeckFK': grpc.unary_unary_rpc_method_handler(
                    servicer.ComputeNeckFK,
                    request_deserializer=head__pb2.NeckFKRequest.FromString,
                    response_serializer=head__pb2.NeckFKSolution.SerializeToString,
            ),
            'ComputeNeckIK': grpc.unary_unary_rpc_method_handler(
                    servicer.ComputeNeckIK,
                    request_deserializer=head__pb2.NeckIKRequest.FromString,
                    response_serializer=head__pb2.NeckIKSolution.SerializeToString,
            ),
            'GoToOrientation': grpc.unary_unary_rpc_method_handler(
                    servicer.GoToOrientation,
                    request_deserializer=head__pb2.NeckGoal.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetOrientation': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrientation,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=kinematics__pb2.Quaternion.SerializeToString,
            ),
            'LookAt': grpc.unary_unary_rpc_method_handler(
                    servicer.LookAt,
                    request_deserializer=head__pb2.HeadTargetPoint.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Audit': grpc.unary_unary_rpc_method_handler(
                    servicer.Audit,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=head__pb2.HeadStatus.SerializeToString,
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
            'GetJointsLimits': grpc.unary_unary_rpc_method_handler(
                    servicer.GetJointsLimits,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=head__pb2.JointsLimits.SerializeToString,
            ),
            'GetTemperatures': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTemperatures,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=head__pb2.HeadTemperatures.SerializeToString,
            ),
            'GetJointGoalPosition': grpc.unary_unary_rpc_method_handler(
                    servicer.GetJointGoalPosition,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=head__pb2.NeckPosition.SerializeToString,
            ),
            'SetSpeedLimit': grpc.unary_unary_rpc_method_handler(
                    servicer.SetSpeedLimit,
                    request_deserializer=head__pb2.SpeedLimitRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'reachy.part.head.HeadService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HeadService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAllHeads(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.head.HeadService/GetAllHeads',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            head__pb2.ListOfHead.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ComputeNeckFK(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.head.HeadService/ComputeNeckFK',
            head__pb2.NeckFKRequest.SerializeToString,
            head__pb2.NeckFKSolution.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ComputeNeckIK(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.head.HeadService/ComputeNeckIK',
            head__pb2.NeckIKRequest.SerializeToString,
            head__pb2.NeckIKSolution.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GoToOrientation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.head.HeadService/GoToOrientation',
            head__pb2.NeckGoal.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrientation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.head.HeadService/GetOrientation',
            part__pb2.PartId.SerializeToString,
            kinematics__pb2.Quaternion.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LookAt(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.head.HeadService/LookAt',
            head__pb2.HeadTargetPoint.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/reachy.part.head.HeadService/Audit',
            part__pb2.PartId.SerializeToString,
            head__pb2.HeadStatus.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/reachy.part.head.HeadService/HeartBeat',
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
        return grpc.experimental.unary_unary(request, target, '/reachy.part.head.HeadService/Restart',
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
        return grpc.experimental.unary_unary(request, target, '/reachy.part.head.HeadService/ResetDefaultValues',
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
        return grpc.experimental.unary_unary(request, target, '/reachy.part.head.HeadService/TurnOn',
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
        return grpc.experimental.unary_unary(request, target, '/reachy.part.head.HeadService/TurnOff',
            part__pb2.PartId.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetJointsLimits(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.head.HeadService/GetJointsLimits',
            part__pb2.PartId.SerializeToString,
            head__pb2.JointsLimits.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTemperatures(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.head.HeadService/GetTemperatures',
            part__pb2.PartId.SerializeToString,
            head__pb2.HeadTemperatures.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetJointGoalPosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.head.HeadService/GetJointGoalPosition',
            part__pb2.PartId.SerializeToString,
            head__pb2.NeckPosition.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/reachy.part.head.HeadService/SetSpeedLimit',
            head__pb2.SpeedLimitRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

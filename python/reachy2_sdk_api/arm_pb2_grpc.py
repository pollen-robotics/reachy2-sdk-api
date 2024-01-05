# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import arm_pb2 as arm__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import kinematics_pb2 as kinematics__pb2
import part_pb2 as part__pb2


class ArmServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAllArms = channel.unary_unary(
                '/reachy.part.arm.ArmService/GetAllArms',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=arm__pb2.ListOfArm.FromString,
                )
        self.GetState = channel.unary_unary(
                '/reachy.part.arm.ArmService/GetState',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=arm__pb2.ArmState.FromString,
                )
        self.ComputeArmFK = channel.unary_unary(
                '/reachy.part.arm.ArmService/ComputeArmFK',
                request_serializer=arm__pb2.ArmFKRequest.SerializeToString,
                response_deserializer=arm__pb2.ArmFKSolution.FromString,
                )
        self.ComputeArmIK = channel.unary_unary(
                '/reachy.part.arm.ArmService/ComputeArmIK',
                request_serializer=arm__pb2.ArmIKRequest.SerializeToString,
                response_deserializer=arm__pb2.ArmIKSolution.FromString,
                )
        self.GetCartesianPosition = channel.unary_unary(
                '/reachy.part.arm.ArmService/GetCartesianPosition',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=kinematics__pb2.Matrix4x4.FromString,
                )
        self.GetJointPosition = channel.unary_unary(
                '/reachy.part.arm.ArmService/GetJointPosition',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=arm__pb2.ArmPosition.FromString,
                )
        self.Audit = channel.unary_unary(
                '/reachy.part.arm.ArmService/Audit',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=arm__pb2.ArmStatus.FromString,
                )
        self.HeartBeat = channel.unary_unary(
                '/reachy.part.arm.ArmService/HeartBeat',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Restart = channel.unary_unary(
                '/reachy.part.arm.ArmService/Restart',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ResetDefaultValues = channel.unary_unary(
                '/reachy.part.arm.ArmService/ResetDefaultValues',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.TurnOn = channel.unary_unary(
                '/reachy.part.arm.ArmService/TurnOn',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.TurnOff = channel.unary_unary(
                '/reachy.part.arm.ArmService/TurnOff',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetJointsLimits = channel.unary_unary(
                '/reachy.part.arm.ArmService/GetJointsLimits',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=arm__pb2.ArmLimits.FromString,
                )
        self.GetTemperatures = channel.unary_unary(
                '/reachy.part.arm.ArmService/GetTemperatures',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=arm__pb2.ArmTemperatures.FromString,
                )
        self.GetJointGoalPosition = channel.unary_unary(
                '/reachy.part.arm.ArmService/GetJointGoalPosition',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=arm__pb2.ArmPosition.FromString,
                )
        self.SetSpeedLimit = channel.unary_unary(
                '/reachy.part.arm.ArmService/SetSpeedLimit',
                request_serializer=arm__pb2.SpeedLimitRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.SendArmCartesianGoal = channel.unary_unary(
                '/reachy.part.arm.ArmService/SendArmCartesianGoal',
                request_serializer=arm__pb2.ArmCartesianGoal.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class ArmServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAllArms(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ComputeArmFK(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ComputeArmIK(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCartesianPosition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetJointPosition(self, request, context):
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

    def SendArmCartesianGoal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ArmServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAllArms': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllArms,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=arm__pb2.ListOfArm.SerializeToString,
            ),
            'GetState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetState,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=arm__pb2.ArmState.SerializeToString,
            ),
            'ComputeArmFK': grpc.unary_unary_rpc_method_handler(
                    servicer.ComputeArmFK,
                    request_deserializer=arm__pb2.ArmFKRequest.FromString,
                    response_serializer=arm__pb2.ArmFKSolution.SerializeToString,
            ),
            'ComputeArmIK': grpc.unary_unary_rpc_method_handler(
                    servicer.ComputeArmIK,
                    request_deserializer=arm__pb2.ArmIKRequest.FromString,
                    response_serializer=arm__pb2.ArmIKSolution.SerializeToString,
            ),
            'GetCartesianPosition': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCartesianPosition,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=kinematics__pb2.Matrix4x4.SerializeToString,
            ),
            'GetJointPosition': grpc.unary_unary_rpc_method_handler(
                    servicer.GetJointPosition,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=arm__pb2.ArmPosition.SerializeToString,
            ),
            'Audit': grpc.unary_unary_rpc_method_handler(
                    servicer.Audit,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=arm__pb2.ArmStatus.SerializeToString,
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
                    response_serializer=arm__pb2.ArmLimits.SerializeToString,
            ),
            'GetTemperatures': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTemperatures,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=arm__pb2.ArmTemperatures.SerializeToString,
            ),
            'GetJointGoalPosition': grpc.unary_unary_rpc_method_handler(
                    servicer.GetJointGoalPosition,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=arm__pb2.ArmPosition.SerializeToString,
            ),
            'SetSpeedLimit': grpc.unary_unary_rpc_method_handler(
                    servicer.SetSpeedLimit,
                    request_deserializer=arm__pb2.SpeedLimitRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SendArmCartesianGoal': grpc.unary_unary_rpc_method_handler(
                    servicer.SendArmCartesianGoal,
                    request_deserializer=arm__pb2.ArmCartesianGoal.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'reachy.part.arm.ArmService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ArmService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAllArms(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.arm.ArmService/GetAllArms',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            arm__pb2.ListOfArm.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/reachy.part.arm.ArmService/GetState',
            part__pb2.PartId.SerializeToString,
            arm__pb2.ArmState.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ComputeArmFK(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.arm.ArmService/ComputeArmFK',
            arm__pb2.ArmFKRequest.SerializeToString,
            arm__pb2.ArmFKSolution.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ComputeArmIK(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.arm.ArmService/ComputeArmIK',
            arm__pb2.ArmIKRequest.SerializeToString,
            arm__pb2.ArmIKSolution.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCartesianPosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.arm.ArmService/GetCartesianPosition',
            part__pb2.PartId.SerializeToString,
            kinematics__pb2.Matrix4x4.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetJointPosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.arm.ArmService/GetJointPosition',
            part__pb2.PartId.SerializeToString,
            arm__pb2.ArmPosition.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/reachy.part.arm.ArmService/Audit',
            part__pb2.PartId.SerializeToString,
            arm__pb2.ArmStatus.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/reachy.part.arm.ArmService/HeartBeat',
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
        return grpc.experimental.unary_unary(request, target, '/reachy.part.arm.ArmService/Restart',
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
        return grpc.experimental.unary_unary(request, target, '/reachy.part.arm.ArmService/ResetDefaultValues',
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
        return grpc.experimental.unary_unary(request, target, '/reachy.part.arm.ArmService/TurnOn',
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
        return grpc.experimental.unary_unary(request, target, '/reachy.part.arm.ArmService/TurnOff',
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
        return grpc.experimental.unary_unary(request, target, '/reachy.part.arm.ArmService/GetJointsLimits',
            part__pb2.PartId.SerializeToString,
            arm__pb2.ArmLimits.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/reachy.part.arm.ArmService/GetTemperatures',
            part__pb2.PartId.SerializeToString,
            arm__pb2.ArmTemperatures.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/reachy.part.arm.ArmService/GetJointGoalPosition',
            part__pb2.PartId.SerializeToString,
            arm__pb2.ArmPosition.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/reachy.part.arm.ArmService/SetSpeedLimit',
            arm__pb2.SpeedLimitRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendArmCartesianGoal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.arm.ArmService/SendArmCartesianGoal',
            arm__pb2.ArmCartesianGoal.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

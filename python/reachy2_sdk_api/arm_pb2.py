# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arm.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import part_pb2 as part__pb2
import kinematics_pb2 as kinematics__pb2
import error_pb2 as error__pb2
import orbita2d_pb2 as orbita2d__pb2
import orbita3d_pb2 as orbita3d__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tarm.proto\x12\x0freachy.part.arm\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\npart.proto\x1a\x10kinematics.proto\x1a\x0b\x65rror.proto\x1a\x0eorbita2d.proto\x1a\x0eorbita3d.proto\"\xd3\x02\n\x08\x41rmState\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1f\n\x02id\x18\x02 \x01(\x0b\x32\x13.reachy.part.PartId\x12\x11\n\tactivated\x18\x03 \x01(\x08\x12\x39\n\x0eshoulder_state\x18\x04 \x01(\x0b\x32!.component.orbita2d.Orbita2dState\x12\x36\n\x0b\x65lbow_state\x18\x05 \x01(\x0b\x32!.component.orbita2d.Orbita2dState\x12\x36\n\x0bwrist_state\x18\x06 \x01(\x0b\x32!.component.orbita3d.Orbita3dState\x12\x39\n\x0creachability\x18\n \x03(\x0b\x32#.reachy.part.arm.ReachabilityAnswer\"\xae\x01\n\x12ReachabilityAnswer\x12-\n\x08order_id\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x30\n\x0cis_reachable\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x37\n\x0b\x64\x65scription\x18\x03 \x01(\x0e\x32\".reachy.part.arm.ReachabilityError\"\x9a\x01\n\x0e\x41rmDescription\x12.\n\x08shoulder\x18\x01 \x01(\x0b\x32\x1c.component.orbita2d.Orbita2d\x12+\n\x05\x65lbow\x18\x02 \x01(\x0b\x32\x1c.component.orbita2d.Orbita2d\x12+\n\x05wrist\x18\x03 \x01(\x0b\x32\x1c.component.orbita3d.Orbita3d\"\x86\x01\n\x03\x41rm\x12$\n\x07part_id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12\x34\n\x0b\x64\x65scription\x18\x02 \x01(\x0b\x32\x1f.reachy.part.arm.ArmDescription\x12#\n\x04info\x18\x05 \x01(\x0b\x32\x15.reachy.part.PartInfo\".\n\tListOfArm\x12!\n\x03\x61rm\x18\x01 \x03(\x0b\x32\x14.reachy.part.arm.Arm\"\xaf\x01\n\x0b\x41rmPosition\x12\x35\n\x11shoulder_position\x18\x01 \x01(\x0b\x32\x1a.component.orbita2d.Pose2d\x12\x32\n\x0e\x65lbow_position\x18\x02 \x01(\x0b\x32\x1a.component.orbita2d.Pose2d\x12\x35\n\x0ewrist_position\x18\x03 \x01(\x0b\x32\x1d.reachy.kinematics.Rotation3d\"\xe2\x04\n\x10\x41rmCartesianGoal\x12\x1f\n\x02id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12/\n\tgoal_pose\x18\x02 \x01(\x0b\x32\x1c.reachy.kinematics.Matrix4x4\x12\x46\n\x12position_tolerance\x18\x03 \x01(\x0b\x32*.reachy.kinematics.PointDistanceTolerances\x12J\n\x15orientation_tolerance\x18\x04 \x01(\x0b\x32+.reachy.kinematics.ExtEulerAnglesTolerances\x12(\n\x02q0\x18\x05 \x01(\x0b\x32\x1c.reachy.part.arm.ArmPosition\x12<\n\x10\x63onstrained_mode\x18\x06 \x01(\x0e\x32\".reachy.part.arm.IKConstrainedMode\x12\x34\n\x0fpreferred_theta\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x30\n\x0b\x64_theta_max\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12:\n\x0f\x63ontinuous_mode\x18\t \x01(\x0e\x32!.reachy.part.arm.IKContinuousMode\x12-\n\x08\x64uration\x18\n \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12-\n\x08order_id\x18\x0f \x01(\x0b\x32\x1b.google.protobuf.Int32Value\"\x91\x01\n\x0c\x41rmJointGoal\x12\x1f\n\x02id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12\x31\n\x0bjoints_goal\x18\x02 \x01(\x0b\x32\x1c.reachy.part.arm.ArmPosition\x12-\n\x08\x64uration\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"<\n\x0e\x41rmEndEffector\x12*\n\x04pose\x18\x01 \x01(\x0b\x32\x1c.reachy.kinematics.Matrix4x4\"_\n\x0c\x41rmFKRequest\x12\x1f\n\x02id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12.\n\x08position\x18\x02 \x01(\x0b\x32\x1c.reachy.part.arm.ArmPosition\"W\n\rArmFKSolution\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x35\n\x0c\x65nd_effector\x18\x02 \x01(\x0b\x32\x1f.reachy.part.arm.ArmEndEffector\"\x8a\x01\n\x0c\x41rmIKRequest\x12\x1f\n\x02id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12/\n\x06target\x18\x02 \x01(\x0b\x32\x1f.reachy.part.arm.ArmEndEffector\x12(\n\x02q0\x18\x03 \x01(\x0b\x32\x1c.reachy.part.arm.ArmPosition\"q\n\rArmIKSolution\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x32\n\x0c\x61rm_position\x18\x02 \x01(\x0b\x32\x1c.reachy.part.arm.ArmPosition\x12\x1b\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x0c.error.Error\"\xbc\x01\n\tArmStatus\x12;\n\x0fshoulder_status\x18\x01 \x01(\x0b\x32\".component.orbita2d.Orbita2dStatus\x12\x38\n\x0c\x65lbow_status\x18\x02 \x01(\x0b\x32\".component.orbita2d.Orbita2dStatus\x12\x38\n\x0cwrist_status\x18\x03 \x01(\x0b\x32\".component.orbita3d.Orbita3dStatus\"C\n\x11SpeedLimitRequest\x12\x1f\n\x02id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12\r\n\x05limit\x18\x02 \x01(\r\"D\n\x12TorqueLimitRequest\x12\x1f\n\x02id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12\r\n\x05limit\x18\x02 \x01(\r\"\xaa\x01\n\tArmLimits\x12\x35\n\x0fshoulder_limits\x18\x01 \x01(\x0b\x32\x1c.component.orbita2d.Limits2d\x12\x32\n\x0c\x65lbow_limits\x18\x02 \x01(\x0b\x32\x1c.component.orbita2d.Limits2d\x12\x32\n\x0cwrist_limits\x18\x03 \x01(\x0b\x32\x1c.component.orbita3d.Limits3d\"\xbc\x01\n\x0f\x41rmTemperatures\x12\x39\n\x14shoulder_temperature\x18\x01 \x01(\x0b\x32\x1b.component.orbita2d.Float2d\x12\x36\n\x11\x65lbow_temperature\x18\x02 \x01(\x0b\x32\x1b.component.orbita2d.Float2d\x12\x36\n\x11wrist_temperature\x18\x03 \x01(\x0b\x32\x1b.component.orbita3d.Float3d*\xdb\x01\n\x08\x41rmField\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04NAME\x10\x01\x12\x06\n\x02ID\x10\x02\x12\x14\n\x10PRESENT_POSITION\x10\x03\x12\x11\n\rPRESENT_SPEED\x10\x04\x12\x10\n\x0cPRESENT_LOAD\x10\x05\x12\x0f\n\x0bTEMPERATURE\x10\x06\x12\x10\n\x0cJOINT_LIMITS\x10\x07\x12\r\n\tCOMPLIANT\x10\x08\x12\x11\n\rGOAL_POSITION\x10\t\x12\x0f\n\x0bSPEED_LIMIT\x10\n\x12\x10\n\x0cTORQUE_LIMIT\x10\x0b\x12\x07\n\x03PID\x10\x0c\x12\x07\n\x03\x41LL\x10\x0f*U\n\x11IKConstrainedMode\x12\x1e\n\x1aUNDEFINED_CONSTRAINED_MODE\x10\x00\x12\x11\n\rUNCONSTRAINED\x10\x01\x12\r\n\tLOW_ELBOW\x10\x02*O\n\x10IKContinuousMode\x12\x1d\n\x19UNDEFINED_CONTINUOUS_MODE\x10\x00\x12\x0e\n\nCONTINUOUS\x10\x01\x12\x0c\n\x08\x44ISCRETE\x10\x02*\x8c\x01\n\x11ReachabilityError\x12\x0c\n\x08NO_ERROR\x10\x00\x12\x12\n\x0e\x44ISTANCE_LIMIT\x10\x01\x12\x12\n\x0eSHOULDER_LIMIT\x10\x02\x12\x0f\n\x0b\x45LBOW_LIMIT\x10\x03\x12\x0f\n\x0bWRIST_LIMIT\x10\x04\x12\x14\n\x10\x43ONTINUITY_LIMIT\x10\x05\x12\t\n\x05OTHER\x10\x06\x32\xe0\t\n\nArmService\x12@\n\nGetAllArms\x12\x16.google.protobuf.Empty\x1a\x1a.reachy.part.arm.ListOfArm\x12:\n\x08GetState\x12\x13.reachy.part.PartId\x1a\x19.reachy.part.arm.ArmState\x12M\n\x0c\x43omputeArmFK\x12\x1d.reachy.part.arm.ArmFKRequest\x1a\x1e.reachy.part.arm.ArmFKSolution\x12M\n\x0c\x43omputeArmIK\x12\x1d.reachy.part.arm.ArmIKRequest\x1a\x1e.reachy.part.arm.ArmIKSolution\x12I\n\x14GetCartesianPosition\x12\x13.reachy.part.PartId\x1a\x1c.reachy.kinematics.Matrix4x4\x12\x45\n\x10GetJointPosition\x12\x13.reachy.part.PartId\x1a\x1c.reachy.part.arm.ArmPosition\x12\x38\n\x05\x41udit\x12\x13.reachy.part.PartId\x1a\x1a.reachy.part.arm.ArmStatus\x12\x38\n\tHeartBeat\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x36\n\x07Restart\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x41\n\x12ResetDefaultValues\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x35\n\x06TurnOn\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x36\n\x07TurnOff\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x42\n\x0fGetJointsLimits\x12\x13.reachy.part.PartId\x1a\x1a.reachy.part.arm.ArmLimits\x12H\n\x0fGetTemperatures\x12\x13.reachy.part.PartId\x1a .reachy.part.arm.ArmTemperatures\x12I\n\x14GetJointGoalPosition\x12\x13.reachy.part.PartId\x1a\x1c.reachy.part.arm.ArmPosition\x12K\n\rSetSpeedLimit\x12\".reachy.part.arm.SpeedLimitRequest\x1a\x16.google.protobuf.Empty\x12M\n\x0eSetTorqueLimit\x12#.reachy.part.arm.TorqueLimitRequest\x1a\x16.google.protobuf.Empty\x12Q\n\x14SendArmCartesianGoal\x12!.reachy.part.arm.ArmCartesianGoal\x1a\x16.google.protobuf.Emptyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'arm_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ARMFIELD']._serialized_start=3198
  _globals['_ARMFIELD']._serialized_end=3417
  _globals['_IKCONSTRAINEDMODE']._serialized_start=3419
  _globals['_IKCONSTRAINEDMODE']._serialized_end=3504
  _globals['_IKCONTINUOUSMODE']._serialized_start=3506
  _globals['_IKCONTINUOUSMODE']._serialized_end=3585
  _globals['_REACHABILITYERROR']._serialized_start=3588
  _globals['_REACHABILITYERROR']._serialized_end=3728
  _globals['_ARMSTATE']._serialized_start=200
  _globals['_ARMSTATE']._serialized_end=539
  _globals['_REACHABILITYANSWER']._serialized_start=542
  _globals['_REACHABILITYANSWER']._serialized_end=716
  _globals['_ARMDESCRIPTION']._serialized_start=719
  _globals['_ARMDESCRIPTION']._serialized_end=873
  _globals['_ARM']._serialized_start=876
  _globals['_ARM']._serialized_end=1010
  _globals['_LISTOFARM']._serialized_start=1012
  _globals['_LISTOFARM']._serialized_end=1058
  _globals['_ARMPOSITION']._serialized_start=1061
  _globals['_ARMPOSITION']._serialized_end=1236
  _globals['_ARMCARTESIANGOAL']._serialized_start=1239
  _globals['_ARMCARTESIANGOAL']._serialized_end=1849
  _globals['_ARMJOINTGOAL']._serialized_start=1852
  _globals['_ARMJOINTGOAL']._serialized_end=1997
  _globals['_ARMENDEFFECTOR']._serialized_start=1999
  _globals['_ARMENDEFFECTOR']._serialized_end=2059
  _globals['_ARMFKREQUEST']._serialized_start=2061
  _globals['_ARMFKREQUEST']._serialized_end=2156
  _globals['_ARMFKSOLUTION']._serialized_start=2158
  _globals['_ARMFKSOLUTION']._serialized_end=2245
  _globals['_ARMIKREQUEST']._serialized_start=2248
  _globals['_ARMIKREQUEST']._serialized_end=2386
  _globals['_ARMIKSOLUTION']._serialized_start=2388
  _globals['_ARMIKSOLUTION']._serialized_end=2501
  _globals['_ARMSTATUS']._serialized_start=2504
  _globals['_ARMSTATUS']._serialized_end=2692
  _globals['_SPEEDLIMITREQUEST']._serialized_start=2694
  _globals['_SPEEDLIMITREQUEST']._serialized_end=2761
  _globals['_TORQUELIMITREQUEST']._serialized_start=2763
  _globals['_TORQUELIMITREQUEST']._serialized_end=2831
  _globals['_ARMLIMITS']._serialized_start=2834
  _globals['_ARMLIMITS']._serialized_end=3004
  _globals['_ARMTEMPERATURES']._serialized_start=3007
  _globals['_ARMTEMPERATURES']._serialized_end=3195
  _globals['_ARMSERVICE']._serialized_start=3731
  _globals['_ARMSERVICE']._serialized_end=4979
# @@protoc_insertion_point(module_scope)

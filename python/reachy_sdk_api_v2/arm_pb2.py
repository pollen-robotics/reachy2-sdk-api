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
import part_pb2 as part__pb2
import kinematics_pb2 as kinematics__pb2
import error_pb2 as error__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tarm.proto\x12\x0freachy.part.arm\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\npart.proto\x1a\x10kinematics.proto\x1a\x0b\x65rror.proto\"\n\n\x08\x41rmState\"P\n\x03\x41rm\x12$\n\x07part_id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12#\n\x04info\x18\x05 \x01(\x0b\x32\x15.reachy.part.PartInfo\".\n\tListOfArm\x12!\n\x03\x61rm\x18\x01 \x03(\x0b\x32\x14.reachy.part.arm.Arm\"\xa0\x01\n\x0b\x41rmPosition\x12\x16\n\x0eshoulder_pitch\x18\x01 \x01(\x02\x12\x15\n\rshoulder_roll\x18\x02 \x01(\x02\x12\x11\n\telbow_yaw\x18\x03 \x01(\x02\x12\x13\n\x0b\x65lbow_pitch\x18\x04 \x01(\x02\x12\x12\n\nwrist_roll\x18\x05 \x01(\x02\x12\x13\n\x0bwrist_pitch\x18\x06 \x01(\x02\x12\x11\n\twrist_yaw\x18\x07 \x01(\x02\"\x92\x01\n\x10\x41rmCartesianGoal\x12\x1f\n\x02id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12.\n\x08position\x18\x02 \x01(\x0b\x32\x1c.reachy.kinematics.Matrix4x4\x12-\n\x08\x64uration\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"\x8e\x01\n\x0c\x41rmJointGoal\x12\x1f\n\x02id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12.\n\x08position\x18\x02 \x01(\x0b\x32\x1c.reachy.part.arm.ArmPosition\x12-\n\x08\x64uration\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"<\n\x0e\x41rmEndEffector\x12*\n\x04pose\x18\x01 \x01(\x0b\x32\x1c.reachy.kinematics.Matrix4x4\"W\n\rArmFKSolution\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x35\n\x0c\x65nd_effector\x18\x02 \x01(\x0b\x32\x1f.reachy.part.arm.ArmEndEffector\"i\n\x0c\x41rmIKRequest\x12/\n\x06target\x18\x01 \x01(\x0b\x32\x1f.reachy.part.arm.ArmEndEffector\x12(\n\x02q0\x18\x02 \x01(\x0b\x32\x1c.reachy.part.arm.ArmPosition\"q\n\rArmIKSolution\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x32\n\x0c\x61rm_position\x18\x02 \x01(\x0b\x32\x1c.reachy.part.arm.ArmPosition\x12\x1b\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x0c.error.Error\"\x0b\n\tArmStatus\"`\n\x11SpeedLimitRequest\x12\x1f\n\x02id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12*\n\x05limit\x18\x02 \x01(\x0e\x32\x1b.reachy.part.arm.SpeedLimit\"\'\n\x0bJointLimits\x12\x0b\n\x03min\x18\x01 \x01(\x02\x12\x0b\n\x03max\x18\x02 \x01(\x02\"\xf3\x02\n\x0cJointsLimits\x12\x34\n\x0eshoulder_pitch\x18\x01 \x01(\x0b\x32\x1c.reachy.part.arm.JointLimits\x12\x33\n\rshoulder_roll\x18\x02 \x01(\x0b\x32\x1c.reachy.part.arm.JointLimits\x12/\n\telbow_yaw\x18\x03 \x01(\x0b\x32\x1c.reachy.part.arm.JointLimits\x12\x31\n\x0b\x65lbow_pitch\x18\x04 \x01(\x0b\x32\x1c.reachy.part.arm.JointLimits\x12\x30\n\nwrist_roll\x18\x05 \x01(\x0b\x32\x1c.reachy.part.arm.JointLimits\x12\x31\n\x0bwrist_pitch\x18\x06 \x01(\x0b\x32\x1c.reachy.part.arm.JointLimits\x12/\n\twrist_yaw\x18\x07 \x01(\x0b\x32\x1c.reachy.part.arm.JointLimits\"-\n\x0cTemperatures\x12\r\n\x05motor\x18\x01 \x01(\x02\x12\x0e\n\x06\x64river\x18\x02 \x01(\x02\"\x91\x03\n\x0f\x41rmTemperatures\x12\x37\n\x10shoulder_motor_1\x18\x01 \x01(\x0b\x32\x1d.reachy.part.arm.Temperatures\x12\x37\n\x10shoulder_motor_2\x18\x02 \x01(\x0b\x32\x1d.reachy.part.arm.Temperatures\x12\x34\n\relbow_motor_1\x18\x03 \x01(\x0b\x32\x1d.reachy.part.arm.Temperatures\x12\x34\n\relbow_motor_2\x18\x04 \x01(\x0b\x32\x1d.reachy.part.arm.Temperatures\x12\x34\n\rwrist_motor_1\x18\x05 \x01(\x0b\x32\x1d.reachy.part.arm.Temperatures\x12\x34\n\rwrist_motor_2\x18\x06 \x01(\x0b\x32\x1d.reachy.part.arm.Temperatures\x12\x34\n\rwrist_motor_3\x18\x07 \x01(\x0b\x32\x1d.reachy.part.arm.Temperatures*\xdb\x01\n\x08\x41rmField\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04NAME\x10\x01\x12\x07\n\x03UID\x10\x02\x12\x14\n\x10PRESENT_POSITION\x10\x03\x12\x11\n\rPRESENT_SPEED\x10\x04\x12\x10\n\x0cPRESENT_LOAD\x10\x05\x12\x0f\n\x0bTEMPERATURE\x10\x06\x12\x0f\n\x0bJOINT_LIMIT\x10\x07\x12\r\n\tCOMPLIANT\x10\x08\x12\x11\n\rGOAL_POSITION\x10\t\x12\x0f\n\x0bSPEED_LIMIT\x10\n\x12\x10\n\x0cTORQUE_LIMIT\x10\x0b\x12\x07\n\x03PID\x10\x0c\x12\x07\n\x03\x41LL\x10\x0f*:\n\nSpeedLimit\x12\x0c\n\x08NO_LIMIT\x10\x00\x12\x08\n\x04\x46\x41ST\x10\x01\x12\n\n\x06NORMAL\x10\x02\x12\x08\n\x04SLOW\x10\x03\x32\xa4\t\n\nArmService\x12@\n\nGetAllArms\x12\x16.google.protobuf.Empty\x1a\x1a.reachy.part.arm.ListOfArm\x12L\n\x0c\x43omputeArmFK\x12\x1c.reachy.part.arm.ArmPosition\x1a\x1e.reachy.part.arm.ArmFKSolution\x12M\n\x0c\x43omputeArmIK\x12\x1d.reachy.part.arm.ArmIKRequest\x1a\x1e.reachy.part.arm.ArmIKSolution\x12R\n\x15GoToCartesianPosition\x12!.reachy.part.arm.ArmCartesianGoal\x1a\x16.google.protobuf.Empty\x12J\n\x11GoToJointPosition\x12\x1d.reachy.part.arm.ArmJointGoal\x1a\x16.google.protobuf.Empty\x12I\n\x14GetCartesianPosition\x12\x13.reachy.part.PartId\x1a\x1c.reachy.kinematics.Matrix4x4\x12\x45\n\x10GetJointPosition\x12\x13.reachy.part.PartId\x1a\x1c.reachy.part.arm.ArmPosition\x12\x38\n\x05\x41udit\x12\x13.reachy.part.PartId\x1a\x1a.reachy.part.arm.ArmStatus\x12\x38\n\tHeartBeat\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x36\n\x07Restart\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x41\n\x12ResetDefaultValues\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x35\n\x06TurnOn\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x36\n\x07TurnOff\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x45\n\x0fGetJointsLimits\x12\x13.reachy.part.PartId\x1a\x1d.reachy.part.arm.JointsLimits\x12H\n\x0fGetTemperatures\x12\x13.reachy.part.PartId\x1a .reachy.part.arm.ArmTemperatures\x12I\n\x14GetJointGoalPosition\x12\x13.reachy.part.PartId\x1a\x1c.reachy.part.arm.ArmPosition\x12K\n\rSetSpeedLimit\x12\".reachy.part.arm.SpeedLimitRequest\x1a\x16.google.protobuf.Emptyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'arm_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_ARMFIELD']._serialized_start=2084
  _globals['_ARMFIELD']._serialized_end=2303
  _globals['_SPEEDLIMIT']._serialized_start=2305
  _globals['_SPEEDLIMIT']._serialized_end=2363
  _globals['_ARMSTATE']._serialized_start=134
  _globals['_ARMSTATE']._serialized_end=144
  _globals['_ARM']._serialized_start=146
  _globals['_ARM']._serialized_end=226
  _globals['_LISTOFARM']._serialized_start=228
  _globals['_LISTOFARM']._serialized_end=274
  _globals['_ARMPOSITION']._serialized_start=277
  _globals['_ARMPOSITION']._serialized_end=437
  _globals['_ARMCARTESIANGOAL']._serialized_start=440
  _globals['_ARMCARTESIANGOAL']._serialized_end=586
  _globals['_ARMJOINTGOAL']._serialized_start=589
  _globals['_ARMJOINTGOAL']._serialized_end=731
  _globals['_ARMENDEFFECTOR']._serialized_start=733
  _globals['_ARMENDEFFECTOR']._serialized_end=793
  _globals['_ARMFKSOLUTION']._serialized_start=795
  _globals['_ARMFKSOLUTION']._serialized_end=882
  _globals['_ARMIKREQUEST']._serialized_start=884
  _globals['_ARMIKREQUEST']._serialized_end=989
  _globals['_ARMIKSOLUTION']._serialized_start=991
  _globals['_ARMIKSOLUTION']._serialized_end=1104
  _globals['_ARMSTATUS']._serialized_start=1106
  _globals['_ARMSTATUS']._serialized_end=1117
  _globals['_SPEEDLIMITREQUEST']._serialized_start=1119
  _globals['_SPEEDLIMITREQUEST']._serialized_end=1215
  _globals['_JOINTLIMITS']._serialized_start=1217
  _globals['_JOINTLIMITS']._serialized_end=1256
  _globals['_JOINTSLIMITS']._serialized_start=1259
  _globals['_JOINTSLIMITS']._serialized_end=1630
  _globals['_TEMPERATURES']._serialized_start=1632
  _globals['_TEMPERATURES']._serialized_end=1677
  _globals['_ARMTEMPERATURES']._serialized_start=1680
  _globals['_ARMTEMPERATURES']._serialized_end=2081
  _globals['_ARMSERVICE']._serialized_start=2366
  _globals['_ARMSERVICE']._serialized_end=3554
# @@protoc_insertion_point(module_scope)

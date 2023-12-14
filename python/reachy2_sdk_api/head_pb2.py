# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: head.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import part_pb2 as part__pb2
import kinematics_pb2 as kinematics__pb2
import error_pb2 as error__pb2
import component_pb2 as component__pb2
import orbita3d_pb2 as orbita3d__pb2
import dynamixel_motor_pb2 as dynamixel__motor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nhead.proto\x12\x10reachy.part.head\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\npart.proto\x1a\x10kinematics.proto\x1a\x0b\x65rror.proto\x1a\x0f\x63omponent.proto\x1a\x0eorbita3d.proto\x1a\x15\x64ynamixel_motor.proto\"\x89\x01\n\x04Head\x12$\n\x07part_id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12\x36\n\x0b\x64\x65scription\x18\x02 \x01(\x0b\x32!.reachy.part.head.HeadDescription\x12#\n\x04info\x18\x05 \x01(\x0b\x32\x15.reachy.part.PartInfo\"\xb9\x01\n\x0fHeadDescription\x12*\n\x04neck\x18\x01 \x01(\x0b\x32\x1c.component.orbita3d.Orbita3d\x12<\n\tl_antenna\x18\x02 \x01(\x0b\x32).component.dynamixel_motor.DynamixelMotor\x12<\n\tr_antenna\x18\x03 \x01(\x0b\x32).component.dynamixel_motor.DynamixelMotor\"2\n\nListOfHead\x12$\n\x04head\x18\x01 \x03(\x0b\x32\x16.reachy.part.head.Head\"\xb7\x02\n\tHeadState\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1f\n\x02id\x18\x02 \x01(\x0b\x32\x13.reachy.part.PartId\x12\x11\n\tactivated\x18\x03 \x01(\x08\x12\x35\n\nneck_state\x18\x04 \x01(\x0b\x32!.component.orbita3d.Orbita3dState\x12G\n\x0fl_antenna_state\x18\x05 \x01(\x0b\x32..component.dynamixel_motor.DynamixelMotorState\x12G\n\x0fr_antenna_state\x18\x06 \x01(\x0b\x32..component.dynamixel_motor.DynamixelMotorState\"\xb6\x01\n\x0cHeadPosition\x12\x34\n\rneck_position\x18\x01 \x01(\x0b\x32\x1d.reachy.kinematics.Rotation3d\x12\x37\n\x12l_antenna_position\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x37\n\x12r_antenna_position\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"\x94\x01\n\x11NeckCartesianGoal\x12\x1f\n\x02id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12/\n\tgoal_pose\x18\x02 \x01(\x0b\x32\x1c.reachy.kinematics.Matrix4x4\x12-\n\x08\x64uration\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"\x92\x01\n\x08NeckGoal\x12\x1f\n\x02id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12\x36\n\x0bjoints_goal\x18\x02 \x01(\x0b\x32!.reachy.part.head.NeckOrientation\x12-\n\x08\x64uration\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"B\n\x0fNeckOrientation\x12/\n\x08rotation\x18\x01 \x01(\x0b\x32\x1d.reachy.kinematics.Rotation3d\"b\n\rNeckFKRequest\x12\x1f\n\x02id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12\x30\n\x08position\x18\x02 \x01(\x0b\x32\x1e.reachy.part.head.HeadPosition\"Y\n\x0eNeckFKSolution\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x36\n\x0borientation\x18\x02 \x01(\x0b\x32!.reachy.part.head.NeckOrientation\"\x8e\x01\n\rNeckIKRequest\x12\x1f\n\x02id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12\x31\n\x06target\x18\x02 \x01(\x0b\x32!.reachy.part.head.NeckOrientation\x12)\n\x02q0\x18\x03 \x01(\x0b\x32\x1d.reachy.kinematics.Rotation3d\"o\n\x0eNeckIKSolution\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12/\n\x08position\x18\x02 \x01(\x0b\x32\x1d.reachy.kinematics.Rotation3d\x12\x1b\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x0c.error.Error\"\x0c\n\nHeadStatus\"\x89\x01\n\x0eHeadLookAtGoal\x12\x1f\n\x02id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12\'\n\x05point\x18\x02 \x01(\x0b\x32\x18.reachy.kinematics.Point\x12-\n\x08\x64uration\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"a\n\x11SpeedLimitRequest\x12\x1f\n\x02id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12+\n\x05limit\x18\x02 \x01(\x0e\x32\x1c.reachy.part.head.SpeedLimit\"\xa5\x01\n\x0cJointsLimits\x12\x31\n\x0bneck_limits\x18\x01 \x01(\x0b\x32\x1c.component.orbita3d.Limits3d\x12\x30\n\x10l_antenna_limits\x18\x02 \x01(\x0b\x32\x16.component.JointLimits\x12\x30\n\x10r_antenna_limits\x18\x03 \x01(\x0b\x32\x16.component.JointLimits\"\x87\x01\n\x10HeadTemperatures\x12\x35\n\x10neck_temperature\x18\x01 \x01(\x0b\x32\x1b.component.orbita3d.Float3d\x12\x1d\n\x15l_antenna_temperature\x18\x02 \x01(\x02\x12\x1d\n\x15r_antenna_temperature\x18\x03 \x01(\x02*\xdb\x01\n\tHeadField\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04NAME\x10\x01\x12\x06\n\x02ID\x10\x02\x12\x14\n\x10PRESENT_POSITION\x10\x03\x12\x11\n\rPRESENT_SPEED\x10\x04\x12\x10\n\x0cPRESENT_LOAD\x10\x05\x12\x0f\n\x0bTEMPERATURE\x10\x06\x12\x0f\n\x0bJOINT_LIMIT\x10\x07\x12\r\n\tCOMPLIANT\x10\x08\x12\x11\n\rGOAL_POSITION\x10\t\x12\x0f\n\x0bSPEED_LIMIT\x10\n\x12\x10\n\x0cTORQUE_LIMIT\x10\x0b\x12\x07\n\x03PID\x10\x0c\x12\x07\n\x03\x41LL\x10\x0f*:\n\nSpeedLimit\x12\x0c\n\x08NO_LIMIT\x10\x00\x12\x08\n\x04\x46\x41ST\x10\x01\x12\n\n\x06NORMAL\x10\x02\x12\x08\n\x04SLOW\x10\x03\x32\xd0\x08\n\x0bHeadService\x12\x43\n\x0bGetAllHeads\x12\x16.google.protobuf.Empty\x1a\x1c.reachy.part.head.ListOfHead\x12<\n\x08GetState\x12\x13.reachy.part.PartId\x1a\x1b.reachy.part.head.HeadState\x12R\n\rComputeNeckFK\x12\x1f.reachy.part.head.NeckFKRequest\x1a .reachy.part.head.NeckFKSolution\x12R\n\rComputeNeckIK\x12\x1f.reachy.part.head.NeckIKRequest\x1a .reachy.part.head.NeckIKSolution\x12\x44\n\x0eGetOrientation\x12\x13.reachy.part.PartId\x1a\x1d.reachy.kinematics.Rotation3d\x12\x42\n\x06LookAt\x12 .reachy.part.head.HeadLookAtGoal\x1a\x16.google.protobuf.Empty\x12:\n\x05\x41udit\x12\x13.reachy.part.PartId\x1a\x1c.reachy.part.head.HeadStatus\x12\x38\n\tHeartBeat\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x36\n\x07Restart\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x41\n\x12ResetDefaultValues\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x35\n\x06TurnOn\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x36\n\x07TurnOff\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x46\n\x0fGetJointsLimits\x12\x13.reachy.part.PartId\x1a\x1e.reachy.part.head.JointsLimits\x12J\n\x0fGetTemperatures\x12\x13.reachy.part.PartId\x1a\".reachy.part.head.HeadTemperatures\x12J\n\x14GetJointGoalPosition\x12\x13.reachy.part.PartId\x1a\x1d.reachy.kinematics.Rotation3d\x12L\n\rSetSpeedLimit\x12#.reachy.part.head.SpeedLimitRequest\x1a\x16.google.protobuf.Emptyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'head_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_HEADFIELD']._serialized_start=2481
  _globals['_HEADFIELD']._serialized_end=2700
  _globals['_SPEEDLIMIT']._serialized_start=2702
  _globals['_SPEEDLIMIT']._serialized_end=2760
  _globals['_HEAD']._serialized_start=226
  _globals['_HEAD']._serialized_end=363
  _globals['_HEADDESCRIPTION']._serialized_start=366
  _globals['_HEADDESCRIPTION']._serialized_end=551
  _globals['_LISTOFHEAD']._serialized_start=553
  _globals['_LISTOFHEAD']._serialized_end=603
  _globals['_HEADSTATE']._serialized_start=606
  _globals['_HEADSTATE']._serialized_end=917
  _globals['_HEADPOSITION']._serialized_start=920
  _globals['_HEADPOSITION']._serialized_end=1102
  _globals['_NECKCARTESIANGOAL']._serialized_start=1105
  _globals['_NECKCARTESIANGOAL']._serialized_end=1253
  _globals['_NECKGOAL']._serialized_start=1256
  _globals['_NECKGOAL']._serialized_end=1402
  _globals['_NECKORIENTATION']._serialized_start=1404
  _globals['_NECKORIENTATION']._serialized_end=1470
  _globals['_NECKFKREQUEST']._serialized_start=1472
  _globals['_NECKFKREQUEST']._serialized_end=1570
  _globals['_NECKFKSOLUTION']._serialized_start=1572
  _globals['_NECKFKSOLUTION']._serialized_end=1661
  _globals['_NECKIKREQUEST']._serialized_start=1664
  _globals['_NECKIKREQUEST']._serialized_end=1806
  _globals['_NECKIKSOLUTION']._serialized_start=1808
  _globals['_NECKIKSOLUTION']._serialized_end=1919
  _globals['_HEADSTATUS']._serialized_start=1921
  _globals['_HEADSTATUS']._serialized_end=1933
  _globals['_HEADLOOKATGOAL']._serialized_start=1936
  _globals['_HEADLOOKATGOAL']._serialized_end=2073
  _globals['_SPEEDLIMITREQUEST']._serialized_start=2075
  _globals['_SPEEDLIMITREQUEST']._serialized_end=2172
  _globals['_JOINTSLIMITS']._serialized_start=2175
  _globals['_JOINTSLIMITS']._serialized_end=2340
  _globals['_HEADTEMPERATURES']._serialized_start=2343
  _globals['_HEADTEMPERATURES']._serialized_end=2478
  _globals['_HEADSERVICE']._serialized_start=2763
  _globals['_HEADSERVICE']._serialized_end=3867
# @@protoc_insertion_point(module_scope)

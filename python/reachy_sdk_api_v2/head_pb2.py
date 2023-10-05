# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: head.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import part_pb2 as part__pb2
import kinematics_pb2 as kinematics__pb2
import error_pb2 as error__pb2
import orbita3d_pb2 as orbita3d__pb2
import dynamixel_motor_pb2 as dynamixel__motor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nhead.proto\x12\x10reachy.part.head\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\npart.proto\x1a\x10kinematics.proto\x1a\x0b\x65rror.proto\x1a\x0eorbita3d.proto\x1a\x15\x64ynamixel_motor.proto\"\x89\x01\n\x04Head\x12$\n\x07part_id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12\x36\n\x0b\x64\x65scription\x18\x02 \x01(\x0b\x32!.reachy.part.head.HeadDescription\x12#\n\x04info\x18\x05 \x01(\x0b\x32\x15.reachy.part.PartInfo\"\xc5\x01\n\x0fHeadDescription\x12.\n\x04neck\x18\x01 \x01(\x0b\x32 .component.orbita3d.Orbita3DInfo\x12@\n\tl_antenna\x18\x02 \x01(\x0b\x32-.component.dynamixel_motor.DynamixelMotorInfo\x12@\n\tr_antenna\x18\x03 \x01(\x0b\x32-.component.dynamixel_motor.DynamixelMotorInfo\"2\n\nListOfHead\x12$\n\x04head\x18\x01 \x03(\x0b\x32\x16.reachy.part.head.Head\"\x9d\x02\n\tHeadState\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\r\x12\x35\n\nneck_state\x18\x04 \x01(\x0b\x32!.component.orbita3d.Orbita3DState\x12G\n\x0fl_antenna_state\x18\x05 \x01(\x0b\x32..component.dynamixel_motor.DynamixelMotorState\x12G\n\x0fr_antenna_state\x18\x06 \x01(\x0b\x32..component.dynamixel_motor.DynamixelMotorState\"G\n\x0cNeckPosition\x12\x11\n\tneck_roll\x18\x01 \x01(\x02\x12\x12\n\nneck_pitch\x18\x02 \x01(\x02\x12\x10\n\x08neck_yaw\x18\x03 \x01(\x02\"\xb7\x01\n\x0cHeadPosition\x12\x35\n\rneck_position\x18\x01 \x01(\x0b\x32\x1e.reachy.part.head.NeckPosition\x12\x37\n\x12l_antenna_position\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x37\n\x12r_antenna_position\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"\x8b\x01\n\x08NeckGoal\x12\x1f\n\x02id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12/\n\x08rotation\x18\x02 \x01(\x0b\x32\x1d.reachy.kinematics.Rotation3D\x12-\n\x08\x64uration\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\";\n\x0fNeckOrientation\x12(\n\x01q\x18\x01 \x01(\x0b\x32\x1d.reachy.kinematics.Quaternion\"b\n\rNeckFKRequest\x12\x1f\n\x02id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12\x30\n\x08position\x18\x02 \x01(\x0b\x32\x1e.reachy.part.head.HeadPosition\"Y\n\x0eNeckFKSolution\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x36\n\x0borientation\x18\x02 \x01(\x0b\x32!.reachy.part.head.NeckOrientation\"\x8f\x01\n\rNeckIKRequest\x12\x1f\n\x02id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12\x31\n\x06target\x18\x02 \x01(\x0b\x32!.reachy.part.head.NeckOrientation\x12*\n\x02q0\x18\x03 \x01(\x0b\x32\x1e.reachy.part.head.NeckPosition\"p\n\x0eNeckIKSolution\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x30\n\x08position\x18\x02 \x01(\x0b\x32\x1e.reachy.part.head.NeckPosition\x12\x1b\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x0c.error.Error\"\x0c\n\nHeadStatus\"[\n\x0fHeadTargetPoint\x12\x1f\n\x02id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12\'\n\x05point\x18\x02 \x01(\x0b\x32\x18.reachy.kinematics.Point\"a\n\x11SpeedLimitRequest\x12\x1f\n\x02id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12+\n\x05limit\x18\x02 \x01(\x0e\x32\x1c.reachy.part.head.SpeedLimit\"\'\n\x0bJointLimits\x12\x0b\n\x03min\x18\x01 \x01(\x02\x12\x0b\n\x03max\x18\x02 \x01(\x02\"\x88\x02\n\x0cJointsLimits\x12\x30\n\tneck_roll\x18\x01 \x01(\x0b\x32\x1d.reachy.part.head.JointLimits\x12\x31\n\nneck_pitch\x18\x02 \x01(\x0b\x32\x1d.reachy.part.head.JointLimits\x12/\n\x08neck_yaw\x18\x03 \x01(\x0b\x32\x1d.reachy.part.head.JointLimits\x12\x30\n\tl_antenna\x18\x04 \x01(\x0b\x32\x1d.reachy.part.head.JointLimits\x12\x30\n\tr_antenna\x18\x05 \x01(\x0b\x32\x1d.reachy.part.head.JointLimits\"-\n\x0cTemperatures\x12\r\n\x05motor\x18\x01 \x01(\x02\x12\x0e\n\x06\x64river\x18\x02 \x01(\x02\"\x9a\x02\n\x10HeadTemperatures\x12\x34\n\x0cneck_motor_1\x18\x01 \x01(\x0b\x32\x1e.reachy.part.head.Temperatures\x12\x34\n\x0cneck_motor_2\x18\x02 \x01(\x0b\x32\x1e.reachy.part.head.Temperatures\x12\x34\n\x0cneck_motor_3\x18\x03 \x01(\x0b\x32\x1e.reachy.part.head.Temperatures\x12\x31\n\tl_antenna\x18\x04 \x01(\x0b\x32\x1e.reachy.part.head.Temperatures\x12\x31\n\tr_antenna\x18\x05 \x01(\x0b\x32\x1e.reachy.part.head.Temperatures*\xdb\x01\n\tHeadField\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04NAME\x10\x01\x12\x06\n\x02ID\x10\x02\x12\x14\n\x10PRESENT_POSITION\x10\x03\x12\x11\n\rPRESENT_SPEED\x10\x04\x12\x10\n\x0cPRESENT_LOAD\x10\x05\x12\x0f\n\x0bTEMPERATURE\x10\x06\x12\x0f\n\x0bJOINT_LIMIT\x10\x07\x12\r\n\tCOMPLIANT\x10\x08\x12\x11\n\rGOAL_POSITION\x10\t\x12\x0f\n\x0bSPEED_LIMIT\x10\n\x12\x10\n\x0cTORQUE_LIMIT\x10\x0b\x12\x07\n\x03PID\x10\x0c\x12\x07\n\x03\x41LL\x10\x0f*:\n\nSpeedLimit\x12\x0c\n\x08NO_LIMIT\x10\x00\x12\x08\n\x04\x46\x41ST\x10\x01\x12\n\n\x06NORMAL\x10\x02\x12\x08\n\x04SLOW\x10\x03\x32\xdb\x08\n\x0bHeadService\x12\x43\n\x0bGetAllHeads\x12\x16.google.protobuf.Empty\x1a\x1c.reachy.part.head.ListOfHead\x12R\n\rComputeNeckFK\x12\x1f.reachy.part.head.NeckFKRequest\x1a .reachy.part.head.NeckFKSolution\x12R\n\rComputeNeckIK\x12\x1f.reachy.part.head.NeckIKRequest\x1a .reachy.part.head.NeckIKSolution\x12\x45\n\x0fGoToOrientation\x12\x1a.reachy.part.head.NeckGoal\x1a\x16.google.protobuf.Empty\x12\x44\n\x0eGetOrientation\x12\x13.reachy.part.PartId\x1a\x1d.reachy.kinematics.Quaternion\x12\x43\n\x06LookAt\x12!.reachy.part.head.HeadTargetPoint\x1a\x16.google.protobuf.Empty\x12:\n\x05\x41udit\x12\x13.reachy.part.PartId\x1a\x1c.reachy.part.head.HeadStatus\x12\x38\n\tHeartBeat\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x36\n\x07Restart\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x41\n\x12ResetDefaultValues\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x35\n\x06TurnOn\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x36\n\x07TurnOff\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x46\n\x0fGetJointsLimits\x12\x13.reachy.part.PartId\x1a\x1e.reachy.part.head.JointsLimits\x12J\n\x0fGetTemperatures\x12\x13.reachy.part.PartId\x1a\".reachy.part.head.HeadTemperatures\x12K\n\x14GetJointGoalPosition\x12\x13.reachy.part.PartId\x1a\x1e.reachy.part.head.NeckPosition\x12L\n\rSetSpeedLimit\x12#.reachy.part.head.SpeedLimitRequest\x1a\x16.google.protobuf.Emptyb\x06proto3')

_HEADFIELD = DESCRIPTOR.enum_types_by_name['HeadField']
HeadField = enum_type_wrapper.EnumTypeWrapper(_HEADFIELD)
_SPEEDLIMIT = DESCRIPTOR.enum_types_by_name['SpeedLimit']
SpeedLimit = enum_type_wrapper.EnumTypeWrapper(_SPEEDLIMIT)
NONE = 0
NAME = 1
ID = 2
PRESENT_POSITION = 3
PRESENT_SPEED = 4
PRESENT_LOAD = 5
TEMPERATURE = 6
JOINT_LIMIT = 7
COMPLIANT = 8
GOAL_POSITION = 9
SPEED_LIMIT = 10
TORQUE_LIMIT = 11
PID = 12
ALL = 15
NO_LIMIT = 0
FAST = 1
NORMAL = 2
SLOW = 3


_HEAD = DESCRIPTOR.message_types_by_name['Head']
_HEADDESCRIPTION = DESCRIPTOR.message_types_by_name['HeadDescription']
_LISTOFHEAD = DESCRIPTOR.message_types_by_name['ListOfHead']
_HEADSTATE = DESCRIPTOR.message_types_by_name['HeadState']
_NECKPOSITION = DESCRIPTOR.message_types_by_name['NeckPosition']
_HEADPOSITION = DESCRIPTOR.message_types_by_name['HeadPosition']
_NECKGOAL = DESCRIPTOR.message_types_by_name['NeckGoal']
_NECKORIENTATION = DESCRIPTOR.message_types_by_name['NeckOrientation']
_NECKFKREQUEST = DESCRIPTOR.message_types_by_name['NeckFKRequest']
_NECKFKSOLUTION = DESCRIPTOR.message_types_by_name['NeckFKSolution']
_NECKIKREQUEST = DESCRIPTOR.message_types_by_name['NeckIKRequest']
_NECKIKSOLUTION = DESCRIPTOR.message_types_by_name['NeckIKSolution']
_HEADSTATUS = DESCRIPTOR.message_types_by_name['HeadStatus']
_HEADTARGETPOINT = DESCRIPTOR.message_types_by_name['HeadTargetPoint']
_SPEEDLIMITREQUEST = DESCRIPTOR.message_types_by_name['SpeedLimitRequest']
_JOINTLIMITS = DESCRIPTOR.message_types_by_name['JointLimits']
_JOINTSLIMITS = DESCRIPTOR.message_types_by_name['JointsLimits']
_TEMPERATURES = DESCRIPTOR.message_types_by_name['Temperatures']
_HEADTEMPERATURES = DESCRIPTOR.message_types_by_name['HeadTemperatures']
Head = _reflection.GeneratedProtocolMessageType('Head', (_message.Message,), {
  'DESCRIPTOR' : _HEAD,
  '__module__' : 'head_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.head.Head)
  })
_sym_db.RegisterMessage(Head)

HeadDescription = _reflection.GeneratedProtocolMessageType('HeadDescription', (_message.Message,), {
  'DESCRIPTOR' : _HEADDESCRIPTION,
  '__module__' : 'head_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.head.HeadDescription)
  })
_sym_db.RegisterMessage(HeadDescription)

ListOfHead = _reflection.GeneratedProtocolMessageType('ListOfHead', (_message.Message,), {
  'DESCRIPTOR' : _LISTOFHEAD,
  '__module__' : 'head_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.head.ListOfHead)
  })
_sym_db.RegisterMessage(ListOfHead)

HeadState = _reflection.GeneratedProtocolMessageType('HeadState', (_message.Message,), {
  'DESCRIPTOR' : _HEADSTATE,
  '__module__' : 'head_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.head.HeadState)
  })
_sym_db.RegisterMessage(HeadState)

NeckPosition = _reflection.GeneratedProtocolMessageType('NeckPosition', (_message.Message,), {
  'DESCRIPTOR' : _NECKPOSITION,
  '__module__' : 'head_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.head.NeckPosition)
  })
_sym_db.RegisterMessage(NeckPosition)

HeadPosition = _reflection.GeneratedProtocolMessageType('HeadPosition', (_message.Message,), {
  'DESCRIPTOR' : _HEADPOSITION,
  '__module__' : 'head_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.head.HeadPosition)
  })
_sym_db.RegisterMessage(HeadPosition)

NeckGoal = _reflection.GeneratedProtocolMessageType('NeckGoal', (_message.Message,), {
  'DESCRIPTOR' : _NECKGOAL,
  '__module__' : 'head_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.head.NeckGoal)
  })
_sym_db.RegisterMessage(NeckGoal)

NeckOrientation = _reflection.GeneratedProtocolMessageType('NeckOrientation', (_message.Message,), {
  'DESCRIPTOR' : _NECKORIENTATION,
  '__module__' : 'head_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.head.NeckOrientation)
  })
_sym_db.RegisterMessage(NeckOrientation)

NeckFKRequest = _reflection.GeneratedProtocolMessageType('NeckFKRequest', (_message.Message,), {
  'DESCRIPTOR' : _NECKFKREQUEST,
  '__module__' : 'head_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.head.NeckFKRequest)
  })
_sym_db.RegisterMessage(NeckFKRequest)

NeckFKSolution = _reflection.GeneratedProtocolMessageType('NeckFKSolution', (_message.Message,), {
  'DESCRIPTOR' : _NECKFKSOLUTION,
  '__module__' : 'head_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.head.NeckFKSolution)
  })
_sym_db.RegisterMessage(NeckFKSolution)

NeckIKRequest = _reflection.GeneratedProtocolMessageType('NeckIKRequest', (_message.Message,), {
  'DESCRIPTOR' : _NECKIKREQUEST,
  '__module__' : 'head_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.head.NeckIKRequest)
  })
_sym_db.RegisterMessage(NeckIKRequest)

NeckIKSolution = _reflection.GeneratedProtocolMessageType('NeckIKSolution', (_message.Message,), {
  'DESCRIPTOR' : _NECKIKSOLUTION,
  '__module__' : 'head_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.head.NeckIKSolution)
  })
_sym_db.RegisterMessage(NeckIKSolution)

HeadStatus = _reflection.GeneratedProtocolMessageType('HeadStatus', (_message.Message,), {
  'DESCRIPTOR' : _HEADSTATUS,
  '__module__' : 'head_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.head.HeadStatus)
  })
_sym_db.RegisterMessage(HeadStatus)

HeadTargetPoint = _reflection.GeneratedProtocolMessageType('HeadTargetPoint', (_message.Message,), {
  'DESCRIPTOR' : _HEADTARGETPOINT,
  '__module__' : 'head_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.head.HeadTargetPoint)
  })
_sym_db.RegisterMessage(HeadTargetPoint)

SpeedLimitRequest = _reflection.GeneratedProtocolMessageType('SpeedLimitRequest', (_message.Message,), {
  'DESCRIPTOR' : _SPEEDLIMITREQUEST,
  '__module__' : 'head_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.head.SpeedLimitRequest)
  })
_sym_db.RegisterMessage(SpeedLimitRequest)

JointLimits = _reflection.GeneratedProtocolMessageType('JointLimits', (_message.Message,), {
  'DESCRIPTOR' : _JOINTLIMITS,
  '__module__' : 'head_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.head.JointLimits)
  })
_sym_db.RegisterMessage(JointLimits)

JointsLimits = _reflection.GeneratedProtocolMessageType('JointsLimits', (_message.Message,), {
  'DESCRIPTOR' : _JOINTSLIMITS,
  '__module__' : 'head_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.head.JointsLimits)
  })
_sym_db.RegisterMessage(JointsLimits)

Temperatures = _reflection.GeneratedProtocolMessageType('Temperatures', (_message.Message,), {
  'DESCRIPTOR' : _TEMPERATURES,
  '__module__' : 'head_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.head.Temperatures)
  })
_sym_db.RegisterMessage(Temperatures)

HeadTemperatures = _reflection.GeneratedProtocolMessageType('HeadTemperatures', (_message.Message,), {
  'DESCRIPTOR' : _HEADTEMPERATURES,
  '__module__' : 'head_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.head.HeadTemperatures)
  })
_sym_db.RegisterMessage(HeadTemperatures)

_HEADSERVICE = DESCRIPTOR.services_by_name['HeadService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HEADFIELD._serialized_start=2648
  _HEADFIELD._serialized_end=2867
  _SPEEDLIMIT._serialized_start=2869
  _SPEEDLIMIT._serialized_end=2927
  _HEAD._serialized_start=209
  _HEAD._serialized_end=346
  _HEADDESCRIPTION._serialized_start=349
  _HEADDESCRIPTION._serialized_end=546
  _LISTOFHEAD._serialized_start=548
  _LISTOFHEAD._serialized_end=598
  _HEADSTATE._serialized_start=601
  _HEADSTATE._serialized_end=886
  _NECKPOSITION._serialized_start=888
  _NECKPOSITION._serialized_end=959
  _HEADPOSITION._serialized_start=962
  _HEADPOSITION._serialized_end=1145
  _NECKGOAL._serialized_start=1148
  _NECKGOAL._serialized_end=1287
  _NECKORIENTATION._serialized_start=1289
  _NECKORIENTATION._serialized_end=1348
  _NECKFKREQUEST._serialized_start=1350
  _NECKFKREQUEST._serialized_end=1448
  _NECKFKSOLUTION._serialized_start=1450
  _NECKFKSOLUTION._serialized_end=1539
  _NECKIKREQUEST._serialized_start=1542
  _NECKIKREQUEST._serialized_end=1685
  _NECKIKSOLUTION._serialized_start=1687
  _NECKIKSOLUTION._serialized_end=1799
  _HEADSTATUS._serialized_start=1801
  _HEADSTATUS._serialized_end=1813
  _HEADTARGETPOINT._serialized_start=1815
  _HEADTARGETPOINT._serialized_end=1906
  _SPEEDLIMITREQUEST._serialized_start=1908
  _SPEEDLIMITREQUEST._serialized_end=2005
  _JOINTLIMITS._serialized_start=2007
  _JOINTLIMITS._serialized_end=2046
  _JOINTSLIMITS._serialized_start=2049
  _JOINTSLIMITS._serialized_end=2313
  _TEMPERATURES._serialized_start=2315
  _TEMPERATURES._serialized_end=2360
  _HEADTEMPERATURES._serialized_start=2363
  _HEADTEMPERATURES._serialized_end=2645
  _HEADSERVICE._serialized_start=2930
  _HEADSERVICE._serialized_end=4045
# @@protoc_insertion_point(module_scope)

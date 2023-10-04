# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dynamixel_motor.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
import component_pb2 as component__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x64ynamixel_motor.proto\x12\x19\x63omponent.dynamixel_motor\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x0f\x63omponent.proto\"\x99\x04\n\x13\x44ynamixelMotorState\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03uid\x18\x03 \x01(\t\x12\x35\n\x10present_position\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x32\n\rpresent_speed\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x31\n\x0cpresent_load\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x30\n\x0btemperature\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12-\n\tcompliant\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x32\n\rgoal_position\x18\t \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x30\n\x0bspeed_limit\x18\n \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x31\n\x0ctorque_limit\x18\x0b \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12 \n\x03pid\x18\x0c \x01(\x0b\x32\x13.component.PIDGains\"\x80\x01\n\x1a\x44ynamixelMotorStateRequest\x12>\n\x06\x66ields\x18\x01 \x03(\x0e\x32..component.dynamixel_motor.DynamixelMotorField\x12\"\n\x02id\x18\x02 \x01(\x0b\x32\x16.component.ComponentId\"t\n DynamixelMotorStreamStateRequest\x12\x42\n\x03req\x18\x01 \x01(\x0b\x32\x35.component.dynamixel_motor.DynamixelMotorStateRequest\x12\x0c\n\x04\x66req\x18\x02 \x01(\x02\"\x83\x02\n\x15\x44ynamixelMotorCommand\x12\"\n\x02id\x18\x01 \x01(\x0b\x32\x16.component.ComponentId\x12-\n\tcompliant\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x32\n\rgoal_position\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x30\n\x0bspeed_limit\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x31\n\x0ctorque_limit\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"O\n\x12\x44ynamixelMotorInfo\x12\"\n\x02id\x18\x01 \x01(\x0b\x32\x16.component.ComponentId\x12\x15\n\rserial_number\x18\x02 \x01(\t\"h\n\x18ListOfDynamixelMotorInfo\x12L\n\x15parallel_gripper_info\x18\x01 \x03(\x0b\x32-.component.dynamixel_motor.DynamixelMotorInfo\"\x16\n\x14\x44ynamixelMotorStatus*\xe6\x01\n\x13\x44ynamixelMotorField\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04NAME\x10\x01\x12\x07\n\x03UID\x10\x02\x12\x14\n\x10PRESENT_POSITION\x10\x03\x12\x11\n\rPRESENT_SPEED\x10\x04\x12\x10\n\x0cPRESENT_LOAD\x10\x05\x12\x0f\n\x0bTEMPERATURE\x10\x06\x12\x0f\n\x0bJOINT_LIMIT\x10\x07\x12\r\n\tCOMPLIANT\x10\x08\x12\x11\n\rGOAL_POSITION\x10\t\x12\x0f\n\x0bSPEED_LIMIT\x10\n\x12\x10\n\x0cTORQUE_LIMIT\x10\x0b\x12\x07\n\x03PID\x10\x0c\x12\x07\n\x03\x41LL\x10\x0f\x32\xed\x05\n\x15\x44ynamixelMotorService\x12\x63\n\x14GetAllDynamixelMotor\x12\x16.google.protobuf.Empty\x1a\x33.component.dynamixel_motor.ListOfDynamixelMotorInfo\x12q\n\x08GetState\x12\x35.component.dynamixel_motor.DynamixelMotorStateRequest\x1a..component.dynamixel_motor.DynamixelMotorState\x12|\n\x0bStreamState\x12;.component.dynamixel_motor.DynamixelMotorStreamStateRequest\x1a..component.dynamixel_motor.DynamixelMotorState0\x01\x12W\n\x0bSendCommand\x12\x30.component.dynamixel_motor.DynamixelMotorCommand\x1a\x16.google.protobuf.Empty\x12[\n\rStreamCommand\x12\x30.component.dynamixel_motor.DynamixelMotorCommand\x1a\x16.google.protobuf.Empty(\x01\x12P\n\x05\x41udit\x12\x16.component.ComponentId\x1a/.component.dynamixel_motor.DynamixelMotorStatus\x12;\n\tHeartBeat\x12\x16.component.ComponentId\x1a\x16.google.protobuf.Empty\x12\x39\n\x07Restart\x12\x16.component.ComponentId\x1a\x16.google.protobuf.Emptyb\x06proto3')

_DYNAMIXELMOTORFIELD = DESCRIPTOR.enum_types_by_name['DynamixelMotorField']
DynamixelMotorField = enum_type_wrapper.EnumTypeWrapper(_DYNAMIXELMOTORFIELD)
NONE = 0
NAME = 1
UID = 2
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


_DYNAMIXELMOTORSTATE = DESCRIPTOR.message_types_by_name['DynamixelMotorState']
_DYNAMIXELMOTORSTATEREQUEST = DESCRIPTOR.message_types_by_name['DynamixelMotorStateRequest']
_DYNAMIXELMOTORSTREAMSTATEREQUEST = DESCRIPTOR.message_types_by_name['DynamixelMotorStreamStateRequest']
_DYNAMIXELMOTORCOMMAND = DESCRIPTOR.message_types_by_name['DynamixelMotorCommand']
_DYNAMIXELMOTORINFO = DESCRIPTOR.message_types_by_name['DynamixelMotorInfo']
_LISTOFDYNAMIXELMOTORINFO = DESCRIPTOR.message_types_by_name['ListOfDynamixelMotorInfo']
_DYNAMIXELMOTORSTATUS = DESCRIPTOR.message_types_by_name['DynamixelMotorStatus']
DynamixelMotorState = _reflection.GeneratedProtocolMessageType('DynamixelMotorState', (_message.Message,), {
  'DESCRIPTOR' : _DYNAMIXELMOTORSTATE,
  '__module__' : 'dynamixel_motor_pb2'
  # @@protoc_insertion_point(class_scope:component.dynamixel_motor.DynamixelMotorState)
  })
_sym_db.RegisterMessage(DynamixelMotorState)

DynamixelMotorStateRequest = _reflection.GeneratedProtocolMessageType('DynamixelMotorStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _DYNAMIXELMOTORSTATEREQUEST,
  '__module__' : 'dynamixel_motor_pb2'
  # @@protoc_insertion_point(class_scope:component.dynamixel_motor.DynamixelMotorStateRequest)
  })
_sym_db.RegisterMessage(DynamixelMotorStateRequest)

DynamixelMotorStreamStateRequest = _reflection.GeneratedProtocolMessageType('DynamixelMotorStreamStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _DYNAMIXELMOTORSTREAMSTATEREQUEST,
  '__module__' : 'dynamixel_motor_pb2'
  # @@protoc_insertion_point(class_scope:component.dynamixel_motor.DynamixelMotorStreamStateRequest)
  })
_sym_db.RegisterMessage(DynamixelMotorStreamStateRequest)

DynamixelMotorCommand = _reflection.GeneratedProtocolMessageType('DynamixelMotorCommand', (_message.Message,), {
  'DESCRIPTOR' : _DYNAMIXELMOTORCOMMAND,
  '__module__' : 'dynamixel_motor_pb2'
  # @@protoc_insertion_point(class_scope:component.dynamixel_motor.DynamixelMotorCommand)
  })
_sym_db.RegisterMessage(DynamixelMotorCommand)

DynamixelMotorInfo = _reflection.GeneratedProtocolMessageType('DynamixelMotorInfo', (_message.Message,), {
  'DESCRIPTOR' : _DYNAMIXELMOTORINFO,
  '__module__' : 'dynamixel_motor_pb2'
  # @@protoc_insertion_point(class_scope:component.dynamixel_motor.DynamixelMotorInfo)
  })
_sym_db.RegisterMessage(DynamixelMotorInfo)

ListOfDynamixelMotorInfo = _reflection.GeneratedProtocolMessageType('ListOfDynamixelMotorInfo', (_message.Message,), {
  'DESCRIPTOR' : _LISTOFDYNAMIXELMOTORINFO,
  '__module__' : 'dynamixel_motor_pb2'
  # @@protoc_insertion_point(class_scope:component.dynamixel_motor.ListOfDynamixelMotorInfo)
  })
_sym_db.RegisterMessage(ListOfDynamixelMotorInfo)

DynamixelMotorStatus = _reflection.GeneratedProtocolMessageType('DynamixelMotorStatus', (_message.Message,), {
  'DESCRIPTOR' : _DYNAMIXELMOTORSTATUS,
  '__module__' : 'dynamixel_motor_pb2'
  # @@protoc_insertion_point(class_scope:component.dynamixel_motor.DynamixelMotorStatus)
  })
_sym_db.RegisterMessage(DynamixelMotorStatus)

_DYNAMIXELMOTORSERVICE = DESCRIPTOR.services_by_name['DynamixelMotorService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DYNAMIXELMOTORFIELD._serialized_start=1426
  _DYNAMIXELMOTORFIELD._serialized_end=1656
  _DYNAMIXELMOTORSTATE._serialized_start=164
  _DYNAMIXELMOTORSTATE._serialized_end=701
  _DYNAMIXELMOTORSTATEREQUEST._serialized_start=704
  _DYNAMIXELMOTORSTATEREQUEST._serialized_end=832
  _DYNAMIXELMOTORSTREAMSTATEREQUEST._serialized_start=834
  _DYNAMIXELMOTORSTREAMSTATEREQUEST._serialized_end=950
  _DYNAMIXELMOTORCOMMAND._serialized_start=953
  _DYNAMIXELMOTORCOMMAND._serialized_end=1212
  _DYNAMIXELMOTORINFO._serialized_start=1214
  _DYNAMIXELMOTORINFO._serialized_end=1293
  _LISTOFDYNAMIXELMOTORINFO._serialized_start=1295
  _LISTOFDYNAMIXELMOTORINFO._serialized_end=1399
  _DYNAMIXELMOTORSTATUS._serialized_start=1401
  _DYNAMIXELMOTORSTATUS._serialized_end=1423
  _DYNAMIXELMOTORSERVICE._serialized_start=1659
  _DYNAMIXELMOTORSERVICE._serialized_end=2408
# @@protoc_insertion_point(module_scope)
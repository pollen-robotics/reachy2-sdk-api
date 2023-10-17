# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: parallel_gripper.proto
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
import component_pb2 as component__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16parallel_gripper.proto\x12\x1a\x63omponent.parallel_gripper\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x0f\x63omponent.proto\"E\n\x14ParallelGripperState\x12-\n\ttimestamp\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x83\x01\n\x1bParallelGripperStateRequest\x12@\n\x06\x66ields\x18\x01 \x03(\x0e\x32\x30.component.parallel_gripper.ParallelGripperField\x12\"\n\x02id\x18\x02 \x01(\x0b\x32\x16.component.ComponentId\"w\n!ParallelGripperStreamStateRequest\x12\x44\n\x03req\x18\x01 \x01(\x0b\x32\x37.component.parallel_gripper.ParallelGripperStateRequest\x12\x0c\n\x04\x66req\x18\x02 \x01(\x02\"\x18\n\x16ParallelGripperCommand\"P\n\x13ParallelGripperInfo\x12\"\n\x02id\x18\x01 \x01(\x0b\x32\x16.component.ComponentId\x12\x15\n\rserial_number\x18\x02 \x01(\t\"k\n\x19ListOfParallelGripperInfo\x12N\n\x15parallel_gripper_info\x18\x01 \x03(\x0b\x32/.component.parallel_gripper.ParallelGripperInfo\"\x17\n\x15ParallelGripperStatus*\xe7\x01\n\x14ParallelGripperField\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04NAME\x10\x01\x12\x06\n\x02ID\x10\x02\x12\x14\n\x10PRESENT_POSITION\x10\x03\x12\x11\n\rPRESENT_SPEED\x10\x04\x12\x10\n\x0cPRESENT_LOAD\x10\x05\x12\x0f\n\x0bTEMPERATURE\x10\x06\x12\x10\n\x0c\x46ORCE_SENSOR\x10\x07\x12\r\n\tCOMPLIANT\x10\x08\x12\x11\n\rGOAL_POSITION\x10\t\x12\x0f\n\x0bSPEED_LIMIT\x10\n\x12\x10\n\x0cTORQUE_LIMIT\x10\x0b\x12\x07\n\x03PID\x10\x0c\x12\x07\n\x03\x41LL\x10\x0f\x32\xf8\x05\n\x0eGripperService\x12\x66\n\x15GetAllParallelGripper\x12\x16.google.protobuf.Empty\x1a\x35.component.parallel_gripper.ListOfParallelGripperInfo\x12u\n\x08GetState\x12\x37.component.parallel_gripper.ParallelGripperStateRequest\x1a\x30.component.parallel_gripper.ParallelGripperState\x12\x80\x01\n\x0bStreamState\x12=.component.parallel_gripper.ParallelGripperStreamStateRequest\x1a\x30.component.parallel_gripper.ParallelGripperState0\x01\x12Y\n\x0bSendCommand\x12\x32.component.parallel_gripper.ParallelGripperCommand\x1a\x16.google.protobuf.Empty\x12]\n\rStreamCommand\x12\x32.component.parallel_gripper.ParallelGripperCommand\x1a\x16.google.protobuf.Empty(\x01\x12R\n\x05\x41udit\x12\x16.component.ComponentId\x1a\x31.component.parallel_gripper.ParallelGripperStatus\x12;\n\tHeartBeat\x12\x16.component.ComponentId\x1a\x16.google.protobuf.Empty\x12\x39\n\x07Restart\x12\x16.component.ComponentId\x1a\x16.google.protobuf.Emptyb\x06proto3')

_PARALLELGRIPPERFIELD = DESCRIPTOR.enum_types_by_name['ParallelGripperField']
ParallelGripperField = enum_type_wrapper.EnumTypeWrapper(_PARALLELGRIPPERFIELD)
NONE = 0
NAME = 1
ID = 2
PRESENT_POSITION = 3
PRESENT_SPEED = 4
PRESENT_LOAD = 5
TEMPERATURE = 6
FORCE_SENSOR = 7
COMPLIANT = 8
GOAL_POSITION = 9
SPEED_LIMIT = 10
TORQUE_LIMIT = 11
PID = 12
ALL = 15


_PARALLELGRIPPERSTATE = DESCRIPTOR.message_types_by_name['ParallelGripperState']
_PARALLELGRIPPERSTATEREQUEST = DESCRIPTOR.message_types_by_name['ParallelGripperStateRequest']
_PARALLELGRIPPERSTREAMSTATEREQUEST = DESCRIPTOR.message_types_by_name['ParallelGripperStreamStateRequest']
_PARALLELGRIPPERCOMMAND = DESCRIPTOR.message_types_by_name['ParallelGripperCommand']
_PARALLELGRIPPERINFO = DESCRIPTOR.message_types_by_name['ParallelGripperInfo']
_LISTOFPARALLELGRIPPERINFO = DESCRIPTOR.message_types_by_name['ListOfParallelGripperInfo']
_PARALLELGRIPPERSTATUS = DESCRIPTOR.message_types_by_name['ParallelGripperStatus']
ParallelGripperState = _reflection.GeneratedProtocolMessageType('ParallelGripperState', (_message.Message,), {
  'DESCRIPTOR' : _PARALLELGRIPPERSTATE,
  '__module__' : 'parallel_gripper_pb2'
  # @@protoc_insertion_point(class_scope:component.parallel_gripper.ParallelGripperState)
  })
_sym_db.RegisterMessage(ParallelGripperState)

ParallelGripperStateRequest = _reflection.GeneratedProtocolMessageType('ParallelGripperStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _PARALLELGRIPPERSTATEREQUEST,
  '__module__' : 'parallel_gripper_pb2'
  # @@protoc_insertion_point(class_scope:component.parallel_gripper.ParallelGripperStateRequest)
  })
_sym_db.RegisterMessage(ParallelGripperStateRequest)

ParallelGripperStreamStateRequest = _reflection.GeneratedProtocolMessageType('ParallelGripperStreamStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _PARALLELGRIPPERSTREAMSTATEREQUEST,
  '__module__' : 'parallel_gripper_pb2'
  # @@protoc_insertion_point(class_scope:component.parallel_gripper.ParallelGripperStreamStateRequest)
  })
_sym_db.RegisterMessage(ParallelGripperStreamStateRequest)

ParallelGripperCommand = _reflection.GeneratedProtocolMessageType('ParallelGripperCommand', (_message.Message,), {
  'DESCRIPTOR' : _PARALLELGRIPPERCOMMAND,
  '__module__' : 'parallel_gripper_pb2'
  # @@protoc_insertion_point(class_scope:component.parallel_gripper.ParallelGripperCommand)
  })
_sym_db.RegisterMessage(ParallelGripperCommand)

ParallelGripperInfo = _reflection.GeneratedProtocolMessageType('ParallelGripperInfo', (_message.Message,), {
  'DESCRIPTOR' : _PARALLELGRIPPERINFO,
  '__module__' : 'parallel_gripper_pb2'
  # @@protoc_insertion_point(class_scope:component.parallel_gripper.ParallelGripperInfo)
  })
_sym_db.RegisterMessage(ParallelGripperInfo)

ListOfParallelGripperInfo = _reflection.GeneratedProtocolMessageType('ListOfParallelGripperInfo', (_message.Message,), {
  'DESCRIPTOR' : _LISTOFPARALLELGRIPPERINFO,
  '__module__' : 'parallel_gripper_pb2'
  # @@protoc_insertion_point(class_scope:component.parallel_gripper.ListOfParallelGripperInfo)
  })
_sym_db.RegisterMessage(ListOfParallelGripperInfo)

ParallelGripperStatus = _reflection.GeneratedProtocolMessageType('ParallelGripperStatus', (_message.Message,), {
  'DESCRIPTOR' : _PARALLELGRIPPERSTATUS,
  '__module__' : 'parallel_gripper_pb2'
  # @@protoc_insertion_point(class_scope:component.parallel_gripper.ParallelGripperStatus)
  })
_sym_db.RegisterMessage(ParallelGripperStatus)

_GRIPPERSERVICE = DESCRIPTOR.services_by_name['GripperService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PARALLELGRIPPERFIELD._serialized_start=702
  _PARALLELGRIPPERFIELD._serialized_end=933
  _PARALLELGRIPPERSTATE._serialized_start=133
  _PARALLELGRIPPERSTATE._serialized_end=202
  _PARALLELGRIPPERSTATEREQUEST._serialized_start=205
  _PARALLELGRIPPERSTATEREQUEST._serialized_end=336
  _PARALLELGRIPPERSTREAMSTATEREQUEST._serialized_start=338
  _PARALLELGRIPPERSTREAMSTATEREQUEST._serialized_end=457
  _PARALLELGRIPPERCOMMAND._serialized_start=459
  _PARALLELGRIPPERCOMMAND._serialized_end=483
  _PARALLELGRIPPERINFO._serialized_start=485
  _PARALLELGRIPPERINFO._serialized_end=565
  _LISTOFPARALLELGRIPPERINFO._serialized_start=567
  _LISTOFPARALLELGRIPPERINFO._serialized_end=674
  _PARALLELGRIPPERSTATUS._serialized_start=676
  _PARALLELGRIPPERSTATUS._serialized_end=699
  _GRIPPERSERVICE._serialized_start=936
  _GRIPPERSERVICE._serialized_end=1696
# @@protoc_insertion_point(module_scope)

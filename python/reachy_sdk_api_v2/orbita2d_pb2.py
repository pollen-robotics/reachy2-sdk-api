# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: orbita2d.proto
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
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import component_pb2 as component__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eorbita2d.proto\x12\x12\x63omponent.orbita2d\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x0f\x63omponent.proto\"\x98\x04\n\rOrbita2DState\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\r\x12\x35\n\x10present_position\x18\x04 \x01(\x0b\x32\x1b.component.orbita2d.Float2D\x12\x32\n\rpresent_speed\x18\x05 \x01(\x0b\x32\x1b.component.orbita2d.Float2D\x12\x31\n\x0cpresent_load\x18\x06 \x01(\x0b\x32\x1b.component.orbita2d.Float2D\x12\x30\n\x0btemperature\x18\x07 \x01(\x0b\x32\x1b.component.orbita2d.Float2D\x12-\n\tcompliant\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x32\n\rgoal_position\x18\t \x01(\x0b\x32\x1b.component.orbita2d.Float2D\x12\x30\n\x0bspeed_limit\x18\n \x01(\x0b\x32\x1b.component.orbita2d.Float2D\x12\x31\n\x0ctorque_limit\x18\x0b \x01(\x0b\x32\x1b.component.orbita2d.Float2D\x12&\n\x03pid\x18\x0c \x01(\x0b\x32\x19.component.orbita2d.PID2D\"m\n\x14Orbita2DStateRequest\x12\x31\n\x06\x66ields\x18\x01 \x03(\x0e\x32!.component.orbita2d.Orbita2DField\x12\"\n\x02id\x18\x02 \x01(\x0b\x32\x16.component.ComponentId\"a\n\x1aOrbita2DStreamStateRequest\x12\x35\n\x03req\x18\x01 \x01(\x0b\x32(.component.orbita2d.Orbita2DStateRequest\x12\x0c\n\x04\x66req\x18\x02 \x01(\x02\"]\n\x05PID2D\x12)\n\x0cgains_axis_1\x18\x01 \x01(\x0b\x32\x13.component.PIDGains\x12)\n\x0cgains_axis_2\x18\x02 \x01(\x0b\x32\x13.component.PIDGains\")\n\x07\x46loat2D\x12\x0e\n\x06\x61xis_1\x18\x01 \x01(\x02\x12\x0e\n\x06\x61xis_2\x18\x02 \x01(\x02\"\xfd\x01\n\x0fOrbita2DCommand\x12\"\n\x02id\x18\x01 \x01(\x0b\x32\x16.component.ComponentId\x12-\n\tcompliant\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x32\n\rgoal_position\x18\x03 \x01(\x0b\x32\x1b.component.orbita2d.Float2D\x12\x30\n\x0bspeed_limit\x18\x04 \x01(\x0b\x32\x1b.component.orbita2d.Float2D\x12\x31\n\x0ctorque_limit\x18\x05 \x01(\x0b\x32\x1b.component.orbita2d.Float2D\"\x9d\x01\n\x0cOrbita2DInfo\x12\"\n\x02id\x18\x01 \x01(\x0b\x32\x16.component.ComponentId\x12\x15\n\rserial_number\x18\x02 \x01(\t\x12(\n\x06\x61xis_1\x18\x03 \x01(\x0e\x32\x18.component.orbita2d.Axis\x12(\n\x06\x61xis_2\x18\x04 \x01(\x0e\x32\x18.component.orbita2d.Axis\"D\n\x12ListOfOrbita2DInfo\x12.\n\x04info\x18\x01 \x03(\x0b\x32 .component.orbita2d.Orbita2DInfo\"\x10\n\x0eOrbita2DStatus*\xdf\x01\n\rOrbita2DField\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04NAME\x10\x01\x12\x06\n\x02ID\x10\x02\x12\x14\n\x10PRESENT_POSITION\x10\x03\x12\x11\n\rPRESENT_SPEED\x10\x04\x12\x10\n\x0cPRESENT_LOAD\x10\x05\x12\x0f\n\x0bTEMPERATURE\x10\x06\x12\x0f\n\x0bJOINT_LIMIT\x10\x07\x12\r\n\tCOMPLIANT\x10\x08\x12\x11\n\rGOAL_POSITION\x10\t\x12\x0f\n\x0bSPEED_LIMIT\x10\n\x12\x10\n\x0cTORQUE_LIMIT\x10\x0b\x12\x07\n\x03PID\x10\x0c\x12\x07\n\x03\x41LL\x10\x0f*$\n\x04\x41xis\x12\x08\n\x04ROLL\x10\x00\x12\t\n\x05PITCH\x10\x01\x12\x07\n\x03YAW\x10\x02\x32\xf9\x04\n\x0fOrbita2DService\x12P\n\x0eGetAllOrbita2D\x12\x16.google.protobuf.Empty\x1a&.component.orbita2d.ListOfOrbita2DInfo\x12W\n\x08GetState\x12(.component.orbita2d.Orbita2DStateRequest\x1a!.component.orbita2d.Orbita2DState\x12\x62\n\x0bStreamState\x12..component.orbita2d.Orbita2DStreamStateRequest\x1a!.component.orbita2d.Orbita2DState0\x01\x12J\n\x0bSendCommand\x12#.component.orbita2d.Orbita2DCommand\x1a\x16.google.protobuf.Empty\x12N\n\rStreamCommand\x12#.component.orbita2d.Orbita2DCommand\x1a\x16.google.protobuf.Empty(\x01\x12\x43\n\x05\x41udit\x12\x16.component.ComponentId\x1a\".component.orbita2d.Orbita2DStatus\x12;\n\tHeartBeat\x12\x16.component.ComponentId\x1a\x16.google.protobuf.Empty\x12\x39\n\x07Restart\x12\x16.component.ComponentId\x1a\x16.google.protobuf.Emptyb\x06proto3')

_ORBITA2DFIELD = DESCRIPTOR.enum_types_by_name['Orbita2DField']
Orbita2DField = enum_type_wrapper.EnumTypeWrapper(_ORBITA2DFIELD)
_AXIS = DESCRIPTOR.enum_types_by_name['Axis']
Axis = enum_type_wrapper.EnumTypeWrapper(_AXIS)
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
ROLL = 0
PITCH = 1
YAW = 2


_ORBITA2DSTATE = DESCRIPTOR.message_types_by_name['Orbita2DState']
_ORBITA2DSTATEREQUEST = DESCRIPTOR.message_types_by_name['Orbita2DStateRequest']
_ORBITA2DSTREAMSTATEREQUEST = DESCRIPTOR.message_types_by_name['Orbita2DStreamStateRequest']
_PID2D = DESCRIPTOR.message_types_by_name['PID2D']
_FLOAT2D = DESCRIPTOR.message_types_by_name['Float2D']
_ORBITA2DCOMMAND = DESCRIPTOR.message_types_by_name['Orbita2DCommand']
_ORBITA2DINFO = DESCRIPTOR.message_types_by_name['Orbita2DInfo']
_LISTOFORBITA2DINFO = DESCRIPTOR.message_types_by_name['ListOfOrbita2DInfo']
_ORBITA2DSTATUS = DESCRIPTOR.message_types_by_name['Orbita2DStatus']
Orbita2DState = _reflection.GeneratedProtocolMessageType('Orbita2DState', (_message.Message,), {
  'DESCRIPTOR' : _ORBITA2DSTATE,
  '__module__' : 'orbita2d_pb2'
  # @@protoc_insertion_point(class_scope:component.orbita2d.Orbita2DState)
  })
_sym_db.RegisterMessage(Orbita2DState)

Orbita2DStateRequest = _reflection.GeneratedProtocolMessageType('Orbita2DStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORBITA2DSTATEREQUEST,
  '__module__' : 'orbita2d_pb2'
  # @@protoc_insertion_point(class_scope:component.orbita2d.Orbita2DStateRequest)
  })
_sym_db.RegisterMessage(Orbita2DStateRequest)

Orbita2DStreamStateRequest = _reflection.GeneratedProtocolMessageType('Orbita2DStreamStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORBITA2DSTREAMSTATEREQUEST,
  '__module__' : 'orbita2d_pb2'
  # @@protoc_insertion_point(class_scope:component.orbita2d.Orbita2DStreamStateRequest)
  })
_sym_db.RegisterMessage(Orbita2DStreamStateRequest)

PID2D = _reflection.GeneratedProtocolMessageType('PID2D', (_message.Message,), {
  'DESCRIPTOR' : _PID2D,
  '__module__' : 'orbita2d_pb2'
  # @@protoc_insertion_point(class_scope:component.orbita2d.PID2D)
  })
_sym_db.RegisterMessage(PID2D)

Float2D = _reflection.GeneratedProtocolMessageType('Float2D', (_message.Message,), {
  'DESCRIPTOR' : _FLOAT2D,
  '__module__' : 'orbita2d_pb2'
  # @@protoc_insertion_point(class_scope:component.orbita2d.Float2D)
  })
_sym_db.RegisterMessage(Float2D)

Orbita2DCommand = _reflection.GeneratedProtocolMessageType('Orbita2DCommand', (_message.Message,), {
  'DESCRIPTOR' : _ORBITA2DCOMMAND,
  '__module__' : 'orbita2d_pb2'
  # @@protoc_insertion_point(class_scope:component.orbita2d.Orbita2DCommand)
  })
_sym_db.RegisterMessage(Orbita2DCommand)

Orbita2DInfo = _reflection.GeneratedProtocolMessageType('Orbita2DInfo', (_message.Message,), {
  'DESCRIPTOR' : _ORBITA2DINFO,
  '__module__' : 'orbita2d_pb2'
  # @@protoc_insertion_point(class_scope:component.orbita2d.Orbita2DInfo)
  })
_sym_db.RegisterMessage(Orbita2DInfo)

ListOfOrbita2DInfo = _reflection.GeneratedProtocolMessageType('ListOfOrbita2DInfo', (_message.Message,), {
  'DESCRIPTOR' : _LISTOFORBITA2DINFO,
  '__module__' : 'orbita2d_pb2'
  # @@protoc_insertion_point(class_scope:component.orbita2d.ListOfOrbita2DInfo)
  })
_sym_db.RegisterMessage(ListOfOrbita2DInfo)

Orbita2DStatus = _reflection.GeneratedProtocolMessageType('Orbita2DStatus', (_message.Message,), {
  'DESCRIPTOR' : _ORBITA2DSTATUS,
  '__module__' : 'orbita2d_pb2'
  # @@protoc_insertion_point(class_scope:component.orbita2d.Orbita2DStatus)
  })
_sym_db.RegisterMessage(Orbita2DStatus)

_ORBITA2DSERVICE = DESCRIPTOR.services_by_name['Orbita2DService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ORBITA2DFIELD._serialized_start=1541
  _ORBITA2DFIELD._serialized_end=1764
  _AXIS._serialized_start=1766
  _AXIS._serialized_end=1802
  _ORBITA2DSTATE._serialized_start=150
  _ORBITA2DSTATE._serialized_end=686
  _ORBITA2DSTATEREQUEST._serialized_start=688
  _ORBITA2DSTATEREQUEST._serialized_end=797
  _ORBITA2DSTREAMSTATEREQUEST._serialized_start=799
  _ORBITA2DSTREAMSTATEREQUEST._serialized_end=896
  _PID2D._serialized_start=898
  _PID2D._serialized_end=991
  _FLOAT2D._serialized_start=993
  _FLOAT2D._serialized_end=1034
  _ORBITA2DCOMMAND._serialized_start=1037
  _ORBITA2DCOMMAND._serialized_end=1290
  _ORBITA2DINFO._serialized_start=1293
  _ORBITA2DINFO._serialized_end=1450
  _LISTOFORBITA2DINFO._serialized_start=1452
  _LISTOFORBITA2DINFO._serialized_end=1520
  _ORBITA2DSTATUS._serialized_start=1522
  _ORBITA2DSTATUS._serialized_end=1538
  _ORBITA2DSERVICE._serialized_start=1805
  _ORBITA2DSERVICE._serialized_end=2438
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: orbita3d.proto
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
import kinematics_pb2 as kinematics__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eorbita3d.proto\x12\x12\x63omponent.orbita3d\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x0f\x63omponent.proto\x1a\x10kinematics.proto\"\xdb\x04\n\rOrbita3DState\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\"\n\x02id\x18\x02 \x01(\x0b\x32\x16.component.ComponentId\x12\x37\n\x10present_position\x18\x03 \x01(\x0b\x32\x1d.reachy.kinematics.Rotation3D\x12\x33\n\rpresent_speed\x18\x04 \x01(\x0b\x32\x1c.component.orbita3d.Vector3D\x12\x32\n\x0cpresent_load\x18\x05 \x01(\x0b\x32\x1c.component.orbita3d.Vector3D\x12\x30\n\x0btemperature\x18\x06 \x01(\x0b\x32\x1b.component.orbita3d.Float3D\x12\x31\n\x0bjoint_limit\x18\x07 \x01(\x0b\x32\x1c.component.orbita3d.Limits3D\x12-\n\tcompliant\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x34\n\rgoal_position\x18\t \x01(\x0b\x32\x1d.reachy.kinematics.Rotation3D\x12\x30\n\x0bspeed_limit\x18\n \x01(\x0b\x32\x1b.component.orbita3d.Float3D\x12\x31\n\x0ctorque_limit\x18\x0b \x01(\x0b\x32\x1b.component.orbita3d.Float3D\x12&\n\x03pid\x18\x0c \x01(\x0b\x32\x19.component.orbita3d.PID3D\"m\n\x14Orbita3DStateRequest\x12\x31\n\x06\x66ields\x18\x01 \x03(\x0e\x32!.component.orbita3d.Orbita3DField\x12\"\n\x02id\x18\x02 \x01(\x0b\x32\x16.component.ComponentId\"a\n\x1aOrbita3DStreamStateRequest\x12\x35\n\x03req\x18\x01 \x01(\x0b\x32(.component.orbita3d.Orbita3DStateRequest\x12\x0c\n\x04\x66req\x18\x02 \x01(\x02\"y\n\x05PID3D\x12$\n\x07motor_1\x18\x01 \x01(\x0b\x32\x13.component.PIDGains\x12$\n\x07motor_2\x18\x02 \x01(\x0b\x32\x13.component.PIDGains\x12$\n\x07motor_3\x18\x03 \x01(\x0b\x32\x13.component.PIDGains\"|\n\x08Limits3D\x12$\n\x04roll\x18\x01 \x01(\x0b\x32\x16.component.JointLimits\x12%\n\x05pitch\x18\x02 \x01(\x0b\x32\x16.component.JointLimits\x12#\n\x03yaw\x18\x03 \x01(\x0b\x32\x16.component.JointLimits\"\x93\x01\n\x07\x46loat3D\x12,\n\x07motor_1\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12,\n\x07motor_2\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12,\n\x07motor_3\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"\x82\x01\n\x08Vector3D\x12&\n\x01x\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12&\n\x01y\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12&\n\x01z\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"\xa7\x02\n\x0fOrbita3DCommand\x12\"\n\x02id\x18\x01 \x01(\x0b\x32\x16.component.ComponentId\x12-\n\tcompliant\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x34\n\rgoal_position\x18\x03 \x01(\x0b\x32\x1d.reachy.kinematics.Rotation3D\x12\x30\n\x0bspeed_limit\x18\x04 \x01(\x0b\x32\x1b.component.orbita3d.Float3D\x12\x31\n\x0ctorque_limit\x18\x05 \x01(\x0b\x32\x1b.component.orbita3d.Float3D\x12&\n\x03pid\x18\x06 \x01(\x0b\x32\x19.component.orbita3d.PID3D\"D\n\x10Orbita3DsCommand\x12\x30\n\x03\x63md\x18\x01 \x03(\x0b\x32#.component.orbita3d.Orbita3DCommand\"E\n\x08Orbita3D\x12\"\n\x02id\x18\x01 \x01(\x0b\x32\x16.component.ComponentId\x12\x15\n\rserial_number\x18\x02 \x01(\t\"<\n\x0eListOfOrbita3D\x12*\n\x04info\x18\x01 \x03(\x0b\x32\x1c.component.orbita3d.Orbita3D\"\x10\n\x0eOrbita3DStatus*\xdf\x01\n\rOrbita3DField\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04NAME\x10\x01\x12\x06\n\x02ID\x10\x02\x12\x14\n\x10PRESENT_POSITION\x10\x03\x12\x11\n\rPRESENT_SPEED\x10\x04\x12\x10\n\x0cPRESENT_LOAD\x10\x05\x12\x0f\n\x0bTEMPERATURE\x10\x06\x12\x0f\n\x0bJOINT_LIMIT\x10\x07\x12\r\n\tCOMPLIANT\x10\x08\x12\x11\n\rGOAL_POSITION\x10\t\x12\x0f\n\x0bSPEED_LIMIT\x10\n\x12\x10\n\x0cTORQUE_LIMIT\x10\x0b\x12\x07\n\x03PID\x10\x0c\x12\x07\n\x03\x41LL\x10\x0f\x32\xf7\x04\n\x0fOrbita3DService\x12L\n\x0eGetAllOrbita3D\x12\x16.google.protobuf.Empty\x1a\".component.orbita3d.ListOfOrbita3D\x12W\n\x08GetState\x12(.component.orbita3d.Orbita3DStateRequest\x1a!.component.orbita3d.Orbita3DState\x12\x62\n\x0bStreamState\x12..component.orbita3d.Orbita3DStreamStateRequest\x1a!.component.orbita3d.Orbita3DState0\x01\x12K\n\x0bSendCommand\x12$.component.orbita3d.Orbita3DsCommand\x1a\x16.google.protobuf.Empty\x12O\n\rStreamCommand\x12$.component.orbita3d.Orbita3DsCommand\x1a\x16.google.protobuf.Empty(\x01\x12\x43\n\x05\x41udit\x12\x16.component.ComponentId\x1a\".component.orbita3d.Orbita3DStatus\x12;\n\tHeartBeat\x12\x16.component.ComponentId\x1a\x16.google.protobuf.Empty\x12\x39\n\x07Restart\x12\x16.component.ComponentId\x1a\x16.google.protobuf.Emptyb\x06proto3')

_ORBITA3DFIELD = DESCRIPTOR.enum_types_by_name['Orbita3DField']
Orbita3DField = enum_type_wrapper.EnumTypeWrapper(_ORBITA3DFIELD)
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


_ORBITA3DSTATE = DESCRIPTOR.message_types_by_name['Orbita3DState']
_ORBITA3DSTATEREQUEST = DESCRIPTOR.message_types_by_name['Orbita3DStateRequest']
_ORBITA3DSTREAMSTATEREQUEST = DESCRIPTOR.message_types_by_name['Orbita3DStreamStateRequest']
_PID3D = DESCRIPTOR.message_types_by_name['PID3D']
_LIMITS3D = DESCRIPTOR.message_types_by_name['Limits3D']
_FLOAT3D = DESCRIPTOR.message_types_by_name['Float3D']
_VECTOR3D = DESCRIPTOR.message_types_by_name['Vector3D']
_ORBITA3DCOMMAND = DESCRIPTOR.message_types_by_name['Orbita3DCommand']
_ORBITA3DSCOMMAND = DESCRIPTOR.message_types_by_name['Orbita3DsCommand']
_ORBITA3D = DESCRIPTOR.message_types_by_name['Orbita3D']
_LISTOFORBITA3D = DESCRIPTOR.message_types_by_name['ListOfOrbita3D']
_ORBITA3DSTATUS = DESCRIPTOR.message_types_by_name['Orbita3DStatus']
Orbita3DState = _reflection.GeneratedProtocolMessageType('Orbita3DState', (_message.Message,), {
  'DESCRIPTOR' : _ORBITA3DSTATE,
  '__module__' : 'orbita3d_pb2'
  # @@protoc_insertion_point(class_scope:component.orbita3d.Orbita3DState)
  })
_sym_db.RegisterMessage(Orbita3DState)

Orbita3DStateRequest = _reflection.GeneratedProtocolMessageType('Orbita3DStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORBITA3DSTATEREQUEST,
  '__module__' : 'orbita3d_pb2'
  # @@protoc_insertion_point(class_scope:component.orbita3d.Orbita3DStateRequest)
  })
_sym_db.RegisterMessage(Orbita3DStateRequest)

Orbita3DStreamStateRequest = _reflection.GeneratedProtocolMessageType('Orbita3DStreamStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORBITA3DSTREAMSTATEREQUEST,
  '__module__' : 'orbita3d_pb2'
  # @@protoc_insertion_point(class_scope:component.orbita3d.Orbita3DStreamStateRequest)
  })
_sym_db.RegisterMessage(Orbita3DStreamStateRequest)

PID3D = _reflection.GeneratedProtocolMessageType('PID3D', (_message.Message,), {
  'DESCRIPTOR' : _PID3D,
  '__module__' : 'orbita3d_pb2'
  # @@protoc_insertion_point(class_scope:component.orbita3d.PID3D)
  })
_sym_db.RegisterMessage(PID3D)

Limits3D = _reflection.GeneratedProtocolMessageType('Limits3D', (_message.Message,), {
  'DESCRIPTOR' : _LIMITS3D,
  '__module__' : 'orbita3d_pb2'
  # @@protoc_insertion_point(class_scope:component.orbita3d.Limits3D)
  })
_sym_db.RegisterMessage(Limits3D)

Float3D = _reflection.GeneratedProtocolMessageType('Float3D', (_message.Message,), {
  'DESCRIPTOR' : _FLOAT3D,
  '__module__' : 'orbita3d_pb2'
  # @@protoc_insertion_point(class_scope:component.orbita3d.Float3D)
  })
_sym_db.RegisterMessage(Float3D)

Vector3D = _reflection.GeneratedProtocolMessageType('Vector3D', (_message.Message,), {
  'DESCRIPTOR' : _VECTOR3D,
  '__module__' : 'orbita3d_pb2'
  # @@protoc_insertion_point(class_scope:component.orbita3d.Vector3D)
  })
_sym_db.RegisterMessage(Vector3D)

Orbita3DCommand = _reflection.GeneratedProtocolMessageType('Orbita3DCommand', (_message.Message,), {
  'DESCRIPTOR' : _ORBITA3DCOMMAND,
  '__module__' : 'orbita3d_pb2'
  # @@protoc_insertion_point(class_scope:component.orbita3d.Orbita3DCommand)
  })
_sym_db.RegisterMessage(Orbita3DCommand)

Orbita3DsCommand = _reflection.GeneratedProtocolMessageType('Orbita3DsCommand', (_message.Message,), {
  'DESCRIPTOR' : _ORBITA3DSCOMMAND,
  '__module__' : 'orbita3d_pb2'
  # @@protoc_insertion_point(class_scope:component.orbita3d.Orbita3DsCommand)
  })
_sym_db.RegisterMessage(Orbita3DsCommand)

Orbita3D = _reflection.GeneratedProtocolMessageType('Orbita3D', (_message.Message,), {
  'DESCRIPTOR' : _ORBITA3D,
  '__module__' : 'orbita3d_pb2'
  # @@protoc_insertion_point(class_scope:component.orbita3d.Orbita3D)
  })
_sym_db.RegisterMessage(Orbita3D)

ListOfOrbita3D = _reflection.GeneratedProtocolMessageType('ListOfOrbita3D', (_message.Message,), {
  'DESCRIPTOR' : _LISTOFORBITA3D,
  '__module__' : 'orbita3d_pb2'
  # @@protoc_insertion_point(class_scope:component.orbita3d.ListOfOrbita3D)
  })
_sym_db.RegisterMessage(ListOfOrbita3D)

Orbita3DStatus = _reflection.GeneratedProtocolMessageType('Orbita3DStatus', (_message.Message,), {
  'DESCRIPTOR' : _ORBITA3DSTATUS,
  '__module__' : 'orbita3d_pb2'
  # @@protoc_insertion_point(class_scope:component.orbita3d.Orbita3DStatus)
  })
_sym_db.RegisterMessage(Orbita3DStatus)

_ORBITA3DSERVICE = DESCRIPTOR.services_by_name['Orbita3DService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ORBITA3DFIELD._serialized_start=2035
  _ORBITA3DFIELD._serialized_end=2258
  _ORBITA3DSTATE._serialized_start=168
  _ORBITA3DSTATE._serialized_end=771
  _ORBITA3DSTATEREQUEST._serialized_start=773
  _ORBITA3DSTATEREQUEST._serialized_end=882
  _ORBITA3DSTREAMSTATEREQUEST._serialized_start=884
  _ORBITA3DSTREAMSTATEREQUEST._serialized_end=981
  _PID3D._serialized_start=983
  _PID3D._serialized_end=1104
  _LIMITS3D._serialized_start=1106
  _LIMITS3D._serialized_end=1230
  _FLOAT3D._serialized_start=1233
  _FLOAT3D._serialized_end=1380
  _VECTOR3D._serialized_start=1383
  _VECTOR3D._serialized_end=1513
  _ORBITA3DCOMMAND._serialized_start=1516
  _ORBITA3DCOMMAND._serialized_end=1811
  _ORBITA3DSCOMMAND._serialized_start=1813
  _ORBITA3DSCOMMAND._serialized_end=1881
  _ORBITA3D._serialized_start=1883
  _ORBITA3D._serialized_end=1952
  _LISTOFORBITA3D._serialized_start=1954
  _LISTOFORBITA3D._serialized_end=2014
  _ORBITA3DSTATUS._serialized_start=2016
  _ORBITA3DSTATUS._serialized_end=2032
  _ORBITA3DSERVICE._serialized_start=2261
  _ORBITA3DSERVICE._serialized_end=2892
# @@protoc_insertion_point(module_scope)

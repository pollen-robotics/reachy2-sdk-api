# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: orbita3d.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
import component_pb2 as component__pb2
import error_pb2 as error__pb2
import kinematics_pb2 as kinematics__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eorbita3d.proto\x12\x12\x63omponent.orbita3d\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x0f\x63omponent.proto\x1a\x0b\x65rror.proto\x1a\x10kinematics.proto\">\n\rOrbita3DState\x12-\n\ttimestamp\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"m\n\x14Orbita3DStateRequest\x12\x31\n\x06\x66ields\x18\x01 \x03(\x0e\x32!.component.orbita3d.Orbita3DField\x12\"\n\x02id\x18\x02 \x01(\x0b\x32\x16.component.ComponentId\"a\n\x1aOrbita3DStreamStateRequest\x12\x35\n\x03req\x18\x01 \x01(\x0b\x32(.component.orbita3d.Orbita3DStateRequest\x12\x0c\n\x04\x66req\x18\x02 \x01(\x02\"3\n\x07\x46loat3D\x12\x0c\n\x04roll\x18\x01 \x01(\x02\x12\r\n\x05pitch\x18\x02 \x01(\x02\x12\x0b\n\x03yaw\x18\x03 \x01(\x02\"\xff\x01\n\x0fOrbita3DCommand\x12\"\n\x02id\x18\x01 \x01(\x0b\x32\x16.component.ComponentId\x12-\n\tcompliant\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x34\n\rgoal_position\x18\x03 \x01(\x0b\x32\x1d.reachy.kinematics.Quaternion\x12\x30\n\x0bspeed_limit\x18\x04 \x01(\x0b\x32\x1b.component.orbita3d.Float3D\x12\x31\n\x0ctorque_limit\x18\x05 \x01(\x0b\x32\x1b.component.orbita3d.Float3D\"I\n\x0cOrbita3DInfo\x12\"\n\x02id\x18\x01 \x01(\x0b\x32\x16.component.ComponentId\x12\x15\n\rserial_number\x18\x02 \x01(\t\"D\n\x12ListOfOrbita3DInfo\x12.\n\x04info\x18\x01 \x03(\x0b\x32 .component.orbita3d.Orbita3DInfo\"W\n\x0bOrbita3DAck\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x1b\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x0c.error.Error\">\n\x0eOrbita3DStatus\x12,\n\x03\x61\x63k\x18\x01 \x01(\x0b\x32\x1f.component.orbita3d.Orbita3DAck*\xe0\x01\n\rOrbita3DField\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04NAME\x10\x01\x12\x07\n\x03UID\x10\x02\x12\x14\n\x10PRESENT_POSITION\x10\x03\x12\x11\n\rPRESENT_SPEED\x10\x04\x12\x10\n\x0cPRESENT_LOAD\x10\x05\x12\x0f\n\x0bTEMPERATURE\x10\x06\x12\x0f\n\x0bJOINT_LIMIT\x10\x07\x12\r\n\tCOMPLIANT\x10\x08\x12\x11\n\rGOAL_POSITION\x10\t\x12\x0f\n\x0bSPEED_LIMIT\x10\n\x12\x10\n\x0cTORQUE_LIMIT\x10\x0b\x12\x07\n\x03PID\x10\x0c\x12\x07\n\x03\x41LL\x10\x0f\x32\x9d\x05\n\x0fOrbita3dService\x12P\n\x0eGetAllOrbita3D\x12\x16.google.protobuf.Empty\x1a&.component.orbita3d.ListOfOrbita3DInfo\x12W\n\x08GetState\x12(.component.orbita3d.Orbita3DStateRequest\x1a!.component.orbita3d.Orbita3DState\x12\x62\n\x0bStreamState\x12..component.orbita3d.Orbita3DStreamStateRequest\x1a!.component.orbita3d.Orbita3DState0\x01\x12S\n\x0bSendCommand\x12#.component.orbita3d.Orbita3DCommand\x1a\x1f.component.orbita3d.Orbita3DAck\x12W\n\rStreamCommand\x12#.component.orbita3d.Orbita3DCommand\x1a\x1f.component.orbita3d.Orbita3DAck(\x01\x12\x43\n\x05\x41udit\x12\x16.component.ComponentId\x1a\".component.orbita3d.Orbita3DStatus\x12\x44\n\tHeartBeat\x12\x16.component.ComponentId\x1a\x1f.component.orbita3d.Orbita3DAck\x12\x42\n\x07Restart\x12\x16.component.ComponentId\x1a\x1f.component.orbita3d.Orbita3DAckb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'orbita3d_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_ORBITA3DFIELD']._serialized_start=1064
  _globals['_ORBITA3DFIELD']._serialized_end=1288
  _globals['_ORBITA3DSTATE']._serialized_start=180
  _globals['_ORBITA3DSTATE']._serialized_end=242
  _globals['_ORBITA3DSTATEREQUEST']._serialized_start=244
  _globals['_ORBITA3DSTATEREQUEST']._serialized_end=353
  _globals['_ORBITA3DSTREAMSTATEREQUEST']._serialized_start=355
  _globals['_ORBITA3DSTREAMSTATEREQUEST']._serialized_end=452
  _globals['_FLOAT3D']._serialized_start=454
  _globals['_FLOAT3D']._serialized_end=505
  _globals['_ORBITA3DCOMMAND']._serialized_start=508
  _globals['_ORBITA3DCOMMAND']._serialized_end=763
  _globals['_ORBITA3DINFO']._serialized_start=765
  _globals['_ORBITA3DINFO']._serialized_end=838
  _globals['_LISTOFORBITA3DINFO']._serialized_start=840
  _globals['_LISTOFORBITA3DINFO']._serialized_end=908
  _globals['_ORBITA3DACK']._serialized_start=910
  _globals['_ORBITA3DACK']._serialized_end=997
  _globals['_ORBITA3DSTATUS']._serialized_start=999
  _globals['_ORBITA3DSTATUS']._serialized_end=1061
  _globals['_ORBITA3DSERVICE']._serialized_start=1291
  _globals['_ORBITA3DSERVICE']._serialized_end=1960
# @@protoc_insertion_point(module_scope)

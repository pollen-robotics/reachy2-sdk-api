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
import kinematics_pb2 as kinematics__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eorbita3d.proto\x12\x12\x63omponent.orbita3d\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x0f\x63omponent.proto\x1a\x10kinematics.proto\"\xdc\x04\n\rOrbita3dState\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\"\n\x02id\x18\x02 \x01(\x0b\x32\x16.component.ComponentId\x12\x37\n\x10present_position\x18\x03 \x01(\x0b\x32\x1d.reachy.kinematics.Rotation3d\x12\x33\n\rpresent_speed\x18\x04 \x01(\x0b\x32\x1c.component.orbita3d.Vector3d\x12\x32\n\x0cpresent_load\x18\x05 \x01(\x0b\x32\x1c.component.orbita3d.Vector3d\x12\x30\n\x0btemperature\x18\x06 \x01(\x0b\x32\x1b.component.orbita3d.Float3d\x12\x32\n\x0cjoint_limits\x18\x07 \x01(\x0b\x32\x1c.component.orbita3d.Limits3d\x12-\n\tcompliant\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x34\n\rgoal_position\x18\t \x01(\x0b\x32\x1d.reachy.kinematics.Rotation3d\x12\x30\n\x0bspeed_limit\x18\n \x01(\x0b\x32\x1b.component.orbita3d.Float3d\x12\x31\n\x0ctorque_limit\x18\x0b \x01(\x0b\x32\x1b.component.orbita3d.Float3d\x12&\n\x03pid\x18\x0c \x01(\x0b\x32\x19.component.orbita3d.PID3d\"m\n\x14Orbita3dStateRequest\x12\x31\n\x06\x66ields\x18\x01 \x03(\x0e\x32!.component.orbita3d.Orbita3dField\x12\"\n\x02id\x18\x02 \x01(\x0b\x32\x16.component.ComponentId\"a\n\x1aOrbita3dStreamStateRequest\x12\x35\n\x03req\x18\x01 \x01(\x0b\x32(.component.orbita3d.Orbita3dStateRequest\x12\x0c\n\x04\x66req\x18\x02 \x01(\x02\"y\n\x05PID3d\x12$\n\x07motor_1\x18\x01 \x01(\x0b\x32\x13.component.PIDGains\x12$\n\x07motor_2\x18\x02 \x01(\x0b\x32\x13.component.PIDGains\x12$\n\x07motor_3\x18\x03 \x01(\x0b\x32\x13.component.PIDGains\"|\n\x08Limits3d\x12$\n\x04roll\x18\x01 \x01(\x0b\x32\x16.component.JointLimits\x12%\n\x05pitch\x18\x02 \x01(\x0b\x32\x16.component.JointLimits\x12#\n\x03yaw\x18\x03 \x01(\x0b\x32\x16.component.JointLimits\"\x93\x01\n\x07\x46loat3d\x12,\n\x07motor_1\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12,\n\x07motor_2\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12,\n\x07motor_3\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"\x82\x01\n\x08Vector3d\x12&\n\x01x\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12&\n\x01y\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12&\n\x01z\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"\xa7\x02\n\x0fOrbita3dCommand\x12\"\n\x02id\x18\x01 \x01(\x0b\x32\x16.component.ComponentId\x12-\n\tcompliant\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x34\n\rgoal_position\x18\x03 \x01(\x0b\x32\x1d.reachy.kinematics.Rotation3d\x12\x30\n\x0bspeed_limit\x18\x04 \x01(\x0b\x32\x1b.component.orbita3d.Float3d\x12\x31\n\x0ctorque_limit\x18\x05 \x01(\x0b\x32\x1b.component.orbita3d.Float3d\x12&\n\x03pid\x18\x06 \x01(\x0b\x32\x19.component.orbita3d.PID3d\"D\n\x10Orbita3dsCommand\x12\x30\n\x03\x63md\x18\x01 \x03(\x0b\x32#.component.orbita3d.Orbita3dCommand\"\x92\x01\n\x0cOrbita3dGoal\x12\"\n\x02id\x18\x01 \x01(\x0b\x32\x16.component.ComponentId\x12/\n\x08rotation\x18\x02 \x01(\x0b\x32\x1d.reachy.kinematics.Rotation3d\x12-\n\x08\x64uration\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"E\n\x08Orbita3d\x12\"\n\x02id\x18\x01 \x01(\x0b\x32\x16.component.ComponentId\x12\x15\n\rserial_number\x18\x02 \x01(\t\"<\n\x0eListOfOrbita3d\x12*\n\x04info\x18\x01 \x03(\x0b\x32\x1c.component.orbita3d.Orbita3d\"\x10\n\x0eOrbita3dStatus*\xe0\x01\n\rOrbita3dField\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04NAME\x10\x01\x12\x06\n\x02ID\x10\x02\x12\x14\n\x10PRESENT_POSITION\x10\x03\x12\x11\n\rPRESENT_SPEED\x10\x04\x12\x10\n\x0cPRESENT_LOAD\x10\x05\x12\x0f\n\x0bTEMPERATURE\x10\x06\x12\x10\n\x0cJOINT_LIMITS\x10\x07\x12\r\n\tCOMPLIANT\x10\x08\x12\x11\n\rGOAL_POSITION\x10\t\x12\x0f\n\x0bSPEED_LIMIT\x10\n\x12\x10\n\x0cTORQUE_LIMIT\x10\x0b\x12\x07\n\x03PID\x10\x0c\x12\x07\n\x03\x41LL\x10\x0f\x32\xc4\x05\n\x0fOrbita3dService\x12L\n\x0eGetAllOrbita3d\x12\x16.google.protobuf.Empty\x1a\".component.orbita3d.ListOfOrbita3d\x12W\n\x08GetState\x12(.component.orbita3d.Orbita3dStateRequest\x1a!.component.orbita3d.Orbita3dState\x12\x62\n\x0bStreamState\x12..component.orbita3d.Orbita3dStreamStateRequest\x1a!.component.orbita3d.Orbita3dState0\x01\x12K\n\x0fGoToOrientation\x12 .component.orbita3d.Orbita3dGoal\x1a\x16.google.protobuf.Empty\x12K\n\x0bSendCommand\x12$.component.orbita3d.Orbita3dsCommand\x1a\x16.google.protobuf.Empty\x12O\n\rStreamCommand\x12$.component.orbita3d.Orbita3dsCommand\x1a\x16.google.protobuf.Empty(\x01\x12\x43\n\x05\x41udit\x12\x16.component.ComponentId\x1a\".component.orbita3d.Orbita3dStatus\x12;\n\tHeartBeat\x12\x16.component.ComponentId\x1a\x16.google.protobuf.Empty\x12\x39\n\x07Restart\x12\x16.component.ComponentId\x1a\x16.google.protobuf.Emptyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'orbita3d_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ORBITA3DFIELD']._serialized_start=2185
  _globals['_ORBITA3DFIELD']._serialized_end=2409
  _globals['_ORBITA3DSTATE']._serialized_start=168
  _globals['_ORBITA3DSTATE']._serialized_end=772
  _globals['_ORBITA3DSTATEREQUEST']._serialized_start=774
  _globals['_ORBITA3DSTATEREQUEST']._serialized_end=883
  _globals['_ORBITA3DSTREAMSTATEREQUEST']._serialized_start=885
  _globals['_ORBITA3DSTREAMSTATEREQUEST']._serialized_end=982
  _globals['_PID3D']._serialized_start=984
  _globals['_PID3D']._serialized_end=1105
  _globals['_LIMITS3D']._serialized_start=1107
  _globals['_LIMITS3D']._serialized_end=1231
  _globals['_FLOAT3D']._serialized_start=1234
  _globals['_FLOAT3D']._serialized_end=1381
  _globals['_VECTOR3D']._serialized_start=1384
  _globals['_VECTOR3D']._serialized_end=1514
  _globals['_ORBITA3DCOMMAND']._serialized_start=1517
  _globals['_ORBITA3DCOMMAND']._serialized_end=1812
  _globals['_ORBITA3DSCOMMAND']._serialized_start=1814
  _globals['_ORBITA3DSCOMMAND']._serialized_end=1882
  _globals['_ORBITA3DGOAL']._serialized_start=1885
  _globals['_ORBITA3DGOAL']._serialized_end=2031
  _globals['_ORBITA3D']._serialized_start=2033
  _globals['_ORBITA3D']._serialized_end=2102
  _globals['_LISTOFORBITA3D']._serialized_start=2104
  _globals['_LISTOFORBITA3D']._serialized_end=2164
  _globals['_ORBITA3DSTATUS']._serialized_start=2166
  _globals['_ORBITA3DSTATUS']._serialized_end=2182
  _globals['_ORBITA3DSERVICE']._serialized_start=2412
  _globals['_ORBITA3DSERVICE']._serialized_end=3120
# @@protoc_insertion_point(module_scope)

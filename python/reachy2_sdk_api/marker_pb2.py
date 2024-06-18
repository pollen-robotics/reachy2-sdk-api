# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: marker.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
import kinematics_pb2 as kinematics__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cmarker.proto\x12\x14reachy.utils.markers\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x10kinematics.proto\"\x89\x02\n\x06Marker\x12.\n\x04pose\x18\x01 \x01(\x0b\x32 .reachy.utils.markers.MarkerPose\x12\x30\n\x05\x63olor\x18\x02 \x01(\x0b\x32!.reachy.utils.markers.MarkerColor\x12\x30\n\x05shape\x18\x03 \x01(\x0e\x32!.reachy.utils.markers.MarkerShape\x12\n\n\x02id\x18\x04 \x01(\x05\x12\x30\n\x05scale\x18\x05 \x01(\x0b\x32!.reachy.utils.markers.MarkerScale\x12-\n\x08lifetime\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"<\n\x0bMarkerArray\x12-\n\x07markers\x18\x01 \x03(\x0b\x32\x1c.reachy.utils.markers.Marker\"\xad\x01\n\x0bMarkerColor\x12&\n\x01r\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12&\n\x01g\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12&\n\x01\x62\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12&\n\x01\x61\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"l\n\nMarkerPose\x12*\n\x08position\x18\x01 \x01(\x0b\x32\x18.reachy.kinematics.Point\x12\x32\n\x0borientation\x18\x02 \x01(\x0b\x32\x1d.reachy.kinematics.Quaternion\"\x85\x01\n\x0bMarkerScale\x12&\n\x01x\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12&\n\x01y\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12&\n\x01z\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValue*\x83\x02\n\x0bMarkerShape\x12\t\n\x05\x41RROW\x10\x00\x12\x08\n\x04\x43UBE\x10\x01\x12\n\n\x06SPHERE\x10\x02\x12\x0c\n\x08\x43YLINDER\x10\x03\x12\x0e\n\nLINE_STRIP\x10\x04\x12\r\n\tLINE_LIST\x10\x05\x12\r\n\tCUBE_LIST\x10\x06\x12\x0f\n\x0bSPHERE_LIST\x10\x07\x12\n\n\x06POINTS\x10\x08\x12\x14\n\x10TEXT_VIEW_FACING\x10\t\x12\x11\n\rMESH_RESOURCE\x10\n\x12\x11\n\rTRIANGLE_LIST\x10\x0b\x12\x07\n\x03\x41\x44\x44\x10\x0c\x12\n\n\x06MODIFY\x10\r\x12\n\n\x06\x44\x45LETE\x10\x0e\x12\r\n\tDELETEALL\x10\x0f\x12\x0e\n\nGRASP_FORK\x10\x10\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'marker_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MARKERSHAPE']._serialized_start=841
  _globals['_MARKERSHAPE']._serialized_end=1100
  _globals['_MARKER']._serialized_start=89
  _globals['_MARKER']._serialized_end=354
  _globals['_MARKERARRAY']._serialized_start=356
  _globals['_MARKERARRAY']._serialized_end=416
  _globals['_MARKERCOLOR']._serialized_start=419
  _globals['_MARKERCOLOR']._serialized_end=592
  _globals['_MARKERPOSE']._serialized_start=594
  _globals['_MARKERPOSE']._serialized_end=702
  _globals['_MARKERSCALE']._serialized_start=705
  _globals['_MARKERSCALE']._serialized_end=838
# @@protoc_insertion_point(module_scope)

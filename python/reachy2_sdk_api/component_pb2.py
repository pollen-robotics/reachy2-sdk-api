# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: component.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x63omponent.proto\x12\tcomponent\x1a\x1egoogle/protobuf/wrappers.proto\"\'\n\x0b\x43omponentId\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x82\x01\n\x08PIDGains\x12&\n\x01p\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12&\n\x01i\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12&\n\x01\x64\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"a\n\x0bJointLimits\x12(\n\x03min\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12(\n\x03max\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.FloatValueb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_COMPONENTID']._serialized_start=62
  _globals['_COMPONENTID']._serialized_end=101
  _globals['_PIDGAINS']._serialized_start=104
  _globals['_PIDGAINS']._serialized_end=234
  _globals['_JOINTLIMITS']._serialized_start=236
  _globals['_JOINTLIMITS']._serialized_end=333
# @@protoc_insertion_point(module_scope)

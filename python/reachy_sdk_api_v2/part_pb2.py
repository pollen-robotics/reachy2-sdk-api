# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: part.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\npart.proto\x12\x0breachy.part\"\"\n\x06PartId\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\"M\n\x08PartInfo\x12\x15\n\rserial_number\x18\x01 \x01(\t\x12\x14\n\x0cversion_hard\x18\x02 \x01(\t\x12\x14\n\x0cversion_soft\x18\x03 \x01(\tb\x06proto3')



_PARTID = DESCRIPTOR.message_types_by_name['PartId']
_PARTINFO = DESCRIPTOR.message_types_by_name['PartInfo']
PartId = _reflection.GeneratedProtocolMessageType('PartId', (_message.Message,), {
  'DESCRIPTOR' : _PARTID,
  '__module__' : 'part_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.PartId)
  })
_sym_db.RegisterMessage(PartId)

PartInfo = _reflection.GeneratedProtocolMessageType('PartInfo', (_message.Message,), {
  'DESCRIPTOR' : _PARTINFO,
  '__module__' : 'part_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.PartInfo)
  })
_sym_db.RegisterMessage(PartInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PARTID._serialized_start=27
  _PARTID._serialized_end=61
  _PARTINFO._serialized_start=63
  _PARTINFO._serialized_end=140
# @@protoc_insertion_point(module_scope)

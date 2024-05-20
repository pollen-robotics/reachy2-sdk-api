# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: reachy.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import arm_pb2 as arm__pb2
import head_pb2 as head__pb2
import hand_pb2 as hand__pb2
import mobile_base_utility_pb2 as mobile__base__utility__pb2
import sound_pb2 as sound__pb2
import video_pb2 as video__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0creachy.proto\x12\x06reachy\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\tarm.proto\x1a\nhead.proto\x1a\nhand.proto\x1a\x19mobile_base_utility.proto\x1a\x0bsound.proto\x1a\x0bvideo.proto\"\x9a\x03\n\x06Reachy\x12\x1c\n\x02id\x18\x01 \x01(\x0b\x32\x10.reachy.ReachyId\x12#\n\x05l_arm\x18\x02 \x01(\x0b\x32\x14.reachy.part.arm.Arm\x12#\n\x05r_arm\x18\x03 \x01(\x0b\x32\x14.reachy.part.arm.Arm\x12$\n\x04head\x18\x04 \x01(\x0b\x32\x16.reachy.part.head.Head\x12&\n\x06l_hand\x18\x05 \x01(\x0b\x32\x16.reachy.part.hand.Hand\x12&\n\x06r_hand\x18\x06 \x01(\x0b\x32\x16.reachy.part.hand.Hand\x12\x34\n\x0bmobile_base\x18\x07 \x01(\x0b\x32\x1f.mobile.base.utility.MobileBase\x12/\n\nmicrophone\x18\x08 \x01(\x0b\x32\x1b.component.sound.Microphone\x12)\n\x07speaker\x18\t \x01(\x0b\x32\x18.component.sound.Speaker\x12 \n\x04info\x18\x14 \x01(\x0b\x32\x12.reachy.ReachyInfo\"$\n\x08ReachyId\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\"O\n\nReachyInfo\x12\x15\n\rserial_number\x18\x01 \x01(\t\x12\x14\n\x0cversion_hard\x18\x02 \x01(\t\x12\x14\n\x0cversion_soft\x18\x03 \x01(\t\"\x92\x03\n\x0bReachyState\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1c\n\x02id\x18\x02 \x01(\x0b\x32\x10.reachy.ReachyId\x12.\n\x0bl_arm_state\x18\x03 \x01(\x0b\x32\x19.reachy.part.arm.ArmState\x12.\n\x0br_arm_state\x18\x04 \x01(\x0b\x32\x19.reachy.part.arm.ArmState\x12/\n\nhead_state\x18\x05 \x01(\x0b\x32\x1b.reachy.part.head.HeadState\x12\x31\n\x0cl_hand_state\x18\x06 \x01(\x0b\x32\x1b.reachy.part.hand.HandState\x12\x31\n\x0cr_hand_state\x18\x07 \x01(\x0b\x32\x1b.reachy.part.hand.HandState\x12?\n\x11mobile_base_state\x18\x08 \x01(\x0b\x32$.mobile.base.utility.MobileBaseState\"S\n\x18ReachyStreamStateRequest\x12\x1c\n\x02id\x18\x01 \x01(\x0b\x32\x10.reachy.ReachyId\x12\x19\n\x11publish_frequency\x18\x02 \x01(\x02\x32\xcb\x01\n\rReachyService\x12\x33\n\tGetReachy\x12\x16.google.protobuf.Empty\x1a\x0e.reachy.Reachy\x12\x37\n\x0eGetReachyState\x12\x10.reachy.ReachyId\x1a\x13.reachy.ReachyState\x12L\n\x11StreamReachyState\x12 .reachy.ReachyStreamStateRequest\x1a\x13.reachy.ReachyState0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'reachy_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_REACHY']._serialized_start=175
  _globals['_REACHY']._serialized_end=585
  _globals['_REACHYID']._serialized_start=587
  _globals['_REACHYID']._serialized_end=623
  _globals['_REACHYINFO']._serialized_start=625
  _globals['_REACHYINFO']._serialized_end=704
  _globals['_REACHYSTATE']._serialized_start=707
  _globals['_REACHYSTATE']._serialized_end=1109
  _globals['_REACHYSTREAMSTATEREQUEST']._serialized_start=1111
  _globals['_REACHYSTREAMSTATEREQUEST']._serialized_end=1194
  _globals['_REACHYSERVICE']._serialized_start=1197
  _globals['_REACHYSERVICE']._serialized_end=1400
# @@protoc_insertion_point(module_scope)

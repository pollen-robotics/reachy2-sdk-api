# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hand.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import error_pb2 as error__pb2
import part_pb2 as part__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nhand.proto\x12\x10reachy.part.hand\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x0b\x65rror.proto\x1a\npart.proto\"Q\n\x04Hand\x12$\n\x07part_id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12#\n\x04info\x18\x05 \x01(\x0b\x32\x15.reachy.part.PartInfo\"2\n\nListOfHand\x12$\n\x04hand\x18\x01 \x03(\x0b\x32\x16.reachy.part.hand.Hand\"\xaa\x03\n\tHandState\x12,\n\x07opening\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12*\n\x05\x66orce\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x32\n\x0eholding_object\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x35\n\rjoints_limits\x18\x04 \x01(\x0b\x32\x1e.reachy.part.hand.JointsLimits\x12\x38\n\x0ctemperatures\x18\x05 \x01(\x0b\x32\".reachy.part.hand.HandTemperatures\x12\x38\n\x10present_position\x18\x06 \x01(\x0b\x32\x1e.reachy.part.hand.HandPosition\x12\x35\n\rgoal_position\x18\x07 \x01(\x0b\x32\x1e.reachy.part.hand.HandPosition\x12-\n\tcompliant\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"*\n\nHandStatus\x12\x1c\n\x06\x65rrors\x18\x01 \x03(\x0b\x32\x0c.error.Error\"\x07\n\x05\x46orce\"\'\n\x0bJointLimits\x12\x0b\n\x03min\x18\x01 \x01(\x02\x12\x0b\n\x03max\x18\x02 \x01(\x02\"F\n\x15ParallelGripperLimits\x12-\n\x06limits\x18\x01 \x01(\x0b\x32\x1d.reachy.part.hand.JointLimits\"]\n\x0cJointsLimits\x12\x43\n\x10parallel_gripper\x18\x01 \x01(\x0b\x32\'.reachy.part.hand.ParallelGripperLimitsH\x00\x42\x08\n\x06limits\"\x99\x01\n\x17ParallelGripperPosition\x12\x39\n\x12opening_percentage\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.FloatValueH\x00\x12/\n\x08position\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.FloatValueH\x00\x42\x12\n\x10gripper_position\"a\n\x0cHandPosition\x12\x45\n\x10parallel_gripper\x18\x01 \x01(\x0b\x32).reachy.part.hand.ParallelGripperPositionH\x00\x42\n\n\x08position\"h\n\x13HandPositionRequest\x12\x1f\n\x02id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12\x30\n\x08position\x18\x02 \x01(\x0b\x32\x1e.reachy.part.hand.HandPosition\"-\n\x0cTemperatures\x12\r\n\x05motor\x18\x01 \x01(\x02\x12\x0e\n\x06\x64river\x18\x02 \x01(\x02\"Q\n\x1aParallelGripperTemperature\x12\x33\n\x0btemperature\x18\x01 \x01(\x0b\x32\x1e.reachy.part.hand.Temperatures\"^\n\x10HandTemperatures\x12:\n\x10parallel_gripper\x18\x01 \x01(\x0b\x32\x1e.reachy.part.hand.TemperaturesH\x00\x42\x0e\n\x0ctemperatures\"a\n\x11SpeedLimitRequest\x12\x1f\n\x02id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12+\n\x05limit\x18\x02 \x01(\x0e\x32\x1c.reachy.part.hand.SpeedLimit*:\n\nSpeedLimit\x12\x0c\n\x08NO_LIMIT\x10\x00\x12\x08\n\x04\x46\x41ST\x10\x01\x12\n\n\x06NORMAL\x10\x02\x12\x08\n\x04SLOW\x10\x03\x32\x9a\x08\n\x0bHandService\x12\x43\n\x0bGetAllHands\x12\x16.google.protobuf.Empty\x1a\x1c.reachy.part.hand.ListOfHand\x12<\n\x08GetState\x12\x13.reachy.part.PartId\x1a\x1b.reachy.part.hand.HandState\x12\x37\n\x08OpenHand\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x38\n\tCloseHand\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12:\n\x05\x41udit\x12\x13.reachy.part.PartId\x1a\x1c.reachy.part.hand.HandStatus\x12\x38\n\tHeartBeat\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x36\n\x07Restart\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x41\n\x12ResetDefaultValues\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x35\n\x06TurnOn\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x36\n\x07TurnOff\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x44\n\rGetJointLimit\x12\x13.reachy.part.PartId\x1a\x1e.reachy.part.hand.JointsLimits\x12I\n\x0eGetTemperature\x12\x13.reachy.part.PartId\x1a\".reachy.part.hand.HandTemperatures\x12J\n\x13GetHandGoalPosition\x12\x13.reachy.part.PartId\x1a\x1e.reachy.part.hand.HandPosition\x12L\n\rSetSpeedLimit\x12#.reachy.part.hand.SpeedLimitRequest\x1a\x16.google.protobuf.Empty\x12P\n\x0fSetHandPosition\x12%.reachy.part.hand.HandPositionRequest\x1a\x16.google.protobuf.Empty\x12\x38\n\x08GetForce\x12\x13.reachy.part.PartId\x1a\x17.reachy.part.hand.Forceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hand_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SPEEDLIMIT']._serialized_start=1629
  _globals['_SPEEDLIMIT']._serialized_end=1687
  _globals['_HAND']._serialized_start=118
  _globals['_HAND']._serialized_end=199
  _globals['_LISTOFHAND']._serialized_start=201
  _globals['_LISTOFHAND']._serialized_end=251
  _globals['_HANDSTATE']._serialized_start=254
  _globals['_HANDSTATE']._serialized_end=680
  _globals['_HANDSTATUS']._serialized_start=682
  _globals['_HANDSTATUS']._serialized_end=724
  _globals['_FORCE']._serialized_start=726
  _globals['_FORCE']._serialized_end=733
  _globals['_JOINTLIMITS']._serialized_start=735
  _globals['_JOINTLIMITS']._serialized_end=774
  _globals['_PARALLELGRIPPERLIMITS']._serialized_start=776
  _globals['_PARALLELGRIPPERLIMITS']._serialized_end=846
  _globals['_JOINTSLIMITS']._serialized_start=848
  _globals['_JOINTSLIMITS']._serialized_end=941
  _globals['_PARALLELGRIPPERPOSITION']._serialized_start=944
  _globals['_PARALLELGRIPPERPOSITION']._serialized_end=1097
  _globals['_HANDPOSITION']._serialized_start=1099
  _globals['_HANDPOSITION']._serialized_end=1196
  _globals['_HANDPOSITIONREQUEST']._serialized_start=1198
  _globals['_HANDPOSITIONREQUEST']._serialized_end=1302
  _globals['_TEMPERATURES']._serialized_start=1304
  _globals['_TEMPERATURES']._serialized_end=1349
  _globals['_PARALLELGRIPPERTEMPERATURE']._serialized_start=1351
  _globals['_PARALLELGRIPPERTEMPERATURE']._serialized_end=1432
  _globals['_HANDTEMPERATURES']._serialized_start=1434
  _globals['_HANDTEMPERATURES']._serialized_end=1528
  _globals['_SPEEDLIMITREQUEST']._serialized_start=1530
  _globals['_SPEEDLIMITREQUEST']._serialized_end=1627
  _globals['_HANDSERVICE']._serialized_start=1690
  _globals['_HANDSERVICE']._serialized_end=2740
# @@protoc_insertion_point(module_scope)

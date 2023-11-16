# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hand.proto
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
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import part_pb2 as part__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nhand.proto\x12\x10reachy.part.hand\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\npart.proto\"Q\n\x04Hand\x12$\n\x07part_id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12#\n\x04info\x18\x05 \x01(\x0b\x32\x15.reachy.part.PartInfo\"2\n\nListOfHand\x12$\n\x04hand\x18\x01 \x03(\x0b\x32\x16.reachy.part.hand.Hand\"\xfb\x02\n\tHandState\x12,\n\x07opening\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12*\n\x05\x66orce\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x32\n\x0eholding_object\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x35\n\rjoints_limits\x18\x04 \x01(\x0b\x32\x1e.reachy.part.hand.JointsLimits\x12\x38\n\x0ctemperatures\x18\x05 \x01(\x0b\x32\".reachy.part.hand.HandTemperatures\x12\x38\n\x10present_position\x18\x06 \x01(\x0b\x32\x1e.reachy.part.hand.HandPosition\x12\x35\n\rgoal_position\x18\x07 \x01(\x0b\x32\x1e.reachy.part.hand.HandPosition\"\x0c\n\nHandStatus\"\x07\n\x05\x46orce\"\'\n\x0bJointLimits\x12\x0b\n\x03min\x18\x01 \x01(\x02\x12\x0b\n\x03max\x18\x02 \x01(\x02\"F\n\x15ParallelGripperLimits\x12-\n\x06limits\x18\x01 \x01(\x0b\x32\x1d.reachy.part.hand.JointLimits\"]\n\x0cJointsLimits\x12\x43\n\x10parallel_gripper\x18\x01 \x01(\x0b\x32\'.reachy.part.hand.ParallelGripperLimitsH\x00\x42\x08\n\x06limits\"+\n\x17ParallelGripperPosition\x12\x10\n\x08position\x18\x01 \x01(\x02\"a\n\x0cHandPosition\x12\x45\n\x10parallel_gripper\x18\x01 \x01(\x0b\x32).reachy.part.hand.ParallelGripperPositionH\x00\x42\n\n\x08position\"-\n\x0cTemperatures\x12\r\n\x05motor\x18\x01 \x01(\x02\x12\x0e\n\x06\x64river\x18\x02 \x01(\x02\"Q\n\x1aParallelGripperTemperature\x12\x33\n\x0btemperature\x18\x01 \x01(\x0b\x32\x1e.reachy.part.hand.Temperatures\"^\n\x10HandTemperatures\x12:\n\x10parallel_gripper\x18\x01 \x01(\x0b\x32\x1e.reachy.part.hand.TemperaturesH\x00\x42\x0e\n\x0ctemperatures\"a\n\x11SpeedLimitRequest\x12\x1f\n\x02id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12+\n\x05limit\x18\x02 \x01(\x0e\x32\x1c.reachy.part.hand.SpeedLimit*:\n\nSpeedLimit\x12\x0c\n\x08NO_LIMIT\x10\x00\x12\x08\n\x04\x46\x41ST\x10\x01\x12\n\n\x06NORMAL\x10\x02\x12\x08\n\x04SLOW\x10\x03\x32\x97\x08\n\x0bHandService\x12\x43\n\x0bGetAllHands\x12\x16.google.protobuf.Empty\x1a\x1c.reachy.part.hand.ListOfHand\x12@\n\x0cGetHandState\x12\x13.reachy.part.PartId\x1a\x1b.reachy.part.hand.HandState\x12\x37\n\x08OpenHand\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x38\n\tCloseHand\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12:\n\x05\x41udit\x12\x13.reachy.part.PartId\x1a\x1c.reachy.part.hand.HandStatus\x12\x38\n\tHeartBeat\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x36\n\x07Restart\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x41\n\x12ResetDefaultValues\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x35\n\x06TurnOn\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x36\n\x07TurnOff\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12\x44\n\rGetJointLimit\x12\x13.reachy.part.PartId\x1a\x1e.reachy.part.hand.JointsLimits\x12I\n\x0eGetTemperature\x12\x13.reachy.part.PartId\x1a\".reachy.part.hand.HandTemperatures\x12J\n\x13GetHandGoalPosition\x12\x13.reachy.part.PartId\x1a\x1e.reachy.part.hand.HandPosition\x12L\n\rSetSpeedLimit\x12#.reachy.part.hand.SpeedLimitRequest\x1a\x16.google.protobuf.Empty\x12I\n\x0fSetHandPosition\x12\x1e.reachy.part.hand.HandPosition\x1a\x16.google.protobuf.Empty\x12\x38\n\x08GetForce\x12\x13.reachy.part.PartId\x1a\x17.reachy.part.hand.Forceb\x06proto3')

_SPEEDLIMIT = DESCRIPTOR.enum_types_by_name['SpeedLimit']
SpeedLimit = enum_type_wrapper.EnumTypeWrapper(_SPEEDLIMIT)
NO_LIMIT = 0
FAST = 1
NORMAL = 2
SLOW = 3


_HAND = DESCRIPTOR.message_types_by_name['Hand']
_LISTOFHAND = DESCRIPTOR.message_types_by_name['ListOfHand']
_HANDSTATE = DESCRIPTOR.message_types_by_name['HandState']
_HANDSTATUS = DESCRIPTOR.message_types_by_name['HandStatus']
_FORCE = DESCRIPTOR.message_types_by_name['Force']
_JOINTLIMITS = DESCRIPTOR.message_types_by_name['JointLimits']
_PARALLELGRIPPERLIMITS = DESCRIPTOR.message_types_by_name['ParallelGripperLimits']
_JOINTSLIMITS = DESCRIPTOR.message_types_by_name['JointsLimits']
_PARALLELGRIPPERPOSITION = DESCRIPTOR.message_types_by_name['ParallelGripperPosition']
_HANDPOSITION = DESCRIPTOR.message_types_by_name['HandPosition']
_TEMPERATURES = DESCRIPTOR.message_types_by_name['Temperatures']
_PARALLELGRIPPERTEMPERATURE = DESCRIPTOR.message_types_by_name['ParallelGripperTemperature']
_HANDTEMPERATURES = DESCRIPTOR.message_types_by_name['HandTemperatures']
_SPEEDLIMITREQUEST = DESCRIPTOR.message_types_by_name['SpeedLimitRequest']
Hand = _reflection.GeneratedProtocolMessageType('Hand', (_message.Message,), {
  'DESCRIPTOR' : _HAND,
  '__module__' : 'hand_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.hand.Hand)
  })
_sym_db.RegisterMessage(Hand)

ListOfHand = _reflection.GeneratedProtocolMessageType('ListOfHand', (_message.Message,), {
  'DESCRIPTOR' : _LISTOFHAND,
  '__module__' : 'hand_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.hand.ListOfHand)
  })
_sym_db.RegisterMessage(ListOfHand)

HandState = _reflection.GeneratedProtocolMessageType('HandState', (_message.Message,), {
  'DESCRIPTOR' : _HANDSTATE,
  '__module__' : 'hand_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.hand.HandState)
  })
_sym_db.RegisterMessage(HandState)

HandStatus = _reflection.GeneratedProtocolMessageType('HandStatus', (_message.Message,), {
  'DESCRIPTOR' : _HANDSTATUS,
  '__module__' : 'hand_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.hand.HandStatus)
  })
_sym_db.RegisterMessage(HandStatus)

Force = _reflection.GeneratedProtocolMessageType('Force', (_message.Message,), {
  'DESCRIPTOR' : _FORCE,
  '__module__' : 'hand_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.hand.Force)
  })
_sym_db.RegisterMessage(Force)

JointLimits = _reflection.GeneratedProtocolMessageType('JointLimits', (_message.Message,), {
  'DESCRIPTOR' : _JOINTLIMITS,
  '__module__' : 'hand_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.hand.JointLimits)
  })
_sym_db.RegisterMessage(JointLimits)

ParallelGripperLimits = _reflection.GeneratedProtocolMessageType('ParallelGripperLimits', (_message.Message,), {
  'DESCRIPTOR' : _PARALLELGRIPPERLIMITS,
  '__module__' : 'hand_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.hand.ParallelGripperLimits)
  })
_sym_db.RegisterMessage(ParallelGripperLimits)

JointsLimits = _reflection.GeneratedProtocolMessageType('JointsLimits', (_message.Message,), {
  'DESCRIPTOR' : _JOINTSLIMITS,
  '__module__' : 'hand_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.hand.JointsLimits)
  })
_sym_db.RegisterMessage(JointsLimits)

ParallelGripperPosition = _reflection.GeneratedProtocolMessageType('ParallelGripperPosition', (_message.Message,), {
  'DESCRIPTOR' : _PARALLELGRIPPERPOSITION,
  '__module__' : 'hand_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.hand.ParallelGripperPosition)
  })
_sym_db.RegisterMessage(ParallelGripperPosition)

HandPosition = _reflection.GeneratedProtocolMessageType('HandPosition', (_message.Message,), {
  'DESCRIPTOR' : _HANDPOSITION,
  '__module__' : 'hand_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.hand.HandPosition)
  })
_sym_db.RegisterMessage(HandPosition)

Temperatures = _reflection.GeneratedProtocolMessageType('Temperatures', (_message.Message,), {
  'DESCRIPTOR' : _TEMPERATURES,
  '__module__' : 'hand_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.hand.Temperatures)
  })
_sym_db.RegisterMessage(Temperatures)

ParallelGripperTemperature = _reflection.GeneratedProtocolMessageType('ParallelGripperTemperature', (_message.Message,), {
  'DESCRIPTOR' : _PARALLELGRIPPERTEMPERATURE,
  '__module__' : 'hand_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.hand.ParallelGripperTemperature)
  })
_sym_db.RegisterMessage(ParallelGripperTemperature)

HandTemperatures = _reflection.GeneratedProtocolMessageType('HandTemperatures', (_message.Message,), {
  'DESCRIPTOR' : _HANDTEMPERATURES,
  '__module__' : 'hand_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.hand.HandTemperatures)
  })
_sym_db.RegisterMessage(HandTemperatures)

SpeedLimitRequest = _reflection.GeneratedProtocolMessageType('SpeedLimitRequest', (_message.Message,), {
  'DESCRIPTOR' : _SPEEDLIMITREQUEST,
  '__module__' : 'hand_pb2'
  # @@protoc_insertion_point(class_scope:reachy.part.hand.SpeedLimitRequest)
  })
_sym_db.RegisterMessage(SpeedLimitRequest)

_HANDSERVICE = DESCRIPTOR.services_by_name['HandService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SPEEDLIMIT._serialized_start=1322
  _SPEEDLIMIT._serialized_end=1380
  _HAND._serialized_start=105
  _HAND._serialized_end=186
  _LISTOFHAND._serialized_start=188
  _LISTOFHAND._serialized_end=238
  _HANDSTATE._serialized_start=241
  _HANDSTATE._serialized_end=620
  _HANDSTATUS._serialized_start=622
  _HANDSTATUS._serialized_end=634
  _FORCE._serialized_start=636
  _FORCE._serialized_end=643
  _JOINTLIMITS._serialized_start=645
  _JOINTLIMITS._serialized_end=684
  _PARALLELGRIPPERLIMITS._serialized_start=686
  _PARALLELGRIPPERLIMITS._serialized_end=756
  _JOINTSLIMITS._serialized_start=758
  _JOINTSLIMITS._serialized_end=851
  _PARALLELGRIPPERPOSITION._serialized_start=853
  _PARALLELGRIPPERPOSITION._serialized_end=896
  _HANDPOSITION._serialized_start=898
  _HANDPOSITION._serialized_end=995
  _TEMPERATURES._serialized_start=997
  _TEMPERATURES._serialized_end=1042
  _PARALLELGRIPPERTEMPERATURE._serialized_start=1044
  _PARALLELGRIPPERTEMPERATURE._serialized_end=1125
  _HANDTEMPERATURES._serialized_start=1127
  _HANDTEMPERATURES._serialized_end=1221
  _SPEEDLIMITREQUEST._serialized_start=1223
  _SPEEDLIMITREQUEST._serialized_end=1320
  _HANDSERVICE._serialized_start=1383
  _HANDSERVICE._serialized_end=2430
# @@protoc_insertion_point(module_scope)

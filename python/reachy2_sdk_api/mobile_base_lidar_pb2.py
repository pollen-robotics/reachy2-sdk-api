# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mobile_base_lidar.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
import mobile_base_mobility_pb2 as mobile__base__mobility__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17mobile_base_lidar.proto\x12\x11mobile.base.lidar\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1amobile_base_mobility.proto\"]\n\x1cLidarObstacleDetectionStatus\x12=\n\x06status\x18\x01 \x01(\x0e\x32-.mobile.base.lidar.LidarObstacleDetectionEnum\"\xfe\x01\n\x0bLidarSafety\x12-\n\tsafety_on\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x34\n\x0fsafety_distance\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x36\n\x11\x63ritical_distance\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12R\n\x19obstacle_detection_status\x18\x04 \x01(\x0b\x32/.mobile.base.lidar.LidarObstacleDetectionStatus\"\x18\n\x08LidarMap\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c*l\n\x1aLidarObstacleDetectionEnum\x12\x16\n\x12NO_OBJECT_DETECTED\x10\x00\x12\x1c\n\x18OBJECT_DETECTED_SLOWDOWN\x10\x01\x12\x18\n\x14OBJECT_DETECTED_STOP\x10\x02\x32\xec\x02\n\x16MobileBaseLidarService\x12Y\n\rSetZuuuSafety\x12\x1e.mobile.base.lidar.LidarSafety\x1a(.mobile.base.mobility.MobilityServiceAck\x12G\n\rGetZuuuSafety\x12\x16.google.protobuf.Empty\x1a\x1e.mobile.base.lidar.LidarSafety\x12\x42\n\x0bGetLidarMap\x12\x16.google.protobuf.Empty\x1a\x1b.mobile.base.lidar.LidarMap\x12j\n\x1fGetLidarObstacleDetectionStatus\x12\x16.google.protobuf.Empty\x1a/.mobile.base.lidar.LidarObstacleDetectionStatusb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mobile_base_lidar_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_LIDAROBSTACLEDETECTIONENUM']._serialized_start=513
  _globals['_LIDAROBSTACLEDETECTIONENUM']._serialized_end=621
  _globals['_LIDAROBSTACLEDETECTIONSTATUS']._serialized_start=135
  _globals['_LIDAROBSTACLEDETECTIONSTATUS']._serialized_end=228
  _globals['_LIDARSAFETY']._serialized_start=231
  _globals['_LIDARSAFETY']._serialized_end=485
  _globals['_LIDARMAP']._serialized_start=487
  _globals['_LIDARMAP']._serialized_end=511
  _globals['_MOBILEBASELIDARSERVICE']._serialized_start=624
  _globals['_MOBILEBASELIDARSERVICE']._serialized_end=988
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mobile_base_utility.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import mobile_base_lidar_pb2 as mobile__base__lidar__pb2
import mobile_base_mobility_pb2 as mobile__base__mobility__pb2
import error_pb2 as error__pb2
import part_pb2 as part__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19mobile_base_utility.proto\x12\x13mobile.base.utility\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17mobile_base_lidar.proto\x1a\x1amobile_base_mobility.proto\x1a\x0b\x65rror.proto\x1a\npart.proto\"S\n\x0eMobileBaseInfo\x12\x15\n\rserial_number\x18\x01 \x01(\t\x12\x14\n\x0cversion_hard\x18\x02 \x01(\t\x12\x14\n\x0cversion_soft\x18\x03 \x01(\t\"`\n\nMobileBase\x12\x1f\n\x02id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12\x31\n\x04info\x18\x02 \x01(\x0b\x32#.mobile.base.utility.MobileBaseInfo\"\xdc\x02\n\x0fMobileBaseState\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1f\n\x02id\x18\x02 \x01(\x0b\x32\x13.reachy.part.PartId\x12\x11\n\tactivated\x18\x03 \x01(\x08\x12\x38\n\rbattery_level\x18\x04 \x01(\x0b\x32!.mobile.base.utility.BatteryLevel\x12\x34\n\x0clidar_safety\x18\x05 \x01(\x0b\x32\x1e.mobile.base.lidar.LidarSafety\x12\x37\n\tzuuu_mode\x18\x06 \x01(\x0b\x32$.mobile.base.utility.ZuuuModeCommand\x12=\n\x0c\x63ontrol_mode\x18\x07 \x01(\x0b\x32\'.mobile.base.utility.ControlModeCommand\"\x8c\x01\n\x0eOdometryVector\x12&\n\x01x\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12&\n\x01y\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12*\n\x05theta\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"P\n\x12\x43ontrolModeCommand\x12:\n\x04mode\x18\x01 \x01(\x0e\x32,.mobile.base.utility.ControlModePossiblities\"J\n\x0fZuuuModeCommand\x12\x37\n\x04mode\x18\x01 \x01(\x0e\x32).mobile.base.utility.ZuuuModePossiblities\":\n\x0c\x42\x61tteryLevel\x12*\n\x05level\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"G\n\x11MobileBaseVersion\x12\x32\n\rmodel_version\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"0\n\x10MobileBaseStatus\x12\x1c\n\x06\x65rrors\x18\x01 \x03(\x0b\x32\x0c.error.Error*H\n\x17\x43ontrolModePossiblities\x12\x15\n\x11NONE_CONTROL_MODE\x10\x00\x12\r\n\tOPEN_LOOP\x10\x01\x12\x07\n\x03PID\x10\x02*\x89\x01\n\x14ZuuuModePossiblities\x12\x12\n\x0eNONE_ZUUU_MODE\x10\x00\x12\x0b\n\x07\x43MD_VEL\x10\x01\x12\t\n\x05\x42RAKE\x10\x02\x12\x0e\n\nFREE_WHEEL\x10\x03\x12\t\n\x05SPEED\x10\x04\x12\x08\n\x04GOTO\x10\x05\x12\x12\n\x0e\x45MERGENCY_STOP\x10\x06\x12\x0c\n\x08\x43MD_GOTO\x10\x07\x32\xc7\x06\n\x18MobileBaseUtilityService\x12\x63\n\x0eSetControlMode\x12\'.mobile.base.utility.ControlModeCommand\x1a(.mobile.base.mobility.MobilityServiceAck\x12Q\n\x0eGetControlMode\x12\x16.google.protobuf.Empty\x1a\'.mobile.base.utility.ControlModeCommand\x12]\n\x0bSetZuuuMode\x12$.mobile.base.utility.ZuuuModeCommand\x1a(.mobile.base.mobility.MobilityServiceAck\x12K\n\x0bGetZuuuMode\x12\x16.google.protobuf.Empty\x1a$.mobile.base.utility.ZuuuModeCommand\x12L\n\x0fGetBatteryLevel\x12\x16.google.protobuf.Empty\x1a!.mobile.base.utility.BatteryLevel\x12J\n\x0bGetOdometry\x12\x16.google.protobuf.Empty\x1a#.mobile.base.utility.OdometryVector\x12Q\n\rResetOdometry\x12\x16.google.protobuf.Empty\x1a(.mobile.base.mobility.MobilityServiceAck\x12H\n\rGetMobileBase\x12\x16.google.protobuf.Empty\x1a\x1f.mobile.base.utility.MobileBase\x12H\n\x08GetState\x12\x16.google.protobuf.Empty\x1a$.mobile.base.utility.MobileBaseState\x12\x46\n\x05\x41udit\x12\x16.google.protobuf.Empty\x1a%.mobile.base.utility.MobileBaseStatusb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mobile_base_utility_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CONTROLMODEPOSSIBLITIES']._serialized_start=1240
  _globals['_CONTROLMODEPOSSIBLITIES']._serialized_end=1312
  _globals['_ZUUUMODEPOSSIBLITIES']._serialized_start=1315
  _globals['_ZUUUMODEPOSSIBLITIES']._serialized_end=1452
  _globals['_MOBILEBASEINFO']._serialized_start=222
  _globals['_MOBILEBASEINFO']._serialized_end=305
  _globals['_MOBILEBASE']._serialized_start=307
  _globals['_MOBILEBASE']._serialized_end=403
  _globals['_MOBILEBASESTATE']._serialized_start=406
  _globals['_MOBILEBASESTATE']._serialized_end=754
  _globals['_ODOMETRYVECTOR']._serialized_start=757
  _globals['_ODOMETRYVECTOR']._serialized_end=897
  _globals['_CONTROLMODECOMMAND']._serialized_start=899
  _globals['_CONTROLMODECOMMAND']._serialized_end=979
  _globals['_ZUUUMODECOMMAND']._serialized_start=981
  _globals['_ZUUUMODECOMMAND']._serialized_end=1055
  _globals['_BATTERYLEVEL']._serialized_start=1057
  _globals['_BATTERYLEVEL']._serialized_end=1115
  _globals['_MOBILEBASEVERSION']._serialized_start=1117
  _globals['_MOBILEBASEVERSION']._serialized_end=1188
  _globals['_MOBILEBASESTATUS']._serialized_start=1190
  _globals['_MOBILEBASESTATUS']._serialized_end=1238
  _globals['_MOBILEBASEUTILITYSERVICE']._serialized_start=1455
  _globals['_MOBILEBASEUTILITYSERVICE']._serialized_end=2294
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: video.proto
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
import error_pb2 as error__pb2
import kinematics_pb2 as kinematics__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bvideo.proto\x12\x0f\x63omponent.video\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0b\x65rror.proto\x1a\x10kinematics.proto\"T\n\x08VideoAck\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x1b\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x0c.error.Error\"=\n\x0e\x43\x61meraFeatures\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06stereo\x18\x02 \x01(\x08\x12\r\n\x05\x64\x65pth\x18\x03 \x01(\x08\"w\n\x10\x43\x61meraParameters\x12\x0e\n\x06height\x18\x01 \x01(\r\x12\r\n\x05width\x18\x02 \x01(\r\x12\x18\n\x10\x64istortion_model\x18\x03 \x01(\t\x12\t\n\x01\x44\x18\x04 \x03(\x02\x12\t\n\x01K\x18\x05 \x03(\x02\x12\t\n\x01R\x18\x06 \x03(\x02\x12\t\n\x01P\x18\x07 \x03(\x02\"D\n\x10\x43\x61meraExtrinsics\x12\x30\n\nextrinsics\x18\x01 \x01(\x0b\x32\x1c.reachy.kinematics.Matrix4x4\"L\n\x14ListOfCameraFeatures\x12\x34\n\x0b\x63\x61mera_feat\x18\x01 \x03(\x0b\x32\x1f.component.video.CameraFeatures\"D\n\x05\x46rame\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\x9b\x01\n\x08\x46rameRaw\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\x0e\n\x06height\x18\x03 \x01(\r\x12\r\n\x05width\x18\x04 \x01(\r\x12\x10\n\x08\x65ncoding\x18\x05 \x01(\t\x12\x0c\n\x04step\x18\x06 \x01(\r\x12\x13\n\x0bisbigendian\x18\x07 \x01(\x08\"v\n\x0bViewRequest\x12\x34\n\x0b\x63\x61mera_feat\x18\x01 \x01(\x0b\x32\x1f.component.video.CameraFeatures\x12(\n\x04view\x18\x02 \x01(\x0e\x32\x15.component.video.ViewH\x00\x88\x01\x01\x42\x07\n\x05_view*&\n\x04View\x12\x08\n\x04LEFT\x10\x00\x12\t\n\x05RIGHT\x10\x01\x12\t\n\x05\x44\x45PTH\x10\x02\x32\x8f\x03\n\x0cVideoService\x12T\n\x13GetAvailableCameras\x12\x16.google.protobuf.Empty\x1a%.component.video.ListOfCameraFeatures\x12@\n\x08GetFrame\x12\x1c.component.video.ViewRequest\x1a\x16.component.video.Frame\x12P\n\rGetParameters\x12\x1c.component.video.ViewRequest\x1a!.component.video.CameraParameters\x12\x43\n\x08GetDepth\x12\x1c.component.video.ViewRequest\x1a\x19.component.video.FrameRaw\x12P\n\rGetExtrinsics\x12\x1c.component.video.ViewRequest\x1a!.component.video.CameraExtrinsicsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'video_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_VIEW']._serialized_start=923
  _globals['_VIEW']._serialized_end=961
  _globals['_VIDEOACK']._serialized_start=157
  _globals['_VIDEOACK']._serialized_end=241
  _globals['_CAMERAFEATURES']._serialized_start=243
  _globals['_CAMERAFEATURES']._serialized_end=304
  _globals['_CAMERAPARAMETERS']._serialized_start=306
  _globals['_CAMERAPARAMETERS']._serialized_end=425
  _globals['_CAMERAEXTRINSICS']._serialized_start=427
  _globals['_CAMERAEXTRINSICS']._serialized_end=495
  _globals['_LISTOFCAMERAFEATURES']._serialized_start=497
  _globals['_LISTOFCAMERAFEATURES']._serialized_end=573
  _globals['_FRAME']._serialized_start=575
  _globals['_FRAME']._serialized_end=643
  _globals['_FRAMERAW']._serialized_start=646
  _globals['_FRAMERAW']._serialized_end=801
  _globals['_VIEWREQUEST']._serialized_start=803
  _globals['_VIEWREQUEST']._serialized_end=921
  _globals['_VIDEOSERVICE']._serialized_start=964
  _globals['_VIDEOSERVICE']._serialized_end=1363
# @@protoc_insertion_point(module_scope)

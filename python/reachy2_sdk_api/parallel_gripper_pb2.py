# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: parallel_gripper.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import component_pb2 as component__pb2
import error_pb2 as error__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16parallel_gripper.proto\x12\x1a\x63omponent.parallel_gripper\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x0f\x63omponent.proto\x1a\x0b\x65rror.proto\"E\n\x14ParallelGripperState\x12-\n\ttimestamp\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x83\x01\n\x1bParallelGripperStateRequest\x12@\n\x06\x66ields\x18\x01 \x03(\x0e\x32\x30.component.parallel_gripper.ParallelGripperField\x12\"\n\x02id\x18\x02 \x01(\x0b\x32\x16.component.ComponentId\"w\n!ParallelGripperStreamStateRequest\x12\x44\n\x03req\x18\x01 \x01(\x0b\x32\x37.component.parallel_gripper.ParallelGripperStateRequest\x12\x0c\n\x04\x66req\x18\x02 \x01(\x02\"\x18\n\x16ParallelGripperCommand\"P\n\x13ParallelGripperInfo\x12\"\n\x02id\x18\x01 \x01(\x0b\x32\x16.component.ComponentId\x12\x15\n\rserial_number\x18\x02 \x01(\t\"k\n\x19ListOfParallelGripperInfo\x12N\n\x15parallel_gripper_info\x18\x01 \x03(\x0b\x32/.component.parallel_gripper.ParallelGripperInfo\"5\n\x15ParallelGripperStatus\x12\x1c\n\x06\x65rrors\x18\x01 \x03(\x0b\x32\x0c.error.Error*\xe7\x01\n\x14ParallelGripperField\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04NAME\x10\x01\x12\x06\n\x02ID\x10\x02\x12\x14\n\x10PRESENT_POSITION\x10\x03\x12\x11\n\rPRESENT_SPEED\x10\x04\x12\x10\n\x0cPRESENT_LOAD\x10\x05\x12\x0f\n\x0bTEMPERATURE\x10\x06\x12\x10\n\x0c\x46ORCE_SENSOR\x10\x07\x12\r\n\tCOMPLIANT\x10\x08\x12\x11\n\rGOAL_POSITION\x10\t\x12\x0f\n\x0bSPEED_LIMIT\x10\n\x12\x10\n\x0cTORQUE_LIMIT\x10\x0b\x12\x07\n\x03PID\x10\x0c\x12\x07\n\x03\x41LL\x10\x0f\x32\xf8\x05\n\x0eGripperService\x12\x66\n\x15GetAllParallelGripper\x12\x16.google.protobuf.Empty\x1a\x35.component.parallel_gripper.ListOfParallelGripperInfo\x12u\n\x08GetState\x12\x37.component.parallel_gripper.ParallelGripperStateRequest\x1a\x30.component.parallel_gripper.ParallelGripperState\x12\x80\x01\n\x0bStreamState\x12=.component.parallel_gripper.ParallelGripperStreamStateRequest\x1a\x30.component.parallel_gripper.ParallelGripperState0\x01\x12Y\n\x0bSendCommand\x12\x32.component.parallel_gripper.ParallelGripperCommand\x1a\x16.google.protobuf.Empty\x12]\n\rStreamCommand\x12\x32.component.parallel_gripper.ParallelGripperCommand\x1a\x16.google.protobuf.Empty(\x01\x12R\n\x05\x41udit\x12\x16.component.ComponentId\x1a\x31.component.parallel_gripper.ParallelGripperStatus\x12;\n\tHeartBeat\x12\x16.component.ComponentId\x1a\x16.google.protobuf.Empty\x12\x39\n\x07Restart\x12\x16.component.ComponentId\x1a\x16.google.protobuf.Emptyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'parallel_gripper_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PARALLELGRIPPERFIELD']._serialized_start=745
  _globals['_PARALLELGRIPPERFIELD']._serialized_end=976
  _globals['_PARALLELGRIPPERSTATE']._serialized_start=146
  _globals['_PARALLELGRIPPERSTATE']._serialized_end=215
  _globals['_PARALLELGRIPPERSTATEREQUEST']._serialized_start=218
  _globals['_PARALLELGRIPPERSTATEREQUEST']._serialized_end=349
  _globals['_PARALLELGRIPPERSTREAMSTATEREQUEST']._serialized_start=351
  _globals['_PARALLELGRIPPERSTREAMSTATEREQUEST']._serialized_end=470
  _globals['_PARALLELGRIPPERCOMMAND']._serialized_start=472
  _globals['_PARALLELGRIPPERCOMMAND']._serialized_end=496
  _globals['_PARALLELGRIPPERINFO']._serialized_start=498
  _globals['_PARALLELGRIPPERINFO']._serialized_end=578
  _globals['_LISTOFPARALLELGRIPPERINFO']._serialized_start=580
  _globals['_LISTOFPARALLELGRIPPERINFO']._serialized_end=687
  _globals['_PARALLELGRIPPERSTATUS']._serialized_start=689
  _globals['_PARALLELGRIPPERSTATUS']._serialized_end=742
  _globals['_GRIPPERSERVICE']._serialized_start=979
  _globals['_GRIPPERSERVICE']._serialized_end=1739
# @@protoc_insertion_point(module_scope)

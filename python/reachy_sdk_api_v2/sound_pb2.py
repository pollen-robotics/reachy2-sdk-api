# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sound.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import component_pb2 as component__pb2
import error_pb2 as error__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bsound.proto\x12\x0f\x63omponent.sound\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x0f\x63omponent.proto\x1a\x0b\x65rror.proto\";\n\nMicrophone\x12-\n\x04info\x18\x01 \x01(\x0b\x32\x1f.component.sound.MicrophoneInfo\"5\n\x07Speaker\x12*\n\x04info\x18\x01 \x01(\x0b\x32\x1c.component.sound.SpeakerInfo\"B\n\x0eMicrophoneInfo\x12\"\n\x02id\x18\x01 \x01(\x0b\x32\x16.component.ComponentId\x12\x0c\n\x04gain\x18\x02 \x01(\x02\"P\n\x14ListOfMicrophoneInfo\x12\x38\n\x0fmicrophone_info\x18\x01 \x03(\x0b\x32\x1f.component.sound.MicrophoneInfo\"T\n\x08SoundAck\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x1b\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x0c.error.Error\"\x15\n\x07SoundId\x12\n\n\x02id\x18\x01 \x01(\t\"f\n\x0cRecordingAck\x12&\n\x03\x61\x63k\x18\x01 \x01(\x0b\x32\x19.component.sound.SoundAck\x12.\n\x0crecording_id\x18\x02 \x01(\x0b\x32\x18.component.sound.SoundId\"A\n\x0bSpeakerInfo\x12\"\n\x02id\x18\x01 \x01(\x0b\x32\x16.component.ComponentId\x12\x0e\n\x06volume\x18\x02 \x01(\x02\"G\n\x11ListOfSpeakerInfo\x12\x32\n\x0cspeaker_info\x18\x01 \x03(\x0b\x32\x1c.component.sound.SpeakerInfo\"C\n\rVolumeRequest\x12\"\n\x02id\x18\x01 \x01(\x0b\x32\x16.component.ComponentId\x12\x0e\n\x06volume\x18\x02 \x01(\x02\x32\xfe\x03\n\x0cSoundService\x12Q\n\x10GetAllMicrophone\x12\x16.google.protobuf.Empty\x1a%.component.sound.ListOfMicrophoneInfo\x12K\n\rGetAllSpeaker\x12\x16.google.protobuf.Empty\x1a\".component.sound.ListOfSpeakerInfo\x12@\n\x0eStartRecording\x12\x16.component.ComponentId\x1a\x16.google.protobuf.Empty\x12\x46\n\rStopRecording\x12\x16.component.ComponentId\x1a\x1d.component.sound.RecordingAck\x12=\n\x0bTestSpeaker\x12\x16.component.ComponentId\x1a\x16.google.protobuf.Empty\x12\x46\n\x0c\x43hangeVolume\x12\x1e.component.sound.VolumeRequest\x1a\x16.google.protobuf.Empty\x12=\n\tPlaySound\x12\x18.component.sound.SoundId\x1a\x16.google.protobuf.Emptyb\x06proto3')



_MICROPHONE = DESCRIPTOR.message_types_by_name['Microphone']
_SPEAKER = DESCRIPTOR.message_types_by_name['Speaker']
_MICROPHONEINFO = DESCRIPTOR.message_types_by_name['MicrophoneInfo']
_LISTOFMICROPHONEINFO = DESCRIPTOR.message_types_by_name['ListOfMicrophoneInfo']
_SOUNDACK = DESCRIPTOR.message_types_by_name['SoundAck']
_SOUNDID = DESCRIPTOR.message_types_by_name['SoundId']
_RECORDINGACK = DESCRIPTOR.message_types_by_name['RecordingAck']
_SPEAKERINFO = DESCRIPTOR.message_types_by_name['SpeakerInfo']
_LISTOFSPEAKERINFO = DESCRIPTOR.message_types_by_name['ListOfSpeakerInfo']
_VOLUMEREQUEST = DESCRIPTOR.message_types_by_name['VolumeRequest']
Microphone = _reflection.GeneratedProtocolMessageType('Microphone', (_message.Message,), {
  'DESCRIPTOR' : _MICROPHONE,
  '__module__' : 'sound_pb2'
  # @@protoc_insertion_point(class_scope:component.sound.Microphone)
  })
_sym_db.RegisterMessage(Microphone)

Speaker = _reflection.GeneratedProtocolMessageType('Speaker', (_message.Message,), {
  'DESCRIPTOR' : _SPEAKER,
  '__module__' : 'sound_pb2'
  # @@protoc_insertion_point(class_scope:component.sound.Speaker)
  })
_sym_db.RegisterMessage(Speaker)

MicrophoneInfo = _reflection.GeneratedProtocolMessageType('MicrophoneInfo', (_message.Message,), {
  'DESCRIPTOR' : _MICROPHONEINFO,
  '__module__' : 'sound_pb2'
  # @@protoc_insertion_point(class_scope:component.sound.MicrophoneInfo)
  })
_sym_db.RegisterMessage(MicrophoneInfo)

ListOfMicrophoneInfo = _reflection.GeneratedProtocolMessageType('ListOfMicrophoneInfo', (_message.Message,), {
  'DESCRIPTOR' : _LISTOFMICROPHONEINFO,
  '__module__' : 'sound_pb2'
  # @@protoc_insertion_point(class_scope:component.sound.ListOfMicrophoneInfo)
  })
_sym_db.RegisterMessage(ListOfMicrophoneInfo)

SoundAck = _reflection.GeneratedProtocolMessageType('SoundAck', (_message.Message,), {
  'DESCRIPTOR' : _SOUNDACK,
  '__module__' : 'sound_pb2'
  # @@protoc_insertion_point(class_scope:component.sound.SoundAck)
  })
_sym_db.RegisterMessage(SoundAck)

SoundId = _reflection.GeneratedProtocolMessageType('SoundId', (_message.Message,), {
  'DESCRIPTOR' : _SOUNDID,
  '__module__' : 'sound_pb2'
  # @@protoc_insertion_point(class_scope:component.sound.SoundId)
  })
_sym_db.RegisterMessage(SoundId)

RecordingAck = _reflection.GeneratedProtocolMessageType('RecordingAck', (_message.Message,), {
  'DESCRIPTOR' : _RECORDINGACK,
  '__module__' : 'sound_pb2'
  # @@protoc_insertion_point(class_scope:component.sound.RecordingAck)
  })
_sym_db.RegisterMessage(RecordingAck)

SpeakerInfo = _reflection.GeneratedProtocolMessageType('SpeakerInfo', (_message.Message,), {
  'DESCRIPTOR' : _SPEAKERINFO,
  '__module__' : 'sound_pb2'
  # @@protoc_insertion_point(class_scope:component.sound.SpeakerInfo)
  })
_sym_db.RegisterMessage(SpeakerInfo)

ListOfSpeakerInfo = _reflection.GeneratedProtocolMessageType('ListOfSpeakerInfo', (_message.Message,), {
  'DESCRIPTOR' : _LISTOFSPEAKERINFO,
  '__module__' : 'sound_pb2'
  # @@protoc_insertion_point(class_scope:component.sound.ListOfSpeakerInfo)
  })
_sym_db.RegisterMessage(ListOfSpeakerInfo)

VolumeRequest = _reflection.GeneratedProtocolMessageType('VolumeRequest', (_message.Message,), {
  'DESCRIPTOR' : _VOLUMEREQUEST,
  '__module__' : 'sound_pb2'
  # @@protoc_insertion_point(class_scope:component.sound.VolumeRequest)
  })
_sym_db.RegisterMessage(VolumeRequest)

_SOUNDSERVICE = DESCRIPTOR.services_by_name['SoundService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MICROPHONE._serialized_start=123
  _MICROPHONE._serialized_end=182
  _SPEAKER._serialized_start=184
  _SPEAKER._serialized_end=237
  _MICROPHONEINFO._serialized_start=239
  _MICROPHONEINFO._serialized_end=305
  _LISTOFMICROPHONEINFO._serialized_start=307
  _LISTOFMICROPHONEINFO._serialized_end=387
  _SOUNDACK._serialized_start=389
  _SOUNDACK._serialized_end=473
  _SOUNDID._serialized_start=475
  _SOUNDID._serialized_end=496
  _RECORDINGACK._serialized_start=498
  _RECORDINGACK._serialized_end=600
  _SPEAKERINFO._serialized_start=602
  _SPEAKERINFO._serialized_end=667
  _LISTOFSPEAKERINFO._serialized_start=669
  _LISTOFSPEAKERINFO._serialized_end=740
  _VOLUMEREQUEST._serialized_start=742
  _VOLUMEREQUEST._serialized_end=809
  _SOUNDSERVICE._serialized_start=812
  _SOUNDSERVICE._serialized_end=1322
# @@protoc_insertion_point(module_scope)

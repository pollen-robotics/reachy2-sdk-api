import * as jspb from 'google-protobuf'

import * as google_protobuf_wrappers_pb from 'google-protobuf/google/protobuf/wrappers_pb';
import * as google_protobuf_empty_pb from 'google-protobuf/google/protobuf/empty_pb';
import * as component_pb from './component_pb';
import * as error_pb from './error_pb';


export class Microphone extends jspb.Message {
  getInfo(): MicrophoneInfo | undefined;
  setInfo(value?: MicrophoneInfo): Microphone;
  hasInfo(): boolean;
  clearInfo(): Microphone;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Microphone.AsObject;
  static toObject(includeInstance: boolean, msg: Microphone): Microphone.AsObject;
  static serializeBinaryToWriter(message: Microphone, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Microphone;
  static deserializeBinaryFromReader(message: Microphone, reader: jspb.BinaryReader): Microphone;
}

export namespace Microphone {
  export type AsObject = {
    info?: MicrophoneInfo.AsObject,
  }
}

export class Speaker extends jspb.Message {
  getInfo(): SpeakerInfo | undefined;
  setInfo(value?: SpeakerInfo): Speaker;
  hasInfo(): boolean;
  clearInfo(): Speaker;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Speaker.AsObject;
  static toObject(includeInstance: boolean, msg: Speaker): Speaker.AsObject;
  static serializeBinaryToWriter(message: Speaker, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Speaker;
  static deserializeBinaryFromReader(message: Speaker, reader: jspb.BinaryReader): Speaker;
}

export namespace Speaker {
  export type AsObject = {
    info?: SpeakerInfo.AsObject,
  }
}

export class MicrophoneInfo extends jspb.Message {
  getId(): component_pb.ComponentId | undefined;
  setId(value?: component_pb.ComponentId): MicrophoneInfo;
  hasId(): boolean;
  clearId(): MicrophoneInfo;

  getGain(): number;
  setGain(value: number): MicrophoneInfo;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MicrophoneInfo.AsObject;
  static toObject(includeInstance: boolean, msg: MicrophoneInfo): MicrophoneInfo.AsObject;
  static serializeBinaryToWriter(message: MicrophoneInfo, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MicrophoneInfo;
  static deserializeBinaryFromReader(message: MicrophoneInfo, reader: jspb.BinaryReader): MicrophoneInfo;
}

export namespace MicrophoneInfo {
  export type AsObject = {
    id?: component_pb.ComponentId.AsObject,
    gain: number,
  }
}

export class ListOfMicrophoneInfo extends jspb.Message {
  getStereoCameraInfoList(): Array<MicrophoneInfo>;
  setStereoCameraInfoList(value: Array<MicrophoneInfo>): ListOfMicrophoneInfo;
  clearStereoCameraInfoList(): ListOfMicrophoneInfo;
  addStereoCameraInfo(value?: MicrophoneInfo, index?: number): MicrophoneInfo;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListOfMicrophoneInfo.AsObject;
  static toObject(includeInstance: boolean, msg: ListOfMicrophoneInfo): ListOfMicrophoneInfo.AsObject;
  static serializeBinaryToWriter(message: ListOfMicrophoneInfo, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListOfMicrophoneInfo;
  static deserializeBinaryFromReader(message: ListOfMicrophoneInfo, reader: jspb.BinaryReader): ListOfMicrophoneInfo;
}

export namespace ListOfMicrophoneInfo {
  export type AsObject = {
    stereoCameraInfoList: Array<MicrophoneInfo.AsObject>,
  }
}

export class SoundAck extends jspb.Message {
  getSuccess(): google_protobuf_wrappers_pb.BoolValue | undefined;
  setSuccess(value?: google_protobuf_wrappers_pb.BoolValue): SoundAck;
  hasSuccess(): boolean;
  clearSuccess(): SoundAck;

  getError(): error_pb.Error | undefined;
  setError(value?: error_pb.Error): SoundAck;
  hasError(): boolean;
  clearError(): SoundAck;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SoundAck.AsObject;
  static toObject(includeInstance: boolean, msg: SoundAck): SoundAck.AsObject;
  static serializeBinaryToWriter(message: SoundAck, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SoundAck;
  static deserializeBinaryFromReader(message: SoundAck, reader: jspb.BinaryReader): SoundAck;
}

export namespace SoundAck {
  export type AsObject = {
    success?: google_protobuf_wrappers_pb.BoolValue.AsObject,
    error?: error_pb.Error.AsObject,
  }
}

export class SoundId extends jspb.Message {
  getId(): string;
  setId(value: string): SoundId;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SoundId.AsObject;
  static toObject(includeInstance: boolean, msg: SoundId): SoundId.AsObject;
  static serializeBinaryToWriter(message: SoundId, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SoundId;
  static deserializeBinaryFromReader(message: SoundId, reader: jspb.BinaryReader): SoundId;
}

export namespace SoundId {
  export type AsObject = {
    id: string,
  }
}

export class RecordingAck extends jspb.Message {
  getAck(): SoundAck | undefined;
  setAck(value?: SoundAck): RecordingAck;
  hasAck(): boolean;
  clearAck(): RecordingAck;

  getRecordingId(): SoundId | undefined;
  setRecordingId(value?: SoundId): RecordingAck;
  hasRecordingId(): boolean;
  clearRecordingId(): RecordingAck;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RecordingAck.AsObject;
  static toObject(includeInstance: boolean, msg: RecordingAck): RecordingAck.AsObject;
  static serializeBinaryToWriter(message: RecordingAck, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RecordingAck;
  static deserializeBinaryFromReader(message: RecordingAck, reader: jspb.BinaryReader): RecordingAck;
}

export namespace RecordingAck {
  export type AsObject = {
    ack?: SoundAck.AsObject,
    recordingId?: SoundId.AsObject,
  }
}

export class SpeakerInfo extends jspb.Message {
  getId(): component_pb.ComponentId | undefined;
  setId(value?: component_pb.ComponentId): SpeakerInfo;
  hasId(): boolean;
  clearId(): SpeakerInfo;

  getVolume(): number;
  setVolume(value: number): SpeakerInfo;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SpeakerInfo.AsObject;
  static toObject(includeInstance: boolean, msg: SpeakerInfo): SpeakerInfo.AsObject;
  static serializeBinaryToWriter(message: SpeakerInfo, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SpeakerInfo;
  static deserializeBinaryFromReader(message: SpeakerInfo, reader: jspb.BinaryReader): SpeakerInfo;
}

export namespace SpeakerInfo {
  export type AsObject = {
    id?: component_pb.ComponentId.AsObject,
    volume: number,
  }
}

export class ListOfSpeakerInfo extends jspb.Message {
  getStereoCameraInfoList(): Array<SpeakerInfo>;
  setStereoCameraInfoList(value: Array<SpeakerInfo>): ListOfSpeakerInfo;
  clearStereoCameraInfoList(): ListOfSpeakerInfo;
  addStereoCameraInfo(value?: SpeakerInfo, index?: number): SpeakerInfo;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListOfSpeakerInfo.AsObject;
  static toObject(includeInstance: boolean, msg: ListOfSpeakerInfo): ListOfSpeakerInfo.AsObject;
  static serializeBinaryToWriter(message: ListOfSpeakerInfo, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListOfSpeakerInfo;
  static deserializeBinaryFromReader(message: ListOfSpeakerInfo, reader: jspb.BinaryReader): ListOfSpeakerInfo;
}

export namespace ListOfSpeakerInfo {
  export type AsObject = {
    stereoCameraInfoList: Array<SpeakerInfo.AsObject>,
  }
}

export class VolumeRequest extends jspb.Message {
  getId(): component_pb.ComponentId | undefined;
  setId(value?: component_pb.ComponentId): VolumeRequest;
  hasId(): boolean;
  clearId(): VolumeRequest;

  getVolume(): number;
  setVolume(value: number): VolumeRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): VolumeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: VolumeRequest): VolumeRequest.AsObject;
  static serializeBinaryToWriter(message: VolumeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): VolumeRequest;
  static deserializeBinaryFromReader(message: VolumeRequest, reader: jspb.BinaryReader): VolumeRequest;
}

export namespace VolumeRequest {
  export type AsObject = {
    id?: component_pb.ComponentId.AsObject,
    volume: number,
  }
}


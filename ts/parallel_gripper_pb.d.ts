import * as jspb from 'google-protobuf'

import * as google_protobuf_timestamp_pb from 'google-protobuf/google/protobuf/timestamp_pb';
import * as google_protobuf_empty_pb from 'google-protobuf/google/protobuf/empty_pb';
import * as component_pb from './component_pb';


export class ParallelGripperState extends jspb.Message {
  getTimestamp(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTimestamp(value?: google_protobuf_timestamp_pb.Timestamp): ParallelGripperState;
  hasTimestamp(): boolean;
  clearTimestamp(): ParallelGripperState;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ParallelGripperState.AsObject;
  static toObject(includeInstance: boolean, msg: ParallelGripperState): ParallelGripperState.AsObject;
  static serializeBinaryToWriter(message: ParallelGripperState, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ParallelGripperState;
  static deserializeBinaryFromReader(message: ParallelGripperState, reader: jspb.BinaryReader): ParallelGripperState;
}

export namespace ParallelGripperState {
  export type AsObject = {
    timestamp?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class ParallelGripperStateRequest extends jspb.Message {
  getFieldsList(): Array<ParallelGripperField>;
  setFieldsList(value: Array<ParallelGripperField>): ParallelGripperStateRequest;
  clearFieldsList(): ParallelGripperStateRequest;
  addFields(value: ParallelGripperField, index?: number): ParallelGripperStateRequest;

  getId(): component_pb.ComponentId | undefined;
  setId(value?: component_pb.ComponentId): ParallelGripperStateRequest;
  hasId(): boolean;
  clearId(): ParallelGripperStateRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ParallelGripperStateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ParallelGripperStateRequest): ParallelGripperStateRequest.AsObject;
  static serializeBinaryToWriter(message: ParallelGripperStateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ParallelGripperStateRequest;
  static deserializeBinaryFromReader(message: ParallelGripperStateRequest, reader: jspb.BinaryReader): ParallelGripperStateRequest;
}

export namespace ParallelGripperStateRequest {
  export type AsObject = {
    fieldsList: Array<ParallelGripperField>,
    id?: component_pb.ComponentId.AsObject,
  }
}

export class ParallelGripperStreamStateRequest extends jspb.Message {
  getReq(): ParallelGripperStateRequest | undefined;
  setReq(value?: ParallelGripperStateRequest): ParallelGripperStreamStateRequest;
  hasReq(): boolean;
  clearReq(): ParallelGripperStreamStateRequest;

  getFreq(): number;
  setFreq(value: number): ParallelGripperStreamStateRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ParallelGripperStreamStateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ParallelGripperStreamStateRequest): ParallelGripperStreamStateRequest.AsObject;
  static serializeBinaryToWriter(message: ParallelGripperStreamStateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ParallelGripperStreamStateRequest;
  static deserializeBinaryFromReader(message: ParallelGripperStreamStateRequest, reader: jspb.BinaryReader): ParallelGripperStreamStateRequest;
}

export namespace ParallelGripperStreamStateRequest {
  export type AsObject = {
    req?: ParallelGripperStateRequest.AsObject,
    freq: number,
  }
}

export class ParallelGripperCommand extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ParallelGripperCommand.AsObject;
  static toObject(includeInstance: boolean, msg: ParallelGripperCommand): ParallelGripperCommand.AsObject;
  static serializeBinaryToWriter(message: ParallelGripperCommand, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ParallelGripperCommand;
  static deserializeBinaryFromReader(message: ParallelGripperCommand, reader: jspb.BinaryReader): ParallelGripperCommand;
}

export namespace ParallelGripperCommand {
  export type AsObject = {
  }
}

export class ParallelGripperInfo extends jspb.Message {
  getId(): component_pb.ComponentId | undefined;
  setId(value?: component_pb.ComponentId): ParallelGripperInfo;
  hasId(): boolean;
  clearId(): ParallelGripperInfo;

  getSerialNumber(): string;
  setSerialNumber(value: string): ParallelGripperInfo;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ParallelGripperInfo.AsObject;
  static toObject(includeInstance: boolean, msg: ParallelGripperInfo): ParallelGripperInfo.AsObject;
  static serializeBinaryToWriter(message: ParallelGripperInfo, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ParallelGripperInfo;
  static deserializeBinaryFromReader(message: ParallelGripperInfo, reader: jspb.BinaryReader): ParallelGripperInfo;
}

export namespace ParallelGripperInfo {
  export type AsObject = {
    id?: component_pb.ComponentId.AsObject,
    serialNumber: string,
  }
}

export class ListOfParallelGripperInfo extends jspb.Message {
  getParallelGripperInfoList(): Array<ParallelGripperInfo>;
  setParallelGripperInfoList(value: Array<ParallelGripperInfo>): ListOfParallelGripperInfo;
  clearParallelGripperInfoList(): ListOfParallelGripperInfo;
  addParallelGripperInfo(value?: ParallelGripperInfo, index?: number): ParallelGripperInfo;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListOfParallelGripperInfo.AsObject;
  static toObject(includeInstance: boolean, msg: ListOfParallelGripperInfo): ListOfParallelGripperInfo.AsObject;
  static serializeBinaryToWriter(message: ListOfParallelGripperInfo, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListOfParallelGripperInfo;
  static deserializeBinaryFromReader(message: ListOfParallelGripperInfo, reader: jspb.BinaryReader): ListOfParallelGripperInfo;
}

export namespace ListOfParallelGripperInfo {
  export type AsObject = {
    parallelGripperInfoList: Array<ParallelGripperInfo.AsObject>,
  }
}

export class ParallelGripperStatus extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ParallelGripperStatus.AsObject;
  static toObject(includeInstance: boolean, msg: ParallelGripperStatus): ParallelGripperStatus.AsObject;
  static serializeBinaryToWriter(message: ParallelGripperStatus, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ParallelGripperStatus;
  static deserializeBinaryFromReader(message: ParallelGripperStatus, reader: jspb.BinaryReader): ParallelGripperStatus;
}

export namespace ParallelGripperStatus {
  export type AsObject = {
  }
}

export enum ParallelGripperField { 
  NONE = 0,
  NAME = 1,
  UID = 2,
  PRESENT_POSITION = 3,
  PRESENT_SPEED = 4,
  PRESENT_LOAD = 5,
  TEMPERATURE = 6,
  FORCE_SENSOR = 7,
  COMPLIANT = 8,
  GOAL_POSITION = 9,
  SPEED_LIMIT = 10,
  TORQUE_LIMIT = 11,
  PID = 12,
  ALL = 15,
}

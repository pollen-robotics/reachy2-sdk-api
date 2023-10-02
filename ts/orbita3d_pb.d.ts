import * as jspb from 'google-protobuf'

import * as google_protobuf_timestamp_pb from 'google-protobuf/google/protobuf/timestamp_pb';
import * as google_protobuf_empty_pb from 'google-protobuf/google/protobuf/empty_pb';
import * as google_protobuf_wrappers_pb from 'google-protobuf/google/protobuf/wrappers_pb';
import * as component_pb from './component_pb';
import * as kinematics_pb from './kinematics_pb';


export class Orbita3DState extends jspb.Message {
  getTimestamp(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTimestamp(value?: google_protobuf_timestamp_pb.Timestamp): Orbita3DState;
  hasTimestamp(): boolean;
  clearTimestamp(): Orbita3DState;

  getName(): string;
  setName(value: string): Orbita3DState;

  getUid(): string;
  setUid(value: string): Orbita3DState;

  getPresentPosition(): Float3D | undefined;
  setPresentPosition(value?: Float3D): Orbita3DState;
  hasPresentPosition(): boolean;
  clearPresentPosition(): Orbita3DState;

  getPresentSpeed(): Float3D | undefined;
  setPresentSpeed(value?: Float3D): Orbita3DState;
  hasPresentSpeed(): boolean;
  clearPresentSpeed(): Orbita3DState;

  getPresentLoad(): Float3D | undefined;
  setPresentLoad(value?: Float3D): Orbita3DState;
  hasPresentLoad(): boolean;
  clearPresentLoad(): Orbita3DState;

  getTemperature(): Float3D | undefined;
  setTemperature(value?: Float3D): Orbita3DState;
  hasTemperature(): boolean;
  clearTemperature(): Orbita3DState;

  getCompliant(): google_protobuf_wrappers_pb.BoolValue | undefined;
  setCompliant(value?: google_protobuf_wrappers_pb.BoolValue): Orbita3DState;
  hasCompliant(): boolean;
  clearCompliant(): Orbita3DState;

  getGoalPosition(): Float3D | undefined;
  setGoalPosition(value?: Float3D): Orbita3DState;
  hasGoalPosition(): boolean;
  clearGoalPosition(): Orbita3DState;

  getSpeedLimit(): Float3D | undefined;
  setSpeedLimit(value?: Float3D): Orbita3DState;
  hasSpeedLimit(): boolean;
  clearSpeedLimit(): Orbita3DState;

  getTorqueLimit(): Float3D | undefined;
  setTorqueLimit(value?: Float3D): Orbita3DState;
  hasTorqueLimit(): boolean;
  clearTorqueLimit(): Orbita3DState;

  getPid(): PID3D | undefined;
  setPid(value?: PID3D): Orbita3DState;
  hasPid(): boolean;
  clearPid(): Orbita3DState;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Orbita3DState.AsObject;
  static toObject(includeInstance: boolean, msg: Orbita3DState): Orbita3DState.AsObject;
  static serializeBinaryToWriter(message: Orbita3DState, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Orbita3DState;
  static deserializeBinaryFromReader(message: Orbita3DState, reader: jspb.BinaryReader): Orbita3DState;
}

export namespace Orbita3DState {
  export type AsObject = {
    timestamp?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    name: string,
    uid: string,
    presentPosition?: Float3D.AsObject,
    presentSpeed?: Float3D.AsObject,
    presentLoad?: Float3D.AsObject,
    temperature?: Float3D.AsObject,
    compliant?: google_protobuf_wrappers_pb.BoolValue.AsObject,
    goalPosition?: Float3D.AsObject,
    speedLimit?: Float3D.AsObject,
    torqueLimit?: Float3D.AsObject,
    pid?: PID3D.AsObject,
  }
}

export class Orbita3DStateRequest extends jspb.Message {
  getFieldsList(): Array<Orbita3DField>;
  setFieldsList(value: Array<Orbita3DField>): Orbita3DStateRequest;
  clearFieldsList(): Orbita3DStateRequest;
  addFields(value: Orbita3DField, index?: number): Orbita3DStateRequest;

  getId(): component_pb.ComponentId | undefined;
  setId(value?: component_pb.ComponentId): Orbita3DStateRequest;
  hasId(): boolean;
  clearId(): Orbita3DStateRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Orbita3DStateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: Orbita3DStateRequest): Orbita3DStateRequest.AsObject;
  static serializeBinaryToWriter(message: Orbita3DStateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Orbita3DStateRequest;
  static deserializeBinaryFromReader(message: Orbita3DStateRequest, reader: jspb.BinaryReader): Orbita3DStateRequest;
}

export namespace Orbita3DStateRequest {
  export type AsObject = {
    fieldsList: Array<Orbita3DField>,
    id?: component_pb.ComponentId.AsObject,
  }
}

export class Orbita3DStreamStateRequest extends jspb.Message {
  getReq(): Orbita3DStateRequest | undefined;
  setReq(value?: Orbita3DStateRequest): Orbita3DStreamStateRequest;
  hasReq(): boolean;
  clearReq(): Orbita3DStreamStateRequest;

  getFreq(): number;
  setFreq(value: number): Orbita3DStreamStateRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Orbita3DStreamStateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: Orbita3DStreamStateRequest): Orbita3DStreamStateRequest.AsObject;
  static serializeBinaryToWriter(message: Orbita3DStreamStateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Orbita3DStreamStateRequest;
  static deserializeBinaryFromReader(message: Orbita3DStreamStateRequest, reader: jspb.BinaryReader): Orbita3DStreamStateRequest;
}

export namespace Orbita3DStreamStateRequest {
  export type AsObject = {
    req?: Orbita3DStateRequest.AsObject,
    freq: number,
  }
}

export class PID3D extends jspb.Message {
  getRoll(): component_pb.PIDGains | undefined;
  setRoll(value?: component_pb.PIDGains): PID3D;
  hasRoll(): boolean;
  clearRoll(): PID3D;

  getPitch(): component_pb.PIDGains | undefined;
  setPitch(value?: component_pb.PIDGains): PID3D;
  hasPitch(): boolean;
  clearPitch(): PID3D;

  getYaw(): component_pb.PIDGains | undefined;
  setYaw(value?: component_pb.PIDGains): PID3D;
  hasYaw(): boolean;
  clearYaw(): PID3D;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): PID3D.AsObject;
  static toObject(includeInstance: boolean, msg: PID3D): PID3D.AsObject;
  static serializeBinaryToWriter(message: PID3D, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): PID3D;
  static deserializeBinaryFromReader(message: PID3D, reader: jspb.BinaryReader): PID3D;
}

export namespace PID3D {
  export type AsObject = {
    roll?: component_pb.PIDGains.AsObject,
    pitch?: component_pb.PIDGains.AsObject,
    yaw?: component_pb.PIDGains.AsObject,
  }
}

export class Float3D extends jspb.Message {
  getRoll(): number;
  setRoll(value: number): Float3D;

  getPitch(): number;
  setPitch(value: number): Float3D;

  getYaw(): number;
  setYaw(value: number): Float3D;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Float3D.AsObject;
  static toObject(includeInstance: boolean, msg: Float3D): Float3D.AsObject;
  static serializeBinaryToWriter(message: Float3D, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Float3D;
  static deserializeBinaryFromReader(message: Float3D, reader: jspb.BinaryReader): Float3D;
}

export namespace Float3D {
  export type AsObject = {
    roll: number,
    pitch: number,
    yaw: number,
  }
}

export class Orbita3DCommand extends jspb.Message {
  getId(): component_pb.ComponentId | undefined;
  setId(value?: component_pb.ComponentId): Orbita3DCommand;
  hasId(): boolean;
  clearId(): Orbita3DCommand;

  getCompliant(): google_protobuf_wrappers_pb.BoolValue | undefined;
  setCompliant(value?: google_protobuf_wrappers_pb.BoolValue): Orbita3DCommand;
  hasCompliant(): boolean;
  clearCompliant(): Orbita3DCommand;

  getGoalPosition(): kinematics_pb.Quaternion | undefined;
  setGoalPosition(value?: kinematics_pb.Quaternion): Orbita3DCommand;
  hasGoalPosition(): boolean;
  clearGoalPosition(): Orbita3DCommand;

  getSpeedLimit(): Float3D | undefined;
  setSpeedLimit(value?: Float3D): Orbita3DCommand;
  hasSpeedLimit(): boolean;
  clearSpeedLimit(): Orbita3DCommand;

  getTorqueLimit(): Float3D | undefined;
  setTorqueLimit(value?: Float3D): Orbita3DCommand;
  hasTorqueLimit(): boolean;
  clearTorqueLimit(): Orbita3DCommand;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Orbita3DCommand.AsObject;
  static toObject(includeInstance: boolean, msg: Orbita3DCommand): Orbita3DCommand.AsObject;
  static serializeBinaryToWriter(message: Orbita3DCommand, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Orbita3DCommand;
  static deserializeBinaryFromReader(message: Orbita3DCommand, reader: jspb.BinaryReader): Orbita3DCommand;
}

export namespace Orbita3DCommand {
  export type AsObject = {
    id?: component_pb.ComponentId.AsObject,
    compliant?: google_protobuf_wrappers_pb.BoolValue.AsObject,
    goalPosition?: kinematics_pb.Quaternion.AsObject,
    speedLimit?: Float3D.AsObject,
    torqueLimit?: Float3D.AsObject,
  }
}

export class Orbita3DInfo extends jspb.Message {
  getId(): component_pb.ComponentId | undefined;
  setId(value?: component_pb.ComponentId): Orbita3DInfo;
  hasId(): boolean;
  clearId(): Orbita3DInfo;

  getSerialNumber(): string;
  setSerialNumber(value: string): Orbita3DInfo;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Orbita3DInfo.AsObject;
  static toObject(includeInstance: boolean, msg: Orbita3DInfo): Orbita3DInfo.AsObject;
  static serializeBinaryToWriter(message: Orbita3DInfo, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Orbita3DInfo;
  static deserializeBinaryFromReader(message: Orbita3DInfo, reader: jspb.BinaryReader): Orbita3DInfo;
}

export namespace Orbita3DInfo {
  export type AsObject = {
    id?: component_pb.ComponentId.AsObject,
    serialNumber: string,
  }
}

export class ListOfOrbita3DInfo extends jspb.Message {
  getInfoList(): Array<Orbita3DInfo>;
  setInfoList(value: Array<Orbita3DInfo>): ListOfOrbita3DInfo;
  clearInfoList(): ListOfOrbita3DInfo;
  addInfo(value?: Orbita3DInfo, index?: number): Orbita3DInfo;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListOfOrbita3DInfo.AsObject;
  static toObject(includeInstance: boolean, msg: ListOfOrbita3DInfo): ListOfOrbita3DInfo.AsObject;
  static serializeBinaryToWriter(message: ListOfOrbita3DInfo, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListOfOrbita3DInfo;
  static deserializeBinaryFromReader(message: ListOfOrbita3DInfo, reader: jspb.BinaryReader): ListOfOrbita3DInfo;
}

export namespace ListOfOrbita3DInfo {
  export type AsObject = {
    infoList: Array<Orbita3DInfo.AsObject>,
  }
}

export class Orbita3DStatus extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Orbita3DStatus.AsObject;
  static toObject(includeInstance: boolean, msg: Orbita3DStatus): Orbita3DStatus.AsObject;
  static serializeBinaryToWriter(message: Orbita3DStatus, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Orbita3DStatus;
  static deserializeBinaryFromReader(message: Orbita3DStatus, reader: jspb.BinaryReader): Orbita3DStatus;
}

export namespace Orbita3DStatus {
  export type AsObject = {
  }
}

export enum Orbita3DField { 
  NONE = 0,
  NAME = 1,
  UID = 2,
  PRESENT_POSITION = 3,
  PRESENT_SPEED = 4,
  PRESENT_LOAD = 5,
  TEMPERATURE = 6,
  JOINT_LIMIT = 7,
  COMPLIANT = 8,
  GOAL_POSITION = 9,
  SPEED_LIMIT = 10,
  TORQUE_LIMIT = 11,
  PID = 12,
  ALL = 15,
}

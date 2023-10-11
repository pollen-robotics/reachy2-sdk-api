import * as jspb from 'google-protobuf'

import * as google_protobuf_wrappers_pb from 'google-protobuf/google/protobuf/wrappers_pb';
import * as google_protobuf_timestamp_pb from 'google-protobuf/google/protobuf/timestamp_pb';
import * as google_protobuf_empty_pb from 'google-protobuf/google/protobuf/empty_pb';
import * as component_pb from './component_pb';


export class Orbita2DState extends jspb.Message {
  getTimestamp(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTimestamp(value?: google_protobuf_timestamp_pb.Timestamp): Orbita2DState;
  hasTimestamp(): boolean;
  clearTimestamp(): Orbita2DState;

  getName(): string;
  setName(value: string): Orbita2DState;

  getId(): number;
  setId(value: number): Orbita2DState;

  getPresentPosition(): Pose2D | undefined;
  setPresentPosition(value?: Pose2D): Orbita2DState;
  hasPresentPosition(): boolean;
  clearPresentPosition(): Orbita2DState;

  getPresentSpeed(): Vector2D | undefined;
  setPresentSpeed(value?: Vector2D): Orbita2DState;
  hasPresentSpeed(): boolean;
  clearPresentSpeed(): Orbita2DState;

  getPresentLoad(): Vector2D | undefined;
  setPresentLoad(value?: Vector2D): Orbita2DState;
  hasPresentLoad(): boolean;
  clearPresentLoad(): Orbita2DState;

  getTemperature(): Float2D | undefined;
  setTemperature(value?: Float2D): Orbita2DState;
  hasTemperature(): boolean;
  clearTemperature(): Orbita2DState;

  getCompliant(): google_protobuf_wrappers_pb.BoolValue | undefined;
  setCompliant(value?: google_protobuf_wrappers_pb.BoolValue): Orbita2DState;
  hasCompliant(): boolean;
  clearCompliant(): Orbita2DState;

  getGoalPosition(): Pose2D | undefined;
  setGoalPosition(value?: Pose2D): Orbita2DState;
  hasGoalPosition(): boolean;
  clearGoalPosition(): Orbita2DState;

  getSpeedLimit(): Float2D | undefined;
  setSpeedLimit(value?: Float2D): Orbita2DState;
  hasSpeedLimit(): boolean;
  clearSpeedLimit(): Orbita2DState;

  getTorqueLimit(): Float2D | undefined;
  setTorqueLimit(value?: Float2D): Orbita2DState;
  hasTorqueLimit(): boolean;
  clearTorqueLimit(): Orbita2DState;

  getPid(): PID2D | undefined;
  setPid(value?: PID2D): Orbita2DState;
  hasPid(): boolean;
  clearPid(): Orbita2DState;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Orbita2DState.AsObject;
  static toObject(includeInstance: boolean, msg: Orbita2DState): Orbita2DState.AsObject;
  static serializeBinaryToWriter(message: Orbita2DState, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Orbita2DState;
  static deserializeBinaryFromReader(message: Orbita2DState, reader: jspb.BinaryReader): Orbita2DState;
}

export namespace Orbita2DState {
  export type AsObject = {
    timestamp?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    name: string,
    id: number,
    presentPosition?: Pose2D.AsObject,
    presentSpeed?: Vector2D.AsObject,
    presentLoad?: Vector2D.AsObject,
    temperature?: Float2D.AsObject,
    compliant?: google_protobuf_wrappers_pb.BoolValue.AsObject,
    goalPosition?: Pose2D.AsObject,
    speedLimit?: Float2D.AsObject,
    torqueLimit?: Float2D.AsObject,
    pid?: PID2D.AsObject,
  }
}

export class Orbita2DStateRequest extends jspb.Message {
  getFieldsList(): Array<Orbita2DField>;
  setFieldsList(value: Array<Orbita2DField>): Orbita2DStateRequest;
  clearFieldsList(): Orbita2DStateRequest;
  addFields(value: Orbita2DField, index?: number): Orbita2DStateRequest;

  getId(): component_pb.ComponentId | undefined;
  setId(value?: component_pb.ComponentId): Orbita2DStateRequest;
  hasId(): boolean;
  clearId(): Orbita2DStateRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Orbita2DStateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: Orbita2DStateRequest): Orbita2DStateRequest.AsObject;
  static serializeBinaryToWriter(message: Orbita2DStateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Orbita2DStateRequest;
  static deserializeBinaryFromReader(message: Orbita2DStateRequest, reader: jspb.BinaryReader): Orbita2DStateRequest;
}

export namespace Orbita2DStateRequest {
  export type AsObject = {
    fieldsList: Array<Orbita2DField>,
    id?: component_pb.ComponentId.AsObject,
  }
}

export class Orbita2DStreamStateRequest extends jspb.Message {
  getReq(): Orbita2DStateRequest | undefined;
  setReq(value?: Orbita2DStateRequest): Orbita2DStreamStateRequest;
  hasReq(): boolean;
  clearReq(): Orbita2DStreamStateRequest;

  getFreq(): number;
  setFreq(value: number): Orbita2DStreamStateRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Orbita2DStreamStateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: Orbita2DStreamStateRequest): Orbita2DStreamStateRequest.AsObject;
  static serializeBinaryToWriter(message: Orbita2DStreamStateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Orbita2DStreamStateRequest;
  static deserializeBinaryFromReader(message: Orbita2DStreamStateRequest, reader: jspb.BinaryReader): Orbita2DStreamStateRequest;
}

export namespace Orbita2DStreamStateRequest {
  export type AsObject = {
    req?: Orbita2DStateRequest.AsObject,
    freq: number,
  }
}

export class PID2D extends jspb.Message {
  getMotor1(): component_pb.PIDGains | undefined;
  setMotor1(value?: component_pb.PIDGains): PID2D;
  hasMotor1(): boolean;
  clearMotor1(): PID2D;

  getMotor2(): component_pb.PIDGains | undefined;
  setMotor2(value?: component_pb.PIDGains): PID2D;
  hasMotor2(): boolean;
  clearMotor2(): PID2D;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): PID2D.AsObject;
  static toObject(includeInstance: boolean, msg: PID2D): PID2D.AsObject;
  static serializeBinaryToWriter(message: PID2D, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): PID2D;
  static deserializeBinaryFromReader(message: PID2D, reader: jspb.BinaryReader): PID2D;
}

export namespace PID2D {
  export type AsObject = {
    motor1?: component_pb.PIDGains.AsObject,
    motor2?: component_pb.PIDGains.AsObject,
  }
}

export class Pose2D extends jspb.Message {
  getAxis1(): number;
  setAxis1(value: number): Pose2D;

  getAxis2(): number;
  setAxis2(value: number): Pose2D;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Pose2D.AsObject;
  static toObject(includeInstance: boolean, msg: Pose2D): Pose2D.AsObject;
  static serializeBinaryToWriter(message: Pose2D, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Pose2D;
  static deserializeBinaryFromReader(message: Pose2D, reader: jspb.BinaryReader): Pose2D;
}

export namespace Pose2D {
  export type AsObject = {
    axis1: number,
    axis2: number,
  }
}

export class Float2D extends jspb.Message {
  getMotor1(): number;
  setMotor1(value: number): Float2D;

  getMotor2(): number;
  setMotor2(value: number): Float2D;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Float2D.AsObject;
  static toObject(includeInstance: boolean, msg: Float2D): Float2D.AsObject;
  static serializeBinaryToWriter(message: Float2D, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Float2D;
  static deserializeBinaryFromReader(message: Float2D, reader: jspb.BinaryReader): Float2D;
}

export namespace Float2D {
  export type AsObject = {
    motor1: number,
    motor2: number,
  }
}

export class Vector2D extends jspb.Message {
  getX(): number;
  setX(value: number): Vector2D;

  getY(): number;
  setY(value: number): Vector2D;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Vector2D.AsObject;
  static toObject(includeInstance: boolean, msg: Vector2D): Vector2D.AsObject;
  static serializeBinaryToWriter(message: Vector2D, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Vector2D;
  static deserializeBinaryFromReader(message: Vector2D, reader: jspb.BinaryReader): Vector2D;
}

export namespace Vector2D {
  export type AsObject = {
    x: number,
    y: number,
  }
}

export class Orbita2DCommand extends jspb.Message {
  getId(): component_pb.ComponentId | undefined;
  setId(value?: component_pb.ComponentId): Orbita2DCommand;
  hasId(): boolean;
  clearId(): Orbita2DCommand;

  getCompliant(): google_protobuf_wrappers_pb.BoolValue | undefined;
  setCompliant(value?: google_protobuf_wrappers_pb.BoolValue): Orbita2DCommand;
  hasCompliant(): boolean;
  clearCompliant(): Orbita2DCommand;

  getGoalPosition(): Float2D | undefined;
  setGoalPosition(value?: Float2D): Orbita2DCommand;
  hasGoalPosition(): boolean;
  clearGoalPosition(): Orbita2DCommand;

  getSpeedLimit(): Float2D | undefined;
  setSpeedLimit(value?: Float2D): Orbita2DCommand;
  hasSpeedLimit(): boolean;
  clearSpeedLimit(): Orbita2DCommand;

  getTorqueLimit(): Float2D | undefined;
  setTorqueLimit(value?: Float2D): Orbita2DCommand;
  hasTorqueLimit(): boolean;
  clearTorqueLimit(): Orbita2DCommand;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Orbita2DCommand.AsObject;
  static toObject(includeInstance: boolean, msg: Orbita2DCommand): Orbita2DCommand.AsObject;
  static serializeBinaryToWriter(message: Orbita2DCommand, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Orbita2DCommand;
  static deserializeBinaryFromReader(message: Orbita2DCommand, reader: jspb.BinaryReader): Orbita2DCommand;
}

export namespace Orbita2DCommand {
  export type AsObject = {
    id?: component_pb.ComponentId.AsObject,
    compliant?: google_protobuf_wrappers_pb.BoolValue.AsObject,
    goalPosition?: Float2D.AsObject,
    speedLimit?: Float2D.AsObject,
    torqueLimit?: Float2D.AsObject,
  }
}

export class Orbita2DInfo extends jspb.Message {
  getId(): component_pb.ComponentId | undefined;
  setId(value?: component_pb.ComponentId): Orbita2DInfo;
  hasId(): boolean;
  clearId(): Orbita2DInfo;

  getSerialNumber(): string;
  setSerialNumber(value: string): Orbita2DInfo;

  getAxis1(): Axis;
  setAxis1(value: Axis): Orbita2DInfo;

  getAxis2(): Axis;
  setAxis2(value: Axis): Orbita2DInfo;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Orbita2DInfo.AsObject;
  static toObject(includeInstance: boolean, msg: Orbita2DInfo): Orbita2DInfo.AsObject;
  static serializeBinaryToWriter(message: Orbita2DInfo, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Orbita2DInfo;
  static deserializeBinaryFromReader(message: Orbita2DInfo, reader: jspb.BinaryReader): Orbita2DInfo;
}

export namespace Orbita2DInfo {
  export type AsObject = {
    id?: component_pb.ComponentId.AsObject,
    serialNumber: string,
    axis1: Axis,
    axis2: Axis,
  }
}

export class ListOfOrbita2DInfo extends jspb.Message {
  getInfoList(): Array<Orbita2DInfo>;
  setInfoList(value: Array<Orbita2DInfo>): ListOfOrbita2DInfo;
  clearInfoList(): ListOfOrbita2DInfo;
  addInfo(value?: Orbita2DInfo, index?: number): Orbita2DInfo;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListOfOrbita2DInfo.AsObject;
  static toObject(includeInstance: boolean, msg: ListOfOrbita2DInfo): ListOfOrbita2DInfo.AsObject;
  static serializeBinaryToWriter(message: ListOfOrbita2DInfo, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListOfOrbita2DInfo;
  static deserializeBinaryFromReader(message: ListOfOrbita2DInfo, reader: jspb.BinaryReader): ListOfOrbita2DInfo;
}

export namespace ListOfOrbita2DInfo {
  export type AsObject = {
    infoList: Array<Orbita2DInfo.AsObject>,
  }
}

export class Orbita2DStatus extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Orbita2DStatus.AsObject;
  static toObject(includeInstance: boolean, msg: Orbita2DStatus): Orbita2DStatus.AsObject;
  static serializeBinaryToWriter(message: Orbita2DStatus, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Orbita2DStatus;
  static deserializeBinaryFromReader(message: Orbita2DStatus, reader: jspb.BinaryReader): Orbita2DStatus;
}

export namespace Orbita2DStatus {
  export type AsObject = {
  }
}

export enum Orbita2DField { 
  NONE = 0,
  NAME = 1,
  ID = 2,
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
export enum Axis { 
  ROLL = 0,
  PITCH = 1,
  YAW = 2,
}

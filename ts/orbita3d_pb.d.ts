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

  getId(): component_pb.ComponentId | undefined;
  setId(value?: component_pb.ComponentId): Orbita3DState;
  hasId(): boolean;
  clearId(): Orbita3DState;

  getPresentPosition(): kinematics_pb.Rotation3D | undefined;
  setPresentPosition(value?: kinematics_pb.Rotation3D): Orbita3DState;
  hasPresentPosition(): boolean;
  clearPresentPosition(): Orbita3DState;

  getPresentSpeed(): Vector3D | undefined;
  setPresentSpeed(value?: Vector3D): Orbita3DState;
  hasPresentSpeed(): boolean;
  clearPresentSpeed(): Orbita3DState;

  getPresentLoad(): Vector3D | undefined;
  setPresentLoad(value?: Vector3D): Orbita3DState;
  hasPresentLoad(): boolean;
  clearPresentLoad(): Orbita3DState;

  getTemperature(): Float3D | undefined;
  setTemperature(value?: Float3D): Orbita3DState;
  hasTemperature(): boolean;
  clearTemperature(): Orbita3DState;

  getJointLimit(): Limits3D | undefined;
  setJointLimit(value?: Limits3D): Orbita3DState;
  hasJointLimit(): boolean;
  clearJointLimit(): Orbita3DState;

  getCompliant(): google_protobuf_wrappers_pb.BoolValue | undefined;
  setCompliant(value?: google_protobuf_wrappers_pb.BoolValue): Orbita3DState;
  hasCompliant(): boolean;
  clearCompliant(): Orbita3DState;

  getGoalPosition(): kinematics_pb.Rotation3D | undefined;
  setGoalPosition(value?: kinematics_pb.Rotation3D): Orbita3DState;
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
    id?: component_pb.ComponentId.AsObject,
    presentPosition?: kinematics_pb.Rotation3D.AsObject,
    presentSpeed?: Vector3D.AsObject,
    presentLoad?: Vector3D.AsObject,
    temperature?: Float3D.AsObject,
    jointLimit?: Limits3D.AsObject,
    compliant?: google_protobuf_wrappers_pb.BoolValue.AsObject,
    goalPosition?: kinematics_pb.Rotation3D.AsObject,
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
  getMotor1(): component_pb.PIDGains | undefined;
  setMotor1(value?: component_pb.PIDGains): PID3D;
  hasMotor1(): boolean;
  clearMotor1(): PID3D;

  getMotor2(): component_pb.PIDGains | undefined;
  setMotor2(value?: component_pb.PIDGains): PID3D;
  hasMotor2(): boolean;
  clearMotor2(): PID3D;

  getMotor3(): component_pb.PIDGains | undefined;
  setMotor3(value?: component_pb.PIDGains): PID3D;
  hasMotor3(): boolean;
  clearMotor3(): PID3D;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): PID3D.AsObject;
  static toObject(includeInstance: boolean, msg: PID3D): PID3D.AsObject;
  static serializeBinaryToWriter(message: PID3D, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): PID3D;
  static deserializeBinaryFromReader(message: PID3D, reader: jspb.BinaryReader): PID3D;
}

export namespace PID3D {
  export type AsObject = {
    motor1?: component_pb.PIDGains.AsObject,
    motor2?: component_pb.PIDGains.AsObject,
    motor3?: component_pb.PIDGains.AsObject,
  }
}

export class Limits3D extends jspb.Message {
  getRoll(): component_pb.JointLimits | undefined;
  setRoll(value?: component_pb.JointLimits): Limits3D;
  hasRoll(): boolean;
  clearRoll(): Limits3D;

  getPitch(): component_pb.JointLimits | undefined;
  setPitch(value?: component_pb.JointLimits): Limits3D;
  hasPitch(): boolean;
  clearPitch(): Limits3D;

  getYaw(): component_pb.JointLimits | undefined;
  setYaw(value?: component_pb.JointLimits): Limits3D;
  hasYaw(): boolean;
  clearYaw(): Limits3D;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Limits3D.AsObject;
  static toObject(includeInstance: boolean, msg: Limits3D): Limits3D.AsObject;
  static serializeBinaryToWriter(message: Limits3D, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Limits3D;
  static deserializeBinaryFromReader(message: Limits3D, reader: jspb.BinaryReader): Limits3D;
}

export namespace Limits3D {
  export type AsObject = {
    roll?: component_pb.JointLimits.AsObject,
    pitch?: component_pb.JointLimits.AsObject,
    yaw?: component_pb.JointLimits.AsObject,
  }
}

export class Float3D extends jspb.Message {
  getMotor1(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setMotor1(value?: google_protobuf_wrappers_pb.FloatValue): Float3D;
  hasMotor1(): boolean;
  clearMotor1(): Float3D;

  getMotor2(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setMotor2(value?: google_protobuf_wrappers_pb.FloatValue): Float3D;
  hasMotor2(): boolean;
  clearMotor2(): Float3D;

  getMotor3(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setMotor3(value?: google_protobuf_wrappers_pb.FloatValue): Float3D;
  hasMotor3(): boolean;
  clearMotor3(): Float3D;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Float3D.AsObject;
  static toObject(includeInstance: boolean, msg: Float3D): Float3D.AsObject;
  static serializeBinaryToWriter(message: Float3D, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Float3D;
  static deserializeBinaryFromReader(message: Float3D, reader: jspb.BinaryReader): Float3D;
}

export namespace Float3D {
  export type AsObject = {
    motor1?: google_protobuf_wrappers_pb.FloatValue.AsObject,
    motor2?: google_protobuf_wrappers_pb.FloatValue.AsObject,
    motor3?: google_protobuf_wrappers_pb.FloatValue.AsObject,
  }
}

export class Vector3D extends jspb.Message {
  getX(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setX(value?: google_protobuf_wrappers_pb.FloatValue): Vector3D;
  hasX(): boolean;
  clearX(): Vector3D;

  getY(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setY(value?: google_protobuf_wrappers_pb.FloatValue): Vector3D;
  hasY(): boolean;
  clearY(): Vector3D;

  getZ(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setZ(value?: google_protobuf_wrappers_pb.FloatValue): Vector3D;
  hasZ(): boolean;
  clearZ(): Vector3D;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Vector3D.AsObject;
  static toObject(includeInstance: boolean, msg: Vector3D): Vector3D.AsObject;
  static serializeBinaryToWriter(message: Vector3D, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Vector3D;
  static deserializeBinaryFromReader(message: Vector3D, reader: jspb.BinaryReader): Vector3D;
}

export namespace Vector3D {
  export type AsObject = {
    x?: google_protobuf_wrappers_pb.FloatValue.AsObject,
    y?: google_protobuf_wrappers_pb.FloatValue.AsObject,
    z?: google_protobuf_wrappers_pb.FloatValue.AsObject,
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

  getGoalPosition(): kinematics_pb.Rotation3D | undefined;
  setGoalPosition(value?: kinematics_pb.Rotation3D): Orbita3DCommand;
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

  getPid(): PID3D | undefined;
  setPid(value?: PID3D): Orbita3DCommand;
  hasPid(): boolean;
  clearPid(): Orbita3DCommand;

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
    goalPosition?: kinematics_pb.Rotation3D.AsObject,
    speedLimit?: Float3D.AsObject,
    torqueLimit?: Float3D.AsObject,
    pid?: PID3D.AsObject,
  }
}

export class Orbita3DsCommand extends jspb.Message {
  getCmdList(): Array<Orbita3DCommand>;
  setCmdList(value: Array<Orbita3DCommand>): Orbita3DsCommand;
  clearCmdList(): Orbita3DsCommand;
  addCmd(value?: Orbita3DCommand, index?: number): Orbita3DCommand;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Orbita3DsCommand.AsObject;
  static toObject(includeInstance: boolean, msg: Orbita3DsCommand): Orbita3DsCommand.AsObject;
  static serializeBinaryToWriter(message: Orbita3DsCommand, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Orbita3DsCommand;
  static deserializeBinaryFromReader(message: Orbita3DsCommand, reader: jspb.BinaryReader): Orbita3DsCommand;
}

export namespace Orbita3DsCommand {
  export type AsObject = {
    cmdList: Array<Orbita3DCommand.AsObject>,
  }
}

export class Orbita3D extends jspb.Message {
  getId(): component_pb.ComponentId | undefined;
  setId(value?: component_pb.ComponentId): Orbita3D;
  hasId(): boolean;
  clearId(): Orbita3D;

  getSerialNumber(): string;
  setSerialNumber(value: string): Orbita3D;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Orbita3D.AsObject;
  static toObject(includeInstance: boolean, msg: Orbita3D): Orbita3D.AsObject;
  static serializeBinaryToWriter(message: Orbita3D, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Orbita3D;
  static deserializeBinaryFromReader(message: Orbita3D, reader: jspb.BinaryReader): Orbita3D;
}

export namespace Orbita3D {
  export type AsObject = {
    id?: component_pb.ComponentId.AsObject,
    serialNumber: string,
  }
}

export class ListOfOrbita3D extends jspb.Message {
  getInfoList(): Array<Orbita3D>;
  setInfoList(value: Array<Orbita3D>): ListOfOrbita3D;
  clearInfoList(): ListOfOrbita3D;
  addInfo(value?: Orbita3D, index?: number): Orbita3D;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListOfOrbita3D.AsObject;
  static toObject(includeInstance: boolean, msg: ListOfOrbita3D): ListOfOrbita3D.AsObject;
  static serializeBinaryToWriter(message: ListOfOrbita3D, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListOfOrbita3D;
  static deserializeBinaryFromReader(message: ListOfOrbita3D, reader: jspb.BinaryReader): ListOfOrbita3D;
}

export namespace ListOfOrbita3D {
  export type AsObject = {
    infoList: Array<Orbita3D.AsObject>,
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

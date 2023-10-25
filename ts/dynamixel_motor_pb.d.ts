import * as jspb from 'google-protobuf'

import * as google_protobuf_timestamp_pb from 'google-protobuf/google/protobuf/timestamp_pb';
import * as google_protobuf_empty_pb from 'google-protobuf/google/protobuf/empty_pb';
import * as google_protobuf_wrappers_pb from 'google-protobuf/google/protobuf/wrappers_pb';
import * as component_pb from './component_pb';


export class DynamixelMotorState extends jspb.Message {
  getTimestamp(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTimestamp(value?: google_protobuf_timestamp_pb.Timestamp): DynamixelMotorState;
  hasTimestamp(): boolean;
  clearTimestamp(): DynamixelMotorState;

  getId(): component_pb.ComponentId | undefined;
  setId(value?: component_pb.ComponentId): DynamixelMotorState;
  hasId(): boolean;
  clearId(): DynamixelMotorState;

  getPresentPosition(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setPresentPosition(value?: google_protobuf_wrappers_pb.FloatValue): DynamixelMotorState;
  hasPresentPosition(): boolean;
  clearPresentPosition(): DynamixelMotorState;

  getPresentSpeed(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setPresentSpeed(value?: google_protobuf_wrappers_pb.FloatValue): DynamixelMotorState;
  hasPresentSpeed(): boolean;
  clearPresentSpeed(): DynamixelMotorState;

  getPresentLoad(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setPresentLoad(value?: google_protobuf_wrappers_pb.FloatValue): DynamixelMotorState;
  hasPresentLoad(): boolean;
  clearPresentLoad(): DynamixelMotorState;

  getTemperature(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setTemperature(value?: google_protobuf_wrappers_pb.FloatValue): DynamixelMotorState;
  hasTemperature(): boolean;
  clearTemperature(): DynamixelMotorState;

  getJointLimit(): component_pb.JointLimits | undefined;
  setJointLimit(value?: component_pb.JointLimits): DynamixelMotorState;
  hasJointLimit(): boolean;
  clearJointLimit(): DynamixelMotorState;

  getCompliant(): google_protobuf_wrappers_pb.BoolValue | undefined;
  setCompliant(value?: google_protobuf_wrappers_pb.BoolValue): DynamixelMotorState;
  hasCompliant(): boolean;
  clearCompliant(): DynamixelMotorState;

  getGoalPosition(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setGoalPosition(value?: google_protobuf_wrappers_pb.FloatValue): DynamixelMotorState;
  hasGoalPosition(): boolean;
  clearGoalPosition(): DynamixelMotorState;

  getSpeedLimit(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setSpeedLimit(value?: google_protobuf_wrappers_pb.FloatValue): DynamixelMotorState;
  hasSpeedLimit(): boolean;
  clearSpeedLimit(): DynamixelMotorState;

  getTorqueLimit(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setTorqueLimit(value?: google_protobuf_wrappers_pb.FloatValue): DynamixelMotorState;
  hasTorqueLimit(): boolean;
  clearTorqueLimit(): DynamixelMotorState;

  getPid(): component_pb.PIDGains | undefined;
  setPid(value?: component_pb.PIDGains): DynamixelMotorState;
  hasPid(): boolean;
  clearPid(): DynamixelMotorState;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DynamixelMotorState.AsObject;
  static toObject(includeInstance: boolean, msg: DynamixelMotorState): DynamixelMotorState.AsObject;
  static serializeBinaryToWriter(message: DynamixelMotorState, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DynamixelMotorState;
  static deserializeBinaryFromReader(message: DynamixelMotorState, reader: jspb.BinaryReader): DynamixelMotorState;
}

export namespace DynamixelMotorState {
  export type AsObject = {
    timestamp?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    id?: component_pb.ComponentId.AsObject,
    presentPosition?: google_protobuf_wrappers_pb.FloatValue.AsObject,
    presentSpeed?: google_protobuf_wrappers_pb.FloatValue.AsObject,
    presentLoad?: google_protobuf_wrappers_pb.FloatValue.AsObject,
    temperature?: google_protobuf_wrappers_pb.FloatValue.AsObject,
    jointLimit?: component_pb.JointLimits.AsObject,
    compliant?: google_protobuf_wrappers_pb.BoolValue.AsObject,
    goalPosition?: google_protobuf_wrappers_pb.FloatValue.AsObject,
    speedLimit?: google_protobuf_wrappers_pb.FloatValue.AsObject,
    torqueLimit?: google_protobuf_wrappers_pb.FloatValue.AsObject,
    pid?: component_pb.PIDGains.AsObject,
  }
}

export class DynamixelMotorStateRequest extends jspb.Message {
  getFieldsList(): Array<DynamixelMotorField>;
  setFieldsList(value: Array<DynamixelMotorField>): DynamixelMotorStateRequest;
  clearFieldsList(): DynamixelMotorStateRequest;
  addFields(value: DynamixelMotorField, index?: number): DynamixelMotorStateRequest;

  getId(): component_pb.ComponentId | undefined;
  setId(value?: component_pb.ComponentId): DynamixelMotorStateRequest;
  hasId(): boolean;
  clearId(): DynamixelMotorStateRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DynamixelMotorStateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DynamixelMotorStateRequest): DynamixelMotorStateRequest.AsObject;
  static serializeBinaryToWriter(message: DynamixelMotorStateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DynamixelMotorStateRequest;
  static deserializeBinaryFromReader(message: DynamixelMotorStateRequest, reader: jspb.BinaryReader): DynamixelMotorStateRequest;
}

export namespace DynamixelMotorStateRequest {
  export type AsObject = {
    fieldsList: Array<DynamixelMotorField>,
    id?: component_pb.ComponentId.AsObject,
  }
}

export class DynamixelMotorStreamStateRequest extends jspb.Message {
  getReq(): DynamixelMotorStateRequest | undefined;
  setReq(value?: DynamixelMotorStateRequest): DynamixelMotorStreamStateRequest;
  hasReq(): boolean;
  clearReq(): DynamixelMotorStreamStateRequest;

  getFreq(): number;
  setFreq(value: number): DynamixelMotorStreamStateRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DynamixelMotorStreamStateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DynamixelMotorStreamStateRequest): DynamixelMotorStreamStateRequest.AsObject;
  static serializeBinaryToWriter(message: DynamixelMotorStreamStateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DynamixelMotorStreamStateRequest;
  static deserializeBinaryFromReader(message: DynamixelMotorStreamStateRequest, reader: jspb.BinaryReader): DynamixelMotorStreamStateRequest;
}

export namespace DynamixelMotorStreamStateRequest {
  export type AsObject = {
    req?: DynamixelMotorStateRequest.AsObject,
    freq: number,
  }
}

export class DynamixelMotorGoal extends jspb.Message {
  getId(): component_pb.ComponentId | undefined;
  setId(value?: component_pb.ComponentId): DynamixelMotorGoal;
  hasId(): boolean;
  clearId(): DynamixelMotorGoal;

  getGoalPosition(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setGoalPosition(value?: google_protobuf_wrappers_pb.FloatValue): DynamixelMotorGoal;
  hasGoalPosition(): boolean;
  clearGoalPosition(): DynamixelMotorGoal;

  getDuration(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setDuration(value?: google_protobuf_wrappers_pb.FloatValue): DynamixelMotorGoal;
  hasDuration(): boolean;
  clearDuration(): DynamixelMotorGoal;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DynamixelMotorGoal.AsObject;
  static toObject(includeInstance: boolean, msg: DynamixelMotorGoal): DynamixelMotorGoal.AsObject;
  static serializeBinaryToWriter(message: DynamixelMotorGoal, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DynamixelMotorGoal;
  static deserializeBinaryFromReader(message: DynamixelMotorGoal, reader: jspb.BinaryReader): DynamixelMotorGoal;
}

export namespace DynamixelMotorGoal {
  export type AsObject = {
    id?: component_pb.ComponentId.AsObject,
    goalPosition?: google_protobuf_wrappers_pb.FloatValue.AsObject,
    duration?: google_protobuf_wrappers_pb.FloatValue.AsObject,
  }
}

export class DynamixelMotorCommand extends jspb.Message {
  getId(): component_pb.ComponentId | undefined;
  setId(value?: component_pb.ComponentId): DynamixelMotorCommand;
  hasId(): boolean;
  clearId(): DynamixelMotorCommand;

  getCompliant(): google_protobuf_wrappers_pb.BoolValue | undefined;
  setCompliant(value?: google_protobuf_wrappers_pb.BoolValue): DynamixelMotorCommand;
  hasCompliant(): boolean;
  clearCompliant(): DynamixelMotorCommand;

  getGoalPosition(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setGoalPosition(value?: google_protobuf_wrappers_pb.FloatValue): DynamixelMotorCommand;
  hasGoalPosition(): boolean;
  clearGoalPosition(): DynamixelMotorCommand;

  getSpeedLimit(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setSpeedLimit(value?: google_protobuf_wrappers_pb.FloatValue): DynamixelMotorCommand;
  hasSpeedLimit(): boolean;
  clearSpeedLimit(): DynamixelMotorCommand;

  getTorqueLimit(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setTorqueLimit(value?: google_protobuf_wrappers_pb.FloatValue): DynamixelMotorCommand;
  hasTorqueLimit(): boolean;
  clearTorqueLimit(): DynamixelMotorCommand;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DynamixelMotorCommand.AsObject;
  static toObject(includeInstance: boolean, msg: DynamixelMotorCommand): DynamixelMotorCommand.AsObject;
  static serializeBinaryToWriter(message: DynamixelMotorCommand, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DynamixelMotorCommand;
  static deserializeBinaryFromReader(message: DynamixelMotorCommand, reader: jspb.BinaryReader): DynamixelMotorCommand;
}

export namespace DynamixelMotorCommand {
  export type AsObject = {
    id?: component_pb.ComponentId.AsObject,
    compliant?: google_protobuf_wrappers_pb.BoolValue.AsObject,
    goalPosition?: google_protobuf_wrappers_pb.FloatValue.AsObject,
    speedLimit?: google_protobuf_wrappers_pb.FloatValue.AsObject,
    torqueLimit?: google_protobuf_wrappers_pb.FloatValue.AsObject,
  }
}

export class DynamixelMotorsCommand extends jspb.Message {
  getCmdList(): Array<DynamixelMotorCommand>;
  setCmdList(value: Array<DynamixelMotorCommand>): DynamixelMotorsCommand;
  clearCmdList(): DynamixelMotorsCommand;
  addCmd(value?: DynamixelMotorCommand, index?: number): DynamixelMotorCommand;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DynamixelMotorsCommand.AsObject;
  static toObject(includeInstance: boolean, msg: DynamixelMotorsCommand): DynamixelMotorsCommand.AsObject;
  static serializeBinaryToWriter(message: DynamixelMotorsCommand, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DynamixelMotorsCommand;
  static deserializeBinaryFromReader(message: DynamixelMotorsCommand, reader: jspb.BinaryReader): DynamixelMotorsCommand;
}

export namespace DynamixelMotorsCommand {
  export type AsObject = {
    cmdList: Array<DynamixelMotorCommand.AsObject>,
  }
}

export class DynamixelMotor extends jspb.Message {
  getId(): component_pb.ComponentId | undefined;
  setId(value?: component_pb.ComponentId): DynamixelMotor;
  hasId(): boolean;
  clearId(): DynamixelMotor;

  getSerialNumber(): string;
  setSerialNumber(value: string): DynamixelMotor;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DynamixelMotor.AsObject;
  static toObject(includeInstance: boolean, msg: DynamixelMotor): DynamixelMotor.AsObject;
  static serializeBinaryToWriter(message: DynamixelMotor, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DynamixelMotor;
  static deserializeBinaryFromReader(message: DynamixelMotor, reader: jspb.BinaryReader): DynamixelMotor;
}

export namespace DynamixelMotor {
  export type AsObject = {
    id?: component_pb.ComponentId.AsObject,
    serialNumber: string,
  }
}

export class ListOfDynamixelMotor extends jspb.Message {
  getInfoList(): Array<DynamixelMotor>;
  setInfoList(value: Array<DynamixelMotor>): ListOfDynamixelMotor;
  clearInfoList(): ListOfDynamixelMotor;
  addInfo(value?: DynamixelMotor, index?: number): DynamixelMotor;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListOfDynamixelMotor.AsObject;
  static toObject(includeInstance: boolean, msg: ListOfDynamixelMotor): ListOfDynamixelMotor.AsObject;
  static serializeBinaryToWriter(message: ListOfDynamixelMotor, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListOfDynamixelMotor;
  static deserializeBinaryFromReader(message: ListOfDynamixelMotor, reader: jspb.BinaryReader): ListOfDynamixelMotor;
}

export namespace ListOfDynamixelMotor {
  export type AsObject = {
    infoList: Array<DynamixelMotor.AsObject>,
  }
}

export class DynamixelMotorStatus extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DynamixelMotorStatus.AsObject;
  static toObject(includeInstance: boolean, msg: DynamixelMotorStatus): DynamixelMotorStatus.AsObject;
  static serializeBinaryToWriter(message: DynamixelMotorStatus, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DynamixelMotorStatus;
  static deserializeBinaryFromReader(message: DynamixelMotorStatus, reader: jspb.BinaryReader): DynamixelMotorStatus;
}

export namespace DynamixelMotorStatus {
  export type AsObject = {
  }
}

export enum DynamixelMotorField { 
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

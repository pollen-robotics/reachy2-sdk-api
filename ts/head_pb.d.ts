import * as jspb from 'google-protobuf'

import * as google_protobuf_wrappers_pb from 'google-protobuf/google/protobuf/wrappers_pb';
import * as google_protobuf_empty_pb from 'google-protobuf/google/protobuf/empty_pb';
import * as google_protobuf_timestamp_pb from 'google-protobuf/google/protobuf/timestamp_pb';
import * as part_pb from './part_pb';
import * as kinematics_pb from './kinematics_pb';
import * as error_pb from './error_pb';
import * as orbita3d_pb from './orbita3d_pb';
import * as dynamixel_motor_pb from './dynamixel_motor_pb';


export class Head extends jspb.Message {
  getPartId(): part_pb.PartId | undefined;
  setPartId(value?: part_pb.PartId): Head;
  hasPartId(): boolean;
  clearPartId(): Head;

  getDescription(): HeadDescription | undefined;
  setDescription(value?: HeadDescription): Head;
  hasDescription(): boolean;
  clearDescription(): Head;

  getInfo(): part_pb.PartInfo | undefined;
  setInfo(value?: part_pb.PartInfo): Head;
  hasInfo(): boolean;
  clearInfo(): Head;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Head.AsObject;
  static toObject(includeInstance: boolean, msg: Head): Head.AsObject;
  static serializeBinaryToWriter(message: Head, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Head;
  static deserializeBinaryFromReader(message: Head, reader: jspb.BinaryReader): Head;
}

export namespace Head {
  export type AsObject = {
    partId?: part_pb.PartId.AsObject,
    description?: HeadDescription.AsObject,
    info?: part_pb.PartInfo.AsObject,
  }
}

export class HeadDescription extends jspb.Message {
  getNeck(): orbita3d_pb.Orbita3DInfo | undefined;
  setNeck(value?: orbita3d_pb.Orbita3DInfo): HeadDescription;
  hasNeck(): boolean;
  clearNeck(): HeadDescription;

  getLAntenna(): dynamixel_motor_pb.DynamixelMotorInfo | undefined;
  setLAntenna(value?: dynamixel_motor_pb.DynamixelMotorInfo): HeadDescription;
  hasLAntenna(): boolean;
  clearLAntenna(): HeadDescription;

  getRAntenna(): dynamixel_motor_pb.DynamixelMotorInfo | undefined;
  setRAntenna(value?: dynamixel_motor_pb.DynamixelMotorInfo): HeadDescription;
  hasRAntenna(): boolean;
  clearRAntenna(): HeadDescription;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HeadDescription.AsObject;
  static toObject(includeInstance: boolean, msg: HeadDescription): HeadDescription.AsObject;
  static serializeBinaryToWriter(message: HeadDescription, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HeadDescription;
  static deserializeBinaryFromReader(message: HeadDescription, reader: jspb.BinaryReader): HeadDescription;
}

export namespace HeadDescription {
  export type AsObject = {
    neck?: orbita3d_pb.Orbita3DInfo.AsObject,
    lAntenna?: dynamixel_motor_pb.DynamixelMotorInfo.AsObject,
    rAntenna?: dynamixel_motor_pb.DynamixelMotorInfo.AsObject,
  }
}

export class ListOfHead extends jspb.Message {
  getHeadList(): Array<Head>;
  setHeadList(value: Array<Head>): ListOfHead;
  clearHeadList(): ListOfHead;
  addHead(value?: Head, index?: number): Head;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListOfHead.AsObject;
  static toObject(includeInstance: boolean, msg: ListOfHead): ListOfHead.AsObject;
  static serializeBinaryToWriter(message: ListOfHead, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListOfHead;
  static deserializeBinaryFromReader(message: ListOfHead, reader: jspb.BinaryReader): ListOfHead;
}

export namespace ListOfHead {
  export type AsObject = {
    headList: Array<Head.AsObject>,
  }
}

export class HeadState extends jspb.Message {
  getTimestamp(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTimestamp(value?: google_protobuf_timestamp_pb.Timestamp): HeadState;
  hasTimestamp(): boolean;
  clearTimestamp(): HeadState;

  getName(): string;
  setName(value: string): HeadState;

  getId(): number;
  setId(value: number): HeadState;

  getActivated(): boolean;
  setActivated(value: boolean): HeadState;

  getNeckState(): orbita3d_pb.Orbita3DState | undefined;
  setNeckState(value?: orbita3d_pb.Orbita3DState): HeadState;
  hasNeckState(): boolean;
  clearNeckState(): HeadState;

  getLAntennaState(): dynamixel_motor_pb.DynamixelMotorState | undefined;
  setLAntennaState(value?: dynamixel_motor_pb.DynamixelMotorState): HeadState;
  hasLAntennaState(): boolean;
  clearLAntennaState(): HeadState;

  getRAntennaState(): dynamixel_motor_pb.DynamixelMotorState | undefined;
  setRAntennaState(value?: dynamixel_motor_pb.DynamixelMotorState): HeadState;
  hasRAntennaState(): boolean;
  clearRAntennaState(): HeadState;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HeadState.AsObject;
  static toObject(includeInstance: boolean, msg: HeadState): HeadState.AsObject;
  static serializeBinaryToWriter(message: HeadState, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HeadState;
  static deserializeBinaryFromReader(message: HeadState, reader: jspb.BinaryReader): HeadState;
}

export namespace HeadState {
  export type AsObject = {
    timestamp?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    name: string,
    id: number,
    activated: boolean,
    neckState?: orbita3d_pb.Orbita3DState.AsObject,
    lAntennaState?: dynamixel_motor_pb.DynamixelMotorState.AsObject,
    rAntennaState?: dynamixel_motor_pb.DynamixelMotorState.AsObject,
  }
}

export class NeckPosition extends jspb.Message {
  getNeckRoll(): number;
  setNeckRoll(value: number): NeckPosition;

  getNeckPitch(): number;
  setNeckPitch(value: number): NeckPosition;

  getNeckYaw(): number;
  setNeckYaw(value: number): NeckPosition;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): NeckPosition.AsObject;
  static toObject(includeInstance: boolean, msg: NeckPosition): NeckPosition.AsObject;
  static serializeBinaryToWriter(message: NeckPosition, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): NeckPosition;
  static deserializeBinaryFromReader(message: NeckPosition, reader: jspb.BinaryReader): NeckPosition;
}

export namespace NeckPosition {
  export type AsObject = {
    neckRoll: number,
    neckPitch: number,
    neckYaw: number,
  }
}

export class HeadPosition extends jspb.Message {
  getNeckPosition(): NeckPosition | undefined;
  setNeckPosition(value?: NeckPosition): HeadPosition;
  hasNeckPosition(): boolean;
  clearNeckPosition(): HeadPosition;

  getLAntennaPosition(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setLAntennaPosition(value?: google_protobuf_wrappers_pb.FloatValue): HeadPosition;
  hasLAntennaPosition(): boolean;
  clearLAntennaPosition(): HeadPosition;

  getRAntennaPosition(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setRAntennaPosition(value?: google_protobuf_wrappers_pb.FloatValue): HeadPosition;
  hasRAntennaPosition(): boolean;
  clearRAntennaPosition(): HeadPosition;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HeadPosition.AsObject;
  static toObject(includeInstance: boolean, msg: HeadPosition): HeadPosition.AsObject;
  static serializeBinaryToWriter(message: HeadPosition, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HeadPosition;
  static deserializeBinaryFromReader(message: HeadPosition, reader: jspb.BinaryReader): HeadPosition;
}

export namespace HeadPosition {
  export type AsObject = {
    neckPosition?: NeckPosition.AsObject,
    lAntennaPosition?: google_protobuf_wrappers_pb.FloatValue.AsObject,
    rAntennaPosition?: google_protobuf_wrappers_pb.FloatValue.AsObject,
  }
}

export class NeckGoal extends jspb.Message {
  getId(): part_pb.PartId | undefined;
  setId(value?: part_pb.PartId): NeckGoal;
  hasId(): boolean;
  clearId(): NeckGoal;

  getRotation(): kinematics_pb.Rotation3D | undefined;
  setRotation(value?: kinematics_pb.Rotation3D): NeckGoal;
  hasRotation(): boolean;
  clearRotation(): NeckGoal;

  getDuration(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setDuration(value?: google_protobuf_wrappers_pb.FloatValue): NeckGoal;
  hasDuration(): boolean;
  clearDuration(): NeckGoal;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): NeckGoal.AsObject;
  static toObject(includeInstance: boolean, msg: NeckGoal): NeckGoal.AsObject;
  static serializeBinaryToWriter(message: NeckGoal, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): NeckGoal;
  static deserializeBinaryFromReader(message: NeckGoal, reader: jspb.BinaryReader): NeckGoal;
}

export namespace NeckGoal {
  export type AsObject = {
    id?: part_pb.PartId.AsObject,
    rotation?: kinematics_pb.Rotation3D.AsObject,
    duration?: google_protobuf_wrappers_pb.FloatValue.AsObject,
  }
}

export class NeckOrientation extends jspb.Message {
  getQ(): kinematics_pb.Quaternion | undefined;
  setQ(value?: kinematics_pb.Quaternion): NeckOrientation;
  hasQ(): boolean;
  clearQ(): NeckOrientation;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): NeckOrientation.AsObject;
  static toObject(includeInstance: boolean, msg: NeckOrientation): NeckOrientation.AsObject;
  static serializeBinaryToWriter(message: NeckOrientation, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): NeckOrientation;
  static deserializeBinaryFromReader(message: NeckOrientation, reader: jspb.BinaryReader): NeckOrientation;
}

export namespace NeckOrientation {
  export type AsObject = {
    q?: kinematics_pb.Quaternion.AsObject,
  }
}

export class NeckFKRequest extends jspb.Message {
  getId(): part_pb.PartId | undefined;
  setId(value?: part_pb.PartId): NeckFKRequest;
  hasId(): boolean;
  clearId(): NeckFKRequest;

  getPosition(): HeadPosition | undefined;
  setPosition(value?: HeadPosition): NeckFKRequest;
  hasPosition(): boolean;
  clearPosition(): NeckFKRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): NeckFKRequest.AsObject;
  static toObject(includeInstance: boolean, msg: NeckFKRequest): NeckFKRequest.AsObject;
  static serializeBinaryToWriter(message: NeckFKRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): NeckFKRequest;
  static deserializeBinaryFromReader(message: NeckFKRequest, reader: jspb.BinaryReader): NeckFKRequest;
}

export namespace NeckFKRequest {
  export type AsObject = {
    id?: part_pb.PartId.AsObject,
    position?: HeadPosition.AsObject,
  }
}

export class NeckFKSolution extends jspb.Message {
  getSuccess(): boolean;
  setSuccess(value: boolean): NeckFKSolution;

  getOrientation(): NeckOrientation | undefined;
  setOrientation(value?: NeckOrientation): NeckFKSolution;
  hasOrientation(): boolean;
  clearOrientation(): NeckFKSolution;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): NeckFKSolution.AsObject;
  static toObject(includeInstance: boolean, msg: NeckFKSolution): NeckFKSolution.AsObject;
  static serializeBinaryToWriter(message: NeckFKSolution, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): NeckFKSolution;
  static deserializeBinaryFromReader(message: NeckFKSolution, reader: jspb.BinaryReader): NeckFKSolution;
}

export namespace NeckFKSolution {
  export type AsObject = {
    success: boolean,
    orientation?: NeckOrientation.AsObject,
  }
}

export class NeckIKRequest extends jspb.Message {
  getId(): part_pb.PartId | undefined;
  setId(value?: part_pb.PartId): NeckIKRequest;
  hasId(): boolean;
  clearId(): NeckIKRequest;

  getTarget(): NeckOrientation | undefined;
  setTarget(value?: NeckOrientation): NeckIKRequest;
  hasTarget(): boolean;
  clearTarget(): NeckIKRequest;

  getQ0(): NeckPosition | undefined;
  setQ0(value?: NeckPosition): NeckIKRequest;
  hasQ0(): boolean;
  clearQ0(): NeckIKRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): NeckIKRequest.AsObject;
  static toObject(includeInstance: boolean, msg: NeckIKRequest): NeckIKRequest.AsObject;
  static serializeBinaryToWriter(message: NeckIKRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): NeckIKRequest;
  static deserializeBinaryFromReader(message: NeckIKRequest, reader: jspb.BinaryReader): NeckIKRequest;
}

export namespace NeckIKRequest {
  export type AsObject = {
    id?: part_pb.PartId.AsObject,
    target?: NeckOrientation.AsObject,
    q0?: NeckPosition.AsObject,
  }
}

export class NeckIKSolution extends jspb.Message {
  getSuccess(): boolean;
  setSuccess(value: boolean): NeckIKSolution;

  getPosition(): NeckPosition | undefined;
  setPosition(value?: NeckPosition): NeckIKSolution;
  hasPosition(): boolean;
  clearPosition(): NeckIKSolution;

  getError(): error_pb.Error | undefined;
  setError(value?: error_pb.Error): NeckIKSolution;
  hasError(): boolean;
  clearError(): NeckIKSolution;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): NeckIKSolution.AsObject;
  static toObject(includeInstance: boolean, msg: NeckIKSolution): NeckIKSolution.AsObject;
  static serializeBinaryToWriter(message: NeckIKSolution, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): NeckIKSolution;
  static deserializeBinaryFromReader(message: NeckIKSolution, reader: jspb.BinaryReader): NeckIKSolution;
}

export namespace NeckIKSolution {
  export type AsObject = {
    success: boolean,
    position?: NeckPosition.AsObject,
    error?: error_pb.Error.AsObject,
  }
}

export class HeadStatus extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HeadStatus.AsObject;
  static toObject(includeInstance: boolean, msg: HeadStatus): HeadStatus.AsObject;
  static serializeBinaryToWriter(message: HeadStatus, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HeadStatus;
  static deserializeBinaryFromReader(message: HeadStatus, reader: jspb.BinaryReader): HeadStatus;
}

export namespace HeadStatus {
  export type AsObject = {
  }
}

export class HeadLookAtGoal extends jspb.Message {
  getId(): part_pb.PartId | undefined;
  setId(value?: part_pb.PartId): HeadLookAtGoal;
  hasId(): boolean;
  clearId(): HeadLookAtGoal;

  getPoint(): kinematics_pb.Point | undefined;
  setPoint(value?: kinematics_pb.Point): HeadLookAtGoal;
  hasPoint(): boolean;
  clearPoint(): HeadLookAtGoal;

  getDuration(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setDuration(value?: google_protobuf_wrappers_pb.FloatValue): HeadLookAtGoal;
  hasDuration(): boolean;
  clearDuration(): HeadLookAtGoal;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HeadLookAtGoal.AsObject;
  static toObject(includeInstance: boolean, msg: HeadLookAtGoal): HeadLookAtGoal.AsObject;
  static serializeBinaryToWriter(message: HeadLookAtGoal, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HeadLookAtGoal;
  static deserializeBinaryFromReader(message: HeadLookAtGoal, reader: jspb.BinaryReader): HeadLookAtGoal;
}

export namespace HeadLookAtGoal {
  export type AsObject = {
    id?: part_pb.PartId.AsObject,
    point?: kinematics_pb.Point.AsObject,
    duration?: google_protobuf_wrappers_pb.FloatValue.AsObject,
  }
}

export class SpeedLimitRequest extends jspb.Message {
  getId(): part_pb.PartId | undefined;
  setId(value?: part_pb.PartId): SpeedLimitRequest;
  hasId(): boolean;
  clearId(): SpeedLimitRequest;

  getLimit(): SpeedLimit;
  setLimit(value: SpeedLimit): SpeedLimitRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SpeedLimitRequest.AsObject;
  static toObject(includeInstance: boolean, msg: SpeedLimitRequest): SpeedLimitRequest.AsObject;
  static serializeBinaryToWriter(message: SpeedLimitRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SpeedLimitRequest;
  static deserializeBinaryFromReader(message: SpeedLimitRequest, reader: jspb.BinaryReader): SpeedLimitRequest;
}

export namespace SpeedLimitRequest {
  export type AsObject = {
    id?: part_pb.PartId.AsObject,
    limit: SpeedLimit,
  }
}

export class JointLimits extends jspb.Message {
  getMin(): number;
  setMin(value: number): JointLimits;

  getMax(): number;
  setMax(value: number): JointLimits;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): JointLimits.AsObject;
  static toObject(includeInstance: boolean, msg: JointLimits): JointLimits.AsObject;
  static serializeBinaryToWriter(message: JointLimits, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): JointLimits;
  static deserializeBinaryFromReader(message: JointLimits, reader: jspb.BinaryReader): JointLimits;
}

export namespace JointLimits {
  export type AsObject = {
    min: number,
    max: number,
  }
}

export class JointsLimits extends jspb.Message {
  getNeckRoll(): JointLimits | undefined;
  setNeckRoll(value?: JointLimits): JointsLimits;
  hasNeckRoll(): boolean;
  clearNeckRoll(): JointsLimits;

  getNeckPitch(): JointLimits | undefined;
  setNeckPitch(value?: JointLimits): JointsLimits;
  hasNeckPitch(): boolean;
  clearNeckPitch(): JointsLimits;

  getNeckYaw(): JointLimits | undefined;
  setNeckYaw(value?: JointLimits): JointsLimits;
  hasNeckYaw(): boolean;
  clearNeckYaw(): JointsLimits;

  getLAntenna(): JointLimits | undefined;
  setLAntenna(value?: JointLimits): JointsLimits;
  hasLAntenna(): boolean;
  clearLAntenna(): JointsLimits;

  getRAntenna(): JointLimits | undefined;
  setRAntenna(value?: JointLimits): JointsLimits;
  hasRAntenna(): boolean;
  clearRAntenna(): JointsLimits;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): JointsLimits.AsObject;
  static toObject(includeInstance: boolean, msg: JointsLimits): JointsLimits.AsObject;
  static serializeBinaryToWriter(message: JointsLimits, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): JointsLimits;
  static deserializeBinaryFromReader(message: JointsLimits, reader: jspb.BinaryReader): JointsLimits;
}

export namespace JointsLimits {
  export type AsObject = {
    neckRoll?: JointLimits.AsObject,
    neckPitch?: JointLimits.AsObject,
    neckYaw?: JointLimits.AsObject,
    lAntenna?: JointLimits.AsObject,
    rAntenna?: JointLimits.AsObject,
  }
}

export class Temperatures extends jspb.Message {
  getMotor(): number;
  setMotor(value: number): Temperatures;

  getDriver(): number;
  setDriver(value: number): Temperatures;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Temperatures.AsObject;
  static toObject(includeInstance: boolean, msg: Temperatures): Temperatures.AsObject;
  static serializeBinaryToWriter(message: Temperatures, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Temperatures;
  static deserializeBinaryFromReader(message: Temperatures, reader: jspb.BinaryReader): Temperatures;
}

export namespace Temperatures {
  export type AsObject = {
    motor: number,
    driver: number,
  }
}

export class HeadTemperatures extends jspb.Message {
  getNeckMotor1(): Temperatures | undefined;
  setNeckMotor1(value?: Temperatures): HeadTemperatures;
  hasNeckMotor1(): boolean;
  clearNeckMotor1(): HeadTemperatures;

  getNeckMotor2(): Temperatures | undefined;
  setNeckMotor2(value?: Temperatures): HeadTemperatures;
  hasNeckMotor2(): boolean;
  clearNeckMotor2(): HeadTemperatures;

  getNeckMotor3(): Temperatures | undefined;
  setNeckMotor3(value?: Temperatures): HeadTemperatures;
  hasNeckMotor3(): boolean;
  clearNeckMotor3(): HeadTemperatures;

  getLAntenna(): Temperatures | undefined;
  setLAntenna(value?: Temperatures): HeadTemperatures;
  hasLAntenna(): boolean;
  clearLAntenna(): HeadTemperatures;

  getRAntenna(): Temperatures | undefined;
  setRAntenna(value?: Temperatures): HeadTemperatures;
  hasRAntenna(): boolean;
  clearRAntenna(): HeadTemperatures;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HeadTemperatures.AsObject;
  static toObject(includeInstance: boolean, msg: HeadTemperatures): HeadTemperatures.AsObject;
  static serializeBinaryToWriter(message: HeadTemperatures, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HeadTemperatures;
  static deserializeBinaryFromReader(message: HeadTemperatures, reader: jspb.BinaryReader): HeadTemperatures;
}

export namespace HeadTemperatures {
  export type AsObject = {
    neckMotor1?: Temperatures.AsObject,
    neckMotor2?: Temperatures.AsObject,
    neckMotor3?: Temperatures.AsObject,
    lAntenna?: Temperatures.AsObject,
    rAntenna?: Temperatures.AsObject,
  }
}

export enum HeadField { 
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
export enum SpeedLimit { 
  NO_LIMIT = 0,
  FAST = 1,
  NORMAL = 2,
  SLOW = 3,
}

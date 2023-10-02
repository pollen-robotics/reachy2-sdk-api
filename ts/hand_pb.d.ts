import * as jspb from 'google-protobuf'

import * as google_protobuf_wrappers_pb from 'google-protobuf/google/protobuf/wrappers_pb';
import * as google_protobuf_empty_pb from 'google-protobuf/google/protobuf/empty_pb';
import * as part_pb from './part_pb';


export class Hand extends jspb.Message {
  getPartId(): part_pb.PartId | undefined;
  setPartId(value?: part_pb.PartId): Hand;
  hasPartId(): boolean;
  clearPartId(): Hand;

  getInfo(): part_pb.PartInfo | undefined;
  setInfo(value?: part_pb.PartInfo): Hand;
  hasInfo(): boolean;
  clearInfo(): Hand;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Hand.AsObject;
  static toObject(includeInstance: boolean, msg: Hand): Hand.AsObject;
  static serializeBinaryToWriter(message: Hand, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Hand;
  static deserializeBinaryFromReader(message: Hand, reader: jspb.BinaryReader): Hand;
}

export namespace Hand {
  export type AsObject = {
    partId?: part_pb.PartId.AsObject,
    info?: part_pb.PartInfo.AsObject,
  }
}

export class ListOfHand extends jspb.Message {
  getHandList(): Array<Hand>;
  setHandList(value: Array<Hand>): ListOfHand;
  clearHandList(): ListOfHand;
  addHand(value?: Hand, index?: number): Hand;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListOfHand.AsObject;
  static toObject(includeInstance: boolean, msg: ListOfHand): ListOfHand.AsObject;
  static serializeBinaryToWriter(message: ListOfHand, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListOfHand;
  static deserializeBinaryFromReader(message: ListOfHand, reader: jspb.BinaryReader): ListOfHand;
}

export namespace ListOfHand {
  export type AsObject = {
    handList: Array<Hand.AsObject>,
  }
}

export class HandState extends jspb.Message {
  getOpening(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setOpening(value?: google_protobuf_wrappers_pb.FloatValue): HandState;
  hasOpening(): boolean;
  clearOpening(): HandState;

  getForce(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setForce(value?: google_protobuf_wrappers_pb.FloatValue): HandState;
  hasForce(): boolean;
  clearForce(): HandState;

  getHoldingObject(): google_protobuf_wrappers_pb.BoolValue | undefined;
  setHoldingObject(value?: google_protobuf_wrappers_pb.BoolValue): HandState;
  hasHoldingObject(): boolean;
  clearHoldingObject(): HandState;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HandState.AsObject;
  static toObject(includeInstance: boolean, msg: HandState): HandState.AsObject;
  static serializeBinaryToWriter(message: HandState, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HandState;
  static deserializeBinaryFromReader(message: HandState, reader: jspb.BinaryReader): HandState;
}

export namespace HandState {
  export type AsObject = {
    opening?: google_protobuf_wrappers_pb.FloatValue.AsObject,
    force?: google_protobuf_wrappers_pb.FloatValue.AsObject,
    holdingObject?: google_protobuf_wrappers_pb.BoolValue.AsObject,
  }
}

export class HandStatus extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HandStatus.AsObject;
  static toObject(includeInstance: boolean, msg: HandStatus): HandStatus.AsObject;
  static serializeBinaryToWriter(message: HandStatus, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HandStatus;
  static deserializeBinaryFromReader(message: HandStatus, reader: jspb.BinaryReader): HandStatus;
}

export namespace HandStatus {
  export type AsObject = {
  }
}

export class Force extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Force.AsObject;
  static toObject(includeInstance: boolean, msg: Force): Force.AsObject;
  static serializeBinaryToWriter(message: Force, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Force;
  static deserializeBinaryFromReader(message: Force, reader: jspb.BinaryReader): Force;
}

export namespace Force {
  export type AsObject = {
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

export class ParallelGripperLimits extends jspb.Message {
  getLimits(): JointLimits | undefined;
  setLimits(value?: JointLimits): ParallelGripperLimits;
  hasLimits(): boolean;
  clearLimits(): ParallelGripperLimits;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ParallelGripperLimits.AsObject;
  static toObject(includeInstance: boolean, msg: ParallelGripperLimits): ParallelGripperLimits.AsObject;
  static serializeBinaryToWriter(message: ParallelGripperLimits, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ParallelGripperLimits;
  static deserializeBinaryFromReader(message: ParallelGripperLimits, reader: jspb.BinaryReader): ParallelGripperLimits;
}

export namespace ParallelGripperLimits {
  export type AsObject = {
    limits?: JointLimits.AsObject,
  }
}

export class JointsLimits extends jspb.Message {
  getParallelGripper(): ParallelGripperLimits | undefined;
  setParallelGripper(value?: ParallelGripperLimits): JointsLimits;
  hasParallelGripper(): boolean;
  clearParallelGripper(): JointsLimits;

  getLimitsCase(): JointsLimits.LimitsCase;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): JointsLimits.AsObject;
  static toObject(includeInstance: boolean, msg: JointsLimits): JointsLimits.AsObject;
  static serializeBinaryToWriter(message: JointsLimits, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): JointsLimits;
  static deserializeBinaryFromReader(message: JointsLimits, reader: jspb.BinaryReader): JointsLimits;
}

export namespace JointsLimits {
  export type AsObject = {
    parallelGripper?: ParallelGripperLimits.AsObject,
  }

  export enum LimitsCase { 
    LIMITS_NOT_SET = 0,
    PARALLEL_GRIPPER = 1,
  }
}

export class ParallelGripperPosition extends jspb.Message {
  getPosition(): number;
  setPosition(value: number): ParallelGripperPosition;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ParallelGripperPosition.AsObject;
  static toObject(includeInstance: boolean, msg: ParallelGripperPosition): ParallelGripperPosition.AsObject;
  static serializeBinaryToWriter(message: ParallelGripperPosition, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ParallelGripperPosition;
  static deserializeBinaryFromReader(message: ParallelGripperPosition, reader: jspb.BinaryReader): ParallelGripperPosition;
}

export namespace ParallelGripperPosition {
  export type AsObject = {
    position: number,
  }
}

export class HandPosition extends jspb.Message {
  getParallelGripper(): ParallelGripperPosition | undefined;
  setParallelGripper(value?: ParallelGripperPosition): HandPosition;
  hasParallelGripper(): boolean;
  clearParallelGripper(): HandPosition;

  getPositionCase(): HandPosition.PositionCase;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HandPosition.AsObject;
  static toObject(includeInstance: boolean, msg: HandPosition): HandPosition.AsObject;
  static serializeBinaryToWriter(message: HandPosition, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HandPosition;
  static deserializeBinaryFromReader(message: HandPosition, reader: jspb.BinaryReader): HandPosition;
}

export namespace HandPosition {
  export type AsObject = {
    parallelGripper?: ParallelGripperPosition.AsObject,
  }

  export enum PositionCase { 
    POSITION_NOT_SET = 0,
    PARALLEL_GRIPPER = 1,
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

export class ParallelGripperTemperature extends jspb.Message {
  getTemperature(): Temperatures | undefined;
  setTemperature(value?: Temperatures): ParallelGripperTemperature;
  hasTemperature(): boolean;
  clearTemperature(): ParallelGripperTemperature;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ParallelGripperTemperature.AsObject;
  static toObject(includeInstance: boolean, msg: ParallelGripperTemperature): ParallelGripperTemperature.AsObject;
  static serializeBinaryToWriter(message: ParallelGripperTemperature, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ParallelGripperTemperature;
  static deserializeBinaryFromReader(message: ParallelGripperTemperature, reader: jspb.BinaryReader): ParallelGripperTemperature;
}

export namespace ParallelGripperTemperature {
  export type AsObject = {
    temperature?: Temperatures.AsObject,
  }
}

export class HandTemperatures extends jspb.Message {
  getParallelGripper(): Temperatures | undefined;
  setParallelGripper(value?: Temperatures): HandTemperatures;
  hasParallelGripper(): boolean;
  clearParallelGripper(): HandTemperatures;

  getTemperaturesCase(): HandTemperatures.TemperaturesCase;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HandTemperatures.AsObject;
  static toObject(includeInstance: boolean, msg: HandTemperatures): HandTemperatures.AsObject;
  static serializeBinaryToWriter(message: HandTemperatures, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HandTemperatures;
  static deserializeBinaryFromReader(message: HandTemperatures, reader: jspb.BinaryReader): HandTemperatures;
}

export namespace HandTemperatures {
  export type AsObject = {
    parallelGripper?: Temperatures.AsObject,
  }

  export enum TemperaturesCase { 
    TEMPERATURES_NOT_SET = 0,
    PARALLEL_GRIPPER = 1,
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

export enum SpeedLimit { 
  NO_LIMIT = 0,
  FAST = 1,
  NORMAL = 2,
  SLOW = 3,
}

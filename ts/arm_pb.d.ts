import * as jspb from 'google-protobuf'

import * as google_protobuf_empty_pb from 'google-protobuf/google/protobuf/empty_pb';
import * as google_protobuf_wrappers_pb from 'google-protobuf/google/protobuf/wrappers_pb';
import * as part_pb from './part_pb';
import * as kinematics_pb from './kinematics_pb';
import * as error_pb from './error_pb';
import * as orbita2d_pb from './orbita2d_pb';
import * as orbita3d_pb from './orbita3d_pb';


export class ArmState extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ArmState.AsObject;
  static toObject(includeInstance: boolean, msg: ArmState): ArmState.AsObject;
  static serializeBinaryToWriter(message: ArmState, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ArmState;
  static deserializeBinaryFromReader(message: ArmState, reader: jspb.BinaryReader): ArmState;
}

export namespace ArmState {
  export type AsObject = {
  }
}

export class ArmDescription extends jspb.Message {
  getShoulder(): orbita2d_pb.Orbita2DInfo | undefined;
  setShoulder(value?: orbita2d_pb.Orbita2DInfo): ArmDescription;
  hasShoulder(): boolean;
  clearShoulder(): ArmDescription;

  getElbow(): orbita2d_pb.Orbita2DInfo | undefined;
  setElbow(value?: orbita2d_pb.Orbita2DInfo): ArmDescription;
  hasElbow(): boolean;
  clearElbow(): ArmDescription;

  getWrist(): orbita3d_pb.Orbita3DInfo | undefined;
  setWrist(value?: orbita3d_pb.Orbita3DInfo): ArmDescription;
  hasWrist(): boolean;
  clearWrist(): ArmDescription;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ArmDescription.AsObject;
  static toObject(includeInstance: boolean, msg: ArmDescription): ArmDescription.AsObject;
  static serializeBinaryToWriter(message: ArmDescription, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ArmDescription;
  static deserializeBinaryFromReader(message: ArmDescription, reader: jspb.BinaryReader): ArmDescription;
}

export namespace ArmDescription {
  export type AsObject = {
    shoulder?: orbita2d_pb.Orbita2DInfo.AsObject,
    elbow?: orbita2d_pb.Orbita2DInfo.AsObject,
    wrist?: orbita3d_pb.Orbita3DInfo.AsObject,
  }
}

export class Arm extends jspb.Message {
  getPartId(): part_pb.PartId | undefined;
  setPartId(value?: part_pb.PartId): Arm;
  hasPartId(): boolean;
  clearPartId(): Arm;

  getDescription(): ArmDescription | undefined;
  setDescription(value?: ArmDescription): Arm;
  hasDescription(): boolean;
  clearDescription(): Arm;

  getInfo(): part_pb.PartInfo | undefined;
  setInfo(value?: part_pb.PartInfo): Arm;
  hasInfo(): boolean;
  clearInfo(): Arm;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Arm.AsObject;
  static toObject(includeInstance: boolean, msg: Arm): Arm.AsObject;
  static serializeBinaryToWriter(message: Arm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Arm;
  static deserializeBinaryFromReader(message: Arm, reader: jspb.BinaryReader): Arm;
}

export namespace Arm {
  export type AsObject = {
    partId?: part_pb.PartId.AsObject,
    description?: ArmDescription.AsObject,
    info?: part_pb.PartInfo.AsObject,
  }
}

export class ListOfArm extends jspb.Message {
  getArmList(): Array<Arm>;
  setArmList(value: Array<Arm>): ListOfArm;
  clearArmList(): ListOfArm;
  addArm(value?: Arm, index?: number): Arm;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListOfArm.AsObject;
  static toObject(includeInstance: boolean, msg: ListOfArm): ListOfArm.AsObject;
  static serializeBinaryToWriter(message: ListOfArm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListOfArm;
  static deserializeBinaryFromReader(message: ListOfArm, reader: jspb.BinaryReader): ListOfArm;
}

export namespace ListOfArm {
  export type AsObject = {
    armList: Array<Arm.AsObject>,
  }
}

export class ArmPosition extends jspb.Message {
  getShoulderPitch(): number;
  setShoulderPitch(value: number): ArmPosition;

  getShoulderRoll(): number;
  setShoulderRoll(value: number): ArmPosition;

  getElbowYaw(): number;
  setElbowYaw(value: number): ArmPosition;

  getElbowPitch(): number;
  setElbowPitch(value: number): ArmPosition;

  getWristRoll(): number;
  setWristRoll(value: number): ArmPosition;

  getWristPitch(): number;
  setWristPitch(value: number): ArmPosition;

  getWristYaw(): number;
  setWristYaw(value: number): ArmPosition;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ArmPosition.AsObject;
  static toObject(includeInstance: boolean, msg: ArmPosition): ArmPosition.AsObject;
  static serializeBinaryToWriter(message: ArmPosition, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ArmPosition;
  static deserializeBinaryFromReader(message: ArmPosition, reader: jspb.BinaryReader): ArmPosition;
}

export namespace ArmPosition {
  export type AsObject = {
    shoulderPitch: number,
    shoulderRoll: number,
    elbowYaw: number,
    elbowPitch: number,
    wristRoll: number,
    wristPitch: number,
    wristYaw: number,
  }
}

export class ArmCartesianGoal extends jspb.Message {
  getId(): part_pb.PartId | undefined;
  setId(value?: part_pb.PartId): ArmCartesianGoal;
  hasId(): boolean;
  clearId(): ArmCartesianGoal;

  getPosition(): kinematics_pb.Matrix4x4 | undefined;
  setPosition(value?: kinematics_pb.Matrix4x4): ArmCartesianGoal;
  hasPosition(): boolean;
  clearPosition(): ArmCartesianGoal;

  getDuration(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setDuration(value?: google_protobuf_wrappers_pb.FloatValue): ArmCartesianGoal;
  hasDuration(): boolean;
  clearDuration(): ArmCartesianGoal;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ArmCartesianGoal.AsObject;
  static toObject(includeInstance: boolean, msg: ArmCartesianGoal): ArmCartesianGoal.AsObject;
  static serializeBinaryToWriter(message: ArmCartesianGoal, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ArmCartesianGoal;
  static deserializeBinaryFromReader(message: ArmCartesianGoal, reader: jspb.BinaryReader): ArmCartesianGoal;
}

export namespace ArmCartesianGoal {
  export type AsObject = {
    id?: part_pb.PartId.AsObject,
    position?: kinematics_pb.Matrix4x4.AsObject,
    duration?: google_protobuf_wrappers_pb.FloatValue.AsObject,
  }
}

export class ArmJointGoal extends jspb.Message {
  getId(): part_pb.PartId | undefined;
  setId(value?: part_pb.PartId): ArmJointGoal;
  hasId(): boolean;
  clearId(): ArmJointGoal;

  getPosition(): ArmPosition | undefined;
  setPosition(value?: ArmPosition): ArmJointGoal;
  hasPosition(): boolean;
  clearPosition(): ArmJointGoal;

  getDuration(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setDuration(value?: google_protobuf_wrappers_pb.FloatValue): ArmJointGoal;
  hasDuration(): boolean;
  clearDuration(): ArmJointGoal;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ArmJointGoal.AsObject;
  static toObject(includeInstance: boolean, msg: ArmJointGoal): ArmJointGoal.AsObject;
  static serializeBinaryToWriter(message: ArmJointGoal, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ArmJointGoal;
  static deserializeBinaryFromReader(message: ArmJointGoal, reader: jspb.BinaryReader): ArmJointGoal;
}

export namespace ArmJointGoal {
  export type AsObject = {
    id?: part_pb.PartId.AsObject,
    position?: ArmPosition.AsObject,
    duration?: google_protobuf_wrappers_pb.FloatValue.AsObject,
  }
}

export class ArmEndEffector extends jspb.Message {
  getPose(): kinematics_pb.Matrix4x4 | undefined;
  setPose(value?: kinematics_pb.Matrix4x4): ArmEndEffector;
  hasPose(): boolean;
  clearPose(): ArmEndEffector;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ArmEndEffector.AsObject;
  static toObject(includeInstance: boolean, msg: ArmEndEffector): ArmEndEffector.AsObject;
  static serializeBinaryToWriter(message: ArmEndEffector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ArmEndEffector;
  static deserializeBinaryFromReader(message: ArmEndEffector, reader: jspb.BinaryReader): ArmEndEffector;
}

export namespace ArmEndEffector {
  export type AsObject = {
    pose?: kinematics_pb.Matrix4x4.AsObject,
  }
}

export class ArmFKSolution extends jspb.Message {
  getSuccess(): boolean;
  setSuccess(value: boolean): ArmFKSolution;

  getEndEffector(): ArmEndEffector | undefined;
  setEndEffector(value?: ArmEndEffector): ArmFKSolution;
  hasEndEffector(): boolean;
  clearEndEffector(): ArmFKSolution;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ArmFKSolution.AsObject;
  static toObject(includeInstance: boolean, msg: ArmFKSolution): ArmFKSolution.AsObject;
  static serializeBinaryToWriter(message: ArmFKSolution, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ArmFKSolution;
  static deserializeBinaryFromReader(message: ArmFKSolution, reader: jspb.BinaryReader): ArmFKSolution;
}

export namespace ArmFKSolution {
  export type AsObject = {
    success: boolean,
    endEffector?: ArmEndEffector.AsObject,
  }
}

export class ArmIKRequest extends jspb.Message {
  getTarget(): ArmEndEffector | undefined;
  setTarget(value?: ArmEndEffector): ArmIKRequest;
  hasTarget(): boolean;
  clearTarget(): ArmIKRequest;

  getQ0(): ArmPosition | undefined;
  setQ0(value?: ArmPosition): ArmIKRequest;
  hasQ0(): boolean;
  clearQ0(): ArmIKRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ArmIKRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ArmIKRequest): ArmIKRequest.AsObject;
  static serializeBinaryToWriter(message: ArmIKRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ArmIKRequest;
  static deserializeBinaryFromReader(message: ArmIKRequest, reader: jspb.BinaryReader): ArmIKRequest;
}

export namespace ArmIKRequest {
  export type AsObject = {
    target?: ArmEndEffector.AsObject,
    q0?: ArmPosition.AsObject,
  }
}

export class ArmIKSolution extends jspb.Message {
  getSuccess(): boolean;
  setSuccess(value: boolean): ArmIKSolution;

  getArmPosition(): ArmPosition | undefined;
  setArmPosition(value?: ArmPosition): ArmIKSolution;
  hasArmPosition(): boolean;
  clearArmPosition(): ArmIKSolution;

  getError(): error_pb.Error | undefined;
  setError(value?: error_pb.Error): ArmIKSolution;
  hasError(): boolean;
  clearError(): ArmIKSolution;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ArmIKSolution.AsObject;
  static toObject(includeInstance: boolean, msg: ArmIKSolution): ArmIKSolution.AsObject;
  static serializeBinaryToWriter(message: ArmIKSolution, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ArmIKSolution;
  static deserializeBinaryFromReader(message: ArmIKSolution, reader: jspb.BinaryReader): ArmIKSolution;
}

export namespace ArmIKSolution {
  export type AsObject = {
    success: boolean,
    armPosition?: ArmPosition.AsObject,
    error?: error_pb.Error.AsObject,
  }
}

export class ArmStatus extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ArmStatus.AsObject;
  static toObject(includeInstance: boolean, msg: ArmStatus): ArmStatus.AsObject;
  static serializeBinaryToWriter(message: ArmStatus, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ArmStatus;
  static deserializeBinaryFromReader(message: ArmStatus, reader: jspb.BinaryReader): ArmStatus;
}

export namespace ArmStatus {
  export type AsObject = {
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
  getShoulderPitch(): JointLimits | undefined;
  setShoulderPitch(value?: JointLimits): JointsLimits;
  hasShoulderPitch(): boolean;
  clearShoulderPitch(): JointsLimits;

  getShoulderRoll(): JointLimits | undefined;
  setShoulderRoll(value?: JointLimits): JointsLimits;
  hasShoulderRoll(): boolean;
  clearShoulderRoll(): JointsLimits;

  getElbowYaw(): JointLimits | undefined;
  setElbowYaw(value?: JointLimits): JointsLimits;
  hasElbowYaw(): boolean;
  clearElbowYaw(): JointsLimits;

  getElbowPitch(): JointLimits | undefined;
  setElbowPitch(value?: JointLimits): JointsLimits;
  hasElbowPitch(): boolean;
  clearElbowPitch(): JointsLimits;

  getWristRoll(): JointLimits | undefined;
  setWristRoll(value?: JointLimits): JointsLimits;
  hasWristRoll(): boolean;
  clearWristRoll(): JointsLimits;

  getWristPitch(): JointLimits | undefined;
  setWristPitch(value?: JointLimits): JointsLimits;
  hasWristPitch(): boolean;
  clearWristPitch(): JointsLimits;

  getWristYaw(): JointLimits | undefined;
  setWristYaw(value?: JointLimits): JointsLimits;
  hasWristYaw(): boolean;
  clearWristYaw(): JointsLimits;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): JointsLimits.AsObject;
  static toObject(includeInstance: boolean, msg: JointsLimits): JointsLimits.AsObject;
  static serializeBinaryToWriter(message: JointsLimits, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): JointsLimits;
  static deserializeBinaryFromReader(message: JointsLimits, reader: jspb.BinaryReader): JointsLimits;
}

export namespace JointsLimits {
  export type AsObject = {
    shoulderPitch?: JointLimits.AsObject,
    shoulderRoll?: JointLimits.AsObject,
    elbowYaw?: JointLimits.AsObject,
    elbowPitch?: JointLimits.AsObject,
    wristRoll?: JointLimits.AsObject,
    wristPitch?: JointLimits.AsObject,
    wristYaw?: JointLimits.AsObject,
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

export class ArmTemperatures extends jspb.Message {
  getShoulderMotor1(): Temperatures | undefined;
  setShoulderMotor1(value?: Temperatures): ArmTemperatures;
  hasShoulderMotor1(): boolean;
  clearShoulderMotor1(): ArmTemperatures;

  getShoulderMotor2(): Temperatures | undefined;
  setShoulderMotor2(value?: Temperatures): ArmTemperatures;
  hasShoulderMotor2(): boolean;
  clearShoulderMotor2(): ArmTemperatures;

  getElbowMotor1(): Temperatures | undefined;
  setElbowMotor1(value?: Temperatures): ArmTemperatures;
  hasElbowMotor1(): boolean;
  clearElbowMotor1(): ArmTemperatures;

  getElbowMotor2(): Temperatures | undefined;
  setElbowMotor2(value?: Temperatures): ArmTemperatures;
  hasElbowMotor2(): boolean;
  clearElbowMotor2(): ArmTemperatures;

  getWristMotor1(): Temperatures | undefined;
  setWristMotor1(value?: Temperatures): ArmTemperatures;
  hasWristMotor1(): boolean;
  clearWristMotor1(): ArmTemperatures;

  getWristMotor2(): Temperatures | undefined;
  setWristMotor2(value?: Temperatures): ArmTemperatures;
  hasWristMotor2(): boolean;
  clearWristMotor2(): ArmTemperatures;

  getWristMotor3(): Temperatures | undefined;
  setWristMotor3(value?: Temperatures): ArmTemperatures;
  hasWristMotor3(): boolean;
  clearWristMotor3(): ArmTemperatures;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ArmTemperatures.AsObject;
  static toObject(includeInstance: boolean, msg: ArmTemperatures): ArmTemperatures.AsObject;
  static serializeBinaryToWriter(message: ArmTemperatures, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ArmTemperatures;
  static deserializeBinaryFromReader(message: ArmTemperatures, reader: jspb.BinaryReader): ArmTemperatures;
}

export namespace ArmTemperatures {
  export type AsObject = {
    shoulderMotor1?: Temperatures.AsObject,
    shoulderMotor2?: Temperatures.AsObject,
    elbowMotor1?: Temperatures.AsObject,
    elbowMotor2?: Temperatures.AsObject,
    wristMotor1?: Temperatures.AsObject,
    wristMotor2?: Temperatures.AsObject,
    wristMotor3?: Temperatures.AsObject,
  }
}

export enum ArmField { 
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
export enum SpeedLimit { 
  NO_LIMIT = 0,
  FAST = 1,
  NORMAL = 2,
  SLOW = 3,
}

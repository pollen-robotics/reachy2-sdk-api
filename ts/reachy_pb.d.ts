import * as jspb from 'google-protobuf'

import * as google_protobuf_empty_pb from 'google-protobuf/google/protobuf/empty_pb';
import * as arm_pb from './arm_pb';
import * as head_pb from './head_pb';
import * as hand_pb from './hand_pb';
import * as mobile_base_pb from './mobile_base_pb';
import * as sound_pb from './sound_pb';
import * as video_pb from './video_pb';


export class Reachy extends jspb.Message {
  getId(): ReachyId | undefined;
  setId(value?: ReachyId): Reachy;
  hasId(): boolean;
  clearId(): Reachy;

  getLArm(): arm_pb.Arm | undefined;
  setLArm(value?: arm_pb.Arm): Reachy;
  hasLArm(): boolean;
  clearLArm(): Reachy;

  getRArm(): arm_pb.Arm | undefined;
  setRArm(value?: arm_pb.Arm): Reachy;
  hasRArm(): boolean;
  clearRArm(): Reachy;

  getHead(): head_pb.Head | undefined;
  setHead(value?: head_pb.Head): Reachy;
  hasHead(): boolean;
  clearHead(): Reachy;

  getLHand(): hand_pb.Hand | undefined;
  setLHand(value?: hand_pb.Hand): Reachy;
  hasLHand(): boolean;
  clearLHand(): Reachy;

  getRHand(): hand_pb.Hand | undefined;
  setRHand(value?: hand_pb.Hand): Reachy;
  hasRHand(): boolean;
  clearRHand(): Reachy;

  getMobileBase(): mobile_base_pb.MobileBase | undefined;
  setMobileBase(value?: mobile_base_pb.MobileBase): Reachy;
  hasMobileBase(): boolean;
  clearMobileBase(): Reachy;

  getMicrophone(): sound_pb.Microphone | undefined;
  setMicrophone(value?: sound_pb.Microphone): Reachy;
  hasMicrophone(): boolean;
  clearMicrophone(): Reachy;

  getSpeaker(): sound_pb.Speaker | undefined;
  setSpeaker(value?: sound_pb.Speaker): Reachy;
  hasSpeaker(): boolean;
  clearSpeaker(): Reachy;

  getStereoCamera(): video_pb.StereoCamera | undefined;
  setStereoCamera(value?: video_pb.StereoCamera): Reachy;
  hasStereoCamera(): boolean;
  clearStereoCamera(): Reachy;

  getInfo(): ReachyInfo | undefined;
  setInfo(value?: ReachyInfo): Reachy;
  hasInfo(): boolean;
  clearInfo(): Reachy;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Reachy.AsObject;
  static toObject(includeInstance: boolean, msg: Reachy): Reachy.AsObject;
  static serializeBinaryToWriter(message: Reachy, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Reachy;
  static deserializeBinaryFromReader(message: Reachy, reader: jspb.BinaryReader): Reachy;
}

export namespace Reachy {
  export type AsObject = {
    id?: ReachyId.AsObject,
    lArm?: arm_pb.Arm.AsObject,
    rArm?: arm_pb.Arm.AsObject,
    head?: head_pb.Head.AsObject,
    lHand?: hand_pb.Hand.AsObject,
    rHand?: hand_pb.Hand.AsObject,
    mobileBase?: mobile_base_pb.MobileBase.AsObject,
    microphone?: sound_pb.Microphone.AsObject,
    speaker?: sound_pb.Speaker.AsObject,
    stereoCamera?: video_pb.StereoCamera.AsObject,
    info?: ReachyInfo.AsObject,
  }
}

export class ReachyId extends jspb.Message {
  getName(): string;
  setName(value: string): ReachyId;

  getId(): string;
  setId(value: string): ReachyId;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReachyId.AsObject;
  static toObject(includeInstance: boolean, msg: ReachyId): ReachyId.AsObject;
  static serializeBinaryToWriter(message: ReachyId, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReachyId;
  static deserializeBinaryFromReader(message: ReachyId, reader: jspb.BinaryReader): ReachyId;
}

export namespace ReachyId {
  export type AsObject = {
    name: string,
    id: string,
  }
}

export class ReachyInfo extends jspb.Message {
  getSerialNumber(): string;
  setSerialNumber(value: string): ReachyInfo;

  getVersionHard(): string;
  setVersionHard(value: string): ReachyInfo;

  getVersionSoft(): string;
  setVersionSoft(value: string): ReachyInfo;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReachyInfo.AsObject;
  static toObject(includeInstance: boolean, msg: ReachyInfo): ReachyInfo.AsObject;
  static serializeBinaryToWriter(message: ReachyInfo, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReachyInfo;
  static deserializeBinaryFromReader(message: ReachyInfo, reader: jspb.BinaryReader): ReachyInfo;
}

export namespace ReachyInfo {
  export type AsObject = {
    serialNumber: string,
    versionHard: string,
    versionSoft: string,
  }
}

export class ListOfReachy extends jspb.Message {
  getReachyList(): Array<Reachy>;
  setReachyList(value: Array<Reachy>): ListOfReachy;
  clearReachyList(): ListOfReachy;
  addReachy(value?: Reachy, index?: number): Reachy;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListOfReachy.AsObject;
  static toObject(includeInstance: boolean, msg: ListOfReachy): ListOfReachy.AsObject;
  static serializeBinaryToWriter(message: ListOfReachy, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListOfReachy;
  static deserializeBinaryFromReader(message: ListOfReachy, reader: jspb.BinaryReader): ListOfReachy;
}

export namespace ListOfReachy {
  export type AsObject = {
    reachyList: Array<Reachy.AsObject>,
  }
}

export class ReachyState extends jspb.Message {
  getLArmState(): arm_pb.ArmState | undefined;
  setLArmState(value?: arm_pb.ArmState): ReachyState;
  hasLArmState(): boolean;
  clearLArmState(): ReachyState;

  getRArmState(): arm_pb.ArmState | undefined;
  setRArmState(value?: arm_pb.ArmState): ReachyState;
  hasRArmState(): boolean;
  clearRArmState(): ReachyState;

  getHeadState(): head_pb.HeadState | undefined;
  setHeadState(value?: head_pb.HeadState): ReachyState;
  hasHeadState(): boolean;
  clearHeadState(): ReachyState;

  getLHandState(): hand_pb.HandState | undefined;
  setLHandState(value?: hand_pb.HandState): ReachyState;
  hasLHandState(): boolean;
  clearLHandState(): ReachyState;

  getRHandState(): hand_pb.HandState | undefined;
  setRHandState(value?: hand_pb.HandState): ReachyState;
  hasRHandState(): boolean;
  clearRHandState(): ReachyState;

  getMobileBaseState(): mobile_base_pb.MobileBaseState | undefined;
  setMobileBaseState(value?: mobile_base_pb.MobileBaseState): ReachyState;
  hasMobileBaseState(): boolean;
  clearMobileBaseState(): ReachyState;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReachyState.AsObject;
  static toObject(includeInstance: boolean, msg: ReachyState): ReachyState.AsObject;
  static serializeBinaryToWriter(message: ReachyState, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReachyState;
  static deserializeBinaryFromReader(message: ReachyState, reader: jspb.BinaryReader): ReachyState;
}

export namespace ReachyState {
  export type AsObject = {
    lArmState?: arm_pb.ArmState.AsObject,
    rArmState?: arm_pb.ArmState.AsObject,
    headState?: head_pb.HeadState.AsObject,
    lHandState?: hand_pb.HandState.AsObject,
    rHandState?: hand_pb.HandState.AsObject,
    mobileBaseState?: mobile_base_pb.MobileBaseState.AsObject,
  }
}


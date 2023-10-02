import * as jspb from 'google-protobuf'

import * as google_protobuf_empty_pb from 'google-protobuf/google/protobuf/empty_pb';
import * as component_pb from './component_pb';


export class StereoCamera extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): StereoCamera.AsObject;
  static toObject(includeInstance: boolean, msg: StereoCamera): StereoCamera.AsObject;
  static serializeBinaryToWriter(message: StereoCamera, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): StereoCamera;
  static deserializeBinaryFromReader(message: StereoCamera, reader: jspb.BinaryReader): StereoCamera;
}

export namespace StereoCamera {
  export type AsObject = {
  }
}

export class DepthCamera extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DepthCamera.AsObject;
  static toObject(includeInstance: boolean, msg: DepthCamera): DepthCamera.AsObject;
  static serializeBinaryToWriter(message: DepthCamera, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DepthCamera;
  static deserializeBinaryFromReader(message: DepthCamera, reader: jspb.BinaryReader): DepthCamera;
}

export namespace DepthCamera {
  export type AsObject = {
  }
}

export class StereoCameraInfo extends jspb.Message {
  getId(): component_pb.ComponentId | undefined;
  setId(value?: component_pb.ComponentId): StereoCameraInfo;
  hasId(): boolean;
  clearId(): StereoCameraInfo;

  getIntrinsicParametersList(): Array<number>;
  setIntrinsicParametersList(value: Array<number>): StereoCameraInfo;
  clearIntrinsicParametersList(): StereoCameraInfo;
  addIntrinsicParameters(value: number, index?: number): StereoCameraInfo;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): StereoCameraInfo.AsObject;
  static toObject(includeInstance: boolean, msg: StereoCameraInfo): StereoCameraInfo.AsObject;
  static serializeBinaryToWriter(message: StereoCameraInfo, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): StereoCameraInfo;
  static deserializeBinaryFromReader(message: StereoCameraInfo, reader: jspb.BinaryReader): StereoCameraInfo;
}

export namespace StereoCameraInfo {
  export type AsObject = {
    id?: component_pb.ComponentId.AsObject,
    intrinsicParametersList: Array<number>,
  }
}

export class ListOfStereoCameraInfo extends jspb.Message {
  getStereoCameraInfoList(): Array<StereoCameraInfo>;
  setStereoCameraInfoList(value: Array<StereoCameraInfo>): ListOfStereoCameraInfo;
  clearStereoCameraInfoList(): ListOfStereoCameraInfo;
  addStereoCameraInfo(value?: StereoCameraInfo, index?: number): StereoCameraInfo;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListOfStereoCameraInfo.AsObject;
  static toObject(includeInstance: boolean, msg: ListOfStereoCameraInfo): ListOfStereoCameraInfo.AsObject;
  static serializeBinaryToWriter(message: ListOfStereoCameraInfo, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListOfStereoCameraInfo;
  static deserializeBinaryFromReader(message: ListOfStereoCameraInfo, reader: jspb.BinaryReader): ListOfStereoCameraInfo;
}

export namespace ListOfStereoCameraInfo {
  export type AsObject = {
    stereoCameraInfoList: Array<StereoCameraInfo.AsObject>,
  }
}

export class DepthCameraInfo extends jspb.Message {
  getId(): component_pb.ComponentId | undefined;
  setId(value?: component_pb.ComponentId): DepthCameraInfo;
  hasId(): boolean;
  clearId(): DepthCameraInfo;

  getIntrinsicParametersList(): Array<number>;
  setIntrinsicParametersList(value: Array<number>): DepthCameraInfo;
  clearIntrinsicParametersList(): DepthCameraInfo;
  addIntrinsicParameters(value: number, index?: number): DepthCameraInfo;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DepthCameraInfo.AsObject;
  static toObject(includeInstance: boolean, msg: DepthCameraInfo): DepthCameraInfo.AsObject;
  static serializeBinaryToWriter(message: DepthCameraInfo, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DepthCameraInfo;
  static deserializeBinaryFromReader(message: DepthCameraInfo, reader: jspb.BinaryReader): DepthCameraInfo;
}

export namespace DepthCameraInfo {
  export type AsObject = {
    id?: component_pb.ComponentId.AsObject,
    intrinsicParametersList: Array<number>,
  }
}

export class ListOfDepthCameraInfo extends jspb.Message {
  getStereoCameraInfoList(): Array<DepthCameraInfo>;
  setStereoCameraInfoList(value: Array<DepthCameraInfo>): ListOfDepthCameraInfo;
  clearStereoCameraInfoList(): ListOfDepthCameraInfo;
  addStereoCameraInfo(value?: DepthCameraInfo, index?: number): DepthCameraInfo;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListOfDepthCameraInfo.AsObject;
  static toObject(includeInstance: boolean, msg: ListOfDepthCameraInfo): ListOfDepthCameraInfo.AsObject;
  static serializeBinaryToWriter(message: ListOfDepthCameraInfo, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListOfDepthCameraInfo;
  static deserializeBinaryFromReader(message: ListOfDepthCameraInfo, reader: jspb.BinaryReader): ListOfDepthCameraInfo;
}

export namespace ListOfDepthCameraInfo {
  export type AsObject = {
    stereoCameraInfoList: Array<DepthCameraInfo.AsObject>,
  }
}

export class Frame extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Frame.AsObject;
  static toObject(includeInstance: boolean, msg: Frame): Frame.AsObject;
  static serializeBinaryToWriter(message: Frame, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Frame;
  static deserializeBinaryFromReader(message: Frame, reader: jspb.BinaryReader): Frame;
}

export namespace Frame {
  export type AsObject = {
  }
}


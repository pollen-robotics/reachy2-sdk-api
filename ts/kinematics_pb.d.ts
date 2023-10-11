import * as jspb from 'google-protobuf'



export class Matrix4x4 extends jspb.Message {
  getDataList(): Array<number>;
  setDataList(value: Array<number>): Matrix4x4;
  clearDataList(): Matrix4x4;
  addData(value: number, index?: number): Matrix4x4;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Matrix4x4.AsObject;
  static toObject(includeInstance: boolean, msg: Matrix4x4): Matrix4x4.AsObject;
  static serializeBinaryToWriter(message: Matrix4x4, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Matrix4x4;
  static deserializeBinaryFromReader(message: Matrix4x4, reader: jspb.BinaryReader): Matrix4x4;
}

export namespace Matrix4x4 {
  export type AsObject = {
    dataList: Array<number>,
  }
}

export class Matrix3x3 extends jspb.Message {
  getDataList(): Array<number>;
  setDataList(value: Array<number>): Matrix3x3;
  clearDataList(): Matrix3x3;
  addData(value: number, index?: number): Matrix3x3;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Matrix3x3.AsObject;
  static toObject(includeInstance: boolean, msg: Matrix3x3): Matrix3x3.AsObject;
  static serializeBinaryToWriter(message: Matrix3x3, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Matrix3x3;
  static deserializeBinaryFromReader(message: Matrix3x3, reader: jspb.BinaryReader): Matrix3x3;
}

export namespace Matrix3x3 {
  export type AsObject = {
    dataList: Array<number>,
  }
}

export class Quaternion extends jspb.Message {
  getW(): number;
  setW(value: number): Quaternion;

  getX(): number;
  setX(value: number): Quaternion;

  getY(): number;
  setY(value: number): Quaternion;

  getZ(): number;
  setZ(value: number): Quaternion;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Quaternion.AsObject;
  static toObject(includeInstance: boolean, msg: Quaternion): Quaternion.AsObject;
  static serializeBinaryToWriter(message: Quaternion, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Quaternion;
  static deserializeBinaryFromReader(message: Quaternion, reader: jspb.BinaryReader): Quaternion;
}

export namespace Quaternion {
  export type AsObject = {
    w: number,
    x: number,
    y: number,
    z: number,
  }
}

export class Rotation3D extends jspb.Message {
  getQ(): Quaternion | undefined;
  setQ(value?: Quaternion): Rotation3D;
  hasQ(): boolean;
  clearQ(): Rotation3D;

  getRpy(): ExtEulerAngles | undefined;
  setRpy(value?: ExtEulerAngles): Rotation3D;
  hasRpy(): boolean;
  clearRpy(): Rotation3D;

  getMatrix(): Matrix3x3 | undefined;
  setMatrix(value?: Matrix3x3): Rotation3D;
  hasMatrix(): boolean;
  clearMatrix(): Rotation3D;

  getRotationCase(): Rotation3D.RotationCase;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Rotation3D.AsObject;
  static toObject(includeInstance: boolean, msg: Rotation3D): Rotation3D.AsObject;
  static serializeBinaryToWriter(message: Rotation3D, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Rotation3D;
  static deserializeBinaryFromReader(message: Rotation3D, reader: jspb.BinaryReader): Rotation3D;
}

export namespace Rotation3D {
  export type AsObject = {
    q?: Quaternion.AsObject,
    rpy?: ExtEulerAngles.AsObject,
    matrix?: Matrix3x3.AsObject,
  }

  export enum RotationCase { 
    ROTATION_NOT_SET = 0,
    Q = 1,
    RPY = 2,
    MATRIX = 3,
  }
}

export class Point extends jspb.Message {
  getX(): number;
  setX(value: number): Point;

  getY(): number;
  setY(value: number): Point;

  getZ(): number;
  setZ(value: number): Point;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Point.AsObject;
  static toObject(includeInstance: boolean, msg: Point): Point.AsObject;
  static serializeBinaryToWriter(message: Point, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Point;
  static deserializeBinaryFromReader(message: Point, reader: jspb.BinaryReader): Point;
}

export namespace Point {
  export type AsObject = {
    x: number,
    y: number,
    z: number,
  }
}

export class ExtEulerAngles extends jspb.Message {
  getRoll(): number;
  setRoll(value: number): ExtEulerAngles;

  getPitch(): number;
  setPitch(value: number): ExtEulerAngles;

  getYaw(): number;
  setYaw(value: number): ExtEulerAngles;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ExtEulerAngles.AsObject;
  static toObject(includeInstance: boolean, msg: ExtEulerAngles): ExtEulerAngles.AsObject;
  static serializeBinaryToWriter(message: ExtEulerAngles, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ExtEulerAngles;
  static deserializeBinaryFromReader(message: ExtEulerAngles, reader: jspb.BinaryReader): ExtEulerAngles;
}

export namespace ExtEulerAngles {
  export type AsObject = {
    roll: number,
    pitch: number,
    yaw: number,
  }
}

export class PointDistanceTolerances extends jspb.Message {
  getXTol(): number;
  setXTol(value: number): PointDistanceTolerances;

  getYTol(): number;
  setYTol(value: number): PointDistanceTolerances;

  getZTol(): number;
  setZTol(value: number): PointDistanceTolerances;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): PointDistanceTolerances.AsObject;
  static toObject(includeInstance: boolean, msg: PointDistanceTolerances): PointDistanceTolerances.AsObject;
  static serializeBinaryToWriter(message: PointDistanceTolerances, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): PointDistanceTolerances;
  static deserializeBinaryFromReader(message: PointDistanceTolerances, reader: jspb.BinaryReader): PointDistanceTolerances;
}

export namespace PointDistanceTolerances {
  export type AsObject = {
    xTol: number,
    yTol: number,
    zTol: number,
  }
}

export class ExtEulerAnglesTolerances extends jspb.Message {
  getRollTol(): number;
  setRollTol(value: number): ExtEulerAnglesTolerances;

  getPitchTol(): number;
  setPitchTol(value: number): ExtEulerAnglesTolerances;

  getYawTol(): number;
  setYawTol(value: number): ExtEulerAnglesTolerances;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ExtEulerAnglesTolerances.AsObject;
  static toObject(includeInstance: boolean, msg: ExtEulerAnglesTolerances): ExtEulerAnglesTolerances.AsObject;
  static serializeBinaryToWriter(message: ExtEulerAnglesTolerances, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ExtEulerAnglesTolerances;
  static deserializeBinaryFromReader(message: ExtEulerAnglesTolerances, reader: jspb.BinaryReader): ExtEulerAnglesTolerances;
}

export namespace ExtEulerAnglesTolerances {
  export type AsObject = {
    rollTol: number,
    pitchTol: number,
    yawTol: number,
  }
}


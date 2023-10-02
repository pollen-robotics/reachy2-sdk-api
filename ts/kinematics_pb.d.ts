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
  }

  export enum RotationCase { 
    ROTATION_NOT_SET = 0,
    Q = 1,
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


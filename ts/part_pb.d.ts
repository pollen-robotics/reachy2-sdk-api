import * as jspb from 'google-protobuf'



export class PartId extends jspb.Message {
  getName(): string;
  setName(value: string): PartId;

  getId(): string;
  setId(value: string): PartId;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): PartId.AsObject;
  static toObject(includeInstance: boolean, msg: PartId): PartId.AsObject;
  static serializeBinaryToWriter(message: PartId, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): PartId;
  static deserializeBinaryFromReader(message: PartId, reader: jspb.BinaryReader): PartId;
}

export namespace PartId {
  export type AsObject = {
    name: string,
    id: string,
  }
}

export class PartInfo extends jspb.Message {
  getSerialNumber(): string;
  setSerialNumber(value: string): PartInfo;

  getVersionHard(): string;
  setVersionHard(value: string): PartInfo;

  getVersionSoft(): string;
  setVersionSoft(value: string): PartInfo;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): PartInfo.AsObject;
  static toObject(includeInstance: boolean, msg: PartInfo): PartInfo.AsObject;
  static serializeBinaryToWriter(message: PartInfo, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): PartInfo;
  static deserializeBinaryFromReader(message: PartInfo, reader: jspb.BinaryReader): PartInfo;
}

export namespace PartInfo {
  export type AsObject = {
    serialNumber: string,
    versionHard: string,
    versionSoft: string,
  }
}


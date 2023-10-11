import * as jspb from 'google-protobuf'



export class ComponentId extends jspb.Message {
  getId(): number;
  setId(value: number): ComponentId;

  getName(): string;
  setName(value: string): ComponentId;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ComponentId.AsObject;
  static toObject(includeInstance: boolean, msg: ComponentId): ComponentId.AsObject;
  static serializeBinaryToWriter(message: ComponentId, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ComponentId;
  static deserializeBinaryFromReader(message: ComponentId, reader: jspb.BinaryReader): ComponentId;
}

export namespace ComponentId {
  export type AsObject = {
    id: number,
    name: string,
  }
}

export class PIDGains extends jspb.Message {
  getP(): number;
  setP(value: number): PIDGains;

  getI(): number;
  setI(value: number): PIDGains;

  getD(): number;
  setD(value: number): PIDGains;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): PIDGains.AsObject;
  static toObject(includeInstance: boolean, msg: PIDGains): PIDGains.AsObject;
  static serializeBinaryToWriter(message: PIDGains, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): PIDGains;
  static deserializeBinaryFromReader(message: PIDGains, reader: jspb.BinaryReader): PIDGains;
}

export namespace PIDGains {
  export type AsObject = {
    p: number,
    i: number,
    d: number,
  }
}


import * as jspb from 'google-protobuf'

import * as google_protobuf_wrappers_pb from 'google-protobuf/google/protobuf/wrappers_pb';


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
  getP(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setP(value?: google_protobuf_wrappers_pb.FloatValue): PIDGains;
  hasP(): boolean;
  clearP(): PIDGains;

  getI(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setI(value?: google_protobuf_wrappers_pb.FloatValue): PIDGains;
  hasI(): boolean;
  clearI(): PIDGains;

  getD(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setD(value?: google_protobuf_wrappers_pb.FloatValue): PIDGains;
  hasD(): boolean;
  clearD(): PIDGains;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): PIDGains.AsObject;
  static toObject(includeInstance: boolean, msg: PIDGains): PIDGains.AsObject;
  static serializeBinaryToWriter(message: PIDGains, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): PIDGains;
  static deserializeBinaryFromReader(message: PIDGains, reader: jspb.BinaryReader): PIDGains;
}

export namespace PIDGains {
  export type AsObject = {
    p?: google_protobuf_wrappers_pb.FloatValue.AsObject,
    i?: google_protobuf_wrappers_pb.FloatValue.AsObject,
    d?: google_protobuf_wrappers_pb.FloatValue.AsObject,
  }
}

export class JointLimits extends jspb.Message {
  getMin(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setMin(value?: google_protobuf_wrappers_pb.FloatValue): JointLimits;
  hasMin(): boolean;
  clearMin(): JointLimits;

  getMax(): google_protobuf_wrappers_pb.FloatValue | undefined;
  setMax(value?: google_protobuf_wrappers_pb.FloatValue): JointLimits;
  hasMax(): boolean;
  clearMax(): JointLimits;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): JointLimits.AsObject;
  static toObject(includeInstance: boolean, msg: JointLimits): JointLimits.AsObject;
  static serializeBinaryToWriter(message: JointLimits, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): JointLimits;
  static deserializeBinaryFromReader(message: JointLimits, reader: jspb.BinaryReader): JointLimits;
}

export namespace JointLimits {
  export type AsObject = {
    min?: google_protobuf_wrappers_pb.FloatValue.AsObject,
    max?: google_protobuf_wrappers_pb.FloatValue.AsObject,
  }
}


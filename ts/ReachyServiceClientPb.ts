/**
 * @fileoverview gRPC-Web generated client stub for reachy
 * @enhanceable
 * @public
 */

// Code generated by protoc-gen-grpc-web. DO NOT EDIT.
// versions:
// 	protoc-gen-grpc-web v1.4.2
// 	protoc              v3.12.4
// source: reachy.proto


/* eslint-disable */
// @ts-nocheck


import * as grpcWeb from 'grpc-web';

import * as google_protobuf_empty_pb from 'google-protobuf/google/protobuf/empty_pb';
import * as reachy_pb from './reachy_pb';


export class ReachyServiceClient {
  client_: grpcWeb.AbstractClientBase;
  hostname_: string;
  credentials_: null | { [index: string]: string; };
  options_: null | { [index: string]: any; };

  constructor (hostname: string,
               credentials?: null | { [index: string]: string; },
               options?: null | { [index: string]: any; }) {
    if (!options) options = {};
    if (!credentials) credentials = {};
    options['format'] = 'text';

    this.client_ = new grpcWeb.GrpcWebClientBase(options);
    this.hostname_ = hostname.replace(/\/+$/, '');
    this.credentials_ = credentials;
    this.options_ = options;
  }

  methodDescriptorGetListOfReachy = new grpcWeb.MethodDescriptor(
    '/reachy.ReachyService/GetListOfReachy',
    grpcWeb.MethodType.UNARY,
    google_protobuf_empty_pb.Empty,
    reachy_pb.ListOfReachy,
    (request: google_protobuf_empty_pb.Empty) => {
      return request.serializeBinary();
    },
    reachy_pb.ListOfReachy.deserializeBinary
  );

  getListOfReachy(
    request: google_protobuf_empty_pb.Empty,
    metadata: grpcWeb.Metadata | null): Promise<reachy_pb.ListOfReachy>;

  getListOfReachy(
    request: google_protobuf_empty_pb.Empty,
    metadata: grpcWeb.Metadata | null,
    callback: (err: grpcWeb.RpcError,
               response: reachy_pb.ListOfReachy) => void): grpcWeb.ClientReadableStream<reachy_pb.ListOfReachy>;

  getListOfReachy(
    request: google_protobuf_empty_pb.Empty,
    metadata: grpcWeb.Metadata | null,
    callback?: (err: grpcWeb.RpcError,
               response: reachy_pb.ListOfReachy) => void) {
    if (callback !== undefined) {
      return this.client_.rpcCall(
        this.hostname_ +
          '/reachy.ReachyService/GetListOfReachy',
        request,
        metadata || {},
        this.methodDescriptorGetListOfReachy,
        callback);
    }
    return this.client_.unaryCall(
    this.hostname_ +
      '/reachy.ReachyService/GetListOfReachy',
    request,
    metadata || {},
    this.methodDescriptorGetListOfReachy);
  }

  methodDescriptorGetReachy = new grpcWeb.MethodDescriptor(
    '/reachy.ReachyService/GetReachy',
    grpcWeb.MethodType.UNARY,
    google_protobuf_empty_pb.Empty,
    reachy_pb.Reachy,
    (request: google_protobuf_empty_pb.Empty) => {
      return request.serializeBinary();
    },
    reachy_pb.Reachy.deserializeBinary
  );

  getReachy(
    request: google_protobuf_empty_pb.Empty,
    metadata: grpcWeb.Metadata | null): Promise<reachy_pb.Reachy>;

  getReachy(
    request: google_protobuf_empty_pb.Empty,
    metadata: grpcWeb.Metadata | null,
    callback: (err: grpcWeb.RpcError,
               response: reachy_pb.Reachy) => void): grpcWeb.ClientReadableStream<reachy_pb.Reachy>;

  getReachy(
    request: google_protobuf_empty_pb.Empty,
    metadata: grpcWeb.Metadata | null,
    callback?: (err: grpcWeb.RpcError,
               response: reachy_pb.Reachy) => void) {
    if (callback !== undefined) {
      return this.client_.rpcCall(
        this.hostname_ +
          '/reachy.ReachyService/GetReachy',
        request,
        metadata || {},
        this.methodDescriptorGetReachy,
        callback);
    }
    return this.client_.unaryCall(
    this.hostname_ +
      '/reachy.ReachyService/GetReachy',
    request,
    metadata || {},
    this.methodDescriptorGetReachy);
  }

  methodDescriptorGetReachyState = new grpcWeb.MethodDescriptor(
    '/reachy.ReachyService/GetReachyState',
    grpcWeb.MethodType.UNARY,
    reachy_pb.ReachyId,
    reachy_pb.ReachyState,
    (request: reachy_pb.ReachyId) => {
      return request.serializeBinary();
    },
    reachy_pb.ReachyState.deserializeBinary
  );

  getReachyState(
    request: reachy_pb.ReachyId,
    metadata: grpcWeb.Metadata | null): Promise<reachy_pb.ReachyState>;

  getReachyState(
    request: reachy_pb.ReachyId,
    metadata: grpcWeb.Metadata | null,
    callback: (err: grpcWeb.RpcError,
               response: reachy_pb.ReachyState) => void): grpcWeb.ClientReadableStream<reachy_pb.ReachyState>;

  getReachyState(
    request: reachy_pb.ReachyId,
    metadata: grpcWeb.Metadata | null,
    callback?: (err: grpcWeb.RpcError,
               response: reachy_pb.ReachyState) => void) {
    if (callback !== undefined) {
      return this.client_.rpcCall(
        this.hostname_ +
          '/reachy.ReachyService/GetReachyState',
        request,
        metadata || {},
        this.methodDescriptorGetReachyState,
        callback);
    }
    return this.client_.unaryCall(
    this.hostname_ +
      '/reachy.ReachyService/GetReachyState',
    request,
    metadata || {},
    this.methodDescriptorGetReachyState);
  }

  methodDescriptorStreamReachyState = new grpcWeb.MethodDescriptor(
    '/reachy.ReachyService/StreamReachyState',
    grpcWeb.MethodType.SERVER_STREAMING,
    reachy_pb.ReachyStreamStateRequest,
    reachy_pb.ReachyState,
    (request: reachy_pb.ReachyStreamStateRequest) => {
      return request.serializeBinary();
    },
    reachy_pb.ReachyState.deserializeBinary
  );

  streamReachyState(
    request: reachy_pb.ReachyStreamStateRequest,
    metadata?: grpcWeb.Metadata): grpcWeb.ClientReadableStream<reachy_pb.ReachyState> {
    return this.client_.serverStreaming(
      this.hostname_ +
        '/reachy.ReachyService/StreamReachyState',
      request,
      metadata || {},
      this.methodDescriptorStreamReachyState);
  }

}


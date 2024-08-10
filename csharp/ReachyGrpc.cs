// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: reachy.proto
// </auto-generated>
#pragma warning disable 0414, 1591, 8981, 0612
#region Designer generated code

using grpc = global::Grpc.Core;

namespace Reachy {
  public static partial class ReachyService
  {
    static readonly string __ServiceName = "reachy.ReachyService";

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static void __Helper_SerializeMessage(global::Google.Protobuf.IMessage message, grpc::SerializationContext context)
    {
      #if !GRPC_DISABLE_PROTOBUF_BUFFER_SERIALIZATION
      if (message is global::Google.Protobuf.IBufferMessage)
      {
        context.SetPayloadLength(message.CalculateSize());
        global::Google.Protobuf.MessageExtensions.WriteTo(message, context.GetBufferWriter());
        context.Complete();
        return;
      }
      #endif
      context.Complete(global::Google.Protobuf.MessageExtensions.ToByteArray(message));
    }

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static class __Helper_MessageCache<T>
    {
      public static readonly bool IsBufferMessage = global::System.Reflection.IntrospectionExtensions.GetTypeInfo(typeof(global::Google.Protobuf.IBufferMessage)).IsAssignableFrom(typeof(T));
    }

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static T __Helper_DeserializeMessage<T>(grpc::DeserializationContext context, global::Google.Protobuf.MessageParser<T> parser) where T : global::Google.Protobuf.IMessage<T>
    {
      #if !GRPC_DISABLE_PROTOBUF_BUFFER_SERIALIZATION
      if (__Helper_MessageCache<T>.IsBufferMessage)
      {
        return parser.ParseFrom(context.PayloadAsReadOnlySequence());
      }
      #endif
      return parser.ParseFrom(context.PayloadAsNewBuffer());
    }

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Google.Protobuf.WellKnownTypes.Empty> __Marshaller_google_protobuf_Empty = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Google.Protobuf.WellKnownTypes.Empty.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Reachy.Reachy> __Marshaller_reachy_Reachy = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Reachy.Reachy.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Reachy.ReachyId> __Marshaller_reachy_ReachyId = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Reachy.ReachyId.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Reachy.ReachyState> __Marshaller_reachy_ReachyState = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Reachy.ReachyState.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Reachy.ReachyStreamStateRequest> __Marshaller_reachy_ReachyStreamStateRequest = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Reachy.ReachyStreamStateRequest.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Reachy.ReachyStatus> __Marshaller_reachy_ReachyStatus = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Reachy.ReachyStatus.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Reachy.ReachyStreamAuditRequest> __Marshaller_reachy_ReachyStreamAuditRequest = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Reachy.ReachyStreamAuditRequest.Parser));

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::Google.Protobuf.WellKnownTypes.Empty, global::Reachy.Reachy> __Method_GetReachy = new grpc::Method<global::Google.Protobuf.WellKnownTypes.Empty, global::Reachy.Reachy>(
        grpc::MethodType.Unary,
        __ServiceName,
        "GetReachy",
        __Marshaller_google_protobuf_Empty,
        __Marshaller_reachy_Reachy);

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::Reachy.ReachyId, global::Reachy.ReachyState> __Method_GetReachyState = new grpc::Method<global::Reachy.ReachyId, global::Reachy.ReachyState>(
        grpc::MethodType.Unary,
        __ServiceName,
        "GetReachyState",
        __Marshaller_reachy_ReachyId,
        __Marshaller_reachy_ReachyState);

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::Reachy.ReachyStreamStateRequest, global::Reachy.ReachyState> __Method_StreamReachyState = new grpc::Method<global::Reachy.ReachyStreamStateRequest, global::Reachy.ReachyState>(
        grpc::MethodType.ServerStreaming,
        __ServiceName,
        "StreamReachyState",
        __Marshaller_reachy_ReachyStreamStateRequest,
        __Marshaller_reachy_ReachyState);

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::Reachy.ReachyId, global::Reachy.ReachyStatus> __Method_Audit = new grpc::Method<global::Reachy.ReachyId, global::Reachy.ReachyStatus>(
        grpc::MethodType.Unary,
        __ServiceName,
        "Audit",
        __Marshaller_reachy_ReachyId,
        __Marshaller_reachy_ReachyStatus);

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::Reachy.ReachyStreamAuditRequest, global::Reachy.ReachyStatus> __Method_StreamAudit = new grpc::Method<global::Reachy.ReachyStreamAuditRequest, global::Reachy.ReachyStatus>(
        grpc::MethodType.ServerStreaming,
        __ServiceName,
        "StreamAudit",
        __Marshaller_reachy_ReachyStreamAuditRequest,
        __Marshaller_reachy_ReachyStatus);

    /// <summary>Service descriptor</summary>
    public static global::Google.Protobuf.Reflection.ServiceDescriptor Descriptor
    {
      get { return global::Reachy.ReachyReflection.Descriptor.Services[0]; }
    }

    /// <summary>Base class for server-side implementations of ReachyService</summary>
    [grpc::BindServiceMethod(typeof(ReachyService), "BindService")]
    public abstract partial class ReachyServiceBase
    {
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::System.Threading.Tasks.Task<global::Reachy.Reachy> GetReachy(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::System.Threading.Tasks.Task<global::Reachy.ReachyState> GetReachyState(global::Reachy.ReachyId request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::System.Threading.Tasks.Task StreamReachyState(global::Reachy.ReachyStreamStateRequest request, grpc::IServerStreamWriter<global::Reachy.ReachyState> responseStream, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::System.Threading.Tasks.Task<global::Reachy.ReachyStatus> Audit(global::Reachy.ReachyId request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::System.Threading.Tasks.Task StreamAudit(global::Reachy.ReachyStreamAuditRequest request, grpc::IServerStreamWriter<global::Reachy.ReachyStatus> responseStream, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

    }

    /// <summary>Client for ReachyService</summary>
    public partial class ReachyServiceClient : grpc::ClientBase<ReachyServiceClient>
    {
      /// <summary>Creates a new client for ReachyService</summary>
      /// <param name="channel">The channel to use to make remote calls.</param>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public ReachyServiceClient(grpc::ChannelBase channel) : base(channel)
      {
      }
      /// <summary>Creates a new client for ReachyService that uses a custom <c>CallInvoker</c>.</summary>
      /// <param name="callInvoker">The callInvoker to use to make remote calls.</param>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public ReachyServiceClient(grpc::CallInvoker callInvoker) : base(callInvoker)
      {
      }
      /// <summary>Protected parameterless constructor to allow creation of test doubles.</summary>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      protected ReachyServiceClient() : base()
      {
      }
      /// <summary>Protected constructor to allow creation of configured clients.</summary>
      /// <param name="configuration">The client configuration.</param>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      protected ReachyServiceClient(ClientBaseConfiguration configuration) : base(configuration)
      {
      }

      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Reachy.Reachy GetReachy(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetReachy(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Reachy.Reachy GetReachy(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_GetReachy, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Reachy.Reachy> GetReachyAsync(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetReachyAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Reachy.Reachy> GetReachyAsync(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_GetReachy, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Reachy.ReachyState GetReachyState(global::Reachy.ReachyId request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetReachyState(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Reachy.ReachyState GetReachyState(global::Reachy.ReachyId request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_GetReachyState, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Reachy.ReachyState> GetReachyStateAsync(global::Reachy.ReachyId request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetReachyStateAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Reachy.ReachyState> GetReachyStateAsync(global::Reachy.ReachyId request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_GetReachyState, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncServerStreamingCall<global::Reachy.ReachyState> StreamReachyState(global::Reachy.ReachyStreamStateRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return StreamReachyState(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncServerStreamingCall<global::Reachy.ReachyState> StreamReachyState(global::Reachy.ReachyStreamStateRequest request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncServerStreamingCall(__Method_StreamReachyState, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Reachy.ReachyStatus Audit(global::Reachy.ReachyId request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return Audit(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Reachy.ReachyStatus Audit(global::Reachy.ReachyId request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_Audit, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Reachy.ReachyStatus> AuditAsync(global::Reachy.ReachyId request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return AuditAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Reachy.ReachyStatus> AuditAsync(global::Reachy.ReachyId request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_Audit, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncServerStreamingCall<global::Reachy.ReachyStatus> StreamAudit(global::Reachy.ReachyStreamAuditRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return StreamAudit(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncServerStreamingCall<global::Reachy.ReachyStatus> StreamAudit(global::Reachy.ReachyStreamAuditRequest request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncServerStreamingCall(__Method_StreamAudit, null, options, request);
      }
      /// <summary>Creates a new instance of client from given <c>ClientBaseConfiguration</c>.</summary>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      protected override ReachyServiceClient NewInstance(ClientBaseConfiguration configuration)
      {
        return new ReachyServiceClient(configuration);
      }
    }

    /// <summary>Creates service definition that can be registered with a server</summary>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    public static grpc::ServerServiceDefinition BindService(ReachyServiceBase serviceImpl)
    {
      return grpc::ServerServiceDefinition.CreateBuilder()
          .AddMethod(__Method_GetReachy, serviceImpl.GetReachy)
          .AddMethod(__Method_GetReachyState, serviceImpl.GetReachyState)
          .AddMethod(__Method_StreamReachyState, serviceImpl.StreamReachyState)
          .AddMethod(__Method_Audit, serviceImpl.Audit)
          .AddMethod(__Method_StreamAudit, serviceImpl.StreamAudit).Build();
    }

    /// <summary>Register service method with a service binder with or without implementation. Useful when customizing the service binding logic.
    /// Note: this method is part of an experimental API that can change or be removed without any prior notice.</summary>
    /// <param name="serviceBinder">Service methods will be bound by calling <c>AddMethod</c> on this object.</param>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    public static void BindService(grpc::ServiceBinderBase serviceBinder, ReachyServiceBase serviceImpl)
    {
      serviceBinder.AddMethod(__Method_GetReachy, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Google.Protobuf.WellKnownTypes.Empty, global::Reachy.Reachy>(serviceImpl.GetReachy));
      serviceBinder.AddMethod(__Method_GetReachyState, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Reachy.ReachyId, global::Reachy.ReachyState>(serviceImpl.GetReachyState));
      serviceBinder.AddMethod(__Method_StreamReachyState, serviceImpl == null ? null : new grpc::ServerStreamingServerMethod<global::Reachy.ReachyStreamStateRequest, global::Reachy.ReachyState>(serviceImpl.StreamReachyState));
      serviceBinder.AddMethod(__Method_Audit, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Reachy.ReachyId, global::Reachy.ReachyStatus>(serviceImpl.Audit));
      serviceBinder.AddMethod(__Method_StreamAudit, serviceImpl == null ? null : new grpc::ServerStreamingServerMethod<global::Reachy.ReachyStreamAuditRequest, global::Reachy.ReachyStatus>(serviceImpl.StreamAudit));
    }

  }
}
#endregion

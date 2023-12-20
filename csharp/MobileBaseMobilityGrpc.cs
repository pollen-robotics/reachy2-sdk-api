// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: mobile_base_mobility.proto
// </auto-generated>
#pragma warning disable 0414, 1591, 8981, 0612
#region Designer generated code

using grpc = global::Grpc.Core;

namespace Mobile.Base.Mobility {
  public static partial class MobileBaseMobilityService
  {
    static readonly string __ServiceName = "mobile.base.mobility.MobileBaseMobilityService";

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
    static readonly grpc::Marshaller<global::Mobile.Base.Mobility.TargetDirectionCommand> __Marshaller_mobile_base_mobility_TargetDirectionCommand = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Mobile.Base.Mobility.TargetDirectionCommand.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Mobile.Base.Mobility.MobilityServiceAck> __Marshaller_mobile_base_mobility_MobilityServiceAck = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Mobile.Base.Mobility.MobilityServiceAck.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Mobile.Base.Mobility.SetSpeedVector> __Marshaller_mobile_base_mobility_SetSpeedVector = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Mobile.Base.Mobility.SetSpeedVector.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Mobile.Base.Mobility.GoToVector> __Marshaller_mobile_base_mobility_GoToVector = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Mobile.Base.Mobility.GoToVector.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Google.Protobuf.WellKnownTypes.Empty> __Marshaller_google_protobuf_Empty = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Google.Protobuf.WellKnownTypes.Empty.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Mobile.Base.Mobility.DistanceToGoalVector> __Marshaller_mobile_base_mobility_DistanceToGoalVector = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Mobile.Base.Mobility.DistanceToGoalVector.Parser));

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::Mobile.Base.Mobility.TargetDirectionCommand, global::Mobile.Base.Mobility.MobilityServiceAck> __Method_SendDirection = new grpc::Method<global::Mobile.Base.Mobility.TargetDirectionCommand, global::Mobile.Base.Mobility.MobilityServiceAck>(
        grpc::MethodType.Unary,
        __ServiceName,
        "SendDirection",
        __Marshaller_mobile_base_mobility_TargetDirectionCommand,
        __Marshaller_mobile_base_mobility_MobilityServiceAck);

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::Mobile.Base.Mobility.SetSpeedVector, global::Mobile.Base.Mobility.MobilityServiceAck> __Method_SendSetSpeed = new grpc::Method<global::Mobile.Base.Mobility.SetSpeedVector, global::Mobile.Base.Mobility.MobilityServiceAck>(
        grpc::MethodType.Unary,
        __ServiceName,
        "SendSetSpeed",
        __Marshaller_mobile_base_mobility_SetSpeedVector,
        __Marshaller_mobile_base_mobility_MobilityServiceAck);

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::Mobile.Base.Mobility.GoToVector, global::Mobile.Base.Mobility.MobilityServiceAck> __Method_SendGoTo = new grpc::Method<global::Mobile.Base.Mobility.GoToVector, global::Mobile.Base.Mobility.MobilityServiceAck>(
        grpc::MethodType.Unary,
        __ServiceName,
        "SendGoTo",
        __Marshaller_mobile_base_mobility_GoToVector,
        __Marshaller_mobile_base_mobility_MobilityServiceAck);

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Mobility.DistanceToGoalVector> __Method_DistanceToGoal = new grpc::Method<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Mobility.DistanceToGoalVector>(
        grpc::MethodType.Unary,
        __ServiceName,
        "DistanceToGoal",
        __Marshaller_google_protobuf_Empty,
        __Marshaller_mobile_base_mobility_DistanceToGoalVector);

    /// <summary>Service descriptor</summary>
    public static global::Google.Protobuf.Reflection.ServiceDescriptor Descriptor
    {
      get { return global::Mobile.Base.Mobility.MobileBaseMobilityReflection.Descriptor.Services[0]; }
    }

    /// <summary>Base class for server-side implementations of MobileBaseMobilityService</summary>
    [grpc::BindServiceMethod(typeof(MobileBaseMobilityService), "BindService")]
    public abstract partial class MobileBaseMobilityServiceBase
    {
      /// <summary>
      /// Mobility commands
      /// </summary>
      /// <param name="request">The request received from the client.</param>
      /// <param name="context">The context of the server-side call handler being invoked.</param>
      /// <returns>The response to send back to the client (wrapped by a task).</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::System.Threading.Tasks.Task<global::Mobile.Base.Mobility.MobilityServiceAck> SendDirection(global::Mobile.Base.Mobility.TargetDirectionCommand request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::System.Threading.Tasks.Task<global::Mobile.Base.Mobility.MobilityServiceAck> SendSetSpeed(global::Mobile.Base.Mobility.SetSpeedVector request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::System.Threading.Tasks.Task<global::Mobile.Base.Mobility.MobilityServiceAck> SendGoTo(global::Mobile.Base.Mobility.GoToVector request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::System.Threading.Tasks.Task<global::Mobile.Base.Mobility.DistanceToGoalVector> DistanceToGoal(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

    }

    /// <summary>Client for MobileBaseMobilityService</summary>
    public partial class MobileBaseMobilityServiceClient : grpc::ClientBase<MobileBaseMobilityServiceClient>
    {
      /// <summary>Creates a new client for MobileBaseMobilityService</summary>
      /// <param name="channel">The channel to use to make remote calls.</param>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public MobileBaseMobilityServiceClient(grpc::ChannelBase channel) : base(channel)
      {
      }
      /// <summary>Creates a new client for MobileBaseMobilityService that uses a custom <c>CallInvoker</c>.</summary>
      /// <param name="callInvoker">The callInvoker to use to make remote calls.</param>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public MobileBaseMobilityServiceClient(grpc::CallInvoker callInvoker) : base(callInvoker)
      {
      }
      /// <summary>Protected parameterless constructor to allow creation of test doubles.</summary>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      protected MobileBaseMobilityServiceClient() : base()
      {
      }
      /// <summary>Protected constructor to allow creation of configured clients.</summary>
      /// <param name="configuration">The client configuration.</param>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      protected MobileBaseMobilityServiceClient(ClientBaseConfiguration configuration) : base(configuration)
      {
      }

      /// <summary>
      /// Mobility commands
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="headers">The initial metadata to send with the call. This parameter is optional.</param>
      /// <param name="deadline">An optional deadline for the call. The call will be cancelled if deadline is hit.</param>
      /// <param name="cancellationToken">An optional token for canceling the call.</param>
      /// <returns>The response received from the server.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Mobility.MobilityServiceAck SendDirection(global::Mobile.Base.Mobility.TargetDirectionCommand request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return SendDirection(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      /// <summary>
      /// Mobility commands
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="options">The options for the call.</param>
      /// <returns>The response received from the server.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Mobility.MobilityServiceAck SendDirection(global::Mobile.Base.Mobility.TargetDirectionCommand request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_SendDirection, null, options, request);
      }
      /// <summary>
      /// Mobility commands
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="headers">The initial metadata to send with the call. This parameter is optional.</param>
      /// <param name="deadline">An optional deadline for the call. The call will be cancelled if deadline is hit.</param>
      /// <param name="cancellationToken">An optional token for canceling the call.</param>
      /// <returns>The call object.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Mobility.MobilityServiceAck> SendDirectionAsync(global::Mobile.Base.Mobility.TargetDirectionCommand request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return SendDirectionAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      /// <summary>
      /// Mobility commands
      /// </summary>
      /// <param name="request">The request to send to the server.</param>
      /// <param name="options">The options for the call.</param>
      /// <returns>The call object.</returns>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Mobility.MobilityServiceAck> SendDirectionAsync(global::Mobile.Base.Mobility.TargetDirectionCommand request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_SendDirection, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Mobility.MobilityServiceAck SendSetSpeed(global::Mobile.Base.Mobility.SetSpeedVector request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return SendSetSpeed(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Mobility.MobilityServiceAck SendSetSpeed(global::Mobile.Base.Mobility.SetSpeedVector request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_SendSetSpeed, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Mobility.MobilityServiceAck> SendSetSpeedAsync(global::Mobile.Base.Mobility.SetSpeedVector request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return SendSetSpeedAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Mobility.MobilityServiceAck> SendSetSpeedAsync(global::Mobile.Base.Mobility.SetSpeedVector request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_SendSetSpeed, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Mobility.MobilityServiceAck SendGoTo(global::Mobile.Base.Mobility.GoToVector request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return SendGoTo(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Mobility.MobilityServiceAck SendGoTo(global::Mobile.Base.Mobility.GoToVector request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_SendGoTo, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Mobility.MobilityServiceAck> SendGoToAsync(global::Mobile.Base.Mobility.GoToVector request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return SendGoToAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Mobility.MobilityServiceAck> SendGoToAsync(global::Mobile.Base.Mobility.GoToVector request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_SendGoTo, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Mobility.DistanceToGoalVector DistanceToGoal(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return DistanceToGoal(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Mobility.DistanceToGoalVector DistanceToGoal(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_DistanceToGoal, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Mobility.DistanceToGoalVector> DistanceToGoalAsync(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return DistanceToGoalAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Mobility.DistanceToGoalVector> DistanceToGoalAsync(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_DistanceToGoal, null, options, request);
      }
      /// <summary>Creates a new instance of client from given <c>ClientBaseConfiguration</c>.</summary>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      protected override MobileBaseMobilityServiceClient NewInstance(ClientBaseConfiguration configuration)
      {
        return new MobileBaseMobilityServiceClient(configuration);
      }
    }

    /// <summary>Creates service definition that can be registered with a server</summary>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    public static grpc::ServerServiceDefinition BindService(MobileBaseMobilityServiceBase serviceImpl)
    {
      return grpc::ServerServiceDefinition.CreateBuilder()
          .AddMethod(__Method_SendDirection, serviceImpl.SendDirection)
          .AddMethod(__Method_SendSetSpeed, serviceImpl.SendSetSpeed)
          .AddMethod(__Method_SendGoTo, serviceImpl.SendGoTo)
          .AddMethod(__Method_DistanceToGoal, serviceImpl.DistanceToGoal).Build();
    }

    /// <summary>Register service method with a service binder with or without implementation. Useful when customizing the service binding logic.
    /// Note: this method is part of an experimental API that can change or be removed without any prior notice.</summary>
    /// <param name="serviceBinder">Service methods will be bound by calling <c>AddMethod</c> on this object.</param>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    public static void BindService(grpc::ServiceBinderBase serviceBinder, MobileBaseMobilityServiceBase serviceImpl)
    {
      serviceBinder.AddMethod(__Method_SendDirection, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Mobile.Base.Mobility.TargetDirectionCommand, global::Mobile.Base.Mobility.MobilityServiceAck>(serviceImpl.SendDirection));
      serviceBinder.AddMethod(__Method_SendSetSpeed, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Mobile.Base.Mobility.SetSpeedVector, global::Mobile.Base.Mobility.MobilityServiceAck>(serviceImpl.SendSetSpeed));
      serviceBinder.AddMethod(__Method_SendGoTo, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Mobile.Base.Mobility.GoToVector, global::Mobile.Base.Mobility.MobilityServiceAck>(serviceImpl.SendGoTo));
      serviceBinder.AddMethod(__Method_DistanceToGoal, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Mobility.DistanceToGoalVector>(serviceImpl.DistanceToGoal));
    }

  }
}
#endregion
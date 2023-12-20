// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: mobile_base_utility.proto
// </auto-generated>
#pragma warning disable 0414, 1591, 8981, 0612
#region Designer generated code

using grpc = global::Grpc.Core;

namespace Mobile.Base.Utility {
  public static partial class MobileBaseUtilityService
  {
    static readonly string __ServiceName = "mobile.base.utility.MobileBaseUtilityService";

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
    static readonly grpc::Marshaller<global::Mobile.Base.Utility.ControlModeCommand> __Marshaller_mobile_base_utility_ControlModeCommand = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Mobile.Base.Utility.ControlModeCommand.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Mobile.Base.Mobility.MobilityServiceAck> __Marshaller_mobile_base_mobility_MobilityServiceAck = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Mobile.Base.Mobility.MobilityServiceAck.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Google.Protobuf.WellKnownTypes.Empty> __Marshaller_google_protobuf_Empty = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Google.Protobuf.WellKnownTypes.Empty.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Mobile.Base.Utility.ZuuuModeCommand> __Marshaller_mobile_base_utility_ZuuuModeCommand = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Mobile.Base.Utility.ZuuuModeCommand.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Mobile.Base.Utility.BatteryLevel> __Marshaller_mobile_base_utility_BatteryLevel = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Mobile.Base.Utility.BatteryLevel.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Mobile.Base.Utility.OdometryVector> __Marshaller_mobile_base_utility_OdometryVector = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Mobile.Base.Utility.OdometryVector.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Mobile.Base.Utility.MobileBase> __Marshaller_mobile_base_utility_MobileBase = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Mobile.Base.Utility.MobileBase.Parser));
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Marshaller<global::Mobile.Base.Utility.MobileBaseState> __Marshaller_mobile_base_utility_MobileBaseState = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Mobile.Base.Utility.MobileBaseState.Parser));

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::Mobile.Base.Utility.ControlModeCommand, global::Mobile.Base.Mobility.MobilityServiceAck> __Method_SetControlMode = new grpc::Method<global::Mobile.Base.Utility.ControlModeCommand, global::Mobile.Base.Mobility.MobilityServiceAck>(
        grpc::MethodType.Unary,
        __ServiceName,
        "SetControlMode",
        __Marshaller_mobile_base_utility_ControlModeCommand,
        __Marshaller_mobile_base_mobility_MobilityServiceAck);

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Utility.ControlModeCommand> __Method_GetControlMode = new grpc::Method<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Utility.ControlModeCommand>(
        grpc::MethodType.Unary,
        __ServiceName,
        "GetControlMode",
        __Marshaller_google_protobuf_Empty,
        __Marshaller_mobile_base_utility_ControlModeCommand);

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::Mobile.Base.Utility.ZuuuModeCommand, global::Mobile.Base.Mobility.MobilityServiceAck> __Method_SetZuuuMode = new grpc::Method<global::Mobile.Base.Utility.ZuuuModeCommand, global::Mobile.Base.Mobility.MobilityServiceAck>(
        grpc::MethodType.Unary,
        __ServiceName,
        "SetZuuuMode",
        __Marshaller_mobile_base_utility_ZuuuModeCommand,
        __Marshaller_mobile_base_mobility_MobilityServiceAck);

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Utility.ZuuuModeCommand> __Method_GetZuuuMode = new grpc::Method<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Utility.ZuuuModeCommand>(
        grpc::MethodType.Unary,
        __ServiceName,
        "GetZuuuMode",
        __Marshaller_google_protobuf_Empty,
        __Marshaller_mobile_base_utility_ZuuuModeCommand);

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Utility.BatteryLevel> __Method_GetBatteryLevel = new grpc::Method<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Utility.BatteryLevel>(
        grpc::MethodType.Unary,
        __ServiceName,
        "GetBatteryLevel",
        __Marshaller_google_protobuf_Empty,
        __Marshaller_mobile_base_utility_BatteryLevel);

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Utility.OdometryVector> __Method_GetOdometry = new grpc::Method<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Utility.OdometryVector>(
        grpc::MethodType.Unary,
        __ServiceName,
        "GetOdometry",
        __Marshaller_google_protobuf_Empty,
        __Marshaller_mobile_base_utility_OdometryVector);

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Mobility.MobilityServiceAck> __Method_ResetOdometry = new grpc::Method<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Mobility.MobilityServiceAck>(
        grpc::MethodType.Unary,
        __ServiceName,
        "ResetOdometry",
        __Marshaller_google_protobuf_Empty,
        __Marshaller_mobile_base_mobility_MobilityServiceAck);

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Utility.MobileBase> __Method_GetMobileBase = new grpc::Method<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Utility.MobileBase>(
        grpc::MethodType.Unary,
        __ServiceName,
        "GetMobileBase",
        __Marshaller_google_protobuf_Empty,
        __Marshaller_mobile_base_utility_MobileBase);

    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    static readonly grpc::Method<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Utility.MobileBaseState> __Method_GetState = new grpc::Method<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Utility.MobileBaseState>(
        grpc::MethodType.Unary,
        __ServiceName,
        "GetState",
        __Marshaller_google_protobuf_Empty,
        __Marshaller_mobile_base_utility_MobileBaseState);

    /// <summary>Service descriptor</summary>
    public static global::Google.Protobuf.Reflection.ServiceDescriptor Descriptor
    {
      get { return global::Mobile.Base.Utility.MobileBaseUtilityReflection.Descriptor.Services[0]; }
    }

    /// <summary>Base class for server-side implementations of MobileBaseUtilityService</summary>
    [grpc::BindServiceMethod(typeof(MobileBaseUtilityService), "BindService")]
    public abstract partial class MobileBaseUtilityServiceBase
    {
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::System.Threading.Tasks.Task<global::Mobile.Base.Mobility.MobilityServiceAck> SetControlMode(global::Mobile.Base.Utility.ControlModeCommand request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::System.Threading.Tasks.Task<global::Mobile.Base.Utility.ControlModeCommand> GetControlMode(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::System.Threading.Tasks.Task<global::Mobile.Base.Mobility.MobilityServiceAck> SetZuuuMode(global::Mobile.Base.Utility.ZuuuModeCommand request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::System.Threading.Tasks.Task<global::Mobile.Base.Utility.ZuuuModeCommand> GetZuuuMode(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::System.Threading.Tasks.Task<global::Mobile.Base.Utility.BatteryLevel> GetBatteryLevel(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::System.Threading.Tasks.Task<global::Mobile.Base.Utility.OdometryVector> GetOdometry(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::System.Threading.Tasks.Task<global::Mobile.Base.Mobility.MobilityServiceAck> ResetOdometry(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::System.Threading.Tasks.Task<global::Mobile.Base.Utility.MobileBase> GetMobileBase(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::System.Threading.Tasks.Task<global::Mobile.Base.Utility.MobileBaseState> GetState(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

    }

    /// <summary>Client for MobileBaseUtilityService</summary>
    public partial class MobileBaseUtilityServiceClient : grpc::ClientBase<MobileBaseUtilityServiceClient>
    {
      /// <summary>Creates a new client for MobileBaseUtilityService</summary>
      /// <param name="channel">The channel to use to make remote calls.</param>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public MobileBaseUtilityServiceClient(grpc::ChannelBase channel) : base(channel)
      {
      }
      /// <summary>Creates a new client for MobileBaseUtilityService that uses a custom <c>CallInvoker</c>.</summary>
      /// <param name="callInvoker">The callInvoker to use to make remote calls.</param>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public MobileBaseUtilityServiceClient(grpc::CallInvoker callInvoker) : base(callInvoker)
      {
      }
      /// <summary>Protected parameterless constructor to allow creation of test doubles.</summary>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      protected MobileBaseUtilityServiceClient() : base()
      {
      }
      /// <summary>Protected constructor to allow creation of configured clients.</summary>
      /// <param name="configuration">The client configuration.</param>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      protected MobileBaseUtilityServiceClient(ClientBaseConfiguration configuration) : base(configuration)
      {
      }

      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Mobility.MobilityServiceAck SetControlMode(global::Mobile.Base.Utility.ControlModeCommand request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return SetControlMode(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Mobility.MobilityServiceAck SetControlMode(global::Mobile.Base.Utility.ControlModeCommand request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_SetControlMode, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Mobility.MobilityServiceAck> SetControlModeAsync(global::Mobile.Base.Utility.ControlModeCommand request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return SetControlModeAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Mobility.MobilityServiceAck> SetControlModeAsync(global::Mobile.Base.Utility.ControlModeCommand request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_SetControlMode, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Utility.ControlModeCommand GetControlMode(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetControlMode(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Utility.ControlModeCommand GetControlMode(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_GetControlMode, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Utility.ControlModeCommand> GetControlModeAsync(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetControlModeAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Utility.ControlModeCommand> GetControlModeAsync(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_GetControlMode, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Mobility.MobilityServiceAck SetZuuuMode(global::Mobile.Base.Utility.ZuuuModeCommand request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return SetZuuuMode(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Mobility.MobilityServiceAck SetZuuuMode(global::Mobile.Base.Utility.ZuuuModeCommand request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_SetZuuuMode, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Mobility.MobilityServiceAck> SetZuuuModeAsync(global::Mobile.Base.Utility.ZuuuModeCommand request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return SetZuuuModeAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Mobility.MobilityServiceAck> SetZuuuModeAsync(global::Mobile.Base.Utility.ZuuuModeCommand request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_SetZuuuMode, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Utility.ZuuuModeCommand GetZuuuMode(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetZuuuMode(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Utility.ZuuuModeCommand GetZuuuMode(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_GetZuuuMode, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Utility.ZuuuModeCommand> GetZuuuModeAsync(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetZuuuModeAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Utility.ZuuuModeCommand> GetZuuuModeAsync(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_GetZuuuMode, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Utility.BatteryLevel GetBatteryLevel(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetBatteryLevel(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Utility.BatteryLevel GetBatteryLevel(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_GetBatteryLevel, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Utility.BatteryLevel> GetBatteryLevelAsync(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetBatteryLevelAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Utility.BatteryLevel> GetBatteryLevelAsync(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_GetBatteryLevel, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Utility.OdometryVector GetOdometry(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetOdometry(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Utility.OdometryVector GetOdometry(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_GetOdometry, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Utility.OdometryVector> GetOdometryAsync(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetOdometryAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Utility.OdometryVector> GetOdometryAsync(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_GetOdometry, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Mobility.MobilityServiceAck ResetOdometry(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return ResetOdometry(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Mobility.MobilityServiceAck ResetOdometry(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_ResetOdometry, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Mobility.MobilityServiceAck> ResetOdometryAsync(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return ResetOdometryAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Mobility.MobilityServiceAck> ResetOdometryAsync(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_ResetOdometry, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Utility.MobileBase GetMobileBase(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetMobileBase(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Utility.MobileBase GetMobileBase(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_GetMobileBase, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Utility.MobileBase> GetMobileBaseAsync(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetMobileBaseAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Utility.MobileBase> GetMobileBaseAsync(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_GetMobileBase, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Utility.MobileBaseState GetState(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetState(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual global::Mobile.Base.Utility.MobileBaseState GetState(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_GetState, null, options, request);
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Utility.MobileBaseState> GetStateAsync(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetStateAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Utility.MobileBaseState> GetStateAsync(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_GetState, null, options, request);
      }
      /// <summary>Creates a new instance of client from given <c>ClientBaseConfiguration</c>.</summary>
      [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
      protected override MobileBaseUtilityServiceClient NewInstance(ClientBaseConfiguration configuration)
      {
        return new MobileBaseUtilityServiceClient(configuration);
      }
    }

    /// <summary>Creates service definition that can be registered with a server</summary>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    public static grpc::ServerServiceDefinition BindService(MobileBaseUtilityServiceBase serviceImpl)
    {
      return grpc::ServerServiceDefinition.CreateBuilder()
          .AddMethod(__Method_SetControlMode, serviceImpl.SetControlMode)
          .AddMethod(__Method_GetControlMode, serviceImpl.GetControlMode)
          .AddMethod(__Method_SetZuuuMode, serviceImpl.SetZuuuMode)
          .AddMethod(__Method_GetZuuuMode, serviceImpl.GetZuuuMode)
          .AddMethod(__Method_GetBatteryLevel, serviceImpl.GetBatteryLevel)
          .AddMethod(__Method_GetOdometry, serviceImpl.GetOdometry)
          .AddMethod(__Method_ResetOdometry, serviceImpl.ResetOdometry)
          .AddMethod(__Method_GetMobileBase, serviceImpl.GetMobileBase)
          .AddMethod(__Method_GetState, serviceImpl.GetState).Build();
    }

    /// <summary>Register service method with a service binder with or without implementation. Useful when customizing the service binding logic.
    /// Note: this method is part of an experimental API that can change or be removed without any prior notice.</summary>
    /// <param name="serviceBinder">Service methods will be bound by calling <c>AddMethod</c> on this object.</param>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    [global::System.CodeDom.Compiler.GeneratedCode("grpc_csharp_plugin", null)]
    public static void BindService(grpc::ServiceBinderBase serviceBinder, MobileBaseUtilityServiceBase serviceImpl)
    {
      serviceBinder.AddMethod(__Method_SetControlMode, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Mobile.Base.Utility.ControlModeCommand, global::Mobile.Base.Mobility.MobilityServiceAck>(serviceImpl.SetControlMode));
      serviceBinder.AddMethod(__Method_GetControlMode, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Utility.ControlModeCommand>(serviceImpl.GetControlMode));
      serviceBinder.AddMethod(__Method_SetZuuuMode, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Mobile.Base.Utility.ZuuuModeCommand, global::Mobile.Base.Mobility.MobilityServiceAck>(serviceImpl.SetZuuuMode));
      serviceBinder.AddMethod(__Method_GetZuuuMode, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Utility.ZuuuModeCommand>(serviceImpl.GetZuuuMode));
      serviceBinder.AddMethod(__Method_GetBatteryLevel, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Utility.BatteryLevel>(serviceImpl.GetBatteryLevel));
      serviceBinder.AddMethod(__Method_GetOdometry, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Utility.OdometryVector>(serviceImpl.GetOdometry));
      serviceBinder.AddMethod(__Method_ResetOdometry, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Mobility.MobilityServiceAck>(serviceImpl.ResetOdometry));
      serviceBinder.AddMethod(__Method_GetMobileBase, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Utility.MobileBase>(serviceImpl.GetMobileBase));
      serviceBinder.AddMethod(__Method_GetState, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Utility.MobileBaseState>(serviceImpl.GetState));
    }

  }
}
#endregion
// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: mobile_base_lidar.proto
// </auto-generated>
#pragma warning disable 0414, 1591
#region Designer generated code

using grpc = global::Grpc.Core;

namespace Mobile.Base.Lidar {
  public static partial class MobileBaseLidarService
  {
    static readonly string __ServiceName = "mobile.base.lidar.MobileBaseLidarService";

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

    static class __Helper_MessageCache<T>
    {
      public static readonly bool IsBufferMessage = global::System.Reflection.IntrospectionExtensions.GetTypeInfo(typeof(global::Google.Protobuf.IBufferMessage)).IsAssignableFrom(typeof(T));
    }

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

    static readonly grpc::Marshaller<global::Mobile.Base.Lidar.LidarSafety> __Marshaller_mobile_base_lidar_LidarSafety = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Mobile.Base.Lidar.LidarSafety.Parser));
    static readonly grpc::Marshaller<global::Mobile.Base.Mobility.MobilityServiceAck> __Marshaller_mobile_base_mobility_MobilityServiceAck = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Mobile.Base.Mobility.MobilityServiceAck.Parser));
    static readonly grpc::Marshaller<global::Google.Protobuf.WellKnownTypes.Empty> __Marshaller_google_protobuf_Empty = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Google.Protobuf.WellKnownTypes.Empty.Parser));
    static readonly grpc::Marshaller<global::Mobile.Base.Lidar.LidarMap> __Marshaller_mobile_base_lidar_LidarMap = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Mobile.Base.Lidar.LidarMap.Parser));
    static readonly grpc::Marshaller<global::Mobile.Base.Lidar.LidarObstacleDetectionStatus> __Marshaller_mobile_base_lidar_LidarObstacleDetectionStatus = grpc::Marshallers.Create(__Helper_SerializeMessage, context => __Helper_DeserializeMessage(context, global::Mobile.Base.Lidar.LidarObstacleDetectionStatus.Parser));

    static readonly grpc::Method<global::Mobile.Base.Lidar.LidarSafety, global::Mobile.Base.Mobility.MobilityServiceAck> __Method_SetZuuuSafety = new grpc::Method<global::Mobile.Base.Lidar.LidarSafety, global::Mobile.Base.Mobility.MobilityServiceAck>(
        grpc::MethodType.Unary,
        __ServiceName,
        "SetZuuuSafety",
        __Marshaller_mobile_base_lidar_LidarSafety,
        __Marshaller_mobile_base_mobility_MobilityServiceAck);

    static readonly grpc::Method<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Lidar.LidarSafety> __Method_GetZuuuSafety = new grpc::Method<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Lidar.LidarSafety>(
        grpc::MethodType.Unary,
        __ServiceName,
        "GetZuuuSafety",
        __Marshaller_google_protobuf_Empty,
        __Marshaller_mobile_base_lidar_LidarSafety);

    static readonly grpc::Method<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Lidar.LidarMap> __Method_GetLidarMap = new grpc::Method<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Lidar.LidarMap>(
        grpc::MethodType.Unary,
        __ServiceName,
        "GetLidarMap",
        __Marshaller_google_protobuf_Empty,
        __Marshaller_mobile_base_lidar_LidarMap);

    static readonly grpc::Method<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Lidar.LidarObstacleDetectionStatus> __Method_GetLidarObstacleDetectionStatus = new grpc::Method<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Lidar.LidarObstacleDetectionStatus>(
        grpc::MethodType.Unary,
        __ServiceName,
        "GetLidarObstacleDetectionStatus",
        __Marshaller_google_protobuf_Empty,
        __Marshaller_mobile_base_lidar_LidarObstacleDetectionStatus);

    /// <summary>Service descriptor</summary>
    public static global::Google.Protobuf.Reflection.ServiceDescriptor Descriptor
    {
      get { return global::Mobile.Base.Lidar.MobileBaseLidarReflection.Descriptor.Services[0]; }
    }

    /// <summary>Base class for server-side implementations of MobileBaseLidarService</summary>
    [grpc::BindServiceMethod(typeof(MobileBaseLidarService), "BindService")]
    public abstract partial class MobileBaseLidarServiceBase
    {
      public virtual global::System.Threading.Tasks.Task<global::Mobile.Base.Mobility.MobilityServiceAck> SetZuuuSafety(global::Mobile.Base.Lidar.LidarSafety request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      public virtual global::System.Threading.Tasks.Task<global::Mobile.Base.Lidar.LidarSafety> GetZuuuSafety(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      public virtual global::System.Threading.Tasks.Task<global::Mobile.Base.Lidar.LidarMap> GetLidarMap(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

      public virtual global::System.Threading.Tasks.Task<global::Mobile.Base.Lidar.LidarObstacleDetectionStatus> GetLidarObstacleDetectionStatus(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

    }

    /// <summary>Client for MobileBaseLidarService</summary>
    public partial class MobileBaseLidarServiceClient : grpc::ClientBase<MobileBaseLidarServiceClient>
    {
      /// <summary>Creates a new client for MobileBaseLidarService</summary>
      /// <param name="channel">The channel to use to make remote calls.</param>
      public MobileBaseLidarServiceClient(grpc::ChannelBase channel) : base(channel)
      {
      }
      /// <summary>Creates a new client for MobileBaseLidarService that uses a custom <c>CallInvoker</c>.</summary>
      /// <param name="callInvoker">The callInvoker to use to make remote calls.</param>
      public MobileBaseLidarServiceClient(grpc::CallInvoker callInvoker) : base(callInvoker)
      {
      }
      /// <summary>Protected parameterless constructor to allow creation of test doubles.</summary>
      protected MobileBaseLidarServiceClient() : base()
      {
      }
      /// <summary>Protected constructor to allow creation of configured clients.</summary>
      /// <param name="configuration">The client configuration.</param>
      protected MobileBaseLidarServiceClient(ClientBaseConfiguration configuration) : base(configuration)
      {
      }

      public virtual global::Mobile.Base.Mobility.MobilityServiceAck SetZuuuSafety(global::Mobile.Base.Lidar.LidarSafety request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return SetZuuuSafety(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::Mobile.Base.Mobility.MobilityServiceAck SetZuuuSafety(global::Mobile.Base.Lidar.LidarSafety request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_SetZuuuSafety, null, options, request);
      }
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Mobility.MobilityServiceAck> SetZuuuSafetyAsync(global::Mobile.Base.Lidar.LidarSafety request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return SetZuuuSafetyAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Mobility.MobilityServiceAck> SetZuuuSafetyAsync(global::Mobile.Base.Lidar.LidarSafety request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_SetZuuuSafety, null, options, request);
      }
      public virtual global::Mobile.Base.Lidar.LidarSafety GetZuuuSafety(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetZuuuSafety(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::Mobile.Base.Lidar.LidarSafety GetZuuuSafety(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_GetZuuuSafety, null, options, request);
      }
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Lidar.LidarSafety> GetZuuuSafetyAsync(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetZuuuSafetyAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Lidar.LidarSafety> GetZuuuSafetyAsync(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_GetZuuuSafety, null, options, request);
      }
      public virtual global::Mobile.Base.Lidar.LidarMap GetLidarMap(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetLidarMap(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::Mobile.Base.Lidar.LidarMap GetLidarMap(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_GetLidarMap, null, options, request);
      }
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Lidar.LidarMap> GetLidarMapAsync(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetLidarMapAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Lidar.LidarMap> GetLidarMapAsync(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_GetLidarMap, null, options, request);
      }
      public virtual global::Mobile.Base.Lidar.LidarObstacleDetectionStatus GetLidarObstacleDetectionStatus(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetLidarObstacleDetectionStatus(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::Mobile.Base.Lidar.LidarObstacleDetectionStatus GetLidarObstacleDetectionStatus(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_GetLidarObstacleDetectionStatus, null, options, request);
      }
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Lidar.LidarObstacleDetectionStatus> GetLidarObstacleDetectionStatusAsync(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
      {
        return GetLidarObstacleDetectionStatusAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncUnaryCall<global::Mobile.Base.Lidar.LidarObstacleDetectionStatus> GetLidarObstacleDetectionStatusAsync(global::Google.Protobuf.WellKnownTypes.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_GetLidarObstacleDetectionStatus, null, options, request);
      }
      /// <summary>Creates a new instance of client from given <c>ClientBaseConfiguration</c>.</summary>
      protected override MobileBaseLidarServiceClient NewInstance(ClientBaseConfiguration configuration)
      {
        return new MobileBaseLidarServiceClient(configuration);
      }
    }

    /// <summary>Creates service definition that can be registered with a server</summary>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    public static grpc::ServerServiceDefinition BindService(MobileBaseLidarServiceBase serviceImpl)
    {
      return grpc::ServerServiceDefinition.CreateBuilder()
          .AddMethod(__Method_SetZuuuSafety, serviceImpl.SetZuuuSafety)
          .AddMethod(__Method_GetZuuuSafety, serviceImpl.GetZuuuSafety)
          .AddMethod(__Method_GetLidarMap, serviceImpl.GetLidarMap)
          .AddMethod(__Method_GetLidarObstacleDetectionStatus, serviceImpl.GetLidarObstacleDetectionStatus).Build();
    }

    /// <summary>Register service method with a service binder with or without implementation. Useful when customizing the  service binding logic.
    /// Note: this method is part of an experimental API that can change or be removed without any prior notice.</summary>
    /// <param name="serviceBinder">Service methods will be bound by calling <c>AddMethod</c> on this object.</param>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    public static void BindService(grpc::ServiceBinderBase serviceBinder, MobileBaseLidarServiceBase serviceImpl)
    {
      serviceBinder.AddMethod(__Method_SetZuuuSafety, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Mobile.Base.Lidar.LidarSafety, global::Mobile.Base.Mobility.MobilityServiceAck>(serviceImpl.SetZuuuSafety));
      serviceBinder.AddMethod(__Method_GetZuuuSafety, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Lidar.LidarSafety>(serviceImpl.GetZuuuSafety));
      serviceBinder.AddMethod(__Method_GetLidarMap, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Lidar.LidarMap>(serviceImpl.GetLidarMap));
      serviceBinder.AddMethod(__Method_GetLidarObstacleDetectionStatus, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::Google.Protobuf.WellKnownTypes.Empty, global::Mobile.Base.Lidar.LidarObstacleDetectionStatus>(serviceImpl.GetLidarObstacleDetectionStatus));
    }

  }
}
#endregion

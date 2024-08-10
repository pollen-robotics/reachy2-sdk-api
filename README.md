# Protobuf for Reachy 2 SDK

## Generate gRPC code

### For Python:

Python code is generated automatically for each commit. Just just need to `git pull` after you push changes to the .proto.

If you need to generate those files locally, just install `pip install mypy-protobuf` to generate the mypy stubs, and run:

```python
python -m grpc_tools.protoc -I./protos --python_out=./python/reachy2_sdk_api --grpc_python_out=./python/reachy2_sdk_api --mypy_out=./python/reachy2_sdk_api --mypy_grpc_out=./python/reachy2_sdk_api  ./protos/*.proto
```

### For C#

On a Windows computer, open `reachy_sdk.sln`` in Visual Studio.
`Click Build > Build Solution`
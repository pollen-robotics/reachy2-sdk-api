## Generate gRPC code

### For Python:
```python
python -m grpc_tools.protoc -I./protos --python_out=./python/reachy2_sdk_api --grpc_python_out=./python/reachy2_sdk_api ./protos/*.proto
```

### For C#

On a Windows computer, open reachy_sdk.sln in Visual Studio.
`Click Build > Build Solution`
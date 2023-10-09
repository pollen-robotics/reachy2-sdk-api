## Generate gRPC code

### For Python:
```python
python -m grpc_tools.protoc -I./protos --python_out=./python/reachy_sdk_api_v2 --grpc_python_out=./python/reachy_sdk_api_v2 ./protos/*.proto
```

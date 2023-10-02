# Installation for ts/js

## Installation of protoc-gen-grpc-web
The `protoc-gen-grpc-web` plugin is a protocol buffer compiler plugin for `gRPC-Web`. Below are the general steps to install it on various operating systems. These steps assume that you already have the protocol buffer compiler (`protoc`) installed on your system. If not, you need to [install it](https://grpc.io/docs/protoc-installation/) first.

### On a Unix-like OS (Linux/MacOS):

1. **Download the Plugin:**
   
   Navigate to the [release page of `grpc-web`](https://github.com/grpc/grpc-web/releases), and download the `protoc-gen-grpc-web-1.2.1-<platform>-x86_64` release (adjust the version number if needed).

2. **Make the Plugin Executable:**

    ```bash
    chmod +x protoc-gen-grpc-web-1.2.1-<platform>-x86_64
    ```

3. **Move the Plugin to Your `$PATH`:**

    ```bash
    sudo mv protoc-gen-grpc-web-1.2.1-<platform>-x86_64 /usr/local/bin/protoc-gen-grpc-web
    ```

### On Windows:

1. **Download the Plugin:**
   
   Navigate to the [release page of `grpc-web`](https://github.com/grpc/grpc-web/releases), and download the `protoc-gen-grpc-web-1.2.1-windows-x86_64.exe` release (adjust the version number if needed).

2. **Move the Plugin to a Directory in Your `%PATH%`:**
   
   - You can move the downloaded `.exe` file to a directory that is in your system’s `%PATH%` (e.g., `C:\Windows\System32`).
   - Alternatively, you can add the directory containing the downloaded `.exe` file to your `%PATH%`.

### Verifying the Installation:

- Open a terminal or command prompt and run:

    ```bash
    protoc-gen-grpc-web --version
    ```

- You should see the version information for `protoc-gen-grpc-web`.

### Usage:

After installation, you can then use the `protoc` command with the `--grpc-web_out` option to generate `gRPC-Web` service clients:

```bash
protoc -I=. your_proto_file.proto --grpc-web_out=import_style=commonjs,mode=grpcwebtext:.
```

Replace `your_proto_file.proto` with the name of your actual `.proto` file. Ensure you have the correct import paths and output paths specified for your project structure.

## Generation of js/ts grpc files
for f in ./protos/*.proto; do
  protoc -I=./protos \
         --js_out=import_style=commonjs:./js \
         --grpc-web_out=import_style=typescript,mode=grpcwebtext:./ts \
         "$f"
done

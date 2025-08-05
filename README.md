# Financial Protocol Python Library

This repository contains Python implementations of various financial market data protocols, generated from protocol definition files using the `fin-protoc` compiler.

## Project Structure

```
.
├── lib/                    # Generated protocol implementations
│   ├── bjse_binary.py     # Beijing Stock Exchange binary protocol
│   ├── bytebuf.py         # Byte buffer utilities
│   ├── checksum.py        # Checksum calculation utilities
│   ├── codec.py           # Generic codec framework
│   ├── rc_binary.py       # Related code binary protocol
│   ├── root_packet.py     # Root packet handling
│   ├── sse_binary.py      # Shanghai Stock Exchange binary protocol
│   └── szse_binary.py     # Shenzhen Stock Exchange binary protocol
├── submodules/            # Protocol definition files
└── Makefile              # Build automation
```

## Prerequisites

- Python 3.x
- `fin-protoc` compiler installed in `~/workspace/fin-protoc/bin/` from https://github.com/xinchentechnote/fin-protoc
- pytest for running tests

## Building the Project

```bash
# Compile all protocol definitions
make compile

# Run tests
make test

# Build and test everything
make all
```

## Available Protocols

The library includes implementations for the following financial market protocols:

1. **BSE Trade Binary v0.9** - Beijing Stock Exchange trading protocol
2. **SSE Binary v0.57** - Shanghai Stock Exchange binary protocol
3. **SZSE Binary v1.29** - Shenzhen Stock Exchange binary protocol
4. **Risk v0.1.0** - Risk management protocol
5. **Sample Protocol** - Example protocol implementation

## Usage

Each protocol implementation can be imported directly:

```python
from lib.sse_binary import SomeSSEMessage
from lib.szse_binary import SomeSZSEMessage
```

## Testing

Run all tests with:

```bash
make test
```

Or run specific test files:

```bash
python -m pytest lib/sse_binary_test.py
```

## Development

Protocol implementations are generated from `.pdsl` (Protocol Description Language) files using the `fin-protoc` compiler. Do not modify the generated Python files directly.

To add new protocols:
1. Add the protocol definition file to `submodules/fin-proto/`
2. Update the `compile` target in [Makefile](file:///home/s0596/workspace/fin-proto-py/Makefile) with the new protocol
3. Run `make compile` to generate the Python implementation
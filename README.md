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

class TestNewOrder(unittest.TestCase):
    def setUp(self):
        appl_extend = Extend100101()
        appl_extend.stop_px = 8
        appl_extend.min_qty = 8
        appl_extend.max_price_levels = 2
        appl_extend.time_in_force = "x"
        appl_extend.cash_margin = "x"
        self.packet = NewOrder()
        self.packet.submitting_pbuid = "xxxxxx"
        self.packet.security_id = "xxxxxxxx"
        self.packet.security_id_source = "xxxx"
        self.packet.owner_type = 2
        self.packet.clearing_firm = "xx"
        self.packet.transact_time = 8
        self.packet.user_info = "xxxxxxxx"
        self.packet.cl_ord_id = "xxxxxxxxxx"
        self.packet.account_id = "xxxxxxxxxxxx"
        self.packet.branch_id = "xxxx"
        self.packet.order_restrictions = "xxxx"
        self.packet.side = "x"
        self.packet.ord_type = "x"
        self.packet.order_qty = 8
        self.packet.price = 8
        self.packet.appl_id = "010"
        self.packet.appl_extend = appl_extend


    def test_encode_decode(self):
        buf = ByteBuf()
        self.packet.encode(buf)
        decoded_packet = NewOrder()
        decoded_packet.decode(buf)
        self.assertEqual(decoded_packet, self.packet)


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

## Related Repositories

- [`fin-proto`](https://github.com/xinchentechnote/fin-proto)

  - A comprehensive financial protocol library
  - Supports SSE, SZSE, and risk protocols
  - Includes Lua dissectors for Wireshark

- [`fin-proto-rs`](https://github.com/xinchentechnote/fin-proto-rs)

  - High-performance binary codec in Rust
  - Zero-copy serialization/deserialization
  - Supports SSE, SZSE, and risk protocols
  - Includes unit testing infrastructure

- [`fin-proto-go`](https://github.com/xinchentechnote/fin-proto-go)

  - Native Go implementation of the protocols
  - Standardized codec interface
  - Modular, exchange-specific architecture
  - This repository has been integrated into the [`gt-auto`](https://github.com/xinchentechnote/gt-auto) repository, an automated testing tool for financial systems(gateway,engine and so on)

- [`fin-proto-cpp`](https://github.com/xinchentechnote/fin-proto-cpp)

  - Efficient C++ implementation
  - Protocol support for SSE, SZSE, risk
  - Optimized serialization logic

- [`fin-proto-java`](https://github.com/xinchentechnote/fin-proto-java)

  - Binary protocol codec for Java
  - Netty ByteBuf integration
  - Gradle build system
  - Java 17+ compatible

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/xinchentechnote/fin-proto-py)

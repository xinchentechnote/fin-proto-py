# Makefile for fin-protoc project

# Variables
PROTO_DSL := ./submodules/fin-proto/sample/sample.pdsl
PROTO_DIR := proto/
OUTPUT_DIR := ./lib/
BIN_DIR := ~/workspace/fin-protoc/bin/

.PHONY: all compile test

all: compile test

build: compile

set_env:
	export PATH=$(BIN_DIR):$$PATH

compile:
	@echo "Compiling protocol..."
	$(BIN_DIR)/fin-protoc compile -f ./submodules/fin-proto/sample/sample.pdsl -p $(OUTPUT_DIR)
	$(BIN_DIR)/fin-protoc compile -f ./submodules/fin-proto/risk/risk_v0.1.0.dsl -p $(OUTPUT_DIR)
	$(BIN_DIR)/fin-protoc compile -f ./submodules/fin-proto/sse/binary/sse_bin_v0.57.pdsl -p $(OUTPUT_DIR)
	$(BIN_DIR)/fin-protoc compile -f ./submodules/fin-proto/szse/binary/szse_bin_v1.29.pdsl -p $(OUTPUT_DIR)

test:
	pytest

# Help target
help:
	@echo "Available targets:"
	@echo "  all       - Run compile, format and fix (default)"
	@echo "  compile   - Compile the protocol definitions"

# Makefile for fin-protoc project

# Variables
PROTO_DSL := ../submodules/fin-proto/sample/sample.pdsl
PROTO_DIR := proto/
OUTPUT_DIR := ./
BIN_DIR := ~/workspace/fin-protoc/bin/

.PHONY: all compile format fix clean

all: compile test

build: compile

set_env:
	export PATH=$(BIN_DIR):$$PATH

compile:
	@echo "Compiling protocol..."
	$(BIN_DIR)/fin-protoc compile -f ../submodules/fin-proto/sample/sample.pdsl -p $(OUTPUT_DIR)
	$(BIN_DIR)/fin-protoc compile -f ../submodules/fin-proto/risk/risk_v0.1.0.dsl -p $(OUTPUT_DIR)
	$(BIN_DIR)/fin-protoc compile -f ../submodules/fin-proto/sse/binary/sse_v0.57.pdsl -p $(OUTPUT_DIR)

# fmt: fix
# 	@echo "Formatting code..."
# 	go fmt ./...

# fix:
# 	@echo "Applying fixes..."
# 	goimports -w ./..
# 	go fix ./...

test:
	@echo "Running tests..."
	pytest

# Help target
help:
	@echo "Available targets:"
	@echo "  all       - Run compile, format and fix (default)"
	@echo "  compile   - Compile the protocol definitions"
	@echo "  build   - Compile the protocol definitions"
	@echo "  fmt       - Format the code using cargo fmt"
	@echo "  fix       - Apply automatic fixes using cargo fix"
	@echo "  help      - Show this help message"

import pytest
from lib.bytebuf import ByteBuf
from checksum import (
    create_checksum_service
)

# Fixture for test data
@pytest.fixture
def sample_data():
    buf =  ByteBuf()
    buf.write_bytes(b"123456789")
    return buf



def test_crc16_calculation(sample_data):
    service = create_checksum_service("CRC16")
    assert service.calc(sample_data) == 0x4B37


def test_crc32_calculation(sample_data):
    service = create_checksum_service("CRC32")
    assert service.calc(sample_data) == 0xCBF43926

def test_ssebin_calculation(sample_data):
    service = create_checksum_service("SSE_BIN")
    assert service.calc(sample_data) == sum(b"123456789") & 0xFF


def test_szsebin_calculation(sample_data):
    service = create_checksum_service("SZSE_BIN")
    assert service.calc(sample_data) == sum(b"123456789") % 256

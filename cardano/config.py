import binascii

# mainchain config
MAINCHAIN_ADDR = b'relays.cardano-mainnet.iohk.io:3000:0'
MAINCHAIN_GENESIS = binascii.unhexlify(
    '89d9b5a5b8ddc8d7e5a6795e9774d97faf1efea59b2caf7eaf9f8c5b32059df4')
MAINCHAIN_GENESIS_PREV = binascii.unhexlify(
    '5f20df933584822601f9e3f8c024eb5eb252fe8cefb24d1317dc3d432e940ebb')

# mainchain genesis data.
PROTOCOL_MAGIC = 764824073
SECURITY_PARAMETER_K = 2160
SLOT_DURATION = 20
START_TIME = 1506203091
MAX_BLOCK_SIZE = 2000000
MAX_HEADER_SIZE = 2000000

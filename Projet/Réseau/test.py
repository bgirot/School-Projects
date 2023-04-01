import struct

# 16.1 ---------------------------------------------------------------------
chaine= b'\x00\x01\x00\x02trois\x00\x00\x00\x04\x05\x00\x00\x00\x06'
unmask_chaine = struct.unpack("!HH5sLBL", chaine )
print(unmask_chaine)

# 16.2 ---------------------------------------------------------------------
octet0 = "01101010"    # 106 en décimal 
octet1 = "11101101"    # 237 en décimal

octet0 = int(octet1, 2) >> 3
octet1 = int(octet1, 2) >> 4
print("octet0 = ", octet0)
print("octet1 = ", octet1)
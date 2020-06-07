# byte 와 인코딩 디코딩
print(bytes(10))
print(bytes([0, 1, 2, 128, 255]))
print(bytes([65, 66, 67]).decode('ascii'))

print("\r\n")

# utf-8이란
print(bytes([234, 185, 128]))
print(bytes([234, 185, 128]).decode('utf-8'))
print("김".encode('utf-8'))
# print(bytes([234, 185, 128]).decode('ascii')) ( 디코딩 불가 )

print("\r\n")

# utf-8과 byte 인코딩 디코딩
print("김기현")
byte_data = "김기현".encode('utf-8')
print(byte_data)
print(byte_data.decode('utf-8'))
# print(byte_data.decode('ascii')) ( 디코딩 불가 )
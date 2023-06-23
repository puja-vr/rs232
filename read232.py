import serial
import serial.tools.list_ports
import struct

def getHex(x):
    if len(hex(x))==3:
        return f'0{hex(x)[-1:]}'
    else:
        return hex(x)[-2:]


com_ports = serial.tools.list_ports.comports()
port,_,_ = com_ports[0]
print(port)
ser = serial.Serial(port, baudrate=115200, bytesize=8, parity="N", stopbits=1, timeout=3)  

ser.write(b"02 04 01 02 10 00 E7")
# ser.write(b"0x02 0x01 0x09 0xED")
res = ser.readline().decode('utf-8')
print(f'result: {res}')
# res='0x06-0x01-0x1F-0x02-0x00-0x00-0x00-0x00-0xFF-0xFF-0xFF-0xFA-0x00-0x00-0x00-0x13-0xFF-0xFF-0xFF-0xF0-0x00-0x00-0x00-0x00-0x00-0x00-0x27-0x10-0x24-0x59-0x00-0x00-0x13-0x88-0x92'
'''
raw_data=[]
for i in range(0,len(res),5):
    raw_data.append(int(res[i:i+4],16))
print(raw_data)
cs = 0
for i in range(34):
    cs+=raw_data[i]
print(f"sum = {hex(cs)}")
hex_cs=hex((~cs & 0xFFFFFFFF) + 0x1)
print(f"bitwise not +1 = {hex_cs}")

data={}
if hex_cs[-2:]==hex(raw_data[34])[-2:]:
    data['ack'] = hex(raw_data[0])
    data['command'] = hex(raw_data[1])
    data['data_len'] = raw_data[2]
    data['ds'] = hex(raw_data[3])
    
    # temp_hex = f'{getHex(raw_data[4])} {getHex(raw_data[5])} {getHex(raw_data[6])} {getHex(raw_data[7])}'
    # temp_byte = bytes.fromhex(temp_hex)
    # data['status'] = struct.unpack('>i', temp_byte)[0]
    data['status'] = f'{hex(raw_data[4])} {hex(raw_data[5])} {hex(raw_data[6])} {hex(raw_data[7])}'
    
    temp_hex = f'{getHex(raw_data[8])} {getHex(raw_data[9])} {getHex(raw_data[10])} {getHex(raw_data[11])}'
    temp_byte = bytes.fromhex(temp_hex)
    data['mc1'] = struct.unpack('>i', temp_byte)[0]
    
    temp_hex = f'{getHex(raw_data[12])} {getHex(raw_data[13])} {getHex(raw_data[14])} {getHex(raw_data[15])}'
    temp_byte = bytes.fromhex(temp_hex)
    data['mc2'] = struct.unpack('>i', temp_byte)[0]
    
    temp_hex = f'{getHex(raw_data[16])} {getHex(raw_data[17])} {getHex(raw_data[18])} {getHex(raw_data[19])}'
    temp_byte = bytes.fromhex(temp_hex)
    data['mc3'] = struct.unpack('>i', temp_byte)[0]
    
    temp_hex = f'{getHex(raw_data[20])} {getHex(raw_data[21])} {getHex(raw_data[22])} {getHex(raw_data[23])}'
    temp_byte = bytes.fromhex(temp_hex)
    data['o2'] = struct.unpack('>i', temp_byte)[0]
    
    temp_hex = f'{getHex(raw_data[24])} {getHex(raw_data[25])} {getHex(raw_data[26])} {getHex(raw_data[27])}'
    temp_byte = bytes.fromhex(temp_hex)
    data['pef'] = struct.unpack('>i', temp_byte)[0] * 0.0001
    
    temp_hex = f'{getHex(raw_data[28])} {getHex(raw_data[29])}'
    temp_byte = bytes.fromhex(temp_hex)
    data['pressure'] = struct.unpack('>H', temp_byte)[0] * 0.1
    
    data['reserved'] = f'{getHex(raw_data[30])} {getHex(raw_data[31])}'
    
    temp_hex = f'{getHex(raw_data[32])} {getHex(raw_data[33])}'
    temp_byte = bytes.fromhex(temp_hex)
    data['temperature'] = struct.unpack('>h', temp_byte)[0] * 0.01
    
    data['checksum'] = hex(raw_data[34])  

print(data)
ser.close()
'''
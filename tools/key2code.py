# ----------------------------------------------------------------
#
# key2code tool kit
# This tool kit helps to generate byte sequence to communicate with immobilizer system
# or get key ID from given sequence
#
# Author: Alex Shkil aka HLinS
#
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# Example dump data: [header] [key] [data_bcc] [stop_byte] [null_end]
# ----------------------------------------------------------------

header = 0x7F  # read-only RFID
key = [0xF, 0xF, 0xB, 0x4, 0x5, 0x1, 0xA, 0x0,
       0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
data_bcc = []
stop_byte = 0x7e
null_end = [0x00, 0x00]


def getCrc(key, params):
    ''' Returns CRC-16 CCITT of given '''
    defaults = {'polynome': 0x1021,
                'init': 0xFFFF,
                'xor_out': 0}
    for key in params.keys():
        if params[key] == None:
            params[key] = defaults[key]
            
    key += ''
    crc = params['init']
    length = len(key)
    i = 0
    
    while i < length:
        pass
    return crc


def getReversedMessageHex2Bin(hex_message):
    ''' Return'''
    bin = ''
    rev_bin = ''
    for element in hex_message:
        segment = format(element, '04b')
        bin += segment
        rev_bin = str([segment[i] for i in range(len(segment)-1, -1, -1)]).replace(
            '[', '').replace('\'', '').replace(',', '').replace(']', '').replace(' ', '') + rev_bin
    print(bin)
    print(rev_bin)
    return rev_bin


def getKeyFromMessage(message):
    result = list()
    for i in range(0, len(message), 4):
        result.append(
            hex(int(message[i]+message[i+1]+message[i+2]+message[i+3], base=2)))
    return result


# getReversedMessageHex2Bin(key)
print([hex(i) for i in key])
print(getKeyFromMessage(getReversedMessageHex2Bin(key)))

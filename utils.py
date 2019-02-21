def pad(val: str, target_length=64) -> str:
    '''Pads the value with zeroes at the front, so that the total length is target_length'''
    assert(len(val) <= target_length)
    return '0' * (target_length - len(val)) + val

def convert_num(num: int) -> str:
    '''Converts num into Ethereum standard format (64 bytes long + hex)'''
    return pad(hex(num).rstrip("L").lstrip("0x"))

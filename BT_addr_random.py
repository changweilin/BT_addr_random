import random

def main():
    BT_address_len = 4
    #BT_address = [0x0002, 0x5b, 0x00ff01, 0x00ff05]
    #BT_address = [0x70B3, 0xD5, 0x902090, 0x902094]
    #BT_address = [0x70B3, 0xD5, 0x90208B, 0x90208F]
    #BT_address = [0x70B3, 0xD5, 0x90200A, 0x90200B]
    BT_address = [0x70B3, 0xD5, 0x902018, 0x902018]
    MASK=[0,0,0,0]
    KEY=[0,0,0,0]
    check_BT=[0,0,0,0]
    random_range = [0xFFFFFF,0xFFFFFF,0xFFFFFF,0xFFFFFF]
    '''
    MASK = [random.randint(1, 16777215) for _ in range(4)]
    MASK = [BT_address[_] ^ MASK[_] for _ in range(4)]
    MASK = [KEY[_] ^ MASK[_] for _ in range(4)]
    '''
    for i in range(4):
        MASK[i] = random.randint(0, 0xFFFFFF)
        KEY[i] = BT_address[i] ^ MASK[i]
        check_BT[i] = KEY[i] ^ MASK[i]

    print("MASK: 0x%06x, 0x%06x, 0x%06x, 0x%06x"%(MASK[0], MASK[1], MASK[2], MASK[3]))
    print("KEY: 0x%06x, 0x%06x, 0x%06x, 0x%06x"%(KEY[0], KEY[1], KEY[2], KEY[3]))
    print("check_BT: 0x%06x, 0x%06x, 0x%06x, 0x%06x"%(check_BT[0], check_BT[1], check_BT[2], check_BT[3]))
    
if __name__ == '__main__':
    main()
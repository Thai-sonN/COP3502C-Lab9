# Ryan Klapmeyer - Encode

def encode(passcode):
    pass_list = list(passcode)
    encode_list = []
    for i in range(len(pass_list)):
        if int(pass_list[i]) < 7:
            pass_list[i] = int(pass_list[i]) + 3
            encode_list.append(pass_list[i])
        else:
            pass_list[i] = (int(pass_list[i]) + 3) - 10
            encode_list.append(pass_list[i])

    encode_str = ''
    for i in range(len(encode_list)):
        encode_str += str(encode_list[i])

    return encode_str

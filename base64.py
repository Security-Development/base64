base64_box = {}
index = 0
args = {
    "A": 26,
    "a": 26,
    "0": 10,
    "+": 1,
    "/": 1
    }

def CreateBoxTool(string, length):
    global index
    ascii_string = None
    for i in range(length):
        ascii_string = ord(string) + i
        base64_box[index] = chr(ascii_string)
        index += 1
        #print(chr(ascii_string)) <= 확인 출력


for k, v in args.items():
    CreateBoxTool(k ,v)
    
print(base64_box)


def setUp(binary_string):
    v,k = 0, 6
    len_binary = len(binary_string)
    for i in range(len_binary):
        if len_binary < v:
            break

        bin_str = str(binary_string[v:k])
        if len(bin_str) != 6:
            bin_str = bin_str.ljust(6, "0")
            
        if bin_str.count("0") == 6:
            bin_str = ""
        else:
            print(base64_box[int("0b"+bin_str, 2)], end="")
            v,k = v+6, k+6

    if len_binary % 3 == 1:
        print("=")
    elif len_binary % 3 == 2:
        print("==")

binary = ""

def CreateBase64(string):
    global binary
    ascii_string = None
    for i in range(len(string)):
        ascii_string = ord(string[i])
        binary += "{0:b}".format(ascii_string).zfill(8)
        print(binary)
        #print(string[i] + " => " + "{0:b}".format(binary1))
    setUp(binary)

CreateBase64("hello")

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


binary = ""

def CreateBase64(string):
    global binary
    ascii_string = None
    for i in range(len(string)):
        ascii_string = ord(string[i])
        binary += "{0:b}".format(ascii_string).zfill(8)
        print(binary)
        #print(string[i] + " => " + "{0:b}".format(binary1))

CreateBase64("abc")
        
    

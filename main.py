ExpandMatrix = [
    [32, 1,  2,  3,  4,  5],
    [4,  5,  6,  7,  8,  9],
    [8,  9,  10, 11, 12, 13],
    [12, 13, 14, 15, 16, 17],
    [16, 17, 18, 19, 20, 21],
    [20, 21, 22, 23, 24, 25],
    [24, 25, 26, 27, 28, 29],
    [28, 29, 30, 31, 32, 1]
]
PC1 = [
    [57, 49, 41, 33, 25, 17, 9],
    [1, 58, 50, 42, 34, 26, 18],
    [10, 2, 59, 51, 43, 35, 27],
    [19, 11, 3, 60, 52, 44, 36],
    [63, 55, 47, 39, 31, 23, 15],
    [7, 62, 54, 46, 38, 30, 22],
    [14, 6, 61, 53, 45, 37, 29],
    [21, 13, 5, 28, 20, 12, 4]
]
PC2 = [
    [14, 17, 11, 24, 1, 5],
    [3, 28, 15, 6, 21, 10],
    [23, 19, 12, 4, 26, 8],
    [16, 7, 27, 20, 13, 2],
    [41, 52, 31, 37, 47, 55],
    [30, 40, 51, 45, 33, 48],
    [44, 49, 39, 56, 34, 53],
    [46, 42, 50, 36, 29, 32]
]
IP_matrix = [
    [58, 50, 42, 34, 26, 18, 10, 2,],
    [60, 52, 44, 36, 28, 20, 12, 4],
    [62, 54, 46, 38, 30, 22, 14, 6],
    [64, 56, 48, 40, 32, 24, 16, 8],
    [57, 49, 41, 33, 25, 17, 9, 1],
    [59, 51, 43, 35, 27, 19, 11, 3],
    [61, 53, 45, 37, 29, 21, 13, 5],
    [63, 55, 47, 39, 31, 23, 15, 7]
]

Sbox = [[] for i in range(9)]
Sbox[1] = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]
Sbox[2] = [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
]
Sbox[3] = [
    [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
    [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
    [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
    [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
]
Sbox[4] = [
    [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
    [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
    [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
    [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
]
Sbox[5] = [
    [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
    [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
    [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
    [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
]
Sbox[6] = [
    [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
    [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
    [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
    [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
]
Sbox[7] = [
    [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
    [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
    [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
    [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
]
Sbox[8] = [
    [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
    [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
    [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
    [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
]

P = [
    [16,7,20,21],
    [29,12,28,17],
    [1,15,23,26],
    [5,18,31,10],
    [2,8,24,14],
    [32,27,3,9],
    [19,13,30,6],
    [22,11,4,25]
]

IP_reverse = [
    [40,8,48,16,56,24,64,32],
    [39,7,47,15,55,23,63,31],
    [38,6,46,14,54,22,62,30],
    [37,5,45,13,53,21,61,29],
    [36,4,44,12,52,20,60,28],
    [35,3,43,11,51,19,59,27],
    [34,2,42,10,50,18,58,26],
    [33,1,41,9,49,17,57,25]
]


def leftShift(key):
    c = key[0]
    d = key[1:]
    e = d + c
    return e
    
def xor(str1, str2):
    if len(str1) != len(str2):
        print("Fail to xor", str1, "and", str2)
        return False
    result = ""
    for i in range(len(str1)):
        if str1[i] == "1" and str2[i] == "1":
            result += "0"
        if str1[i] == "1" and str2[i] == "0":
            result += "1"
        if str1[i] == "0" and str2[i] == "1":
            result += "1"
        if str1[i] == "0" and str2[i] == "0":
            result += "0"
    return result


def permute(matrix, input):
    result = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result = result + input[matrix[i][j] - 1]
    return result

def address(string):
    # print(string)
    arr = splitstr(string)
    # print(arr)
    result = ""
    for index in range(1,9):
        i = int(arr[index][0]+arr[index][5], 2)
        j = int(arr[index][1:5], 2)
        # print(Sbox[index][i][j])
        value = str(bin(Sbox[index][i][j]))
        result += sanitize(value, 4)
    return result

def splitstr(str):
    result = [[]]
    tmp = ""
    count = 0
    for i in range(len(str)):
        tmp += str[i]
        count += 1
        if count == 6:
            result.append(tmp)
            tmp = ""
            count = 0
    return result

def sanitize(bi, size):
    bi = bi[2:]
    while len(str(bi)) < size:
        bi = "0" + bi
    return bi

def binaryToHex(string, size):
    result = ""
    count = 0
    tmp = ""
    for i in range(len(string)):
        tmp += string[i]
        count += 1
        if count == size:
            hexNumber = (hex(int(tmp, 2)))
            result += sanitize(hexNumber, 2)
            count = 0
            tmp = ""
    return result.upper()

def encodeInput(message):
    filt = [" ", ".", ","]
    for f in filt:
        message = message.replace(f, "")
    message = message.upper()
    result = ""
    for char in message:
        number = int(char, 16)
        binaryNumber = bin(number)
        value = sanitize(binaryNumber, 4)
        result += value
    return result

Message = input("Nhập thông điệp dạng hex:")
Message = encodeInput(Message)
Key = input("Nhập khoá dưới dạng hex: ")
Key = encodeInput(Key)

K = ["" for i in range(17)]
K[0] = permute(PC1, Key)

C = ["" for i in range(0,17)]
D = ["" for i in range(0,17)]

C[0] = K[0][0:28]
D[0] = K[0][28:]

#create C1->C16 D1->D16
for i in range(1,17):
    # print(i)
    if i in [1,2,9,16]:
        C[i] = leftShift(C[i-1])
        D[i] = leftShift(D[i-1])
    else:
        C[i] = leftShift(leftShift(C[i-1]))
        D[i] = leftShift(leftShift(D[i-1]))
    # print(C[i])
        
#create K1->K16
for i in range(1,17):
    temp = C[i] + D[i]
    K[i] = permute(PC2, temp)
    # print(i, K[i])

#initial permutation of message
IP = ""
IP = permute(IP_matrix, Message)

L = ["" for i in range(17)]
R = ["" for i in range(17)]

L[0] = IP[:32]
R[0] = IP[32:]



F = ["" for i in range(17)]
for i in range(1,17):
    L[i] = R[i-1]
    F[i] = permute(P, address(xor(K[i], permute(ExpandMatrix, R[i-1]))))
    R[i] = xor(L[i-1], F[i])
    # print("L[",i,"] ",L[i])
    # print("R[",i,"] ",R[i])


final = R[16] + L[16]

cipherTextBinary = permute(IP_reverse, final)
cipherText = binaryToHex(cipherTextBinary, 8)

print(cipherText)


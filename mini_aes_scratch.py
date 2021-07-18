def sBox(str):
    d = {
        "0000": "1110",
        "0001": "0100",
        "0010": "1101",
        "0011": "0001",
        "0100": "0010",
        "0101": "1111",
        "0110": "1011",
        "0111": "1000",
        "1000": "0011",
        "1001": "1010",
        "1010": "0110",
        "1011": "1100",
        "1100": "0101",
        "1101": "1001",
        "1110": "0000",
        "1111": "0111",
    }
    return d[str]

def nibbleSub(arr):
    arr[0][0] = sBox(str(arr[0][0]))
    arr[0][1] = sBox(str(arr[0][1]))
    arr[1][0] = sBox(str(arr[1][0]))
    arr[1][1] = sBox(str(arr[1][1]))
    return arr

def shiftRows(arr):
    temp = arr[1][1]
    arr[1][1] = arr[1][0]
    arr[1][0] = temp
    return arr

def mul(t, b):
    a = bin(t)[2::]
    a="0"*(4-len(a))+a
    # print(a)
    # print(b)
    # x
    return x

def mixColums(arr):
    arr[0][0] = mul(3, arr[0][0]) + mul(2, arr[1][0])
    arr[0][1] = mul(3, arr[0][1]) + mul(2, arr[1][1])
    arr[1][0] = mul(2, arr[0][0]) + mul(3, arr[1][0])
    arr[1][1] = mul(2, arr[0][1]) + mul(3, arr[1][1])
    return arr

def xorOnString(str1,str2):
    s=""
    for i in range(4):
        if str1[i]=="0" and str2[i]=="0":
            s+="0"
        elif str1[i]=="1" and str2[i]=="1":
            s+="0"
        elif str1[i]=="0" and str2[i]=="1":
            s+="1"
        elif str1[i]=="1" and str2[i]=="0":
            s+="1"
    return s

def AddRoundKey(arr,key):
    for i in range(2):
        for j in range(2):
            arr[i][j] = xorOnString(arr[i][j],key[i][j])

ar = [["0001", "0010"], ["0011", "1111"]]
# nibbleSub(ar)
# shiftRows(ar)
# mixColums(ar)
AddRoundKey(ar,ar)
for i in range(2):
    for j in range(2):
        print(ar[i][j], end=" ")

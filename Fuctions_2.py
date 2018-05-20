#!/usr/bin/env python
#-*- coding:utf-8 -*-
import base64   #输出用base64编码
from tkinter import messagebox
IP_table=[58,50,42,34,26,18,10,2,
          60,52,44,36,28,20,12,4,
          62,54,46,38,30,22,14,6,
          64,56,48,40,32,24,16,8,
          57,49,41,33,25,17,9,1,
          59,51,43,35,27,19,11,3,
          61,53,45,37,29,21,13,5,
          63,55,47,39,31,23,15,7]

IP_table_1=[40,8,48,16,56,24,64,32,
            39,7,47,15,55,23,63,31,
            38,6,46,14,54,22,62,30,
            37,5,45,13,53,21,61,29,
            36,4,44,12,52,20,60,28,
            35,3,43,11,51,19,59,27,
            34,2,42,10,50,18,58,26,
            33,1,41,9,49,17,57,25]

PC_1_table=[57,49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43,35, 27,
            19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4]

PC_2_table=[14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32]

S_BOX=[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
    0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
    4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
    15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13,],
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
    3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
    0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
    13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
    13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
    13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
    1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
    13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
    10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
    3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
    14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
    4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
    11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
    10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
    9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
    4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
    13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
    1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
    6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
    1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
    7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
    2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

P_table=[16, 7, 20, 21,
        29, 12, 28, 17,
        1, 15, 23, 26, 5,
        18, 31, 10, 2, 8,
        24, 14, 32, 27,
        3, 9, 19, 13, 30,
        6, 22, 11, 4, 25]

# 用base64编码字符串
def Base64_Encode(s):
    encodestr = base64.b64encode(s.encode('utf-8'))
    encodestr_after = str(encodestr, 'utf-8')  # 用base64编码后的字符串
    return encodestr_after

# 用base64解码字符串
def Base64_Decode(s):
    decodestr_utf8 = bytes(s, encoding='utf-8')  # 将得到的字符串用utf-8编码
    decodestr_b64 = base64.b64decode(decodestr_utf8)  # 用base64解码
    decodestr_b64_utf8 = decodestr_b64.decode('utf-8')  # 用utf-8解码
    return decodestr_b64_utf8

# 将字符转换成八位的二进制 接收 l：字符串 返回值为字符串
def Str2bit(l):
    l=list(l)
    bit_list=[]
    for i in l:
        if 0<len(bin(ord(i)))<=10:
            bit_0b=bin(ord(i)).replace('0b','')
            bit_8=(8-len(bit_0b))*'0'+bit_0b
            bit_list.append(bit_8)
        else:
            messagebox.showerror('错误','输入有误')
            raise SystemError("输入有误")
    bit_list=''.join(bit_list)
    return bit_list

# 加入奇校验  接收 key：字符串返回值为字符串
def Key(key):
    K=Str2bit(key)
    K_list=[]
    for i in range(0,8):
        K_list.append(K[7*i:7+7*i]+str((K[7*i:7+7*i].count('1')%2)^1))
    for i in K_list:
        KEY=''.join(K_list)
    return KEY

# 将明文/密文分成64bit一组 并填充 接收 s：字符串/字节 返回值为字符串列表
def Divide_64(s):
    stri=Str2bit(s)
    Plaintext_64=[]
    i=1
    while i <= len(stri)//64:
        Plaintext_64.append(stri[64*(i-1):64*i])
        i=i+1
    m=(64-(len(stri[64*(len(stri)//64):])))%64
    if m!=0 :
        Plaintext_64.append(stri[64*(len(stri)//64):]+(56-len(stri[64*(len(stri)//64):]))*'0')  #用0填充
        Plaintext_64[-1]=Plaintext_64[-1]+bin(m-8).replace('0b','0'*(10-len(bin(m-8))))     #最后8bit存放填放0的个数
    return Plaintext_64

# 置换 接收 key：字符串 table：列表 返回值为字符列表
def Display(key,table):
    key_list=list(key)
    key_after=[]
    for i in range(0,len(table)):
        key_after.append(key_list[table[i]-1])
    return key_after

# 左移函数  接收 key：字符列表 i：整数 返回值为字符列表
def LS(key,i):
    C = key[0:28]
    D = key[28:56]
    if i==1 or i==2 or i==9 or i==16:
        C.append(C[0])
        del C[0]
        D.append(D[0])
        del D[0]
    else:
        C.append(C[0])
        C.append(C[1])
        del C[0:2]
        D.append(D[0])
        D.append(D[1])
        del D[0:2]
    return C+D

# 密钥拓展 接收 key:字符串 返回字符串列表
def Key_Expansion(key):
    key_list=[]                              #密钥列表
    Key_PC_1=Display(key,PC_1_table)         #置换PC-1
    Key_After_LS = Key_PC_1                  #初始值
    for i in range(1,17):                    #生成子密钥
        Key_After_LS=LS(Key_After_LS,i)          #左移
        Key_After_LS_Str=''.join(Key_After_LS)       #把字符列表转换为字符串
        Key_PC_2_list=Display(Key_After_LS_Str,PC_2_table)  #置换PC-2
        Key_PC_2=''.join(Key_PC_2_list)
        key_list.append(Key_PC_2)
    return key_list

# E变换  接收 R:字符串 返回 字符列表
def E_change(R):
    E=[]
    E.append(R[31])
    E.extend(R[0:5])
    for i in range(0,6):
        R0=R[3+i*4:9+i*4]
        E.extend(R0)
    E.extend(R[27:32])
    E.append(R[0])
    return E

# S-盒变换  接收 E：字符列表 返回字符串
def S_change(E):
    S=''
    for k in range(0,8):
        i=int(E[0+k*6]+E[5+k*6],2)
        j=int(E[1+k*6]+E[2+k*6]+E[3+k*6]+E[4+k*6],2)
        OUT=bin(S_BOX[k][i*16+j]).replace('0b','')
        OUT=(4-len(OUT))*'0'+OUT
        S=S+OUT
    return S

# 异或操作 接收 k1:字符列表 k2:字符串 返回字符列表
def XOR(k1,k2):
    E=[]
    if len(k1)!=len(k2):
        raise SystemError("字符数量不匹配")
    else:
        for i in range(0,len(k1)):
            E.append(str(int(k1[i])^int(k2[i])))

    return E

# f函数 接收  R,K：字符列表 返回字符列表
def f(R,K):
    R0=''.join(R)
    E=E_change(R0)
    E_XOR_K=XOR(E,K)
    S=S_change(E_XOR_K)
    P=Display(S,P_table)
    return P

# 加密函数 接收 plaintext:字符串,key:字符串列表 返回字符串
def Encrypt(plaintext,key):
    ciphertext_list=[]
    #十六轮轮函数
    for i in range(0,len(plaintext)):
        L = list(range(0,17))
        R = list(range(0,17))
        plaintext_ip=Display(plaintext[i],IP_table)
        L[0] = plaintext_ip[0:32]
        R[0] = plaintext_ip[32:64]
        for i in range(1,17):
            L[i]=R[i-1]
            R[i]=XOR(L[i-1],f(R[i-1],key[i-1]))
        plaintext_list = R[16]+L[16]
        plaintext_list_ip_1 = Display(plaintext_list,IP_table_1)
        ciphertext_list=ciphertext_list+plaintext_list_ip_1
    ciphertext_bit=''.join(ciphertext_list)
    ciphertext = []
    #把生成的字符串每八位分成一段
    for i in range(0,len(ciphertext_bit)//8):
        ciphertext.append(ciphertext_bit[i*8:8+i*8])
    cipher_show = ''
    #每八位转换为一个字符
    for i in ciphertext:
        cipher_show=cipher_show+chr(int(i,2))
    return cipher_show

# 解密函数 接收 ciphertext:字符串 key:字符串列表 返回字符串
def Decrypt(ciphertext,key):
    ciphertext_list=Divide_64(ciphertext)
    ciphertext_list_2=[]
    for i in range(0,len(ciphertext_list)):
        L=list(range(0,17))
        R=list(range(0,17))
        ciphertext_ip=Display(ciphertext_list[i],IP_table)
        L[0]=ciphertext_ip[0:32]
        R[0]=ciphertext_ip[32:64]
        for i in range(1,17):
            L[i]=R[i-1]
            R[i]=XOR(L[i-1],f(R[i-1],key[16-i]))
        ciphertext_list_after=R[16]+L[16]
        ciphertext_list_after_ip=Display(ciphertext_list_after,IP_table_1)
        ciphertext_list_2=ciphertext_list_2+ciphertext_list_after_ip
    plaintext_bit=''.join(ciphertext_list_2)
    plaintext=[]
    # 把生成的字符串每八位分成一段
    for i in range(0,len(plaintext_bit)//8):
        plaintext.append(plaintext_bit[i*8:8+i*8])
    n = int(plaintext[-1], 2)   #从最后一段取出填充的‘0’的个数
    #如果n=0 那么没有填充 直接删去最后一段
    if n == 0:
        plaintext.pop(-1)
    else:
        plaintext_1 = plaintext[::-1]  # 倒序存放
        plaintext_1.pop(0)             # 把最后一段拿掉
        number = 0                     # 统计出现的0的个数
        k = 0                          # 标记列表里的下标
        for i in plaintext_1:
            k = k + 1
            if i.count('0') != 8:      #如果一段里的8位不全为0，那肯定不是填充的0 退出循环
                break
            else:
                number = number + 8
        if number == n:
            del plaintext[len(plaintext_1) - k + 1:]    #当判断得到的0与n相等时，删除填充的0
    plaintext_show=''
    for i in plaintext:
        plaintext_show=plaintext_show+chr(int(i,2))
    return plaintext_show



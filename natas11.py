#!/bin/python3
# compare two asciis with chr(x) after xor
#horrible program but it works :) 
from base64 import b64decode, b64encode

#input1 = '\nUK"..H+..O%...pS.Wh]UZ-..T%.U.hR.^,..^h.'
input1= '\nUK"\x1e\x00H+\x02\x04O%\x03\x13\x1apS\x19Wh]UZ-\x12\x18T%\x03U\x02hR\x11^,\x17\x11^h\x0c'
outputlol = '{"showpassword":"no","bgcolor":"#ffffff"}'

pingissues = ''  
for word in range(0, len(input1)):
    xoroutput = ord(input1[word]) 
    #print(xoroutput)
    for i in range(128):
        compare = xoroutput ^ i
        if outputlol[word] == chr(compare):
            pingissues+=chr(i)
            break

pingissues+='w'
print(pingissues)
outputnolol = '{"showpassword":"yes","bgcolor":"#ffffff"}'
cookiea=''
for word in range(0, len(outputnolol)):
    xoroutputlol = ord(outputnolol[word])
    #for word2 in range(0, len(pingissues)):
    pingissueslol = ord(pingissues[word])
    cookie = xoroutputlol ^ pingissueslol
    cookiea+=chr(cookie)

print(cookiea)
print(b64encode(cookiea.encode("utf-8")))





"""
    for i in range(128):
        xoroutput=ord(input1[word]) ^ i 
        #print(chr(xor))
        for word2 in outputlol:
            #print(word2)
            if ord(word2) == xor:
                print=chr(xor)
"""

# for i in range(128):
##    output=ord('K') ^ i
# #   print(output)
# 
# print('printing ORD')
# print(ord('{'))


# this is the cookie decoded hex string
# "0a 55 4b 22 1e 00 48 2b 02 04 4f 25 03 13 1a 70 53 19 57 68 5d 55 5a 2d 12 18 54 25 03 55 02 68 52 11 5e 2c 17 11 5e 68 0c"


# print (hex(x))
# b2 1a 30 a5 ab 2c c2 8a dd 9e 86 e0 72 89 68 ad f7 df 7d f7

# for first every word in base64 decoded cookie, XOR with all letters from ascii
# stop and print if match same poisiton of letter in output




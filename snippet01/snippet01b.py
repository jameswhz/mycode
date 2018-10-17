#!/usr/bin/env python3

def ipRequest(ipAddress):
  ipList = ipAddress.split(".")
  if int(ipList[3]) + 10 > 255:
    print("greater than 255, Rejected!")
    return False
  else:
    print("Accepted")
    return True

count = 0
while 1:
  ipAddress = input("please enter IP address you want(max 3 in total): ")
  count = count + 1
  print(count)
  if count > 3:
    print("Max total is 3 each time, no more request will be accepted!")
    break
  ipRequest(ipAddress)

  
  

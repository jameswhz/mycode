#!/usr/bin/env python3
myFile = open('admin.rc', 'r')
myFileList = myFile.readlines()
myFile.close()

print(myFileList)
print("\n".join(myFileList))
print("	".join(myFileList))

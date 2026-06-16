import os
print("\033c\033[47;31m")
print("give me a file to check ...")
a=input().strip()
os.system("nm86 $1".replace("$1",a))

str = "Hello World"
str1 = [None] * 11
str2 = [None] * 11
len = len(str)

for i in range(len):
    str1[i] = chr(ord(str[i]) & 127)
    print(str1[i], end="")
print()

for i in range(len):
    original = ord(str[i])
    modified = original ^ 127
    print("i", i, "char", str[i], "orig", hex(original), "mod", hex(modified))

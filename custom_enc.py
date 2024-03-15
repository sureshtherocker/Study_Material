FLAG = REDACTED
KEY = REDACTED

f = open("output.txt","w")

output = []

for _ in range(0,len(FLAG)-1):
	output.append(ord(FLAG[_])^ord(KEY[_%len(KEY)])^ord(FLAG[_+1]))

f.write(str(output))

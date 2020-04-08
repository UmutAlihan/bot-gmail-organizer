with open('../gmail_bot_functions.py', 'r') as f:
    text = f.readlines()

newlines = []
for line in text:
    if("def" in line):
        newline = line.strip("def ").strip("\n").strip(":").strip("\"").strip(" ")
        newlines.append(newline + "\n")
print(newlines)

with open('dev_functions.txt', 'w+') as f:
    f.write("".join(newlines))

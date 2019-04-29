import socket

s = socket.socket()
s.connect(('localhost', 1111))

def readLine(s):
    line = ""
    while 1:
        a = s.recv(1)
        if a != "\n":
            line += a
        else:
            break
    return line

print readLine(s) # Welcome to math class
print readLine(s) # Answer quest below
print readLine(s) #

while 1:
    line = readLine(s)
    print line
    # if line != "[+] Wow let's try more!":
    #     print "WOW"
    #     break
    lines = line.split(" ")

    print readLine(s)
    result = 0
    if lines[1] == "+":
        results = long(lines[0]) + long(lines[2])
    elif lines[1] == "-":
        result = long(lines[0]) - long(lines[2])
    elif lines[1] == "*":
        result = long(lines[0]) * long(lines[2])
    elif lines[1] == "/":
        result = long(lines[0]) / long(lines[2])
    elif lines[1] == "%":
        result = long(lines[0]) % long(lines[2])
    print "*** Your answer: " + str(result)
    s.send(str(result))
    s.send("\n")
    readLine(s)
    print readLine(s)
    print readLine(s)
    print readLine(s)

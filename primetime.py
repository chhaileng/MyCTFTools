import socket

s = socket.socket()
s.connect(('primetime.baectf.com', 443))

def readLine(s):
    line = ""
    while 1:
        a = s.recv(1)
        if a != "\n":
            line += a
        else:
            break
    return line

def prime(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    else:
        for n in range(2, x):
            if x % n == 0:
                return False

        return True


def checkPrime(before):
    for num in list(reversed(range(1,before))):
        if prime(num):
            return num
        

print(s.recv(16))
s.send("terminaldisc\n")
print readLine(s)
print readLine(s)

while 1:
    line = readLine(s)
    print line
    try: 
        before = long(line.split(" ")[5])
    except:
        print readLine(s)
        print readLine(s)
        print readLine(s)
        
    print(str(checkPrime(before)))
    s.send(str(checkPrime(before)))
    s.send("\n")
    print readLine(s)
    

print readLine(s)
print readLine(s)
print readLine(s)

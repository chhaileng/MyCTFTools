#ctf chhaipov guess crush's birthday :D
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
    DateLists = open("DateList.txt", "r")
except IOError:
    print ("File DateList.txt not found. Run python DateGenerator.py")
    sys.exit(0)
try:
    try:
        while 1:
            s = socket.socket()
            s.connect(('ctf.chhaipov.com', 143))
            #ans = '22/12/1992'
            lst = DateLists.readline().split('\n')
            ans = lst[0]
            s.recv(1024)
            #print ans
            s.send(ans + '\n')

            read_line(s)
            read_line(s)
            print read_line(s) + ans
            read_line(s)
            a = read_line(s)
            print a
            read_line(s)
            if a != 'Incorrect Answer. Try again na bro':
                print 'Congrats jeje :D'
                print read_line(s)
                print read_line(s)
                break
            s.close()
            #print s.recv(1024)
    except socket.error:
        print 'Socket disconnected'
except KeyboardInterrupt:
	#s.close()
    print "Bye bye jeje"

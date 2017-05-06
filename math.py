import socket

def read_line(s):
    a = ""
    while 1:
        b = s.recv(1)
        if b != "\n":
            a = a + b
        else:
            break
    return a


s = socket.socket()
s.connect(('195.154.53.62', 7331))

try:
	while 1:
	    a = read_line(s)
	    print a
	    b = a.split(' ')
	    value = 0
	    try:
	        value = long(b[0])

	    except ValueError:
	        value = 0
	    if value != 0:
		    value1 = long(b[0])
		    value2 = long(b[2])

		    if (b[1] == "+"):
		    	result = value1 + value2
		    elif (b[1] == "-"):
		    	result = value1 - value2
		    elif (b[1] == "*"):
		    	result = value1 * value2
		    elif (b[1] == "/"):
		    	result = value1 / value2
		    elif (b[1] == "%"):
		    	result = value1 % value2
		    print "Result: " + str(result)
		    s.send(str(result))
		    s.send('\n')
except KeyboardInterrupt:
	s.close()
	print "Bye bye"

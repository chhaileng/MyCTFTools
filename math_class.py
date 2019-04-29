import socket, time, os, thread, random
s = socket.socket()
host = 'localhost'
port = 1111
s.bind((host, port))
s.listen(5)

def Readline(c):
    a = ""
    while 1:
        b = c.recv(1)
        if b != "\n":
            a = a + b
        else:
            break
    return a

def question(c):
    operators = ['+', '-', '*', '/', '%']
    operator = random.choice(operators);
    a = random.randint(1000000000000000000000000000000000000, 9999999999999999999999999999999999999)
    b = random.randint(1000000000000000000000000000000000000, 9999999999999999999999999999999999999)
    c.send(str(a) + " " + operator + " " + str(b))
    result = 0
    if (operator == "+"):
        result = a + b
    elif (operator == "-"):
        result = a - b
    elif (operator == "*"):
        result = a * b
    elif (operator == "/"):
        result = a / b
    elif (operator == "%"):
        result = a % b
    return result

def clientthread(c):
        c.send("***** Welcome to math class *****\n")
        c.send("Answer answer below!\n\n")
        
        n = 1
        
        while 1:
            ans = question(c)
            c.send("\n\n*** Your answer: ")
            
            user_ans = 0
    
            try:
                user_ans = long(Readline(c))
            except ValueError:
                c.send("\n[-] Answer is number bro, don't input text :(")
                c.close()
            
            if user_ans != ans:
                user_ans = 0
                c.send("\n[-] Answer incorrect! Try again later :(\n")
                c.close()
            else:
                c.send("\n[+] Wow let's try more!\n\n")
            
            n+=1

            if n > 200:
                c.send("[+] Congratulation bro! how smart you are!")
                c.close()
                break

while True:
    c, addr = s.accept()
    thread.start_new_thread(clientthread, (c,))
s.close()
c.close()


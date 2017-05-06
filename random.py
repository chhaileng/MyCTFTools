from socket import socket

class Run(object):

    def __init__(self):
        self.cycle = {}
        self.s = socket()
        self.s.connect(('195.154.53.62', 7412))
        self.buf = ''

    def Run(self):
        print '[*] Get full cycle'
        self.get_full_cycle()
        print '[*] Predict numbers'
        n = self.get_nb()
        for _ in range(11):
            n = self.cycle[n]
            self.s.sendall('1\n%d\n' % n)
        print '[*] Print flag'
        print self.recv(lambda x: 'ALEXCTF' in x)

    def recv(self, test):
        while True:
            if '\n' not in self.buf:
                self.buf += self.s.recv(1024)
                continue
            val, self.buf = self.buf.split('\n', 1)
            if test(val):
                return val

    def get_nb(self, send=True):
        if send:
            self.s.sendall('2\n')
        return int(self.recv(lambda x: all(c in '0123456789' for c in x)))

    def get_full_cycle(self):
        self.s.sendall('2\n' * 0x8001)  # sending all at once for speedup
        p = self.get_nb(False)
        for _ in range(0x8000):
            n = self.get_nb(False)
            self.cycle[p] = n
            p = n


if __name__ == '__main__':
    Run().Run()
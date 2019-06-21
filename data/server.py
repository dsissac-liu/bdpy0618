#!/usr/bin/env python2
import socket, threading, string, random, hashlib
from datetime import datetime
from config import *

random.seed(datetime.now())
letters = string.ascii_letters + string.digits
gen_seed = lambda: ''.join(random.choice(letters) for i in xrange(5))
chk = '0'*PoW

def handler(c):
    try:
        while True:
            data = c.recv(6)[:-1]
            while True:
                s = gen_seed()
                h = hashlib.sha256(s+data).hexdigest()
                if (h.startswith(chk)):
                    c.send(','.join([data, s, h])+'\n')
                    break
    except Exception:
        pass
    finally:
        c.close()

def main(): 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port)) 
    s.listen(5) 
    print '[*] server starts at {}:{}'.format(host, port)
    while True: 
        c, _ = s.accept() 
        threading.Thread(target = handler, args = (c,)).start()
    s.close() 

if __name__ == '__main__': 
	main() 

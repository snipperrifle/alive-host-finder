import socket
socket.setdefaulttimeout(0.3)
def isON(hostIP):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((hostIP,80))
        return True
    except:
        return False
for a in range(0,255):
    ip = "5.28.191." + str(a)
    if(isON(ip)):
        print "Host:",ip , socket.getfqdn(ip)
print "Done"

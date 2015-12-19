import socket
import argparse

def banner():
    print "_" * 80
    print "Usage: ./alive-host-finder.py --ip 192.168.1.0 --subnet 255.255.255.0"
    print "Additional options: -timeout 0.1 "
    print "Additional options: -verbose true or -verbose 1"
    print "Designed By: cyrus the great"
    print "Remember: Even if the skies were shorter than my knees, I would not kneel."
    print "_" * 80


#exit()

#argument handling { - means it's optional}  {-- means it's required}
parser = argparse.ArgumentParser()
parser.add_argument("--ip",  help="{First ip address} {network address} {Last host portion is zero}" , default="192.168.1.0")
parser.add_argument("--subnet", help="{Subnet mask}{classfull}" , required=False ,default="255.255.255.0")
parser.add_argument("-timeout", required=False , help="{set timeout for respnse}{defaault 0.3}{less then this may give false result}" , default=0.3)
parser.add_argument("-verbose", required=False , help="{Show all host enen if he is offline}")
verbose = False
args = parser.parse_args()

#checking the args and setting default values if not assigned
if args.ip:
    ip = args.ip
if args.subnet:
    subnet = args.subnet
if args.timeout:
    timeout = float(args.timeout)
    socket.setdefaulttimeout(timeout)
if args.verbose:
    verbose = True


#this is jest for pirnting ip , subnet mask in a good design
def printInfo():
    print "*" * 40
    print "IP address : "+ ip , (40 - len("IP address : "+ ip)-3) * " " , "|"
    print " " * 38 , "|"
    print "Subnet Mask : "+ subnet, (40 - len("Subnet Mask : "+ subnet)-3) * " " , "|"
    print "*" * 40


def isON(hostIP):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#ipv4 , TCP
        sock.connect((hostIP,80))#connect to port 80 {if yes he's online}
        print "Host : " , hostIP , " is ON"
    except:
        if(verbose):
            print "Offline :" , hostIP
        pass
#checking how many times we have to loop
timea = timeb = timec = False
if subnet.split(".")[1] == "0":
    timea = True
if subnet.split(".")[2] == "0":
    timeb = True
if subnet.split(".")[3] == "0":
    timec = True
    
#print subnet.split(".")[1], subnet.split(".")[2] , subnet.split(".")[3]
#print timea , timeb , " .", timec

banner()
print "\n\n"
printInfo()

#Baic question  before starting
answer = raw_input("Application has locked on {0} with {1} subnetmask\ndo you wana continue ? (Y/N):".format(ip , subnet))
answer = answer.lower()
if(answer=="no" or answer=="n"):
    exit(0)

if timec:
    for a in range(0,256):
        isON(ip.split(".")[0] + "." + ip.split(".")[1] + "." + ip.split(".")[2] + "." +str(a))
        if(timeb):
            for b in range(0,256):
                isON(ip.split(".")[0] + "." + ip.split(".")[1] + "." + str(a) + "." + str(b))
                if(timea):
                    for c in range(0,256):
                        isON(ip.split(".")[0] + "." + str(a) + "." + str(b) + "." + str(c))

print "Done"

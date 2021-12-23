#!/data/data/com.termux/files/usr/bin/python3
import subprocess
import subprocess as sp
import http.server
import cgi

# These variables are used as settings
PORT       = 80        #the port in which the captive portal web server listens 
IFACE      = "wlan0"   #sp.getoutput('ifmnet') # the AP interface that captive portal protects
IP_ADDRESS = "0.0.0.0" #sp.getoutput('apgw') # the ip address of the captive portal (it can be the IP of IFACE) 

'''
This is the http server used by the the captive portal
'''
class WebPortal(http.server.SimpleHTTPRequestHandler):
    #this is the index of the captive portal
    #it simply redirects the user to the to login page
    html_redirect = """
    <html>
    <head>
        <meta http-equiv="refresh" content="0; url=http://%s:%s/login"/>
    </head>
    <body>
        <b>Redirecting to login page</b>
    </body>
    </html>
    """%(IP_ADDRESS, PORT)
    #the login page
    html_login = """
    <html>
    <head>
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <title>mnet agree</title>
        <style>
        body {
        color:#F1F3F3;
        background-image: url("https://mnet-repo.github.io/wall.jpg");
        height: 100%; width: 100%;
        no-repeat center center fixed;
        -webkit-background-size: cover;
        -moz-background-size: cover;
        -o-background-size: cover;
        background-size: cover;
        }
    </style>
    </head>
    <body>
        <a href="https://mnet-repo.github.io"><img src="https://mnet-repo.github.io/radio.svg" style="float:left"></a><b>mnet</br></left>
        <p>This network is repeating another network to devices that may not be authorized on the repeated network...</p>
        <form method="POST" action="do_login" name=agree><label>I understand and/or do not give a shit, connect me...<input type="checkbox" onchange="document.getElementById('agree').disabled = !this.checked;" /><input type="submit" name="agree" class="inputButton" id="agree" value="Connect"  disabled /></style></label></form>
    </body>
    </html>
    """
    #Alternative user/password login form
    #default form is one-liner click-through
    #remove <form-----to-----/form> from html_login
    #note the hashes below to enable the back-end
        #<b>mnet</b>
        #<form method="POST" action="do_login">
        #Username: <input type="text" name="username"><br>
        #Password: <input type="password" name="password"><br>
        #<input type="submit" value="Submit">
        #</form>

    #connected page
    html_connected = """
    <html>
    <head>
        <title>mnet connected</title>
        <style>
            body {
            color:#F1F3F3;
            background-image: url("https://mnet-repo.github.io/wall.jpg");
            height: 100%; width: 100%;
            no-repeat center center fixed;
            -webkit-background-size: cover;
            -moz-background-size: cover;
            -o-background-size: cover;
            background-size: cover;
            }
        </style>
    </head>
    <body>
        <a href="https://mnet-repo.github.io"><img src="https://mnet-repo.github.io/wifi.svg" style="float:left"></a><b>mnet</br></left>
        <p>Connected</p>
    </body>
    </html>
    """
    '''
    if the user requests the login page show it, else
    use the redirect page
    '''
    def do_GET(self):
        path = self.path
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if path == "/login":
            self.wfile.write(self.html_login.encode())
        else:
            self.wfile.write(self.html_redirect.encode())
    '''
    this is called when the user submits the login form
    '''
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
	#Keep text aligned if removing comment hashes!
	#these are TAB aligned from <--to--># 
	#remove hashes from the three code lines below, use TAB re-position
	#add hashes to both lines between "authorized user" and "if username"
	#username = form.getvalue("username")
	#password = form.getvalue("password")
	#if username == 'mnet' and password == 'changeme':
	agree = form.getvalue("agree")
	if agree == 'Connect':
            #authorized user
            remote_IP = self.client_address[0]
            print('New authorization from '+ remote_IP)
            print('Updating IP tables')
            subprocess.call(["iptables","-t", "nat", "-I", "PREROUTING","1", "-s", remote_IP, "-j" ,"ACCEPT"])
            subprocess.call(["iptables", "-I", "FORWARD", "-s", remote_IP, "-j" ,"ACCEPT"])
            self.wfile.write(self.html_connected.encode())
        else:
            #show the login form
            self.wfile.write(self.html_login.encode())

    #the following function makes server produce no output
    #comment it out if you want to print diagnostic messages
    #def log_message(self, format, *args):
    #    return
#PRETTY COLOR OUTPUT
GRAY="\033[01;30m"
CYAN="\033[01;36m"
GREEN="\033[01;32m"
RED="\033[01;31m"
CEND="\033[0m"
print(GRAY + "====================================================================================" + CEND)
print(CYAN +"mportal"+ CEND, end=' ')
print("|captive portal using python3 and iptables |", end=' ')
print(GREEN + "setting up routing tables...." + CEND, end=' ')
print("|")
print(GRAY + "====================================================================================" + CEND)
print(GREEN + "ALLOW" + CEND, end=' ')
print("TCP/UDP PORT 53", end=' ')
print(CYAN + "                                                 DNS" + CEND, end=' ')
print("TABLE", end=' ')
subprocess.call(["iptables", "-A", "FORWARD", "-i", IFACE, "-p", "tcp", "--dport", "53", "-j" ,"ACCEPT"])
subprocess.call(["iptables", "-A", "FORWARD", "-i", IFACE, "-p", "udp", "--dport", "53", "-j" ,"ACCEPT"])
print(GREEN +"SET"+ CEND)
print(GREEN + "ALLOW" + CEND, end=' ')
print("LOCAL SERVER", end=' ')
print(CYAN +"                                                 PORTAL"+CEND, end=' ')
print("TABLE", end=' ')
subprocess.call(["iptables", "-A", "FORWARD", "-i", IFACE, "-p", "tcp", "--dport", str(PORT),"-d", IP_ADDRESS, "-j" ,"ACCEPT"])
print(GREEN +"SET"+ CEND)
print(RED +"BLOCK"+ CEND, end=' ')
print("UNAUTHORIZED", end=' ')
print(RED +"                                                   DROP"+ CEND, end=' ')
print("TABLE", end=' ')
subprocess.call(["iptables", "-A", "FORWARD", "-i", IFACE, "-j" ,"DROP"])
print(GREEN +"SET"+ CEND)
print(GRAY +"===================================================================================="+ CEND)
print(CYAN+"mserver"+ CEND, end=' ')
print(GRAY+"|"+CEND, end=' ')
print(RED +"HTTP"+ CEND, end=' ')
print(GRAY+"|"+CEND, end=' ')
print("hosting web page....", end=' ')
httpd = http.server.HTTPServer(('', PORT), WebPortal)
print(GRAY+"|"+CEND, end=' ')
print(GREEN +"new traffic now redirects to..."+ CEND, end=' ')
subprocess.call(["iptables", "-t", "nat", "-A", "PREROUTING", "-i", IFACE, "-p", "tcp", "--dport", "80", "-j" ,"DNAT", "--to-destination", IP_ADDRESS+":"+str(PORT)])
print(CYAN+IP_ADDRESS+ ':'+str(PORT)+ CEND, end=' ')
print(GRAY+"|"+CEND)
print(GRAY +"===================================================================================="+ CEND)

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()

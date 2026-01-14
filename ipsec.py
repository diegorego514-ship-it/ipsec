import socket
import argparse 
import requests

SERVER_HOST = "192.167.87.145"
SERVER_PORT = 5003
SERVER_LISTS = SERVER_HOST, SERVER_PORT

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def _AF_INET():
    s.bind(socket, _AF_INET)
    s.connect("192.167.87.145")
    s.connect_ex((SERVER_HOST, SERVER_PORT))
    s.close()
    s.settimeout(5)
    def call_time_sleep():
        call_time_sleep()
        return s
    s.call_time_sleep(10) # Time in Seconds

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def _AF_INET():
        s.bind(socket, _AF_INET)
        s.connect("192.167.87.145")
        s.connect_ex((SERVER_HOST, SERVER_PORT))
        s.close()
        s.settimeout(10)
        def call_time_sleep():
            call_time_sleep()    
            return s
        s.call_time_sleep(15) # Time in Seconds
            
except:
        print("[+] Your Port is secure.")
else:
        print("[-] Your Port is not vulnerable to Hackers.")
import threading
import socket
import sys
from argparse import ArgumentParser
sys.path.append("..")

from tools.iPrint import *
from misc.Color import Colors


pts = []
now = 0

def get_input():
    parser = ArgumentParser()
    parser.add_argument("host", help="The host")
    parser.add_argument("-sp", help="The start port", required=True)
    parser.add_argument("-np", help="The end port", required=True)
    args = parser.parse_args()
    ip = args.host
    start_port = int(args.sp)
    end_port = int(args.np)
    return ip, start_port, end_port

def scan_port(ip, port):
    global now
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        print('                                                                                                                  ',end='\r')
        iPrintLog(f'Port {port} is open',"SuperScan", typer="success")
        pts.append(port)
    except:
        pass
    finally:
        now += 1
        s.close()

print(Colors.CYAN + '''
========================================================
   _____                          _____                 
  / ____|                        / ____|                
 | (___  _   _ _ __   ___ _ __  | (___   ___ __ _ _ __  
  \___ \| | | | '_ \ / _ \ '__|  \___ \ / __/ _` | '_ \ 
  ____) | |_| | |_) |  __/ |     ____) | (_| (_| | | | |
 |_____/ \__,_| .__/ \___|_|    |_____/ \___\__,_|_| |_|
              | |                                       
              |_|
========================================================
    阉割版 | Author: Lanbin | Github: lanbinshijie
========================================================'''+Colors.END)
    
ip, start_port, end_port = get_input()
iPrintLog(f"Scan is ready to start.", "SuperScan", typer="info")
iPrintLog(f"Target: {ip}", "SuperScan", typer="info")
iPrintLog(f"Start Port: {start_port}", "SuperScan", typer="info")
iPrintLog(f"End Port: {end_port}", "SuperScan", typer="info")
iPrintLog(f"========================================================", "SuperScan", typer="info")

total_ports = end_port - start_port + 1
ports_scanned = 0
print('                                                     \r',end='')
for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(ip, port))
    t.start()
    ports_scanned += 1
    if(ports_scanned % 25 == 0):
        iPrintLogNative(f'Scanned {len(pts)} Open Ports ({now}/{ports_scanned}/{total_ports})\r',"SuperScan", typer="info")
while now != total_ports:
    if(now % 2 == 0):
        iPrintLogNative(f'Scanned {len(pts)} Open Ports ({now}/{ports_scanned}/{total_ports})\r',"SuperScan", typer="info")
print("                                                                                                                  \r")
iPrintLog("========================================================","SuperScan", typer="warning")
iPrintLog("Scanned Finish!","SuperScan", typer="warning")
iPrintLog("There aren't any Result.","SuperScan", typer="warning")
iPrintLog("========================================================","SuperScan", typer="warning")



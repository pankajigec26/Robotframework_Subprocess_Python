from subprocess import Popen 
from subprocess import Popen, CREATE_NEW_CONSOLE,PIPE,STDOUT
import time
import subprocess
import platform
#K option tells cmd to run the command and keep the command window from closing. You may use /C instead to close the command window after the command finishes.

class Server:
    def __init__(self):
        pass
    def open_appium(self,terminal,command1,command2):
        test=[]
        if platform.system()=='Windows':
            self.terminal=terminal
            self.command1=command1
            self.command2=command2
            self.command_server1=self.terminal+' '+self.command1
            self.command_server2=self.terminal+' '+self.command2
            self.server1_start=Popen(self.command_server1,creationflags=CREATE_NEW_CONSOLE)
            self.server2_start=Popen(self.command_server2,creationflags=CREATE_NEW_CONSOLE)
            self.server_pid1=self.server1_start.pid
            self.server_pid2=self.server2_start.pid  
            print self.server_pid1
            print self.server_pid2
            
            
    def kill_appium(self):
        print self.server_pid1
        print self.server_pid2
        subprocess.Popen('taskkill /F /T /PID %i' % self.server_pid1)
        subprocess.Popen('taskkill /F /T /PID %i' % self.server_pid2)

ab=Server()
ab.open_appium("cmd"," /K appium -p 4723"," /K appium -p 4750")
ab.kill_appium()
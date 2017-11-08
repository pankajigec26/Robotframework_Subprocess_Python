# Robotframework_Subprocess_Python


These script will invoke the command prompt, open up the appium during SuiteSetup and then close it in Suite Teardown.
Prerequiste:
Python 2.7.14
Robot Framework 3.0.2 (Python 2.7.14 on win32)

Brief Decsription about each file :
process.robot

This import python file 'process.py' in library section , which have the function writeen to do the tasks . 
In SuiteSetup it will invoke the process 
In SuiteTeardown it will close all the opened processes

Handling_process.py 

This have two function in class Server 

open_appium - Two open applications
kill_appium - Kill the applications 

Run.bat 
This will run the script
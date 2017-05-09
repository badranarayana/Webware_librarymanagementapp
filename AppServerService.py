#!C:\Python27\python.exe

# You can adjust several parameters here
# (more info in WebKit.AppServerService):

workDir = None
webwareDir = 'C:\\Users\\balavala\\Downloads\\w4py-master\\w4py-master'
libraryDirs = ['Lib']
runProfile = False
logFile = None
appServer = 'ThreadedAppServer'
serviceName = 'WebKit'
serviceDisplayName = 'WebKit Application Server'
serviceDescription = ("This is the threaded application server"
    " of the Webware for Python web framework.")
serviceDeps = []

import sys
import os
sys.path.insert(0, webwareDir)

from WebKit import AppServerService as service

class AppServerService(service.AppServerService):
    # this class must be defined here in __main__
    _svc_name_ = serviceName
    _svc_display_name_ = serviceDisplayName
    _svc_description_ = serviceDescription
    _svc_deps_ = serviceDeps
    _workDir = workDir or os.path.dirname(__file__)
    _webwareDir = webwareDir
    _libraryDirs = libraryDirs
    _runProfile = runProfile
    _logFile = logFile
    _appServer = appServer

if __name__ == '__main__':
    service.AppServerService = AppServerService
    service.main()

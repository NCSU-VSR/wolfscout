"""
collarFileWatcher is to be started upon login. It uses a statically defined variable in this script to
determine what directory to monitor. Once launched it will look for changes in the directory.
As changes occur it will start a new thread which uses collarFileTrasnmitter to send the files to
The master server, which is also statically defined in this file.

Based on code from:
http://timgolden.me.uk/python/win32_how_do_i/watch_directory_for_changes.html
"""

###Global Imports
import os
### Win32 Imports
import win32file
import win32con
###Local Imports
from collarFileTransmitter import CollarFileTransmitter
###Static Definitions
#Actions are all the possible choices of things that can happen to a file in our directory
ACTIONS = {
    1 : "Created",
    2 : "Deleted",
    3 : "Updated",
    4 : "Renamed from something",
    5 : "Renamed to something"
}
# Thanks to Claudio Grondi for the correct set of numbers
FILE_LIST_DIRECTORY = 0x0001
#PATH_TO_WATCH is the directory that we will be watching during this time.
#It should be an absolute path, not a relative one.
PATH_TO_WATCH = "C:\\Users\\CNR\\AppData\\Local\\VirtualStore\\Program Files\\Lotek Wireless Inc\\GPS Total Host\\GPS Data"

#Create a directory to watch here.
hDir = win32file.CreateFile (
    PATH_TO_WATCH,
    FILE_LIST_DIRECTORY,
    win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE,
    None,
    win32con.OPEN_EXISTING,
    win32con.FILE_FLAG_BACKUP_SEMANTICS,
    None
)

#class FileMoverThread(Thread)

class FileWatcher(object):
    def __init__(self):
        self.listOfFilesToSend = []
        pass

    def isTextFile(self, filename):
        """
        isTextFile parses the file name to determine if it is a text file.
        if it is a text file True is returned.
        Else, False is returned.
        """
        if filename.split('.')[-1] in ( 'txt', 'TXT' ):
            return True
        return False

    def shouldFileBeSent(self, action, filename):
        """
        shouldFileBeSent checks first that the action merits sending the file.
        If the file has been updated it will then check to see if it is a text file.
        If both conditions are met, theFile is added to the list and true is returned
        """
        if action == 3:
            if self.isTextFile(filename):
                self.listOfFilesToSend.append(filename)
                return True
        return False

    def sendFile(self, filename):
        pass

    def main(self):
        #This loop runs forever
        print "Watching Files Now:"
        print "Directory being Watched: ", PATH_TO_WATCH
        while 1:
            #
            # ReadDirectoryChangesW takes a previously-created
            #    handle to a directory, a buffer size for results,
            #    a flag to indicate whether to watch subtrees and
            #    a filter of what changes to notify.
            #
            # NB Tim Juchcinski reports that he needed to up
            #    the buffer size to be sure of picking up all
            #    events when a large number of files were
            #    deleted at once.
            #
            results = win32file.ReadDirectoryChangesW (
                hDir,
                1024,
                True,
                win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
                 win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
                 win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
                 win32con.FILE_NOTIFY_CHANGE_SIZE |
                 win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
                 win32con.FILE_NOTIFY_CHANGE_SECURITY,
                None,
                None
            )
            for action, file in results:
                full_filename = os.path.join (PATH_TO_WATCH, file)
                if self.shouldFileBeSent(action, full_filename):
                    filer = CollarFileTransmitter(full_filename)
                    del filer

### Executed as a stand alone script
if __name__ == '__main__':
    fileWatcher = FileWatcher()
    fileWatcher.main()
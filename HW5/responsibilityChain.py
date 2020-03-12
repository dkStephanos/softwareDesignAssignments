import os   #Required to make os calls to open applications
from abc import ABC, abstractmethod     #Required to implement abstract classes in python
from getFileFromUser import getFileFromUser #Imports method to get filename from user

#Abstract Handler class to outline functionality/set up constructor
class Handler(ABC):
    def __init__(self, successor=None, sideChainSuccessor=None):
        self._successor = successor
        self._sideChainSuccessor = sideChainSuccessor

    @abstractmethod
    def handle_request(self):
        pass

#The file type specific handlers that will make up the chain/side chain
class txtWordFileHandler(Handler):
    def handle_request(self, fileExt, fileName):
        if fileExt == 'txt':
            value = os.system("open -b com.microsoft.Word " + fileName)
            if value != 0:
                self._sideChainSuccessor.handle_request(fileExt, fileName)
        elif self._successor is not None:
            self._successor.handle_request(fileExt, fileName)

class txtTextEditorFileHandler(Handler):
    def handle_request(self, fileExt, fileName):
        if fileExt == 'txt':  # if can_handle:
            value = os.system("open -a TextEdit " + fileName)
            if value != 0:
                self._sideChainSuccessor.handle_request(fileExt, fileName)
        elif self._successor is not None:
            self._successor.handle_request(fileExt, fileName)

class txtNotesFileHandler(Handler):
    def handle_request(self, fileExt, fileName):
        if fileExt == 'txt':  # if can_handle:
            value = os.system("open -a Notes " + fileName)
            if value != 0:
                self._sideChainSuccessor.handle_request(fileExt, fileName)
        elif self._successor is not None:
            self._successor.handle_request(fileExt, fileName)

class mp3FileHandler(Handler):
    def handle_request(self, fileExt, fileName):
        if fileExt == 'mp3':
            os.system("open -a 'quicktime player' " + fileName)
        elif self._successor is not None:
            self._successor.handle_request(fileExt, fileName)

class jpegFileHandler(Handler):
    def handle_request(self, fileExt, fileName):
        if fileExt == 'jpeg':
            os.system("open -a Preview " + fileName)
        elif self._successor is not None:
            self._successor.handle_request(fileExt, fileName)

class csvFileHandler(Handler):
    def handle_request(self, fileExt, fileName):
        if fileExt == 'csv':
            os.system("open -a Atom " + fileName)
        elif self._successor is not None:
            self._successor.handle_request(fileExt, fileName)

class defaultFileHandler(Handler):
    def handle_request(self, fileExt, fileName):
        print("\nUnsupported file type!!!")

#Instantiate the various handlers in reverse order of the chain, so as we create the next link,
#we can pass it it's successor (for the side chain, also pass the side chaing successor as the 2nd param)
defaultHandler = defaultFileHandler()
csvHandler = csvFileHandler(defaultHandler)
jpegHandler = jpegFileHandler(csvHandler)
mp3Handler = mp3FileHandler(jpegHandler)
txtNotesHandler = txtNotesFileHandler(defaultHandler)
txtTextEditorHandler = txtTextEditorFileHandler(txtNotesHandler)
txtWordHandler = txtWordFileHandler(mp3Handler, txtTextEditorHandler)

#Get file name from user
[fileName, fileDesc, fileExt] = getFileFromUser()

#Launch the chain with the first link
txtWordHandler.handle_request(fileExt, fileName)

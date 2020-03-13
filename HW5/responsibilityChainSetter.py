import os   #Required to make os calls to open applications
from abc import ABC, abstractmethod  #Required to implement abstract classes in python
from getFileFromUser import getFileFromUser #Imports method to get filename from user

#Abstract Handler class to outline functionality/set up constructor
class Handler(ABC):
    def __init__(self):
        self._successor = None
        self._sideChainSuccessor = None

    def set_successor(self, successor):
        self._successor = successor

    def set_sideChainSuccessor(self, sideChainSuccessor):
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

#Instantiate the various handlers in reverse order of the chain
defaultHandler = defaultFileHandler()
csvHandler = csvFileHandler()
jpegHandler = jpegFileHandler()
mp3Handler = mp3FileHandler()
txtNotesHandler = txtNotesFileHandler()
txtTextEditorHandler = txtTextEditorFileHandler()
txtWordHandler = txtWordFileHandler()

#Step back through the chain, and assign each the appropiate successor/sideChainSuccessor
txtWordHandler.set_successor(mp3Handler)
txtWordHandler.set_sideChainSuccessor(txtTextEditorHandler)
txtTextEditorHandler.set_successor(txtNotesHandler)
txtNotesHandler.set_successor(defaultHandler)
mp3Handler.set_successor(jpegHandler)
jpegHandler.set_successor(csvHandler)
csvHandler.set_successor(defaultHandler)

#Get file name from user
[fileName, fileDesc, fileExt] = getFileFromUser()

#Launch the chain with the first link
txtWordHandler.handle_request(fileExt, fileName)

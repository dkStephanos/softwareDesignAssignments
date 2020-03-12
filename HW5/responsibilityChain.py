import os
from abc import ABC, abstractmethod
from getFileFromUser import getFileFromUser

class Handler(ABC):
    def __init__(self, successor=None, sideChainSuccessor=None):
        self._successor = successor
        self._sideChainSuccessor = sideChainSuccessor

    @abstractmethod
    def handle_request(self):
        pass

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

defaultHandler = defaultFileHandler()
csvHandler = csvFileHandler(defaultHandler)
jpegHandler = jpegFileHandler(csvHandler)
mp3Handler = mp3FileHandler(jpegHandler)
txtNotesHandler = txtNotesFileHandler(defaultHandler)
txtTextEditorHandler = txtTextEditorFileHandler(txtNotesHandler)
txtWordHandler = txtWordFileHandler(mp3Handler, txtTextEditorHandler)

[fileName, fileDesc, fileExt] = getFileFromUser()

txtWordHandler.handle_request(fileExt, fileName)

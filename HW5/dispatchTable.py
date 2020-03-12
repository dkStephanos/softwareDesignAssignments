import os   #Required to make os calls to open applications
from getFileFromUser import getFileFromUser #Imports method to get filename from user

[fileName, fileDesc, fileExt] = getFileFromUser()

#Declaring functions for each open method, tiered for .txt's
def openTxt():
    value = os.system("open -b com.microsoft.Word " + fileName)
    if value != 0:
        value = os.system("open -a TextEdit " + fileName)
    if value != 0:
        value = os.system("open -a Notes " + fileName)

def openMp3():
    os.system("open -a 'quicktime player' " + fileName)

def openJpeg():
    os.system("open -a Preview " + fileName)

def openCsv():
    os.system("open -a Atom " + fileName)

#Dispatch table associating file extensions with methods to open them
dispatchFileOpenByExt = {
  'txt': openTxt,
  'mp3': openMp3,
  'jpeg': openJpeg,
  'csv': openCsv,
}

#Pass fileExt into dispatch table to trigger corresponding application execution
try:
    dispatchFileOpenByExt[fileExt]()
except KeyError:
    print("\nUnsupported file type!!!")

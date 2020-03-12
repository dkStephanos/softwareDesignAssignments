import os   #Required to make os calls to open applications
from getFileFromUser import getFileFromUser #Imports method to get filename from user

[fileName, fileDesc, fileExt] = getFileFromUser()

#Run through switch based on fileExt, opening file in appropriate application, printing error
#if file type not supported, for 'txt' case, try secondary and tertiary applications only on open failure
if fileExt == 'txt':
    value = os.system("open -b com.microsoft.Word " + fileName)
    if value != 0:
        value = os.system("open -a TextEdit " + fileName)
    if value != 0:
        value = os.system("open -a Notes " + fileName)
elif fileExt == 'mp3':
    os.system("open -a 'quicktime player' " + fileName)
elif fileExt == 'jpeg':
    os.system("open -a Preview " + fileName)
elif fileExt == 'csv':
    os.system("open -a Atom " + fileName)
else:
    print("\nUnsupported file type!!!")

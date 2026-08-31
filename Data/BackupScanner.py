############################################################
#
# Importing Required Libraries
#
############################################################

import os
import hashlib

############################################################
#
# Function Name : CalculateChecksum
# Description   : Calculate MD5 checksum of a file
#
############################################################

def CalculateChecksum(FileName):

    hobj = hashlib.md5()

    try:
        fobj = open(FileName,"rb")

        Buffer = fobj.read(1024)

        while(len(Buffer) > 0):
            hobj.update(Buffer)
            Buffer = fobj.read(1024)

        fobj.close()

        return hobj.hexdigest()
    
    except Exception as e:
        print("Unable to calculate checksum :", e)
        return None

############################################################
#
# Function Name : ScanDirectory
# Description   : Scan directory and collect file hashes
#
############################################################

def ScanDirectory(DirectoryName):

    FileData = {}

    Ret = os.path.isdir(DirectoryName)
    if(Ret == False):
        print("Invalid directory :", DirectoryName)
        return FileData

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            AbsolutePath = os.path.join(FolderName, fname)
            Checksum = CalculateChecksum(AbsolutePath)

            if Checksum is not None:
                FileData[AbsolutePath] = Checksum

    return FileData

############################################################
#
# Function Name : GetRelativeFileData
# Description   : Store relative paths with checksums
#
############################################################

def GetRelativeFileData(SourceDirectory):

    FileData = {}

    for FolderName, SubFolderNames, FileNames in os.walk(SourceDirectory):
        for fname in FileNames:
            AbsolutePath = os.path.join(FolderName, fname)
            RelativePath = os.path.relpath(AbsolutePath,SourceDirectory)
            Checksum = CalculateChecksum(AbsolutePath)

            if Checksum is not None:
                FileData[RelativePath] = Checksum

    return FileData
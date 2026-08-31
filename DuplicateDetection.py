############################################################
#
# Importing Required Libraries
#
############################################################

import os
from Data.BackupScanner import GetRelativeFileData

############################################################
#
# Function Name : CompareDirectories
# Description   : Compare source and backup directories
#
############################################################

def CompareDirectories(SourceDirectory, BackupDirectory):

    SourceFiles = GetRelativeFileData(SourceDirectory)

    BackupFiles = {}

    Ret = os.path.exists(BackupDirectory)
    if(Ret == True):
        BackupFiles = GetRelativeFileData(BackupDirectory)

    NewFiles = []
    ModifiedFiles = []
    UnchangedFiles = []

    for RelativePath in SourceFiles:
        SourceHash = SourceFiles[RelativePath]

        if RelativePath not in BackupFiles:
            NewFiles.append(RelativePath)

        else:
            BackupHash = BackupFiles[RelativePath]

            if(SourceHash != BackupHash):
                ModifiedFiles.append(RelativePath)

            else:
                UnchangedFiles.append(RelativePath)

    return NewFiles, ModifiedFiles, UnchangedFiles

############################################################
#
# Function Name : DisplayComparison
# Description   : Display comparison report
#
############################################################

def DisplayComparison(NewFiles,ModifiedFiles,UnchangedFiles):

    print("\n------------------------------------------------")
    
    print("NEW FILES :", len(NewFiles))
    for fname in NewFiles:
        print("  +", fname)

    print("\nMODIFIED FILES :", len(ModifiedFiles))
    for fname in ModifiedFiles:
        print("  *", fname)

    print("\nUNCHANGED FILES :", len(UnchangedFiles))

    print("------------------------------------------------")
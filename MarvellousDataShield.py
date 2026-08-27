############################################################
#
# Importing Required Libraries
#
############################################################

import os
import sys
import time
import shutil

from DuplicateDetection import CompareDirectories,DisplayComparison

############################################################
#
# Function Name : BackupFiles
# Description   : Copy new and modified files
# 
############################################################

def BackupFiles(SourceDirectory,BackupDirectory,NewFiles,ModifiedFiles):

    FilesToBackup = NewFiles + ModifiedFiles

    BackedUpFiles = []

    if not FilesToBackup:
        print("\nNo new or modified files found")
        return BackedUpFiles

    BackupCount = 0

    for RelativePath in FilesToBackup:

        SourceFile = os.path.join(SourceDirectory,RelativePath)

        DestinationFile = os.path.join(BackupDirectory,RelativePath)

        DestinationFolder = os.path.dirname(DestinationFile)

        Ret = os.path.exists(DestinationFolder)
        if(Ret == False):
            os.makedirs(DestinationFolder)

        try:
            shutil.copy2(SourceFile,DestinationFile)
            print("Backed up :",RelativePath)
            BackedUpFiles.append(RelativePath)
            BackupCount = BackupCount + 1

        except Exception as e:
            print("Unable to backup file :",e)

    return BackedUpFiles

############################################################
#
# Function Name : DataShield
# Description   : Main backup operation
# 
############################################################

def DataShield(SourceDirectory,BackupDirectory):

    print("\n")
    print("*" * 60)

    print("MARVELLOUS DATA SHIELD")

    print("Backup Started At :")

    start_time = time.ctime()
    print(start_time)

    print("*" * 60)

    Ret = os.path.exists(SourceDirectory)
    if(Ret == False):
        print("Source directory does not exist")
        return

    Ret = os.path.exists(BackupDirectory)
    if(Ret == False):
        os.makedirs(BackupDirectory)
        print("Backup directory created")

    ########################################################
    #
    #  Function Calling : To Compare directories
    #
    ########################################################

    NewFiles, ModifiedFiles, UnchangedFiles = \
        CompareDirectories(SourceDirectory,BackupDirectory)

    ########################################################
    #
    # Function Calling : To Display report
    #
    ########################################################

    DisplayComparison(NewFiles,ModifiedFiles,UnchangedFiles)

    ########################################################
    #
    # Function Calling : To Backup changed files
    #
    ########################################################
 
    BackedUpFiles = BackupFiles(SourceDirectory,BackupDirectory,NewFiles,ModifiedFiles)

############################################################
#
# Function Name : main
#
############################################################

def main():

    print("*" * 60)
    print("MARVELLOUS DATA SHIELD")
    print("Automated Backup & File Monitoring System")
    print("*" * 60)

    if len(sys.argv) < 3:
        print("\nUsage :")
        print("python MarvellousDataShield.py <SourceDirectory> <BackupDirectory>")
        print("\nExample :")
        print("python MarvellousDataShield.py Data Backup")
        return

    SourceDirectory = sys.argv[1]
    BackupDirectory = sys.argv[2]

    ########################################################
    #
    # Run first backup immediately
    #
    ########################################################

    DataShield(SourceDirectory,BackupDirectory)

############################################################
#
# Application Starter
#
############################################################

if __name__ == "__main__":
    main()
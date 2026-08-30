############################################################
#
# Importing Required Libraries
#
############################################################

import os
import sys
import time
import shutil
import schedule

from DuplicateDetection import CompareDirectories,DisplayComparison

from ReportAndLog import GenerateReport,CreateLog

from Email import SendEmail

############################################################
#
# Function Name : CreateArchive
# Description   : Create ZIP archive of backup
#
############################################################

def CreateArchive(BackupDirectory):

    try:
        ZipFilePath = ("Archive/DataShield_"+ time.strftime("%Y%m%d_%H%M%S"))

        Ret = os.path.exists("Archive")
        if(Ret == False):
            os.mkdir("Archive")

        shutil.make_archive(ZipFilePath,"zip",BackupDirectory)
        print("------------------------------------------------")
        print("\nArchive created successfully")
        print("------------------------------------------------")
        return ZipFilePath + ".zip"

    except Exception as e:
        print("------------------------------------------------")
        print("Unable to create archive :", e)
        print("------------------------------------------------")
        return None

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

    ########################################################
    #
    # Function Calling : To Create archive
    #
    ########################################################

    ZipFilePath = CreateArchive(BackupDirectory)

    if(ZipFilePath == None):
        print("Unable to create ZIP Archive")
        return
    
    end_time = time.ctime()
    print(end_time)

    ########################################################
    #
    # To Generate log
    #
    ########################################################


    LogFilePath = CreateLog(
        NewFiles,
        ModifiedFiles,
        BackedUpFiles,
        start_time,
        end_time,
        ZipFilePath
        )
    
    print("*" * 60)
    print("Backup Completed Successfully")
    print("Start Time :", start_time)
    print("End Time   :", end_time)
    print("Log File   :", LogFilePath)
    print("ZIP File   :", ZipFilePath)
    print("*" * 60)

    ########################################################
    #
    # Final Report
    #
    ########################################################

    Report = GenerateReport(NewFiles,ModifiedFiles,UnchangedFiles)

    Report = Report + "\n\nBacked Up Files Are : "

    Report = Report + str(BackedUpFiles)

    Report = Report + "\nArchive File : "

    Report = Report + str(ZipFilePath)

    print("\n")

    print(Report)

    print("*" * 60)
    print("Backup Completed Successfully")
    print("*" * 60)

    ########################################################
    #
    # Email Automation
    #
    ########################################################

    SenderEmail = "your_email@gmail.com"
    SenderPassword = "your_16_characters_password"
    ReceiverEmail = "receiver_email@gmail.com"

    EmailStatus = SendEmail(SenderEmail,SenderPassword,ReceiverEmail,"Marvellous Data Shield Backup Report",Report,ZipFilePath)

    if(EmailStatus == True):
        print("Backup Report sent successfully through email")
    else:
        print("Unable to send backup report through email")

############################################################
#
# Function Name : ScheduledBackup
# Description   : Run backup continuously
#
############################################################

def ScheduledBackup(SourceDirectory,BackupDirectory,Interval):

    schedule.every(Interval).minutes.do(DataShield,SourceDirectory,BackupDirectory)

    print("\nBackup scheduled every",Interval,"minutes")

    while True:
        schedule.run_pending()
        time.sleep(1)

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

    if len(sys.argv) < 4:
        print("\nUsage :")
        print("python MarvellousDataShield.py <SourceDirectory> <BackupDirectory> <Interval>")
        print("\nExample :")
        print("python MarvellousDataShield.py Data Backup 5")
        return

    SourceDirectory = sys.argv[1]
    BackupDirectory = sys.argv[2]
    Interval = int(sys.argv[3])

    ########################################################
    #
    # Run first backup immediately
    #
    ########################################################

    DataShield(SourceDirectory,BackupDirectory)

    ########################################################
    #
    # Start scheduled monitoring
    #
    ########################################################

    ScheduledBackup(SourceDirectory,BackupDirectory,Interval)

############################################################
#
# Application Starter
#
############################################################

if __name__ == "__main__":
    main()
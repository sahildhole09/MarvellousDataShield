import os
import time

############################################################
#
# Function Name : GenerateReport
# Description   : Generate backup report
#
############################################################

def GenerateReport(NewFiles,ModifiedFiles,UnchangedFiles):

    Report = ""

    Report = Report + "*" * 50
    Report = Report + "MARVELLOUS DATA SHIELD REPORT\n"
    Report = Report + "*" * 50

    Report = Report + "\n\nNew Files : "
    Report = Report + str(len(NewFiles))

    Report = Report + "\nModified Files : "
    Report = Report + str(len(ModifiedFiles))

    Report = Report + "\nUnchanged Files : "
    Report = Report + str(len(UnchangedFiles))

    Report = Report + "\n\nNew Files List:\n"
    for fname in NewFiles:
        Report = Report + fname + "\n"

    Report = Report + "\nModified Files List:\n"
    for fname in ModifiedFiles:
        Report = Report + fname + "\n"
    
    Report = Report + "*" * 50

    return Report

############################################################
#
#    Function Name : CreateLog
#    Description   : Creates detailed backup log file
#
############################################################

def CreateLog(NewFiles, ModifiedFiles, BackedUpFiles,StartTime, EndTime, ArchiveFile):

    Border = "*" * 60

    Ret = os.path.exists("Log")
    if(Ret == False):
        os.mkdir("Log")

    LogFileName = ("Log/DataShield_" +time.strftime("%Y%m%d_%H%M%S") +".log")

    try:
        fobj = open(LogFileName, "w")

        fobj.write(Border + "\n")
        fobj.write("           MARVELLOUS DATA SHIELD REPORT\n")
        fobj.write(Border + "\n\n")

        fobj.write("BACKUP EXECUTION DETAILS\n")
        fobj.write("-" * 60 + "\n")

        fobj.write("Start Time : " + StartTime + "\n")
        fobj.write("End Time   : " + EndTime + "\n\n")

        fobj.write(Border + "\n")
        fobj.write("NEW FILES\n")
        fobj.write(Border + "\n")

        fobj.write("Total New Files : " +str(len(NewFiles)) +"\n\n")

        if(len(NewFiles) == 0):
            fobj.write("No new files found.\n")
        else:
            for fname in NewFiles:
                fobj.write("New File : "+ fname +"\n")

        fobj.write("\n")

        fobj.write(Border + "\n")
        fobj.write("MODIFIED FILES\n")
        fobj.write(Border + "\n")

        fobj.write("Total Modified Files : " +str(len(ModifiedFiles)) +"\n\n")

        if len(ModifiedFiles) == 0:
            fobj.write("No modified files found.\n")
        else:
            for fname in ModifiedFiles:
                fobj.write("Modified File : "+ fname +"\n")

        fobj.write("\n")

        fobj.write(Border + "\n")
        fobj.write("BACKED UP FILES\n")
        fobj.write(Border + "\n")

        fobj.write("Total Backed Up Files : " +str(len(BackedUpFiles)) +"\n\n")

        if len(BackedUpFiles) == 0:
            fobj.write("No files backed up.\n")
        else:
            for fname in BackedUpFiles:
                fobj.write("Backed Up File : "+ fname +"\n")

        fobj.write("\n")

        fobj.write(Border + "\n")
        fobj.write("ARCHIVE INFORMATION\n")
        fobj.write(Border + "\n")

        fobj.write("Archive File : " +str(ArchiveFile) +"\n\n")

        fobj.write(Border + "\n")
        fobj.write("FINAL SUMMARY\n")
        fobj.write(Border + "\n")

        fobj.write("New Files       : " +str(len(NewFiles)) +"\n")

        fobj.write("Modified Files  : " +str(len(ModifiedFiles)) +"\n")

        fobj.write("Backed Up Files : " +str(len(BackedUpFiles)) +"\n")

        fobj.write("\n")
        fobj.write(Border + "\n")
        fobj.write("Backup Completed Successfully\n")
        fobj.write(Border + "\n")

        fobj.close()

        print("Log file created successfully")

        return LogFileName

    except Exception as e:
        print("Unable to create log file :", e)

        return None
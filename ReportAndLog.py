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

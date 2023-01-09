import os

totalBytes = 0

dirList = os.listdir()
for entry in dirList:
    if os.path.isfile(entry):
        filesize = os.path.getsize(entry)
        totalBytes += filesize


os.mkdir("results")

resultFile = open("results/results.txt", "w+")
if resultFile.mode == "w+":
    resultFile.write("Total bytecount:" + str(totalBytes) + "\n")
    resultFile.write("Files list:\n")
    resultFile.write("==============\n")
    
    for entry in dirList:
        if os.path.isfile(entry):
            resultFile.write(entry + "\n")

    resultFile.close()
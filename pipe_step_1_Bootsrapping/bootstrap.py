import os
import sys
from random import shuffle
import glob
import pandas as pd
import re



def lineLinesToOutString(mylist):
    s = ""
    for line in mylist:
        s += line
    return s


def removeSampleName(s):
    splitList = s.split(",")
    splitList = splitList[1:]
    s = ""
    for i in splitList:
        s += ","
        s += i
    return s
def split_dataset(filename,outputdir):
    fname=filename
    outdir=outputdir
    f = open(fname, "r")
    lines = f.readlines()
    print("I am here")
    print(os.getcwd())
    sizeOfAttributes = len(lines) - 2
    print("Number of observations is %d" % sizeOfAttributes)
    print("")
    print("You can use following table for choosing the split size.")
    print("Number of lines in splits. (An estimate of lines need to be provided.)")
    print("---------------------")
    print("")
    print("50% splits (creating two files) -> " , end='')
    print(sizeOfAttributes*(50/100))
    print("40% splits -> ", end='')
    print(sizeOfAttributes * (40 / 100))
    print("30% splits -> ", end='')
    print(sizeOfAttributes * (30 / 100))
    print("20% splits -> ", end='')
    print(sizeOfAttributes * (20 / 100))
    print("10% split -> ", end='')
    print(sizeOfAttributes * (10 / 100))
    indexPool = []
    for i in range(1, sizeOfAttributes + 1):
        indexPool.append(i)
    shuffle(indexPool)

    head = lines[0]
    tail = lines[len(lines) - 1]
    head = head


    threshold = int(input("Please, input the threshold value here :\n"))
    # threshold for partition


    k = threshold
    outLines = []
    while k < len(indexPool):
        outLines = []
        outLines.append(head)
        for j in range(k - threshold, k):
            line = lines[indexPool[j]]
            outLines.append(line)
        outLines.append(tail)
        fpath = os.path.join(outdir, "%d.csv" % (k))
        f = open(fpath, "w+")
        f.write(lineLinesToOutString(outLines))
        k += threshold

    # process the tail
    outLines = []
    outLines.append(head)
    for j in range(k - threshold, len(indexPool)):
        line = lines[indexPool[j]]
        outLines.append(line)
    outLines.append(tail)
    fpath = os.path.join(outdir, "%d.csv" % (k))
    f = open(fpath, "w+")
    f.write(lineLinesToOutString(outLines))

    #Detecting the created csv files
    csvFiles = sorted(glob.glob('*.csv'))
    os.system(("bash ../run_step_1_clean.sh"))
    for filepicker in range(0, len(csvFiles)):
        print("Operation created "+ str(len(csvFiles)) +" number of csv files.")
        print("")
        print("Creating the file structure for downstream analysis...")
        print("")
        fileName=str(csvFiles[filepicker])
        folderName=re.sub('.csv', '', fileName)

        os.system("mkdir -p {0}".format(re.sub('.csv', '', folderName)))

        os.system("mkdir -p {0}/pipe_step_2_FS".format(re.sub('.csv', '', str(csvFiles[filepicker]))))
        os.system("mkdir -p {0}/pipe_step_3_FAggregation".format(re.sub('.csv', '', str(csvFiles[filepicker]))))
        os.system("mkdir -p {0}/pipe_step_4_clf".format(re.sub('.csv', '', str(csvFiles[filepicker]))))


        #print("done too")


        os.system("cp -r ./../pipe_step_2_FS/ ./{0}/pipe_step_2_FS/".format(folderName))
        #print("done")
        os.system("cp -r ./../bootsrap_scripts/pipe_step_3_FAggregation/ ./{0}/pipe_step_3_FAggregation/".format(folderName))
        os.system("cp -r ./../pipe_step_4_clf/ ./{0}/pipe_step_4_clf/".format(folderName))
        os.system("chmod +x ./{0}/run_pipeline.sh".format(folderName))
        os.system("chmod +x ./{0}/pipe_step_2_FS/pipe_step_2_FS.sh".format(folderName))
        os.system("chmod +x ./{0}/pipe_step_3_FAggregation/pipe_step_3_FA.sh".format(folderName))
        os.system("chmod +x ./{0}/pipe_step_4_clf/pipe_step_4_clf.sh".format(folderName))
        #os.system("cp -r ./../input_file/ ./{0}/input_file/".format(folderName))
        os.system("mkdir -p ./{0}/input_file/".format(folderName))
        #os.system("mkdir -p {0}/pipe_step_2_FS/pipe_step_2_input".format(re.sub('.csv', '', str(csvFiles[filepicker]))))
        #os.system("mkdir -p {0}/pipe_step_2_FS/pipe_step_2_output".format(re.sub('.csv', '', str(csvFiles[filepicker]))))
        #os.system("mkdir -p {0}/pipe_step_2_FS/pipe_step_2_scripts".format(re.sub('.csv', '', str(csvFiles[filepicker]))))

        os.system("cp ./../bootsrap_scripts/run_pipeline.sh ./{0}/run_pipeline.sh".format(folderName))

        os.system("mv -f '{0}' ./{1}/pipe_step_2_FS/pipe_step_2_input/input.csv".format(str(csvFiles[filepicker]),folderName))
        #os.system("ls {0}".format(re.sub('.csv', '', str(csvFiles[filepicker]))))
        #os.system("bash ./{0}/run_pipeline.sh".format(folderName))
        #os.system("ls")
        #os.system("cd ..")
        # color_count = color_count + 1
        #dataCSV = pd.read_csv(os.getcwd() + '/' + csvFiles[filepicker], delimiter=',', header=0)
        #dataCSV_dummy = pd.get_dummies(dataCSV)





split_dataset('./../input_file/input.csv','.')

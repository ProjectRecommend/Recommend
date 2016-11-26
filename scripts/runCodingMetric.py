
import os
import sys
pathToStore="C:/Users/riflerRick/Desktop/NiitUniversityCSE_course/3rdyr/semester5/softwareEngineering/project/gitRepos/Recommend/recommend/codingMetrics/"
pathToCrawl="C:/Users/riflerRick/Desktop/NiitUniversityCSE_course/3rdyr/semester5/softwareEngineering/project/gitRepos/Recommend/recommend/"

# fileList=[]
pathToFetch=""
for dirpath, dirnames, filenames in os.walk(pathToCrawl):
    # print("dirpath:")
    # print (dirpath)
    # print("dirname:")
    # print (dirnames)
    # print("filename:")
    # print(filenames) 

    #filePath=pathToStore+"CodingMetric.txt"
    #sys.stdout=open(filePath,"a")

    for file in filenames:
        if file[-2:] == "py":
            pathToFetch=dirpath+file
            # print ("current pathToFetch:"+pathToFetch)
            print("\n Path: "+dirpath)
            print ("\n Filename:"+file)
            print ("\n Cyclomatic Complexity")
            command="radon cc -s "+pathToFetch 
            os.system(command)
            print ("\n Maintainability Index")
            command="radon mi -s "+pathToFetch
            os.system(command)
            print ("\n RAW")
            command="radon raw -s "+pathToFetch
            os.system(command)
    # for val in filenames:
    #     ext=val[-2:]
    #     if "py" in ext:
    #         fileList.append(val)
# for filePath in fileList:
#     command="radon cc -s "+path
# command="radon cc -s "+path+" > codingMetricCCOverview.txt"
# # os.system(command) simply takes the command and runs it on the default shell, in case of Windows cmd, in case of Linux, bash
# os.system(command)
# command="radon mi -s "+path+" > codingMetricMIOverview.txt"
# os.system(command)
# command="radon raw "+path+" > codingMetricRAWOverview.txt"
# os.system(command)

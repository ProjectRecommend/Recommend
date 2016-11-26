
import os
path="C:/Users/riflerRick/Desktop/NiitUniversityCSE_course/3rdyr/semester5/softwareEngineering/project/gitRepos/Recommend/recommend/"
# fileList=[]
# for dirpath, dirnames, filenames in os.walk(path):
#     for val in filenames:
#         ext=val[-2:]
#         if "py" in ext:
#             fileList.append(val)
command="radon cc -s "+path+"> codingMetricOverview.txt"
# os.system(command) simply takes the command and runs it on the default shell, in case of Windows cmd, in case of Linux, bash
os.system(command)
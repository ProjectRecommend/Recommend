# D:\\Songs(english)\\naked\\13 Hey There Delilah.mp3
# All Of Me - John Legend.mp3

# For manually testing ManageMetadata module.

from Metadata.ManageMetaDataModule import ManageMetaData

print ("starting test...")
obj=ManageMetaData()
print(obj.titleTIT2)
a=obj.ReadMetaData("D:\\Songs(english)\\naked\\All Of Me - John Legend.mp3")
print(obj.titleTIT2)
print ("printing metadata read:\n")
print(a)
print ("read metadata done")
obj.WriteMetaData(a,"D:/Songs(english)/Coldplay/1. Ghost Stories - Always In My Head.mp3")
print ("write metadata done")

print("lets now see if it has worked!!!\n")
a=obj.ReadMetaData("D:/Songs(english)/Coldplay/1. Ghost Stories - Always In My Head.mp3")
print ("printing metadata read:\n")
print(a)
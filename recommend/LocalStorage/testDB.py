from ManageLocalStorageModule import ManageLocalStorage
from AccessLocalStorageModule import AccessLocalStorage

obj=ManageLocalStorage("testCon")
obj.connect()
obj.dump()
obj.build()
objAccess=AccessLocalStorage("testCon")
objAccess.write("D:/Songs(english)/Selena Gomez/Hands to Myself.mp3") 
print(objAccess.read("D:/Songs(english)/Selena Gomez/Hands to Myself.mp3"))


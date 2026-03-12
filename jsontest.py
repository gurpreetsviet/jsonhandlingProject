import json
import os
data_list=(("surjit","khan","kalele"),("gurpreet","singh","barnala"))

emp_dct={}
if os.path.exists("empDataFile.json") and os.path.getsize("empDataFile.json")>0:
    with open("empDataFile.json","r") as file:
          emp_dct=json.load(file)
          print(emp_dct)
for i,list in enumerate(data_list):
      emp_dct[(f"emp{i+1}")]={"name":list[0],"Surname":list[1],"address":list[2]}
with open("empDataFile.json","w") as filew:
        json.dump(emp_dct,filew,indent=4)
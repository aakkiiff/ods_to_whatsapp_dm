import email
import json
from numpy import number
from odftoarray import ODSReader  

numbers = []
fileLocation = ODSReader("/home/akif/Desktop/ODSTOEMAILLIST.PY/data.ods")
arrays = fileLocation.getSheet("Form Responses 1")
BatchIndex = 2
contactIndex = 3
numbersFileName="numbers.txt"
final_numbers_list=[]

def getNumbers(arrays):
    for i in range(len(arrays)):
        if i == 0:
            continue
        if arrays[i][BatchIndex]=="63":
            numbers.append(arrays[i][contactIndex])

def renderNumber(numbers):
    getNumbers(arrays)
    for i in numbers:
        x=i.removeprefix('+880')
        y=x.removeprefix('0')
        final_numbers_list.append(y)
        
    with open(numbersFileName, 'w') as fp:
        for i in final_numbers_list:
            fp.write(i)
            fp.write("\n")

        
renderNumber(numbers)
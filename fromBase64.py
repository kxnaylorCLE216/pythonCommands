import pyperclip
import sys
import base64

base = 'https://intqa.amtrustgroup.com/TestResults/TestResults?VersionPass='
url = 'https://intqa.amtrustgroup.com/TestResults/TestResults?VersionPass=Q3VycmVudA%3D%3D&AppPass=QU5BV0M%3D&SubAppPass=QXNzaWduZWQgUmlzaw%3D%3D&EnvironmentPass=U3RhZ2luZw%3D%3D&TypePass=QXNzaWduZWQgUmlzaw%3D%3D&MatrixPass=RlBB&TestIDPass=MjUzNDc2MTY%3D&ViewingEnvironmentPass=UHJvZHVjdGlvbg%3D%3D&Key=aa15aa9aa6c93de838099fd56ecfdac6'

removeStr = ['SubApp', 'App', 'Environment', 'Type', 'Matrix', 'TestID', 'Key', 'Viewing'] 

base64Str = url.replace(base, "")

for item in removeStr:
    base64Str = base64Str.replace(item, "")

base64Str = base64Str.replace('=', "")
base64Str = base64Str.replace('%3D', "")

#splitB64 = '%3D&' 

base64Str = base64Str.split('&')
b64 = '%3D'

items = []

for item in base64Str:
    item = item.replace('Pass', "")
    items.append(item + '==')

printItems = []

for item in items:

    try:
        print(item)
        convert = base64.b64decode(item).decode("utf-8") 
        printItems.append(convert)
    except:
        pass
    
print(removeStr[1] + ": " + printItems[1])
print(removeStr[0] + ": " + printItems[2])
print(removeStr[2] + ": " + printItems[3])
print(removeStr[3] + ": " + printItems[4])
print(removeStr[4] + ": " + printItems[5])
print(removeStr[5] + ": " + printItems[6])
print(removeStr[7] + ": " + printItems[7])
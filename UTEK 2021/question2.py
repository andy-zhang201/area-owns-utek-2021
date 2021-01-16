import jsonFunctions
import json

extracted_json = jsonFunctions.extractJson("UTEK 2021/2.json","Nodes")
print(extracted_json)
sources = jsonFunctions.extractinput("UTEK 2021/2.in")
print("The sources: ", sources)

# with open("UTEK 2021/2.json","r") as f:

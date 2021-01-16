import jsonFunctions
import json
from collections import deque


extracted_json = jsonFunctions.extractJson("UTEK 2021/2.json","Nodes")
print(extracted_json)
sources = jsonFunctions.extractinput("UTEK 2021/2.in")
print("The sources: ", sources)
print(type(extracted_json[0]))
print(extracted_json[0]["Name"])

# for source in sources[0]:
    # print(source)
    #TODO: Use Djikstra on source.


# with open("UTEK 2021/2.json","r") as f:

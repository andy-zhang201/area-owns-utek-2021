import json
from jsonFunctions import extractJson
from sortingFunctions import mergesort

def find_k_most_accesible(inputFile:str,k:int):
    '''
    Inputs:
        inputFile: file name of the input, k: an integer for the number of results to be displayed
    Returns
        k most accessible paths as a list
    '''
    list_paths = extractJson(inputFile,'Paths')

    lst_out = []

    for path in list_paths:
        accessible=0
        for node in path["Nodes"]:
            if node["Accessible"]:
                accessible+=1
        lst_out.append(tuple((path["PathName"], accessible/(len(path["Nodes"])-accessible))))               # appends a tuple consisting of the name of the path and the accessibility ratio of that path

    kMostAccessible = mergesort(lst_out)[-k:]
    kMostAccessible.reverse()
    return kMostAccessible                                                                                  # Returns a list of k paths that are in decreasing order of the accesibility ratio.

def output1b(lst_out):                                                                                      # Writes the output to the .out file
    f = open("1b.out", "w")
    f.write(', '.join(lst_out))
    f.close()

def main():
    kMostAccessible = find_k_most_accesible('1b.json', 3)
    pathNames = [path[0] for path in kMostAccessible]
    output1b(pathNames)

main()


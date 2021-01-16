import json
from jsonFunctions import extractJson
from sortingFunctions import mergesort


def output1b(output_lst):
    f = open("1b.out", "w")
    f.write(', '.join(output_lst))
    f.close()

def Most_accessible (File_Name:str, k):

    list_paths = extractJson(File_Name, 'Paths')

    lst_out = []

    k = 3 

    for path in list_paths:
        accessible=0
        for node in path["Nodes"]:
            if node["Accessible"]:
                accessible+=1

        lst_out.append(tuple((path["PathName"], accessible/(len(path["Nodes"])-accessible))))

    final_l = mergesort(lst_out)[-k:]
    final_l.reverse()

    output_lst = []

    for x in final_l:
        output_lst.append(x[0])

    output1b(output_lst)

def main():
    Most_accessible('UTEK 2021/1b.json', 3)


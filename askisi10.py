import json
filepath = input("Please insert dictionary file path:")#Eisodos arxeiou apo xrhsth

file = open(filepath, "r")
text = file.read()

dictionary = json.loads(text)#metatroph tou string se dictionary
max_depth = 0 

#methodos gia thn euresh vathous enos leksikou
def find_depth_dict(dictionary,depth = 0):
    global max_depth
    for key, value in dictionary.items():
        if(depth+1>max_depth):
            max_depth = depth+1
        if isinstance(value, dict):
            find_depth_dict(value,depth=depth+1)
        elif isinstance(value, list):
            find_depth_list(value,depth=depth+1)
            
#methodos gia thn euresh vathous mias listas
def find_depth_list(lista,depth = 0):
    global max_depth
    for element in lista:
        if(depth+1>max_depth):
            max_depth = depth+1
        if isinstance(element, dict):
            find_depth_dict(element,depth=depth+1)
        elif isinstance(element, list):
            find_depth_list(element,depth=depth+1)    
            
find_depth_dict(dictionary)
print(dictionary,"Depth:", max_depth)

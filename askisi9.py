import math
filepath = input("Please insert ASCII file path:")#Eisodo arxeiou apo xrhsth

file = open(filepath, "r")
text = ""
for char in file.read(): 
    if(ord(char)%2 == 1):#ord(char) gia metatropi kathe xarakthra ston antistoixo arithmo ASCII kai ord(char)%2 == 1 gia na krataei mono tous monous.  
        text += char # to text tha periexei mono tous monous.
    
list1 = [] #h list1 tha periexei tous xarakthres pou uparxoun mesa sth metavlhth 'text'.
list2 = [] #h list2 tha periexei ton arithmo emfanisewn tou kathe xarakthra.
number_of_chars = 0 
for char in text:
    number_of_chars += 1
    i = text.count(char)    
    if(i==0):
        continue
    text = text.replace(char, "")
    list1.append(char)
    list2.append(i)

list3 = [] #pososto emfanisis epi tis ekato gia kathe xarakthra
for i in range(len(list1)):
    a = (list2[i]/number_of_chars)*100
    list3.append(math.ceil(a))
    
#emfanish twn statistikwn kathe grammatos
for i in range(len(list1)):
    temp_string = list1[i]+":"
    for z in range(list3[i]):
        temp_string += "*"
    print(temp_string)

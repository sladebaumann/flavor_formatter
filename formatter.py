#! /usr/bin/python


numbers_file = open('numbers_one_disk.txt')
target = open('flavor_list.json', 'w')
NewList =  []    #creating new list to append to
for line in numbers_file:    #for the lines in the text file, read them
    line.rstrip()   # strip the white space
    words = line.split()   #split the txt file into string words

    for word in words:      #for every word in txt file
        if words not in NewList:  #if not in the NewList
                NewList.append(words) #then appended words to Newlist 

#print(NewList[-1])

target.write('{\n')
i=1

for group in NewList:
	target.write('    "%s": {\n        "name": "c%s.m%s.d%s",\n        "vcpus": %s,\n        "ram": %s,\n        "disk": %s,\n        "id": "%s"\n    },\n' 
		% (i,group[0],group[1],group[2],group[0],group[1],group[2],i))
	i+=1
#"extra_specs": {\n            "disk2":

target.write('}')

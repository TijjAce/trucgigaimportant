
#!/usr/bin/env python3
# coding:utf8
import sys

liste=["girafe", "souris", "singe"]

add=[]
addSuite=[]

for element in liste:
    
    addSuite.append(element[1:len(element)])
    add.append(element[0])


addEnMajuscule= [lettre.upper() for lettre in add]

print(addEnMajuscule)
print(addSuite)

final=[]

for i,j in zip(addEnMajuscule,addSuite):
     final.append(str(i)+ str(j))
print(final)

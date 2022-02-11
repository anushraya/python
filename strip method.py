name="       anu       shraya      "
dots="..........."
print(name+dots)
print(name.lstrip()+dots)
print(name.rstrip()+dots)
print(name.strip()+dots)
print(name.replace(" ","")+dots)


#counting length after removing spaces
name=input("enter your name")
name1=name.replace(" ","")
print(len(name1))


string="hello hi hi hi hi hi hi"
print(string.replace("hi","hello",3))   #3->3 hii will be replaced

string1="she is beautiful and she is kind"
print(string1.find("is",1))    #1->position from where we want to start the search  
#                                 #find-to find the position of a word

# now to find 2nd position of "is" when length is unknown
string3=input("enter your string")
pos1=string3.find("is") 
pos2=string3.find("is",pos1+1)
print(pos2)
print(pos1)

#center method with program
name= "Anushraya"
print(name.center(13,"*"))
print(name.center(11,"*"))
print(name.center(10,"*"))
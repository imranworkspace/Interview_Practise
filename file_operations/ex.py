# r,r+ FileNotFoundError error 
# x FileExistsError 
# w,w+ overriden
# a append text on last of the file 

f = open("demo.tx2","a")
content=f.writelines(["bike\n","rabiyaa\n","\tkuri"])
f.close()
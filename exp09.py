string=input("ENTER THE STRING:")
n=len(string)
first=string[0]
last=string[n-1]
mod_str=last+string[1:n-1]+first
print("modified string:",mod_str)

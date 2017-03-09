fullname = input("Please enter your name and press Enter. ")

def get_initials(fullname):
    name_split = fullname.split()
    initials = "". join(name[0].upper() for name in fullname.split())
    return(initials)

print (get_initials(fullname))

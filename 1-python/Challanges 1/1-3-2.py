'''
def cleanup(dirtystr:str) -> str:
    noPunct = dirtystr.strip("?,.,!")
    return noPunct.strip().lower()
'''

def cleanup(dirtystr:str) -> str:
    for ch in "?,.!":
        if ch in dirtystr:
            return dirtystr.replace(ch, "").strip().lower()
        

dirty = "Hello, World!   "
cleanstr = cleanup(dirty)
print(cleanstr)
import os

dir = '/path/to/directory'

print os.listdir(dir)
os.chdir(dir)
lsnames = os.listdir(dir)

for names in lsnames:
    ext = names.split('.')[-1]                  # Stores the extensions in ext variable
    filename = names.split('.')[0]              # Stores the filename
    name = filename.split()[1:]                 
    newname = str(name[1]) + '_' + str(name[0]) + '.' + ext
    print newname
    os.rename(names, newname)


"""
If the original filename is '001 abc xyz'
then it will be renamed to
'xyz_abc'
"""
src = open('gt.txt','r')

for line in src.readlines():
    dest_fname = line.split(';')
    print(dest_fname)
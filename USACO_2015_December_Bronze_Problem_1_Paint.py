fin = open("paint.in", "r")
fout = open("paint.out", "w")
lines = fin.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].split()
    for j in range(len(lines[i])):
        lines[i][j] = int(lines[i][j])

if max(lines)[0]>min(lines)[1]:
    fout.write(str(max(lines)[1]-max(lines)[0]+min(lines)[1]-min(lines)[0]))

else:
    fout.write(str(max(lines[1][1], lines[0][1])-min(lines[0][0], lines[1][0])))


fin.close()
fout.close()


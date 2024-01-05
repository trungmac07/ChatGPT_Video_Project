
f = open("report.md", "r")
g = open("a.txt", "r")

w = open("report1.ipynb","w")

for line in g:
    if "\"#" in line:
        e=""
        c = 1
        for j in line:
            if j == "\"":
                continue
            if j=="#":
                e+="#"
                c+=1
            else:
                break
        w.write("\""+ e + " **"+line[c:-1]+"**\"")
        w.write("\n")





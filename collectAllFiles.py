import glob

# make md table of all files(kind,year,name)

print("|kind|year|name|")
print("|:--:|:--:|:--:|")


for file in glob.glob("**/*.tex", recursive=True):
    words = file[:-4].split("\\")
    kind = words[0]
    year = words[1]
    name = words[2][-1]
    print("|" + kind + "|" + year + "|" + name + "|")

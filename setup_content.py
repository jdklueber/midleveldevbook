import os
import shutil

def makeFileName(line):
    line = line.replace("#","")
    line = line.replace(" ","")
    line = line.replace("/","")
    return line

def buildPath(path, idx, filename):
    return f"{path}/{idx}_{filename}.md"

f = open("01_Outline.md")

current_dir = "content"
current_idx = 0
current_chapter = 0

shutil.rmtree(current_dir)
os.mkdir(current_dir)

for line in f:
    line = line.strip()
    if len(line) > 0:    
        if (line.startswith("###")):
            file = buildPath(current_dir, current_idx, makeFileName(line))
            current_idx += 1
            print("File: " + file)
            f = open(file, "w")
            f.write("# " + line.replace("#", "") + "\n")
            f.close()
        elif (line.startswith("##")):
            current_dir = "content/" + makeFileName(str(current_chapter) + "_" + line)
            current_chapter += 1    
            print("Directory: " + current_dir)
            os.mkdir(current_dir)
            current_idx = 0

f.close()
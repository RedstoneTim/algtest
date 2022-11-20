import os, requests

# Settings
algsDirectory = "algs"
outDirectory = "docs"
title = "My Algorithms"

i = 0
mdFiles = []
for file in os.listdir(algsDirectory):
    name = file.split(".")[0]
    markdownFile = name + ".md"
    mdFiles.append(markdownFile)
    filePath = algsDirectory + "/" + file
    fileIn = open(filePath)
    lines = fileIn.read().split("\n")
    fileIn.close()
    link = lines[0]
    algorithms = lines[1:]
    fileOut = open(outDirectory + "/" + markdownFile, "w")
    toWrite = "|Case|Algorithm|\n"
    j = 0
    for algorithm in algorithms:
        imageLink = link.replace("$ALG", algorithm)
        print(imageLink)
        imageName = "image" + str(i)+ "_" + str(j) + ".svg"
        imagePath = outDirectory + "/" + imageName
        response = requests.get(imageLink)
        response = "" if response is None else response
        imageFile = open(imagePath, "wb")
        imageFile.write(response.content)
        imageFile.close()
        toWrite += "|![](" + imageName + ")|" + algorithm + "|\n"
        j += 1
    fileOut.write(toWrite)
    fileOut.close()
    i += 1

indexFile = open(outDirectory + "/index.md", "w")
index = "# " + title + "\n\n"
for mdFile in mdFiles:
    index += "- [" + mdFile.split(".")[0] + "](" + mdFile + ")"
indexFile.write(index)
indexFile.close()

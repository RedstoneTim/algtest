import os, requests

# Settings
algsDirectory = "algs"
outDirectory = "docs"

i = 0
for file in os.listdir(algsDirectory):
    name = file.split(".")[0]
    filePath = algsDirectory + "/" + file
    fileIn = open(filePath)
    lines = fileIn.read().split("\n")
    fileIn.close()
    link = lines[0]
    algorithms = lines[1:]
    fileOut = open(outDirectory + "/" + name + ".md", "w")
    toWrite = "|Case|Algorithm|\n"
    j = 0
    for algorithm in algorithms:
        imageLink = link.replace("$ALG", algorithm)
        print(imageLink)
        imagePath = outDirectory + "/image" + str(i)+ "_" + str(j) + ".svg"
        response = requests.get(imageLink)
        response = "" if response is None else response
        imageFile = open(imagePath, "wb")
        imageFile.write(response.content)
        imageFile.close()
        toWrite += "|![](" + imagePath + ")|" + algorithm + "|\n"
        j += 1
    fileOut.write(toWrite)
    fileOut.close()
    i += 1

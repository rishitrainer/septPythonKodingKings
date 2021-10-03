
path = "/RISHI/H2K/H2KProjects/SEDAP/sampleFile.txt"

file = open(path, "a")
for i in range(10):
    file.write("This is Line Number {}".format(i))
    file.write("\n")

file.close()
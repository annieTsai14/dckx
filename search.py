def search(word):
        master = open ("file.txt", "r")
        for name in master:
                name = name.rstrip("\n")
                infile = open (name, "r")
                found = False
                for line in infile:
                        line = line.rstrip("\n")
                        if word in line:
                                found = True
                                break
                if found:
                        print(name)
                else:
                        print("Not found")
        infile.close()
search("mushroom")

file = open("my_file.txt")

contents =file.readlines()
print(contents)
file.close()



# with open("my_file.txt", mode="a") as file:
#     file.write("New Text.\n")

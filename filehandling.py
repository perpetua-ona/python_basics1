# What is filehandling 
# file handling is the act performing  file operations like read, write
# append etc. with a python script. with file handleing, you can create a file, read from a 
# file, write into a file etc with your python script.
import json
import csv

# book  = open("file3.py", "w")
# book.write()
# book.close()

dictionary = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

listoflits = [
    ["name", "age", "city"],
    ["John", "30", "New York"],
    ["Jane", "25", "New York"],
    ["Bob", "35", "New York"]
    ]
# with open("file2.json", "w") as file:
#     print(json.dump(dictionary, file))
with open("file1.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(listoflits)
       
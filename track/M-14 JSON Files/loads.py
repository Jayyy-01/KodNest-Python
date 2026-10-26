import json

name = input("Enter name: ")
score = int(input("Enter score: "))

print(name, type(name))
print(score, type(score)) 

student = {"name" : name, "score" : score}

print(student, type(student))

strObj = json.dumps(student)
print(strObj, type(strObj))

with open("data.json", "w") as file:
    file.write(strObj)
    
#json.loads() ---> json string to python dict
python_data = json.loads(strObj)
print(python_data, type(python_data["name"], type(python_data)))

#json.load() ---> json file to python dict
with open("data.json", "r") as file:
    python_data = json.load(file)
    print(python_data, type(python_data))


#json dump
import json
student = {
    "name": "Jay",
    "age": 20,
    "courses": "python",
    "mobile": 9876543210,
}

with open("data2.json", "w") as file:
    json.dump(student, file)

with open("data2.json", "r") as file:
    python_data = json.load(file)
    print(python_data, type(python_data))
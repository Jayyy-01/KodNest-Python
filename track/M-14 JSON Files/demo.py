import json
name = input()
score = int(input())

student = {
    "name": name,
    "score": score
}

print(json.dumps(student))          #to convert python dict into json string, if this is not done then it will print the type of name as str and score as int.json

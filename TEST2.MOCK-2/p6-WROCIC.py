import json

def f(years: int, course: str, average_grade: int) -> int:
    with open("data.json", "r") as file:
        data = json.loads(file.read())

    count = 0

    for student in data:
        if (student["age"] >= years):
            for subject in student["studies"]["courses"]:
                if (subject["name"] == course):
                    avg = 0
                    
                    for x in subject["grades"]:
                        avg += x
                        
                    avg = (avg / len(subject["grades"]))
                        
                    if (avg >= average_grade):
                        count += 1
                        
                    break
                
    return count

print(f(21, "statistics", 4))
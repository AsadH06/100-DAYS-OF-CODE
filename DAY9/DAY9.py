student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key,value in student_scores.items():
    if value > 90:
        student_grades[key] = 'Outstanding'
    elif value > 80:
        student_grades[key] = 'Exceeds Expectations'
    elif value > 70:
        student_grades[key] = 'Acceptable'
    elif value <= 70:
        student_grades[key] = 'Fail'

print(student_grades)


capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
### NESTED LIST
travel_log = {
    "France": {
        "Cities visited": ["Paris", "Lille", "Dijon"],
        "tota_visits": 12,
    },
    "Germany": {
        "Cities visited": ["Stuttgart", "Berlin", "Hamburg"],
        "tota_visits": 12,
    },
}

print(travel_log['France']['Cities visited'][1])
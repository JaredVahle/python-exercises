students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]


# 1. How many students are there?

len(students)

# 2. How many students prefer light coffee? For each type of coffee roast?

def light_coffee_count(students):
    i = 0
    light_count = 0
    while i < len(students):
        if students[i]["coffee_preference"] == "light":
            light_count += 1
            i += 1
        else:
            i += 1
            
    return light_count

light_coffee_count(students)
    
# 3. How many types of each pet are there?
def unique_animal_list(students):
    i = 0
    animal_list = []
    
    while i <= len(students)-1:
        holder = (students[i])
        if len(holder["pets"]) > 1:
            animal_list.append(holder["pets"][0]["species"])
            i += 1
        else:
            i+= 1
        
    return set(animal_list)

unique_animal_list(students)

# 4. How many grades does each student have? Do they all have the same number of grades?

def grade_count(students):
    grade_count = []
    for student in students:
        grade_count.append(len(student["grades"]))
    return grade_count

grade_count(students)

# 5. What is each student's grade average?

def grade_avg(students):
    student_grade_avg = []
    for student in students:
        grade_total = 0
        for grade in student["grades"]:
            grade_total += int(grade)
        avg_grade = grade_total
        student_grade_avg.append(avg_grade/4)
    return student_grade_avg

grade_avg(students)

# 6. How many pets does each student have?

def pet_count(students):
    pet_count_list = []
    for student in students:
        pet_count_list.append(len(student["pets"]))
    return pet_count_list

pet_count(students)

# 7. How many students are in web development? data science?

def class_count(students):
    web_dev_count = 0
    data_sci_count = 0
    for student in students:
        if student["course"] == "web development":
            web_dev_count += 1
        elif student["course"] == "data science":
            data_sci_count += 1
        else:
            pass
    return (f"{web_dev_count} students in web dev and {data_sci_count} students in data sci")

class_count(students)

# 8. What is the average number of pets for students in web development?

def pets_for_web_dev_students(students):
    pet_count = 0
    web_dev_student = 0
    for student in students:
        if student["course"] == "web development":
            pet_count += len(student["pets"])
            web_dev_student += 1
    return pet_count / web_dev_student

pets_for_web_dev_students(students)

# 9. What is the average pet age for students in data science?

def pet_age_data_science_students(students):
    num_of_pets = 0
    total_pet_age = 0
    for student in students:
        if student["course"] == "data science":
            num_of_pets += len(student["pets"])
            for pet in student["pets"]:
                total_pet_age += pet["age"]
    return total_pet_age / num_of_pets
            
pet_age_data_science_students(students)

# 10. What is most frequent coffee preference for data science students?

def data_sci_coffee_pref(students):
    light_count = 0
    medium_count = 0
    dark_count = 0
    coffee_count = []
    for student in students:
        if student["course"] == "data science":
            if student["coffee_preference"] == "light":
                light_count += 1
            elif student["coffee_preference"] == "medium":
                medium_count += 1
            elif student["coffee_preference"] == "dark":
                dark_count += 1
    coffee_count.append(light_count)
    coffee_count.append(medium_count)
    coffee_count.append(dark_count)
    return f"{coffee_count[0]} light, {coffee_count[1]} medium, {coffee_count[2]} dark" , max(coffee_count)

data_sci_coffee_pref(students)

# 11. What is the least frequent coffee preference for web development students?

def web_dev_least_coffee_pref(students):
    light_count = 0
    medium_count = 0
    dark_count = 0
    coffee_count = []
    for student in students:
        if student["course"] == "web development":
            if student["coffee_preference"] == "light":
                light_count += 1
            elif student["coffee_preference"] == "medium":
                medium_count += 1
            elif student["coffee_preference"] == "dark":
                dark_count += 1
    coffee_count.append(light_count)
    coffee_count.append(medium_count)
    coffee_count.append(dark_count)
    return f"{coffee_count[0]} light, {coffee_count[1]} medium, {coffee_count[2]} dark" , min(coffee_count)

web_dev_least_coffee_pref(students)

# 12. What is the average grade for students with at least 2 pets?

def avg_grade_two_pets(students):
    total_grade = 0
    num_of_grades = 0
    for student in students:
        if len(student["pets"]) >= 2:
            for grade in student["grades"]:
                num_of_grades += 1
                total_grade += grade
    return (total_grade/num_of_grades)

avg_grade_two_pets(students)

# 13. How many students have 3 pets?

def students_with_three_pets(students):
    student_count = 0
    for student in students:
        if len(student["pets"]) == 3:
            student_count += 1
    return student_count

students_with_three_pets(students)

# 14. What is the average grade for students with 0 pets?

def avg_grade_students_zero_pets(students):
    grade_total = 0
    grade_count = 0
    for student in students:
        if len(student["pets"]) == 0:
            for grade in student["grades"]:
                grade_count += 1
                grade_total += grade
    return grade_total / grade_count

avg_grade_students_zero_pets(students)

# 15. What is the average grade for web development students? data science students?

def avg_grade_per_class(students):
    #ds = datascience
    #wd = webdev
    ds_total_grade = 0
    ds_grade_count = 0
    wd_total_grade = 0
    wd_grade_count = 0
    for student in students:
        if student["course"] == "data science":
            for grade in student["grades"]:
                ds_grade_count += 1
                ds_total_grade += grade
        elif student["course"] == "web development":
            for grade in student["grades"]:
                wd_grade_count += 1
                wd_total_grade += grade
                
    ds_avg_grade = ds_total_grade / ds_grade_count
    wd_avg_grade = wd_total_grade / wd_grade_count
    return(f"datascience avg grade is {ds_avg_grade}, web development avg grade is {wd_avg_grade}")

avg_grade_per_class(students)

# 16. What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?


# 17. What is the average number of pets for medium coffee drinkers?


# 18. What is the most common type of pet for web development students?


# 19. What is the average name length?


# 20. What is the highest pet age for light coffee drinkers?


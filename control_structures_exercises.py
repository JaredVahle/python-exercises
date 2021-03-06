1. Conditional Basics

    a. prompt the user for a day of the week, print out whether the day is Monday or not
    day_of_week = input("what day of the week is it:")
    if day_of_week.lower() ==  "monday":
        print("lame its monday")
    else:
        print("yay its not monday")

    b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

    day_of_week = input("what day of the week is it:")
    if day_of_week.lower() in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
        print("weekday")
    if day_of_week[0] == "s" or day_of_week[0] == "S":
        print("its the weekend")

    c. create variables and make up values for
        a. the number of hours worked in one week

        hours_worked = 40

        b. the hourly rate

        hourly_rate = 22.5

        c. how much the week's paycheck will be

        check = hours_worked * hourly_rate

        d. write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
        
        def pay(hourly_rate,hours_worked):
            total_pay = 0
            
            if hours_worked > 40:
                total_pay += 40 * hourly_rate
                hours_worked -= 40
                total_pay += hours_worked * (hourly_rate * 1.5)
            else:
                total pay += hours_worked * hourly_rate
        return(total_pay)

2. Loop Basics

    a. while

        a. Create an integer variable i with a value of 5.

            i = 5

        b. Create a while loop that runs so long as i is less than or equal to 15

            while i <= 15:

        c. Each loop iteration, output the current value of i, then increment i by one.

            while i <= 15:
                print(i)
                i += 1

        d. Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

            i = 0 
            while i <= 100:
                print(i)
                i += 2

        e. Alter your loop to count backwards by 5's from 100 to -10.

            i = 100
            while i >= -10:
                print(i)
                i -= 5

        f. Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:

            i = 2
            while i < 1000000:
                print(i)
                i += i**2

        g. Write a loop that uses print to create the output shown below.
            i = 100
            while i > 0:
                print(i)
                i -= 5

    b. For Loops

        a. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number. For example, if the user enters 7, your program should output:

# done writing down questions they are on the control structures portion

i = 1
num = input("pick a number")

while i <= 10:
    print(f"{num} X {i} = "+ str (int(num) * i))
    i += 1


i = 1

while i < 10:
    print(str(i) * i)
    i += 1




odd_in_50 = input("pick an odd number 1-50")
i = 1
while i <= 50:
    if odd_in_50.isdigit() == True and int(odd_in_50) % 2 != 0:
        if i == int(odd_in_50):
            print(f"yikes! skipping number {odd_in_50}")
            i += 1
            continue
        elif i % 2 == 1:
            print(f"here is an odd number: {i}")
            i += 1
        else:
            i += 1
    else:
        break



target_num = input("put in any positive number:")
i = 0
if target_num.isdigit and int(target_num) > 0:
    while i < int(target_num):
        i += 1



target_num = input("put in any positive number:")
i = int(target_num)
if target_num.isdigit and int(target_num) > 0:
    while i >= 1:
        print(i)
        i -= 1




num = range(1,100)
def fizz_buzz(num):
    for i in num:
        if i % 3 == 0 and i % 5 == 0:
            print("fizz_buzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

fizz_buzz(num)



keep_going = True
while keep_going == True:
    i = input("pick a number preferably 3-10:  ---'quit' to exit")
    if i.isdigit():
        print("number | squared | cubed")
        print("-------|---------|------")
        for num in range(1,int(i)):
            print(f" {num: <4}  | {num ** 2: <6}  | {num ** 3}")
    else:
        keep_going = False




def grade_template():
    more_grades = "y"
    while more_grades == "y":
        grade = input("what grade did you get on this test?: ---'quit' to exit")
        if grade.isdigit:
            num = int(grade)
            if num >= 0 and num <= 59:
                if num >= 55:
                    print(f"{num} the range for 'F+' is 55-59")
                else:
                    print(f"{num} the range for 'F' is 0-54")
            elif num >= 60 and num <= 66:
                if num <= 62:
                    print(f"{num} the range for 'd-' is 60-62")
                elif num >= 64:
                    print(f"{num} the range for 'd+' is 64-66")
                else:
                    print(f"{num} the range for 'd' is 63")
            elif num >= 67 and num <= 79:
                if num <= 69:
                    print(f"{num} the range for 'c-' is 67-69")
                elif num >= 77:
                    print(f"{num} the range for 'c+' is 77-79")
                else:
                    print(f"{num} the range for 'c' is 70-76")
            elif num >= 80 and num <= 87:
                if num <= 82:
                    print(f"{num} the range for 'b-' is 80-82")
                elif num >= 85:
                    print(f"{num} the range for 'b+' is 85-87")
                else:
                    print(f"{num} the range for 'b' is 83-84")
            elif num >= 88 and num <= 100:
                if num <= 90:
                    print(f"{num} the range for 'a-' is 88-90")
                elif num >= 98:
                    print(f"{num} the range for 'a+' is 98-100")
                else:
                    print(f"{num} the range for 'a' is 91-97")
            else:
                pass


books = [
    {
        "title": "The Subtle Art of Not Giving a F*ck",
        "author": "Mark Manson",
        "genre's": ["Self-help book"]
    },
    {
        "title": "Breath",
        "author": "James Nestor",
        "genre's": ["Self-help book", "Creative nonfiction"]
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "genre's": ["Science fiction","political fiction","Dystopian fiction","Social science fiction"]
    }
]
user_genre = input("what kind of book genre are you looking for: ")
for book in books:
    for genre in book["genre's"]:
        if genre == user_genre:
            print(book)
    
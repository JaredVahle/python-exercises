
movies = [
    {
        "title" : "The little mermaid",
        "time_rented" : 3
    },
    {
        "title" : "Brother Bear",
        "time_rented" : 5
    },
    {
        "title" : "Hercules",
        "time_rented" : 1
    }
]

movie_1 = movies[0]
movie_2 = movies[1]
movie_3 = movies[2]

print(movie_1["time_rented"] * 3)
print(movie_2["time_rented"] * 3)
print(movie_3["time_rented"] * 3)




companies = [
    {
        "company_name" : "Google",
        "pay_per_hour" : 400,
        "hours_worked" : 6
    },
    {
        "company_name" : "Amazon",
        "pay_per_hour" : 380,
        "hours_worked" : 4
    },
    {
        "company_name" : "Facebook",
        "pay_per_hour" : 350,
        "hours_worked" : 10
    },
]

google_pay_total = companies[0]["pay_per_hour"] * companies[0]["hours_worked"]
amazon_pay_total = companies[1]["pay_per_hour"] * companies[1]["hours_worked"]
facebook_pay_total = companies[2]["pay_per_hour"] * companies[2]["hours_worked"]

total_pay = google_pay_total + amazon_pay_total + facebook_pay_total 
print(f"${total_pay}")





def student_enrollment(full,timing):
    if full == False and timing == True:
        print("this is the perfect class for you")
    elif full == True and timing == True:
        print("sorry but the class is full")
    elif full == False and timing == False:
        print("the class isnt full but the timing is just off")
    else:
        print("nothing is lining up right with this class")


full = False
timing = True

student_enrollment(full,timing)




expired = True
items = 3
premium_member = True

def product_offer(expired,items,premium_member):
    if expired and items > 2 or premium_member:
        return(True)
    else:
        return(False)

product_offer(expired,items,premium_member)






username = "codeup"
password = "notastrongpassword"

def user_pass_check (username,password):
    if len(password) >= 5 and len(username) <= 20 and password != username and username.strip() != username and password.strip() != password:
        return True
    else:
        return False


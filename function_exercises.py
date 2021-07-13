def is_two(num):
    #takes in a number and checks it against 2 to see if it indeed is the number two and returns true or false
    return (num == 2) or (num == "2")

def is_vowel(letter):
    # Checks to see if letter is a vowel and returns true or false
    return (letter.lower() in ("aeiou"))

def is_consonant(letter):
    # Checks to see if letter is a vowel and returns false if it isnt a vowel because it is a consonant
    if is_vowel(letter) == True:
        return False
    else:
        return True

def upper_a_consonant(word):
    # checks to see if the first letter is a consonant
    if is_consonant(word[0]):
        return word.capitalize
    else:
        return word

def calculate_tip(percent,cost):
    # gives you a total based on multiplying both a percent and a cost together to give a tip
    return percent * cost


def apply_discount(org_price,discount_percent):
    # returns the price after it has been discounted
    return org_price - (org_price * discount_percent)

def handle_commas(num):
    # checks if there are any commas and i number and strips them if there are
    return num.replace(",","")

def get_letter_grade(grade):
    #checks if the grade is an int type that can be used below
    if grade.is_digit() == True:
        if grade <= 59:
            return "F"
        elif grade >= 60 and grade <= 69:
            return "D"
        elif grade >= 70 and grade <= 79:
            return "C"
        elif grade >=80  and grade <= 89:
            return "B"
        elif grade >= 90 and grade <= 100:
            return "A"

def remove_vowels(word):
    # Made a new empty string that will hold the new word
    word_without_vowels = ""
    # going through each letter in the word
    for letter in word:
        #checking if the letter is a vowel
        if is_vowel(letter) == True:
            pass
        else:
            #if its not a vowel im going to add it to the new list
            word_without_vowels += letter

    return word_without_vowels


def normalize_name(name):
    # creating an empty string
    normalized_name = ""
    # making a trip wire for my while statement
    starter = True
    while starter == True:
        # enumerating name so i can find the index of the first position that has an _ or a letter
        for index, letter in enumerate(name):
            if letter.isalpha() or letter == "_":
                start = index
                starter = False
                break
    # changing the new name to a string with the beginning index at where an _ or letter starts
    new_name = name[int(start):]
    for letter in new_name:
        if letter == " ":
            normalized_name += "_"
        elif letter.isalpha() or letter.isnumeric() or letter == "_":
            normalized_name += letter
            
    return normalized_name


def cumulative_sum(nums):
    #making an empty list and an empty variable i can use to compare against my list
    new_sums = []
    number = 0
    for num in nums:
        # setting number to add the last number and appending that onto my list each time
        number += num
        new_sums.append(number)
    return new_sums


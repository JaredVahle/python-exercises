import function_exercises as fe

fe.is_vowel("h")

fe.calculate_tip(100,.2)

fe.normalize_name("    4  ## This is a function")

from itertools import combinations,permutations

list(product("abc",[1,2,3]))

list(combinations("abcd",2))

list(permutations("abcd",2))

import json

user = json.load(open('profiles.json'))

len(json.load(open('profiles.json')))

items = json.load(open('profiles.json'))

active_user_count = 0
for item in items:
    if item["isActive"] == True:
        active_user_count += 1
print(active_user_count)

active_user_count = 0
for item in items:
    if item["isActive"] == False:
        active_user_count += 1
print(active_user_count)

def money(money):
    new_list = ""
    for item in money:
        holder = item
        if holder in "1234567890.":
            new_list += item
    return new_list

total = 0
for item in items:
    single_balance = float(money(item["balance"]))
    total += single_balance
    
print(total)

def min_balance(items):
    user_balance = []
    index = -1
    for item in items:
        user_balance.append(float(money(item["balance"])))
    for amount in user_balance:
        index += 1
        if amount == min(user_balance):
            return items[index]["name"]

min_balance(items)

def max_balance(items):
    user_balance = []
    index = -1
    for item in items:
        user_balance.append(float(money(item["balance"])))
    for amount in user_balance:
        index += 1
        if amount == max(user_balance):
            return items[index]["name"]

def most_fruits(items):
    counts = {}
    for item in items:
        if item["favoriteFruit"] in counts.keys():
            counts[item["favoriteFruit"]] += 1
        else:
            counts[item['favoriteFruit']] = 1
    return max(counts),counts

most_fruits(items)

def least_fruits(items):
    counts = {}
    for item in items:
        if item["favoriteFruit"] in counts.keys():
            counts[item["favoriteFruit"]] += 1
        else:
            counts[item['favoriteFruit']] = 1
    return min(counts),counts

least_fruits(items)

def num_of_msgs(greeting):
    new_list = ""
    for item in greeting:
        holder = item
        if holder in "1234567890":
            new_list += item
    return new_list

def messages(items):
    each_user_msgs = []
    single_user_msgs = 0
    total = 0
    for item in items:
        single_user_msgs = int(num_of_msgs(item["greeting"]))
        each_user_msgs.append(int(num_of_msgs(item["greeting"])))
        total += single_user_msgs
    return total,each_user_msgs

messages(items)
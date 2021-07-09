{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ded8e2df",
   "metadata": {},
   "outputs": [],
   "source": [
    "students = [\n",
    "    {\n",
    "        \"id\": \"100001\",\n",
    "        \"student\": \"Ada Lovelace\",\n",
    "        \"coffee_preference\": \"light\",\n",
    "        \"course\": \"web development\",\n",
    "        \"grades\": [70, 91, 82, 71],\n",
    "        \"pets\": [{\"species\": \"horse\", \"age\": 8}],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100002\",\n",
    "        \"student\": \"Thomas Bayes\",\n",
    "        \"coffee_preference\": \"medium\",\n",
    "        \"course\": \"data science\",\n",
    "        \"grades\": [75, 73, 86, 100],\n",
    "        \"pets\": [],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100003\",\n",
    "        \"student\": \"Marie Curie\",\n",
    "        \"coffee_preference\": \"light\",\n",
    "        \"course\": \"web development\",\n",
    "        \"grades\": [70, 89, 69, 65],\n",
    "        \"pets\": [{\"species\": \"cat\", \"age\": 0}],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100004\",\n",
    "        \"student\": \"Grace Hopper\",\n",
    "        \"coffee_preference\": \"dark\",\n",
    "        \"course\": \"data science\",\n",
    "        \"grades\": [73, 66, 83, 92],\n",
    "        \"pets\": [{\"species\": \"dog\", \"age\": 4}, {\"species\": \"cat\", \"age\": 4}],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100005\",\n",
    "        \"student\": \"Alan Turing\",\n",
    "        \"coffee_preference\": \"dark\",\n",
    "        \"course\": \"web development\",\n",
    "        \"grades\": [78, 98, 85, 65],\n",
    "        \"pets\": [\n",
    "            {\"species\": \"horse\", \"age\": 6},\n",
    "            {\"species\": \"horse\", \"age\": 7},\n",
    "            {\"species\": \"dog\", \"age\": 5},\n",
    "        ],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100006\",\n",
    "        \"student\": \"Rosalind Franklin\",\n",
    "        \"coffee_preference\": \"dark\",\n",
    "        \"course\": \"data science\",\n",
    "        \"grades\": [76, 70, 96, 81],\n",
    "        \"pets\": [],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100007\",\n",
    "        \"student\": \"Elizabeth Blackwell\",\n",
    "        \"coffee_preference\": \"dark\",\n",
    "        \"course\": \"web development\",\n",
    "        \"grades\": [69, 94, 89, 86],\n",
    "        \"pets\": [{\"species\": \"cat\", \"age\": 10}],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100008\",\n",
    "        \"student\": \"Rene Descartes\",\n",
    "        \"coffee_preference\": \"medium\",\n",
    "        \"course\": \"data science\",\n",
    "        \"grades\": [87, 79, 90, 99],\n",
    "        \"pets\": [{\"species\": \"cat\", \"age\": 10}, {\"species\": \"cat\", \"age\": 8}],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100009\",\n",
    "        \"student\": \"Ahmed Zewail\",\n",
    "        \"coffee_preference\": \"medium\",\n",
    "        \"course\": \"data science\",\n",
    "        \"grades\": [74, 99, 93, 89],\n",
    "        \"pets\": [{\"species\": \"cat\", \"age\": 0}, {\"species\": \"cat\", \"age\": 0}],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100010\",\n",
    "        \"student\": \"Chien-Shiung Wu\",\n",
    "        \"coffee_preference\": \"medium\",\n",
    "        \"course\": \"web development\",\n",
    "        \"grades\": [82, 92, 91, 65],\n",
    "        \"pets\": [{\"species\": \"cat\", \"age\": 8}],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100011\",\n",
    "        \"student\": \"William Sanford Nye\",\n",
    "        \"coffee_preference\": \"dark\",\n",
    "        \"course\": \"data science\",\n",
    "        \"grades\": [70, 92, 65, 99],\n",
    "        \"pets\": [{\"species\": \"cat\", \"age\": 8}, {\"species\": \"cat\", \"age\": 5}],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100012\",\n",
    "        \"student\": \"Carl Sagan\",\n",
    "        \"coffee_preference\": \"medium\",\n",
    "        \"course\": \"data science\",\n",
    "        \"grades\": [100, 86, 91, 87],\n",
    "        \"pets\": [{\"species\": \"cat\", \"age\": 10}],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100013\",\n",
    "        \"student\": \"Jane Goodall\",\n",
    "        \"coffee_preference\": \"light\",\n",
    "        \"course\": \"web development\",\n",
    "        \"grades\": [80, 70, 68, 98],\n",
    "        \"pets\": [{\"species\": \"horse\", \"age\": 4}],\n",
    "    },\n",
    "    {\n",
    "        \"id\": \"100014\",\n",
    "        \"student\": \"Richard Feynman\",\n",
    "        \"coffee_preference\": \"medium\",\n",
    "        \"course\": \"web development\",\n",
    "        \"grades\": [73, 99, 86, 98],\n",
    "        \"pets\": [{\"species\": \"dog\", \"age\": 6}],\n",
    "    },\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "7c9eee9e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def avg_grade_per_class(students):\n",
    "    #ds = datascience\n",
    "    #wd = webdev\n",
    "    ds_total_grade = 0\n",
    "    ds_grade_count = 0\n",
    "    wd_total_grade = 0\n",
    "    wd_grade_count = 0\n",
    "    for student in students:\n",
    "        if student[\"course\"] == \"data science\":\n",
    "            for grade in student[\"grades\"]:\n",
    "                ds_grade_count += 1\n",
    "                ds_total_grade += grade\n",
    "        elif student[\"course\"] == \"web development\":\n",
    "            for grade in student[\"grades\"]:\n",
    "                wd_grade_count += 1\n",
    "                wd_total_grade += grade\n",
    "                \n",
    "    ds_avg_grade = ds_total_grade / ds_grade_count\n",
    "    wd_avg_grade = wd_total_grade / wd_grade_count\n",
    "    return(f\"datascience avg grade is {ds_avg_grade}, web development avg grade is {wd_avg_grade}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "5c6f7a2f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'datascience avg grade is 84.67857142857143, web development avg grade is 81.17857142857143'"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "avg_grade_per_class(students)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "13878cce",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
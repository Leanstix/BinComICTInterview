#!/usr/bin/python3
import re
from collections import Counter
from statistics import mean, variance, median
import psycopg2

colors_by_day = {
    "MONDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "TUESDAY": "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE",
    "WEDNESDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE",
    "THURSDAY": "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "FRIDAY": "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE",
}

all_colors = []
for day, colors in colors_by_day.items():
    each_colors = re.sub(r'\s+', '', colors).upper().split(",")
    all_colors.extend(each_colors)

color_counts = Counter(all_colors)
most_common_color = color_counts.most_common(1)[0][0]
sorted_colors = sorted(color_counts.values())
color_frequencies = list(color_counts.values())
mean_color = mean(color_frequencies)
median_color = median(color_frequencies)
red_probability = color_counts['RED'] / len(all_colors)
color_variance = variance(color_frequencies)

def save_to_postgresql(data):
    try:
        conn = psycopg2.connect(
            database="my_database",
            user="leanstixx",
            password="Lekan",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS color_frequency (color VARCHAR, frequency INTEGER);")
        for color, freq in data.items():
            cursor.execute("INSERT INTO color_frequency (color, frequency) VALUES (%s, %s);", (color, freq))
        conn.commit()
        cursor.close()
        conn.close()
        print("Success!!!")
    except Exception as e:
        print(f"Datebase error: {e}")

def recursive_search(lst, target, index=0):
    if index == len(lst):
        return -1
    if lst[index] == target:
        return index
    return recursive_search(lst, target, index + 1)

def random_binary_to_decimal():
    from random import randint
    binary = ''.join(str(randint(0, 1)) for _ in range(4))
    decimal = int(binary, 2)
    return binary, decimal

def fibonacci_sum(n):
    a, b = 0,1
    total = 0
    for _ in range(n):
        total += a
        a, b = b, a + b
    return total
#question 1
print(f"Mean color: {mean_color}")
#question 2
print(f"Most common color: {most_common_color}")
#question 3
print(f"Median color: {median_color}")
#question 4
print(f"Variance of colors: {color_variance}")
#question 5
print(f"Probability of RED: {red_probability}")
#question 6
save_to_postgresql(color_counts)
#question 7
numbers = [5, 10, 15, 20, 25, 30,]
print(f"Recursive Search (30): {recursive_search(numbers, 25)}")
#qustion 8
binary, decimal = random_binary_to_decimal()
print(f"Random Binary: {binary}, Decimal: {decimal}")
#question 9
print(f"Sum of First 50 Fibonacci Numbers: {fibonacci_sum(50)}")

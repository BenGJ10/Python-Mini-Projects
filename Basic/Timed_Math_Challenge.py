''' This is a Python program showcasing Timed Math problems, if you don't know 
answer to any specific question, type skip to jump to next question. '''

import random 
import time

OPERATORS = ["+", "-", "*"]    # Capital Variables are constants
MIN_OPERAND = 2
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10 

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    
    return expr, answer
correct = 0
wrong = 0
skip = 0
input("Press Enter to start!")
print("---------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, ans = generate_problem()
    while True:
        guess = input(f"Problem # { i + 1}: {expr} = ").lower()
        if guess == "skip":
            skip += 1
            break
        elif guess == str(ans):
            correct += 1
            break
        else:
            wrong += 1       

end_time = time.time()             
total_time = end_time - start_time
print("---------------------\n")
print("Scorecard: \n")
print(f"Correct Answer: {correct}\n")
print(f"Wrong Answer: {wrong}\n")
print(f"Skipped Questions: {skip}\n")

print(f"Nice Work, You finished within {total_time:.1f} seconds")

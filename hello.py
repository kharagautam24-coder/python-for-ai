"""
import requests

# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200
str="hello how are you?"
print(len(str))
print(str[5:])

def calculate_avg(a,b,c):
    print((a+b+c)/3)

calculate_avg(10,20,30)
def table_of_n(a):
    for i in range (0,11):
        
        print(a*i)

table_of_n(10)

import math
import random
p=math.sqrt(16)
print(p)
number = random.randint(1,10)
print(number)
choice=random.choice(["gautam","dax","divyesh","prince"])
print(choice)

import datetime as dt
today = dt.date.today()
print("Today's date:", today)

import os
current_directory = os.getcwd()
print("Current directory:", curret_directory)

"heelo"+5
5+5
"hhello"+"hi"
try:
    result=10/0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
"""
import response
# Without classes - data and functions separate
name = "OpenAI"
model = "gpt-4o-mini"

def generate_response(prompt):
    # Process prompt...
    return response

# With classes - everything bundled together
class OpenAIClient:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    
    def generate_response(self, prompt):
        # Process prompt...
        return response
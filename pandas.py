#TODO :: Separate out theory questions. OOPS Questions and Quiz
#Ref : https://www.edureka.co/blog/interview-questions/python-interview-questions/
#Ref : https://www.interviewmocha.com/tests/python-3-coding-test-high

import sys
import json

question = int(sys.argv[1])

with open('questions.json', 'r') as questions_dict:
    all_questions = json.load(questions_dict)
print(all_questions.get(str(question)))

print(question)
if question == 1:
    # Question 1: Count |, _, and Vowels from the given string and get total pipes in string.
    # Solution :
    sentence = input()
    dashesh = "_|"
    dash_count = len([char for char in sentence if char in dashesh])
    print(sentence.count('|'))
    print(sentence.count('_'))
    print("vowels_count", dash_count)
elif question == 2:
    # Question 2: get total pipes from given integer.
    sentence = input()
    dict = {'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':4,'8':7,'9':6}
    # Solution :
    print(dict.get(sentence))
elif question == 3:
    # Question 3 : What would be the output of the following programme.
    number = 5.0
    try:
        r = 10/number
        print("Absolute division",r)
        r = 10 // 2.5
        print("Floor division", r)
    except e:
        print("Oops! Error occurred.")
elif question == 4:
    List = ['a','b','c','d','e']
    print(List[10:])
elif question == 5:
    # Question 5 : What would be the output of the following programme.
    num=3
    while True:
        if num%0o12 == 0:
            break
        print(num)
        num += 1
elif question == 6:
    # Question 6 : How to do division without using operator.
    print("Not yet implemented logic for this.")
elif question == 7:
    # Question 7 : Write the programme to generate total of prime number between 2 given numbers.
    numberone = input()
    numbertwo = input()
    total = 0
    while int(numberone) < int(numbertwo):
        if (int(numberone) // 2 == 0 or int(numberone) // 3 == 0) and int(numberone) not in (1,2,3):
            numberone = int(numberone) + 1
            continue
        else:
            total += int(numberone)
            numberone = int(numberone) + 1
    print("total",total)
elif question == 8:
    # Question 8 : Get the factorial of given number.
    number = int(input())
    factorial = 1
    while number > 0:
        factorial = factorial * number
        number = number -1

    print(factorial)
elif question == 9:
    # Question 9 : Is string immutable? or not? Prove with below code.
    s  = "anup"
    print(s.replace("anup","update"))
    print(s)
elif question == 10:
    # Question 10 : Add new dict into fruits index in dict with new dict.
    foods = [{
        "fruits":{
            "apple": "red",
            "banana": "yellow",
            "kiwi": "green"
        },
        "vegetables": {
            "cucumber": "green",
            "tomato": "red",
            "lettuce": "green"
        }
    }]
    newFruit = {"cherry": "red"}
    foods[0]["fruits"].update(newFruit)
    print(foods)
# Question 11 : What would be the output of following calls.
elif question == 11:
    def test(*args, **kwargs):
        print(type(args), type(kwargs))
    # a.
    test(1, 3)
    # b.
    test(1, x=3)
    # c.
    # test(1, x=3,4)
# Solution :
# a. tuple, dict
# b. tuple, dict
# c. Error.
elif question == 12:
    print("Not yet implemented.")
    # Question 11 : Write down the logic / programme to get input and output as below.
    # Input :   A  L Y
    # Output :  D  O B
elif question == 13:
    # Question 13 : Write down code to achieve output.
    # input = "I am programmer"
    # output = "programmer am I"
    print("Not yet implemented.")
elif question == 14:
    print("Not yet implemented.")
    # Question 13 : Capitalize all characters from file.
elif question == 15:
    print("Not yet implemented.")
    # Question 14 : Open file in read, write, append mode.
elif question == 16:
    print("Not yet implemented.")
    # Question 16 : What is use of finally in Python
elif question == 17:
    print("Not yet implemented.")
    # Question 17 : Difference between shallow copy and deep copy
elif question == 18:
    print("Not yet implemented.")
    # Question 18 : What is GIL in Python.
elif question == 19:
    print("Not yet implemented.")
# Question 19 : Python method overloading example.
elif question == 20:
    print("Not yet implemented.")
# Question 20 : What is Reference Counting
elif question == 21:
    print("Not yet implemented.")
# Question 21 : What is namespace in Python
elif question == 22:
    print("Not yet implemented.")
# Question 22 : What is the difference between sort and sorted.
elif question == 23:
    print("Not yet implemented.")
# Question 23 : What is the function to get space id of python object.
elif question == 24:
    print("Not yet implemented.")
# Question 24 : Explain data types of Python
elif question == 25:
    print("Not yet implemented.")
# Question 25 : Explain collection of Python
elif question == 26:
    print("Not yet implemented.")
# Question 26 : Difference between set and dict
elif question == 27:
    print("Not yet implemented.")
# Question 27 : Difference between tuple and list
elif question == 28:
    print("Not yet implemented.")
# Question 28 : Difference between __ini__ and __new__ function
elif question == 29:
    print("Not yet implemented.")
# Question 29 : Explain Iterators and Generators.
elif question == 30:
    print("Not yet implemented.")
# Question 30 : Explain Closures in python
elif question == 31:
    print("Not yet implemented.")
# Question 31 : Explain Lambda in python
elif question == 32:
    print("Not yet implemented.")
# Question 32 : Decorators in python
elif question == 33:
    print("Not yet implemented.")
# Question 33 : What is module/package ?
elif question == 34:
    print("Not yet implemented.")
# Question 34 : What is pickling and unpickling
elif question == 35:
    print("Not yet implemented.")
# Question 35 : List/Dictionary/tuple comprehension
elif question == 36:
    print("Not yet implemented.")
# Question 36 : Explain Dict Enumeration
elif question == 37:
    print("Not yet implemented.")
# Question 37 : Types of Decorators
elif question == 38:
    print("Not yet implemented.")
# Question 38 : Can class be a decorator?
elif question == 39:
    print("Not yet implemented.")
# Question 39 : Explain Inheritance in Python.
elif question == 40:
    print("Not yet implemented.")
# Question 40 : How can I push value at certain position in list?
elif question == 41:
    print("Not yet implemented.")
# Question 41 : How to reverse the string without using inbuilt functions
elif question == 42:
    print("Not yet implemented.")
# Question 42 : Explain globals vs locals
elif question == 43:
    print("Not yet implemented.")
# Question 43 : Usage of __main__, __name__
elif question == 44:
    print("Not yet implemented.")
# Question 44 : Difference between __str__ and __repr__
elif question == 45:
    print("Not yet implemented.")
# Question 45 : Explain lambda map, reduce, filter
elif question == 46:
    print("Not yet implemented.")
# Question 46 : Explain Python threading
elif question == 47:
    print("Not yet implemented.")
# Question 47 : What are Meta Classes in Python
elif question == 48:
    print("Not yet implemented.")
# Question 48 : What is Monkey Patching in Python
elif question == 49:
    print("Not yet implemented.")
# Question 49 : What is best Sorting Algorithm
elif question == 50:
    print("Not yet implemented.")
# Question 50 : What is best Search Algorithm
elif question == 51:
    print("Not yet implemented.")
# Question 51 : Explain Python memory management.
elif question == 52:
    print("Not yet implemented.")
# Question 52 : Switch case from lower to upper and upper to lower for all chars in given file
elif question == 53:
    print("Not yet implemented.")
# Question 53 : Convert csv file to json file
elif question == 54:
    print("Not yet implemented.")
# Question 54 : How to read and process huge files, how memory is managed
elif question == 55:
    print("Not yet implemented.")
# Question 55 : sort ascending and descending list
elif question == 56:
    print("Not yet implemented.")
# Question 56 : Why python is interpreter language.
# Python will fall under byte code interpreted. .py source code is first compiled to byte code as .pyc. This byte code can be interpreted (official CPython), or JIT compiled (PyPy). Python source code (.py) can be compiled to different byte code also like IronPython (.Net) or Jython (JVM). There are multiple implementations of Python language. The official one is a byte code interpreted one. There are byte code JIT compiled implementations too.
# https://softwareengineering.stackexchange.com/questions/24558/is-python-interpreted-or-compiled
elif question == 57:
    print("Not yet implemented.")
# Question 57 : What's the difference between Python multi threading and multiprocessing
elif question == 58:
    print("Not yet implemented.")
# Question 58:How to print all arguments of command line.
# Solution : print(sys.argv)
    print("Not yet implemented.")
elif question == 59:
    # Question 59 : Explain regular expressions with example.
    print("Not yet implemented.")
elif question == 60:
    # Question 60 : How to troubleshoot Python code and what is pdb?
    print("Not yet implemented.")
elif question == 61:
    # Question 61 : Time and Space complexity of the function
    print("Not yet implemented.")
elif question == 62:
    # Question 41 : Difference between Class, Static and instance method.
    print("Not yet implemented.")
elif question == 63:
    # Question 15 : What is catch in python
    print("Not yet implemented.")
else:
    print("No question input...")

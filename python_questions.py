# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. def hello_name(user_name):

def hello_name(user_name):
    first="hello_"
    result=first + user_name.upper() + "!"
    print(result)
hello_name("Tom")




# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():

def first_odds():
    for numbers in range(1,100,2):
        print(numbers)
    return None
first_odds()




# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. def max_num_in_list(a_list):

def max_num_in_list(a_list):
    return max(a_list)
print(max_num_in_list([1,2,3]))
print(max_num_in_list([1,9,3]))




# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. The return should be boolean Type (true/false). def is_leap_year(a_year):

def is_leap_year(a_year):
    if (a_year % 4 == 0): #if remainder is 0
        if (a_year % 100 != 0): #not divisiable 
            return True
        elif (a_year % 400 == 0):
            return True   
    return False
print(is_leap_year(2023))
    




# Question 5
# Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):

def is_consecutive(a_list):
    for i in range(1, len(a_list)):
        previous_val = a_list[i - 1]
        current_val = a_list[i]
        print(current_val)  
        if current_val != previous_val + 1:
            return False
    return True

print(is_consecutive([1,2,3,4,5]))
print(is_consecutive([1,2,3,4,6]))

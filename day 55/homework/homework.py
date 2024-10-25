# 1
def check_even_or_odd(number):
    if number % 2 == 0:
        return "ლუწი"
    else:
        return "კენტი"


result = check_even_or_odd(8)
print(result) 

# 2

def check_size(number):
    if number > 10:
        return "დიდია"
    else:
        return "პატარა"

result = check_size(9)
print(result)  # შედეგი: "პატარა"


def good_day_message():
    return "კარგი დღე გქონდეს!"


message = good_day_message()
print(message)  


def sum_two_numbers(a, b):
    return a + b

sum_result = sum_two_numbers(7, 3)
print(sum_result) 

def cube(number):
    return number ** 3


cube_result = cube(3)
print(cube_result)  

def best_message():
    return "საუკეთესო ხარ!"


best_result = best_message()
print(best_result)  

#3

def difference(x, y):
    return x - y


diff_result = difference(10, 5)
print(diff_result)  # შედეგი: 5


def merge_words(word1, word2):
    return f"{word1} {word2}"

merged_result = merge_words("გამარჯობა", "მეგობარო")
print(merged_result) 


def rectangle_area(length, width):
    return length * width


area_result = rectangle_area(4, 6)
print(area_result) 


def greet(name):
    return f"გამარჯობა, {name}"


greet_result = greet("ანა")
print(greet_result)  

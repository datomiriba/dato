# 1)

def add_one():
   
    number = int(input("შეიყვანეთ რიცხვი: "))
   
    number += 1
    print(f"შედეგი: {number}")


add_one()



# 2)


def check_greater_than_ten():
  
    number = int(input("შეიყვანეთ რიცხვი: "))
    
    if number > 10:
        print("მაგარია!")
    else:
        print("რიცხვი არ არის 10-ზე მეტი.")


check_greater_than_ten()

# 3)
def min_of_two_numbers():
    num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
    num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))
    
    minimum = min(num1, num2)
    print(f"უმცირესი რიცხვი არის: {minimum}")


min_of_two_numbers()




# 4)

def text_length():
    text = input("შეიყვანეთ ტექსტი: ")
    length = len(text)
    print(f"ტექსტის სიგრძე: {length}")

text_length()






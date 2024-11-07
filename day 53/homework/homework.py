#   1)
def calculator():

    num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
    num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
    operation = input("რა ოპერაცია გსურთ? (+, -, *, /): ")

    
    if operation == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operation == "/":
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("მოძრაობა არ შეიძლება, 0-ზე არ შეიძლება გაყოფა.")
    else:
        print("არასწორი ოპერაცია.")


# 2)
calculator()

def sum_of_numbers(numbers):
    return sum(numbers)


numbers = [1, 2, 3, 4, 5]
print("რიცხვების ჯამი:", sum_of_numbers(numbers))


# 3)
def average_of_numbers(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


numbers = [10, 20, 30, 40, 50]
print("რიცხვების საშუალო:", average_of_numbers(numbers))

# 4)
def even_or_odd():
    number = int(input("შეიყვანეთ რიცხვი: "))
    if number % 2 == 0:
        print(f"{number} არის ლუწი რიცხვი.")
    else:
        print(f"{number} არის კენტი რიცხვი.")


even_or_odd()

# 5)
def time_travel():
    current_age = int(input("შეიყვანეთ თქვენი ახლანდელი ასაკი: "))
    current_year = int(input("შეიყვანეთ ამჟამინდელი წელი: "))
    travel_years = int(input("რამდენი ხნით სურთ დროში მოგზაურობა? "))
    direction = input("მომავალში (future) თუ წარსულში (past) სურთ მოგზაურობა? ")

    if direction.lower() == "future":
        future_year = current_year + travel_years
        future_age = current_age + travel_years
        print(f"წარმატებით მოგზაურობთ მომავალში! წელი იქნება {future_year}, თქვენი ასაკი კი {future_age}.")
    elif direction.lower() == "past":
        past_year = current_year - travel_years
        past_age = current_age - travel_years
        print(f"წარმატებით მოგზაურობთ წარსულში! წელი იქნება {past_year}, თქვენი ასაკი კი {past_age}.")
    else:
        print("არასწორი მიმართულება. გთხოვთ, აირჩიოთ 'future' ან 'past'.")


time_travel()





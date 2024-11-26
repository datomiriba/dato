#   5) შექმენით რიცხვებით სავსე სია რომელშიც იქნება 1 დან 20 მდე ყველა რიცხვი, შემდეგ კი ამ სიიდან ამოშალეთ ყველა კენტი რიცხვი და დაამატეთ ახალ სიაში, ორივე სია დაბეჭდეთ


numbers = list(range(1, 21))


odd_numbers = []


for num in numbers[:]:
    if num % 2 != 0:  
        odd_numbers.append(num)
        numbers.remove(num)  


print( numbers)
print( odd_numbers)

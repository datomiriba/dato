# შექმენით ორი სია ერთში თქვენი ხელით ჩაწერეთ ლუწი რიცხვები, მეორეში კენტი რიცხვები შემდეგ კი ეს ორი სია გააერთიანეთ extend ის გამოყენებით 

even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


odd_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


even_numbers.extend(odd_numbers)


print(even_numbers)
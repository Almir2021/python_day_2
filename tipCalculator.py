#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = input("what was the total bill?  $")
tip = input("what percentage tip wouls you like to give? 10, 12, or 15? ")
people = input("how many people to split the bill?")
   
bill = float(bill)
tip = int (tip)
people = int (people)

tip2 = tip/100
   
 
result = ((bill/people) + ((bill*(tip2)/people)))

res = "{:.2f}" . format(result)
 
print(res)




"""
To start, we will generate a random intefer between 1 and 20, and
based on the result of the random number, we check to see if it fails under certain range
if the number is greater than 15, then the result will be "Cherries"
otherwise if the number is > 10, then the result will be "Orange"
otherwise if the number is > 5, then the result will be "Plum"
otherwise if the number is > 2, then the resul twill be "Melon"
otherwise if the number is > 1, then the result will be "Bell"
if the number is not any of the above, then the result will be "Bar"

we iterate over using a loop three times and print the results to the user. As an example "Plum Cherries"

"""

"""
import random
num = generate random number

if num is greater than 15,
  then the result will be "Cherries"
otherwise if num is > 10,
  then the result will be "Orange"
otherwise if num is > 5,
  then the result will be "Plum"
otherwise if num is > 2, 
  then the result will be "Melon"
otherwise if num is > 1, 
  then the result will be "Bell"
otherwise
  the result will be "Bar"

loop three times
  print the output (fruit) to the user

"""
import random
total_earned = 0 
def main(total_earned):
  results = []
  for i in range(0, 3):
    results.append(spin())
  print("results", results)
  winner = jackpot(results)

  if(winner):
    print("Winner! You Win")
  else:
    print("Sorry try again!")

  grand_total = count(results, total_earned)
  print("grand_total", grand_total)
  option = input("Play again? ")
  if option.lower() == "y" or option.lower() == "yes":
    main(total_earned)

def spin():
  rand_num = random.randint(1, 20)
  output = ""
  if(rand_num > 15):
    output = "Cherries"
  elif(rand_num > 10):
    output = "Orange"
  elif(rand_num > 5):
    output = "Plum"
  elif(rand_num > 2):
    output = "Bell"
  elif(rand_num > 1):
    output = "Melon"
  else:
    output = "Bar"
  print(output, end=" ")
  return output

def jackpot(results):
  return results[0] == results[1] == results[2]

def count(results, total_earned):
  total = 0
  money_dict = {
    "Cherries": 1,
    "Orange": 7,
    "Plum": 6,
    "Bell": .4,
    "Melon": .2,
    "Bar": .1
  }

  for i in results:
    total += money_dict[i]
  return total_earned + total
  
main(total_earned)
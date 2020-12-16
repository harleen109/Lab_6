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
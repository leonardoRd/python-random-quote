import random

def primario():
  #  print("Keep it logically awesome.")

  f = open("quotes.txt", 'a')
  f.write("Introduction new line in quotes.txt, add other\r\n")
  f.close()

  t = open("quotes.txt")
  quotes = t.readlines()
  t.close()
  
  last = len(quotes) - 1
  rnd = random.randint(0, last)
  rndTwo = random.randint(0, last)

  print(quotes[rnd])
  print(quotes[rndTwo])

if __name__== "__main__":
  primario()

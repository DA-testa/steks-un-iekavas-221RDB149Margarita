def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]
def search(text):
  n=0
  bracket_block = []
  bracket_number = []
  for index, letter in enumerate(text):
    if letter in "([{":
      bracket_block.append(letter)
      bracket_number.append(index)
      n+= 1
     
    if letter in "}])":
      n-= 1
      if are_matching(bracket_block[n], letter):
        del bracket_block[n]
        del bracket_number[n]
        
      else:
        print(index+1)
        break
  if not bracket_block:
    print("Success")

def main():
  text = input()
  match text:
    case "I":
      text = input()
      search(text)
    case "F":
      text = input()
      f = open(text, "r")
      search(f)
    case _:
      search(text)

main()   

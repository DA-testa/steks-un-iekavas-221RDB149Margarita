from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]
def search(text):
  
  bracket_block = []

  for index, letter in enumerate(text):
    if letter in "([{":
      bracket_block.append(Bracket(letter, index))

     
    if letter in "}])":
     if not bracket_block:
       return index+1
     last = bracket_block.pop()
     
     if are_matching(last.char, letter):
          del bracket_block[-1]
     else:
        print(index+1)
        break
  
  if not bracket_block:
      print("Success")
def main():
  text = input().upper();
  match text:
    case "F":
      print("enter filename")
      text = input()
      f = open(text, "r")
      search(f)
    case _:
      print("enter text below")
      text = input()
      search(text)

main()   

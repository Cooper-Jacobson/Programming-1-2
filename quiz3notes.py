text = input("Enter text: ")
for index in range(len(text)):
  print(text[index], end=" ")
print()
numwords = 0
for letter in text:
    if letter == " ":
    numwords = numwords + 1
  print(letter)
def main():
  text = "cool beans"
  print("In main: " + text)

main()
print("After main: " + text)
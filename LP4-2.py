def main():
  weight = int(input("Enter package weight in kilograms: "))
  length = int(input("Enter package length in centimeters: "))
  width = int(input("Enter package width in centimeters: "))
  height = int(input("Enter package height in centimeters: "))

  if weight > 27:
    print("Too heavy")
  elif length > 0.1:
    print("Too large")
  elif width > 0.1:
    print("Too large")
  elif height > 0.1:
    print("Too large")
  elif weight > 27 and length > 0.1:
    print("Too heavy and too large")
  pass


if __name__ == "__main__":
  main()
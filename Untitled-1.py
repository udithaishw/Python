

while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  


  if choice == "+":
    number_1=input("Enter frist number: ")
    number_2=input("Enter frist number: ")
    varr_add=int(number_1)+int(number_2)
    print(float(number_1)+"+"+float(number_2)+"="+float(varr_add))
  
  elif choice == "-":
    number_1=input("Enter frist number: ")
    number_2=input("Enter frist number: ")
    varr_add=int(number_1)-int(number_2)
    print(float(number_1)+"-"+float(number_2)+"="+float(varr_add)) 
  
  elif choice == "*":
    number_1=input("Enter frist number: ")
    number_2=input("Enter frist number: ")
    varr_add=int(number_1)*int(number_2)
    print(float(number_1)+"*"+float(number_2)+"="+float(varr_add))
    
  elif choice == "#":
    print("Done. Terminating")
    exit()
    

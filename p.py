en=str(input("Enter the Employer Name: "))
bs=int(input("Enter the Basic Sallery: "))
ba=int(input("Enter the Budgetary Allowance: "))
ot=int(input("Enter the OT Hours: "))
otp=130
ts=bs+ba+(ot*otp)
ts=int(ts)
print(en,"'s This month SALLRY is Rs ",ts)

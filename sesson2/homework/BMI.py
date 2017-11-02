print("Chi so BMI cua ban ")
chieucao = float(input("nhap chieu cao (don vi met): "))
cannang = float(input("nhap can nang: "))

BMI = cannang / (chieucao * chieucao)
print("Chi so BMI cua ban la: ", BMI)

if BMI < 16:
    print("severly")
elif BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("normal")
elif BMI < 30:
    print("Overweight")
else:
    print("obese")            

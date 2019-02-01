s = float(input("実数 s を入力: "))
t = float(input("実数 t を入力: "))

print()

sum = s + t
rem = s - t
prod = s * t

isWarned = False
isZeroDivide = False

if t == 0:
    print("ゼロ除算をスキップします");
    isWarned = True
    isZeroDivide = True
else:
    div = s / t

if int(sum) >= 100000 or int(sum) <= -10000:
    print("指定された桁数を超えています: s + t")
    isWarned = True

if int(rem) >= 100000 or int(rem) <= -10000:
    print("指定された桁数を超えています: s - t")
    isWarned = True

if int(prod) >= 100000 or int(prod) <= -10000:
    print("指定された桁数を超えています: s * t")
    isWarned = True

if isZeroDivide == False:
    if int(div) >= 100000 or int(div) <= -10000:
        print("指定された桁数を超えています: s / t")
        isWarned = True

if isWarned:
    print()
    
print("a + b = %10.4f" %sum)
print("a - b = %10.4f" %rem)
print("a × b = %10.4f" %prod)

if isZeroDivide == False:
    print("a ÷ b = %10.4f" %div)
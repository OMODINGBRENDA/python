math=input("input maths")
english=input("input english")
kiswahili=input("input kiswahili")
science=input("input science")
total=(math+english+kiswahili+science)
average=(total/4)
print(total)
print(average)
if math or english or kiswahili or science > 100:
    print("invalid input A")
if math or english or kiswahili or science < 0:
    print("invalid input B")
if average > 70:
    print("your score is A")
elif average > 60 < 71:
    print("your score is B")
elif average > 50 < 61:
    print("your score is c")
elif average > 40 > 51:
    print("your score is D")
elif average < 40:
    print("your score is E")
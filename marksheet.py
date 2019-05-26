
mark1 = float(input("Please enter Maths's marks "))
mark2 = float(input("Please enter English's marks "))
mark3 = float(input("Please enter Physics's marks "))
mark4 = float(input("Please enter Chemistry's marks "))
mark5 = float(input("Please enter Computer's marks "))

total = mark1+mark2+mark3+mark4+mark5
average = total/5

if(average>=91.0 and average<=100.0):
    print("Your Grade is A+");
elif(average>=81.0 and average<=90.0):
    print("Your Grade is A");
elif(average>=71.0 and average<=80.0):
    print("Your Grade is B+");
elif(average>=61.0 and average<=70.0):
    print("Your Grade is B");
elif(average>=51.0 and average<=60.0):
    print("Your Grade is C+");
elif(average>=41.0 and average<=50.0):
    print("Your Grade is C");
elif(average>=0.0 and average<=40.0):
    print("Your Grade is F");
else:
    print("Strange Grade..!!");  
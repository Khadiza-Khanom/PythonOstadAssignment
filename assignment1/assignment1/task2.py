a=1;
while a==1:
    number1=int(input("Enter first number: "))
    number2=int(input("Enter second number: "))
    operator=input("Enter any operator (+,-,*,/): ")
    while a==1:
        if( operator == '+' or  operator  == '-' or operator  == '*' or operator  == '/' ):
            if operator=='+':
                print(number1+number2)
                break
            if operator=='-':
                print(number1-number2)
                break
            if operator=='*':
                print(number1*number2)
                break
            if operator=='/':
                print(number1/number2)
                break
            
            
        else:
            operator=input("Enter a valid operator (+,-,*,/): ")
            continue

    print("do you want to continue?")
    action=input( "yes / no: ")
    if action=='yes':
        continue
    else:
        break
    






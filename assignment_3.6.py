print("My Student ID is JaiHea8080")
 
 
def functionTwo():
    num1 = float(input("Please enter a number: "))
    num2 = float(input("Please enter a number: "))
    theSum = num1 + num2
    print(f"The sum of {int(num1)} and {int(num2)} is {int(theSum)}.")
    return theSum
 
 
def functionThree(theSum):
    if theSum > 5:
        print("The sum is greater than 5.")
    else:
        print("The sum is 5 or less.")
    return 8080
 
 
def main():
    functionOne()                               
    returnedSum = functionTwo()             
    studentIdNum = functionThree(returnedSum)   
    print(f"functionThree returned the value of {studentIdNum}.")  
 
 
main()

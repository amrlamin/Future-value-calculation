def main():
    principal = int(input("Enter principal:"))
    interestRate = int(input("Enter interest rate (as %):"))
    numYears = int(input("Enter number of years:"))
    investFutureValue(principal, interestRate, numYears)

def investFutureValue(principal, interestRate, numYears):
   futureValue = principal * ((1 + (interestRate / 100)) ** numYears)
   print("Future value: ${0:,.2f}".format(futureValue))

main()

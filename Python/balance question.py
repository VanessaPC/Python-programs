def creditCard (balance, annualInterestRate):
    
    updatedBalance = balance
 
    highMP = balance
    minimunMP = 0
        
    for m in range (0, 12): 
                
        
        while (guess - balance) >= 0:
            m += 1
            
            monthlyInterestRate = annualInterestRate / 12.0 
        
            unpaidBalance = previousBalance - minimunMP
        
            updatedBalance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
            
            minimunMP = guess
            
            guess = (highMP + minimunMP) / 2.0
            
            if guess < balance:
                minimunMP = guess
            else:
                highMP = guess
            guess = (minimunMP + highMP)/2.0
            balance -= guess
            
        print('Test case: ' + str(m))
        print('Balance: ' + str(round(balance)))
        print('Annual Interest Rate: ' + str(round(minimunMP)))
        
 
creditCard (3329, 0.2)
def creditCard (balance, annualInterestRate):
    
    updatedBalance = balance
    guess = 0
    monthlyInterestRate = annualInterestRate / 12 
    monthlyPaymentLowerBound = balance / 12
    monthlyPaymentUpperBound = (balance * (1 + monthlyInterestRate)**12)/12.0
    epsilon = 0.01
    while abs(updatedBalance) >= epsilon:
        
        updatedBalance = balance
        guess = (monthlyPaymentUpperBound + monthlyPaymentLowerBound) / 2
    
        for m in range (0, 12): 
            
            m +=1 
                        
            minimunMonthlyPayment = guess
            
            unpaidBalance = updatedBalance - minimunMonthlyPayment
            
            updatedBalance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
            
        
        if updatedBalance > 0:
            
            monthlyPaymentLowerBound = guess
             
        else :
            
            monthlyPaymentUpperBound = guess
            
                
                
    print 'Lowest Payment:' + str(round(guess, 2))
    
creditCard (999999, 0.18)
print('\33c')

principle = 103208.56
interest_rates = [.103, .067, .099, .10]
total_interest=0
print(f"Principal: ${principle:,.2f} \n")
for rate in interest_rates:
    interest = rate * principle
    total_interest=total_interest+interest
    print(f"Your interest with {rate:.2f}% will be: ${interest:,.2f}")
print(f"\n The total interest you would pay is {total_interest:,.2f} \n")
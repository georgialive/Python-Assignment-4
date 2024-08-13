# Name: Georgia Vrana
# Date Submitted: Friday, March 1st, 2024
# Assignment-3: Savings
# Description: The program `savings.py` The program calculates daily changes in the balances
#              of two individuals to determine who reaches their financial goal first, completing
#              in 4 days with Jane saving $50 before Sara spends down to $50.

sarah_spender = 100
jane_saver = 27
days = 0

while sarah_spender > 50 and jane_saver < 50:
    sarah_spender -= 11  # Sarah spends $11 each day
    jane_saver += 7      # Jane earns $7 each day
    days += 1            # Increment days

if sarah_spender <= 50:
    print(f"Sara spent down to $50 before Jane reached her goal. It took {days} days.")
elif jane_saver >= 50:
    print(f"Jane reached a savings of $50 before Sara spent down to $50. It took {days} days.")


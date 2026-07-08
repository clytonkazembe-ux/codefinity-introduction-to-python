start_number = 5
current_number=start_number
countdown_values = []

while current_number>0:
    countdown_values.append(current_number)
    print(f"Countdown: {current_number}")
    current_number-=1

else:
    print("Discount countdown complete!")
    print("Countdown values:", countdown_values)
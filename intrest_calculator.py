#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: May 12, 2025
# This code calculates the user interest


def InterestCalculator(p, r, t, amt_of_t):
    # Calculates intrest based on what the time range is
    if t == "years":
        interest = p * r * amt_of_t * 0.01
    if t == "months":
        interest = p * r * (amt_of_t / 12) * 0.01
    if t == "days":
        interest = p * r * (amt_of_t / 365) * 0.01
    return interest


def main():
    # Greets user
    print("Hello! Welcome to Jayden’s interest calculator")

    # Ensures that if given erroneous it will loop back to get the user input
    while True:
        principal = input("What is your starting amount (principal): ")
        rate = input("What is your your rate (%)? ")
        time = input("Please enter the range of time (years, months, days) ")

        # Make sure that the time range is valid
        if (time == "years") or (time == "months") or (time == "days"):
            # Get the amount of time passed
            amount_of_time = input("How long has it been since you made this deposit?")
            
            # Try catch the numerical data and convert  them to floats
            try:
                principal_float = float(principal)
                try:
                    rate_float = float(rate)
                    try:
                        amount_of_time_float = float(amount_of_time)

                        # Checks if the numbers are negative
                        if rate_float <= 0:
                            print(" Your rate cannot be negative or 0!")
                        elif amount_of_time_float < 0:
                            print("Your amount of time cannot be negative!")
                        # Ask about if principal can be negative

                        # If everything is right the loop is broken
                        else:
                            break

                    # All the exceptions for if the converstion goes wrong
                    except Exception:
                        print(amount_of_time, " is not a float!")
                except Exception:
                    print(rate, " is not a float!")
            except Exception:
                print(principal, " is not a float!")
        # If the time range isnt any of the ones listed this happens
        else:
            print("Please enter a valid time range!")
    # Call function
    interest = InterestCalculator(
        principal_float, rate_float, time, amount_of_time_float
    )

    # Displayed how much earned and total amount
    print(
        "The amount that you have earned in",
        (amount_of_time_float),
        (time),
        "given your original",
        (principal_float),
        "deposit is",
        (interest),
        "$. Making your total amount",
        (interest + principal_float),
        "$",
    )


if __name__ == "__main__":
    main()

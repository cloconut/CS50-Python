def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    print(d.replace("$", " "))


def percent_to_float(p):
    # TODO
    print(p)


main()

#which should accept a str as input
    # (formatted as $##.##, wherein each # is a decimal digit), remove
    # the leading $, and return the amount as a float.
    # For instance, given $50.00 as input, it should return 50.0.
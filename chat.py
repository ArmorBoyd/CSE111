def main():
    start = float(input("Enter the starting odometer value in miles: "))
    end = float(input("Enter the ending odometer value in miles: "))
    fuel = float(input("Enter the amount of fuel in gallons: "))
    mpg = miles_per_gallon(start, end, fuel)
    lp100k = lp100k_from_mpg(mpg)
    print("Fuel efficiency:")
    print("- Miles per gallon: {:.2f}".format(mpg))
    print("- Liters per 100 kilometers: {:.2f}".format(lp100k))

def miles_per_gallon(start, end, fuel):
    return (end - start) / fuel

def lp100k_from_mpg(mpg):
    kpl = mpg * 0.425144
    lp100k = 100 / kpl
    return lp100k

if __name__ == "__main__":
    main()
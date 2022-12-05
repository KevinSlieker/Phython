def read_int(prompt, min, max):
    while True: 
        try: 
            number = int(input(prompt))
            assert number > min
            assert number < max
            return number
        except (ValueError):
            print("Error: wrong input")
        except AssertionError:
            print("Error: the value is not within permitted range (" , min,  ".." , max, ")")


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)

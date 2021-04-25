def fizz_buzz(n):
    for fizz_buzz in range(n+1):
        if fizz_buzz % 3 == 0 and fizz_buzz % 5 == 0:
            print("fizzbuzz")
            continue
        elif fizz_buzz % 3 == 0:
            print("fizz")
            continue
        elif fizz_buzz % 5 == 0:
            print("buzz")
        print(fizz_buzz)

fizz_buzz(26)

if __name__ == "__main__":
    fizz_buzz(100)
    # FizzBuzz is a children’s game where
    # you count from 1 to 20. Easy, right?

    # Here’s the catch: instead of saying
    # numbers divisible by 3, say “Fizz”.
    # And instead of saying numbers
    # divisible by 5, say “Buzz”. For
    # numbers divisible by both 3 and 5, say
    # “FizzBuzz”.

    # “1, 2, Fizz, 4, Buzz”…and so forth

    # But don’t type out the numbers in
    # order—find a more awesome way!

for i in range(100):
    div_3 = i % 3 == 0
    div_5 = i % 5 == 0
    if div_3 and div_5:
        print("FizzBuzz")
    elif div_3:
        print("Fizz")
    elif div_5:
        print("Buzz")
    else:
        print(i)
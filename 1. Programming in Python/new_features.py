"""New Features in Python"""


# The Match-Case Statement
# The match statement In Python was introduced in version 3.10 using the match statement you can achieve cleaner more readable code that allows all the same functionality as the if controlled statement.
# The match statement compares a value to several different conditions until one of these conditions is met.


def print_http_status(http_status: int) -> None:
    """Function printing http sttus."""

    match http_status:
        case 200 | 201:  # Combining
            print("Success")
        case 400:
            print("Bad request")
        case 500 | 501:
            print("Server Error")
        case _:  # Default if nothing is found in the case
            print("Unkown status")


print_http_status(200)


# Unpacking a function using positional argument
# This method is very useful while printing your data in a raw format (without any comma and brackets ). Many of the programmer try to remove comma and bracket by using a convolution of functions, Hence this simple prefix asterisk can solve your problem in unpacking them.

list_numbers = [1, 2, 3, 4, 5]
print(list_numbers)  # list_numbers: [1, 2, 3, 4, 5]
print(*list_numbers)  # *list_numbers: 1 2 3 4 5


# args and also kwargs, or keyword args. Using these has the advantage that you could pass in any amounts of non-keyword variables, and keyword arguments


def get_sum_of_numbers(*args: int) -> int:
    """Function returning sum of the given numbers as *args"""

    sum_of_numbers = 0

    for number in args:
        sum_of_numbers += number

    return sum_of_numbers


print(get_sum_of_numbers(1, 2, 3, 5))


def get_sum_of_fruits_price(**kwargs: int) -> int:
    """Function returning sum of the price of the given fruits as **kwargs"""

    sum_of_fruits_price = 0

    for fruit, price in kwargs.items():
        sum_of_fruits_price += price
        print("fruit:", fruit, ", price:", price)

    return sum_of_fruits_price


print(get_sum_of_fruits_price(mango=1, strawberry=2, banana=1))

""" The Match-Case Statement """

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


# Unpacking a function using positional argument.
# This method is very useful while printing your data in a raw format (without any comma and brackets ). Many of the programmer try to remove comma and bracket by using a convolution of functions, Hence this simple prefix asterisk can solve your problem in unpacking them.

list_numbers = [1, 2, 3, 4, 5]
print(list_numbers)  # list_numbers: [1, 2, 3, 4, 5]
print(*list_numbers)  # *list_numbers: 1 2 3 4 5

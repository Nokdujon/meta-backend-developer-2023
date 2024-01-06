"""New Features in Python"""


def match_case() -> None:
    """The Match-Case Statement
    The match statement In Python was introduced in version 3.10 using
    the match statement you can achieve cleaner more readable code that allows
    all the same functionality as the if controlled statement.

    The match statement compares a value to several different conditions
    until one of these conditions is met.
    """

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


def pure_function() -> None:
    """Function A pure function is a function that does not change or
    have any effect on a variable, data, list, or sets beyond its own scope."""

    numbers: list = [1, 2, 3]
    print("numbers =", numbers)  # [1, 2, 3]

    def add_to(item: int) -> list:
        """Function it changes the numbers by appending the item which
        is passed as an argument."""
        numbers.append(item)
        return numbers

    print("add_to(4) =", add_to(4))  # [1, 2, 3, 4]
    print("numbers =", numbers)  # [1, 2, 3, 4]

    def add_to_pure_function(lst: list, item: int) -> list:
        """Function a pure function, you need to think how to extend
        the function to accept a list as an argument, add the item to
        the list without modifying the original list, and how to return
        a new list with the newly added item.

        The solution is to create a new list and copy or clone the data from
        the original list."""

        new_numbers: list = lst.copy()
        new_numbers.append(item)
        return new_numbers

    print(
        "add_to_pure_function(numbers, 5) =", add_to_pure_function(numbers, 5)
    )  # [1, 2, 3, 4, 5]
    print("numbers =", numbers)  # 1, 2, 3, 4]

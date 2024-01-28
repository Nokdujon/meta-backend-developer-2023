names: list[str] = ["Al", "Bo", "Chi", "Ma"]


def is_present(person: list[str]):
    return True if person in names else False


def is_alphabet(person: list[str]):
    return True if person.isalpha() else False

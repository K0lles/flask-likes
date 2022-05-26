def processing_likes(name_list: list):
    """Returns the string with information about people who liked post"""
    try:
        # checking if name_list has any names
        if not name_list:
            return f"Это никому не нравится.", False

        # checking if name_list is list
        if not isinstance(name_list, list):
            return f"Требуеться list", True

        if len(name_list) >= 1:

            if not list_with_letters(name_list):
                return f"Не алфавитный символ обнаружен в имени.", True

            if not list_in_range(name_list):
                return f"Слишком длинные имена.", True

            if len(name_list) == 1:
                return f"{name_list[0]} лайкнул это", False

            elif len(name_list) == 2:
                return f"{name_list[0]} и {name_list[1]} лайкнули это.", False

            elif len(name_list) == 3:
                return f"{name_list[0]}, {name_list[1]} и {name_list[2]} лайкнули это.", False

            else:
                return f"{name_list[0]}, {name_list[1]} и ещё  {len(name_list) - 2} лайкнули это.", False

    except TypeError:
        return f"Функция принимает только list", True


def list_with_letters(name_list: list):
    """Checks if list objects contains only letters and spaces"""
    try:
        for name in name_list:
            # checking if the letter in word is alphabet sign
            for letter in name:
                if not letter.isalpha():
                    return False
        return True
    except TypeError:
        return f"Что-то пошло не так"


def list_in_range(name_list: list):
    """Checks if list objects have less than 10 symbols"""
    for name in name_list:
        if len(name) > 10:
            return False
    return True

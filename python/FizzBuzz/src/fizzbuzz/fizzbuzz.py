def get_message(value: int) -> str:
    result = ""

    if value % 3 == 0:
        result += "Fizz"
    
    if value % 5 == 0:
        result += "Buzz"

    if not result:
        result = f"{value}"

    return result
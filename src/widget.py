# src/utils/widget.py
from src.mask import get_mask_card_number
from src.mask import get_mask_account


def mask_account_card(info: str) -> str:
    """Функция маскирует номер карты или счета,
    основываясь на типе
    """
    parts = info.split()
    if len(parts) < 2:
        return "Некорректный ввод."

    type_info = " ".join(parts[:-1])
    number = parts[-1]

    if type_info.lower() in ["visa", "mastercard", "maestro"]:
        masked_number = get_mask_card_number(number)
    elif type_info.lower() == "счет":
        masked_number = get_mask_account(number)
    else:
        return "Неизвестный тип."

    return f"{type_info} {masked_number}"

print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("Unknown Type 1234567890"))

from datetime import datetime


def get_date(date_string: str) -> str:
    """
    Преобразует строку с датой в формат ДД.ММ.ГГГГ..
    """
    date_obj = datetime.fromisoformat(date_string)

    formatted_date = date_obj.strftime("%d.%m.%Y")

    return formatted_date

masked_account = input()
masked_number = input()


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты, оставляя видимыми только первые 6 и последние 4 цифры.
    """
    card_number = card_number.replace(" ", "")
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Некорректный номер карты. Должен содержать 16 цифр.")

    masked_number = f"{card_number[:6]} {card_number[6:8]}** **** {card_number[-4:]}"
    return masked_number


print(masked_account)


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета, оставляя видимыми только последние 4 цифры.
    """
    if len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Некорректный номер счета. Должен содержать как минимум 4 цифры.")

    masked_account = f"**{account_number[-4:]}"
    return masked_account


print(masked_number)

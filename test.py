number = int(input("Введите число: "))
text = ""
for digit, value in enumerate(str(number), start=1):
    value = int(value)

    if digit == 1:

        if value == 1:
            text += "сто "
        elif value == 2:
            text += "двести "
        elif value == 3:
            text += "триста "
        elif value == 4:
            text += "четыреста "
        elif value == 5:
            text += "пятьсот "
        elif value == 6:
            text += "шестьсот "
        elif value == 7:
            text += "семьсот "
        elif value == 8:
            text += "восемьсот "
        elif value == 9:
            text += "девятьсот "

    elif digit == 2 and value ==

    elif digit == 2:
        if value == 1:
            text += "десять "
        elif value == 2:
            text += "двадцать "
        elif value == 3:
            text += "тридцать "
        elif value == 4:
            text += "сорок "
        elif value == 5:
            text += "пятьдесят "
        elif value == 6:
            text += "шестьдесят "
        elif value == 7:
            text += "семьдесят "
        elif value == 8:
            text += "восемьдесят "
        elif value == 9:
            text += "девяносто "

    elif digit == 3:
        if value == 1:
            text += "один"
        elif value == 2:
            text += "два"
        elif value == 3:
            text += "три"
        elif value == 4:
            text += "четыре"
        elif value == 5:
            text += "пять"
        elif value == 6:
            text += "шесть"
        elif value == 7:
            text += "семь"
        elif value == 8:
            text += "восемь"
        elif value == 9:
            text += "девять"

print(text)

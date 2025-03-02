def number_to_words(n):
    ones = [
        "", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять",
        "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
        "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"
    ]
    
    tens = [
        "", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", 
        "семьдесят", "восемьдесят", "девяносто"
    ]
    
    hundreds = [
        "", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", 
        "семьсот", "восемьсот", "девятьсот"
    ]
    
    if n == 0:
        return "ноль"
    
    if n < 1 or n > 1000:
        return "Число вне диапазона"

    word = ""
    if n >= 100:
        word += hundreds[n // 100] + " "
        n %= 100

    if n >= 20:
        word += tens[n // 10] + " "
        n %= 10

    if n > 0:
        word += ones[n] + " "
    
    return word.strip()

input_number = int(input("Введите число от 1 до 1000: "))
result = number_to_words(input_number)
print(result)
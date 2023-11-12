# TODO  Напишите функцию count_letters

def count_letters(text):
    dict_count = {}
    little_symb = text.lower()
    for symbol in little_symb:
        if symbol.isalpha():
            if symbol in dict_count:
                dict_count[symbol] += 1
            else:
                dict_count[symbol] = 1
    return dict_count

# TODO Напишите функцию calculate_frequency

def calculate_frequency(dict_count):

    letters_frequency = {}
    letters_amount = 0
    for letter_amount in dict_count.values():
        letters_amount += letter_amount
    for letter, amount in dict_count.items():
        letter_frequency = amount / letters_amount
        letters_frequency[letter] = letter_frequency
    return letters_frequency

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте

result_count = count_letters(main_str)

for key, value in calculate_frequency(result_count).items():
    print(f"{key}: {value:.2f}")



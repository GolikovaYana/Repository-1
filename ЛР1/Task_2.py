# TODO Найдите количество книг, которое можно разместить на дискете
inf = 1.44 #Мб
page = 100
n_str = 50
symb = 25
inf_symb = 4 #байт

inf_2 = inf* 1024 ** 2

inf_book = page * n_str * symb * inf_symb
n_book = int(inf_2 // inf_book)
print("Количество книг, помещающихся на дискету:", n_book)

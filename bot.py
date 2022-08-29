from random import *
films=[]
films.append("Матрица")
films.append("Солярис")
films.append("Властелин колец")
films.append("Техасская резня бензопилой")
films.append("Санта Барбара")
while True:
    command=input("Введите команду ")
    if command=="/start":
        print("Бот-фильмотека начал свою работу")
    elif command=="/stop":
        print("Бот остановил свою работу. Заходите еще, будем рады!")
        break
    elif command=="/all":
        print("Вот текущий список фильмов")
        print(films)
    elif command =="/add":
        f=input("Введите название фильма ")
        films.append(f)
        print("Фильм был успешно добавлен в коллекцию!")
    elif command=="/help":
        print("здесь какой-то манул")
    elif command=="/delete":
        f=input("Введите название фильма, который надо удалить ")
        films.remove(f)
        print("Фильм был успешно удален!")
    else:
        print("Неопознанная команда. Просьба погладить манула через /help")

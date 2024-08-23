print(
    'Это викторина на знание кухни разных народов. Ответь на вопросы и узнай, насколько хорошо ты разбираешься в еде!'
)

question1 = "Кто придумал эчпочмак?"

question2 = "Луковый суп — это блюдо какой кухни?"

question3 = "Где родина начос?"

question4 = "Как называются китайские пельмени?"

question5 = "В национальную кухню какой страны входят драники?"

question6 = "В какой стране придумали пасту карбанару?"

question7 = "Какой орех считается самым дорогим в мире?"

question8 = "Популярное блюдо венской кухни?"

question9 = "Где распологаутся самый дорогой ресторан в мире?"

question10 = "Какой самый популярный десерт в России?"

true_answer1 = "татары"

true_answer2 = "Франция"

true_answer3 = "Мексика"

true_answer4 = "гёдза"

true_answer5 = "Беларусь"

true_answer6 = "Италия"

true_answer7 = "Макамедия"

true_answer8 = "Шницель"

true_answer9 = "Ибица"

true_answer10 = "торт напалеон"

score = 0

answer1 = input(question1)

if answer1 == true_answer1:

    score += 1

answer2 = input(question2)

if answer2 == true_answer2:

    score += 1

answer3 = input(question3)

if answer3 == true_answer3:

    score += 1

answer4 = input(question4)

if answer4 == true_answer4:

    score += 1

answer5 = input(question5)

if answer5 == true_answer5:

    score += 1

answer6 = input(question6)

if answer6 == true_answer6:

    score += 1

answer7 = input(question7)

if answer7 == true_answer7:

    score += 1

answer8 = input(question8)

if answer8 == true_answer8:

    score += 1

answer9 = input(question9)

if answer9 == true_answer9:

    score += 1

answer10 = input(question10)

if answer10 == true_answer10:

    score += 1

if score >= 5:

    print("Вы набрали много баллов! Вас можно считать экспертом")

else:

    print(
        "Вы набрали не очень много баллов. Расширяйте свой кругозор, вам есть, куда стремиться"
    )

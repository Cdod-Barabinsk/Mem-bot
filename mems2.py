import turtle
import time
import random

# Инициализация экрана
screen = turtle.Screen()
player = turtle.Turtle()
player.shape("square")  # Форма игрока
player.color("red")  # Цвет игрока
player.penup()  # Игрок не оставляет след

# Координаты начала и конца уровня
start_x = -300
start_y = -300
end_x = 300
end_y = -300

# Создание противников
enemy = turtle.Turtle()
enemy.shape("triangle")  # Форма противника
enemy.color("blue")  # Цвет противника
enemy.penup()  # Противник не оставляет след
enemy.setposition(-200, 0)  # Начальная позиция противника

# Функция движения игрока
def move():
    global lives
    if player.xcor() >= start_x and player.xcor() <= end_x and player.heading() == 0:  # Если игрок достиг конца
        player.setposition(start_x, player.ycor())
    elif player.xcor() <= -start_x and player.xcor() >= -end_x and player.heading() == 180:  # Если игрок вернулся к началу
        player.setposition(end_x, player.ycor())
        player.setheading(0)
    elif player.ycor() >= start_y and player.ycor() <= end_y and player.heading() == 90:  # Если игрок достиг конца
        player.setposition(player.xcor(), start_y)
        player.setheading(0)
    elif player.ycor() <= -start_y and player.ycor() >= -end_y and player.heading() == 270:  # Если игрок вернулся к началу
        player.setposition(player.xcor(), end_y)
        player.setheading(0)
    else:
        player.forward(5)  # Движение игрокаaa

# Функция создания противников
def create_enemies():
    enemy.setposition(random.randint(-300, 300), random.randint(-300, 300))

# Функция обновления игры
def update():
    global lives
    move()
    create_enemies()
    screen.ontimer(update, 200)  # Увеличиваем скорость игры

# Запуск игры
lives = 3
update()
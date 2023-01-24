from turtle import Turtle, Screen
import random
soop = Turtle()
display = Screen()
soop.pensize(8)
soop.screen.colormode(255)
soop.speed("fastest")
soop.hideturtle()
start_pos = -375
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184),
              (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
              (27, 68, 102), (12, 70, 64), (107, 127, 153),(176, 192, 208), (168, 99, 102)]


def draw_row(running, position):
    if running <= 14:
        soop.penup()
        soop.setpos(-485, position)
        for _ in range(0, 13):
            dot_color = random.choice(color_list)
            soop.pencolor(dot_color)
            soop.penup()
            soop.forward(37)
            soop.dot(25)
            soop.forward(37)
        position += 53
        running += 1
        draw_row(running, position)


draw_row(0, start_pos)
display.exitonclick()

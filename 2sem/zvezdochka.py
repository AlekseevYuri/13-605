import turtle as tl
def draw_fractal(scale):
    if scale >= 25:
        draw_fractal(scale/3)
        tl.left(60)
        draw_fractal(scale/3)
        tl.right(120)
        draw_fractal(scale/3)
        tl.left(60)
        draw_fractal(scale/3)   
    else:
        tl.forward(scale)
scale = 500
tl.pensize(2)
tl.penup()
tl.forward(-200)
tl.left(90)
tl.forward(110)
tl.right(90)
tl.pendown()
draw_fractal(scale)
tl.right(120)
draw_fractal(scale)
tl.right(120)
draw_fractal(scale)
tl.right(120)

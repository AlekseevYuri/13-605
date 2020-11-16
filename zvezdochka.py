import turtle as tl
def draw_fractal(scale):
    if scale >= 1:
        draw_fractal(scale/3)
        tl.left(60)
        draw_fractal(scale/3)
        tl.right(120)
        draw_fractal(scale/3)
        tl.left(60)
        draw_fractal(scale/3)
    else:
        tl.forward(scale)
scale = 200
tl.pensize(2)
draw_fractal(scale)
tl.right(120)
draw_fractal(scale)
tl.right(120)
draw_fractal(scale)
tl.right(120)

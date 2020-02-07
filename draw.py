from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x = int(x0)
    y = int(y0)
    A = y1 - y
    B = -1 * (x1 - x)
    d = 2 * A + B
    while x <= x1:
        plot (screen, color, x, y)
        if d > 0:
            y = y + 1
            d = d + 2 * B
        x = x + 1
        d = d + 2 * A
    d = A + 2 * B
    while y <= y1:
        plot (screen, color, x, y)
        if d < 0:
            x = x + 1
            d = d + 2 * A
        y = y + 1
        d = d + 2 * B
    # d = 2A + B
    # while x <= x1:
    #     plot (x, y)
    #     if d > 0:
    #         y = y + 1
    #         d = d + 2B
    #     x = x + 1
    #     d = d + 2A
    # d = 2A + B
    # while x <= x1:
    #     plot (x, y)
    #     if d > 0:
    #         y = y + 1
    #         d = d + 2B
    #     x = x + 1
    #     d = d + 2A

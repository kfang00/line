from display import *
from draw import *
import math

s = new_screen()
c = [ 0, 255, 0 ]

# #octants 1 and 5
# draw_line(0, 0, XRES-1, YRES-1, s, c)
# draw_line(0, 0, XRES-1, YRES / 2, s, c)
# draw_line(XRES-1, YRES-1, 0, YRES / 2, s, c)
#
# #octants 8 and 4
# c[BLUE] = 255;
# draw_line(0, YRES-1, XRES-1, 0, s, c);
# draw_line(0, YRES-1, XRES-1, YRES/2, s, c);
# draw_line(XRES-1, 0, 0, YRES/2, s, c);
#
# #octants 2 and 6
# c[RED] = 255;
# c[GREEN] = 0;
# c[BLUE] = 0;
# draw_line(0, 0, XRES/2, YRES-1, s, c);
# draw_line(XRES-1, YRES-1, XRES/2, 0, s, c);
#
# #octants 7 and 3
# c[BLUE] = 255;
# draw_line(0, YRES-1, XRES/2, 0, s, c);
# draw_line(XRES-1, 0, XRES/2, YRES-1, s, c);
#
# #horizontal and vertical
# c[BLUE] = 0;
# c[GREEN] = 255;
# draw_line(0, YRES/2, XRES-1, YRES/2, s, c);
# draw_line(XRES/2, 0, XRES/2, YRES-1, s, c);
x = 0
while x < 500:
    c[RED] = x % 250
    c[GREEN] = int(x / 10)
    draw_line((XRES) + 2 * x, (YRES / 3) + 4 * x, (XRES / 5) + 6 * x, (YRES / 6) + 5 * x, s, c);
    draw_line((XRES / 5) + 6 * x, (YRES / 6) + 5 * x, (XRES / 4) + 3 * x, (YRES / 2) + x, s, c);
    draw_line((XRES / 4) + 3 * x, (YRES / 2) + x, (XRES) + 2 * x, (YRES / 3) + 4 * x, s, c);
    #draw_line(250, 250, x, (YRES * 56) % 500, s, c);
    x = x + 10

display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')

from display import *
from draw import *
import math

s = new_screen()
c = [ 250, 0, 250 ]

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
while x < 600:
    draw_line(0, 0, x+1, YRES-1, s, c)
    draw_line(0, 0, x+1, YRES / 2 + x, s, c)
    draw_line(x+1, YRES-1, 0, YRES / 2 + x, s, c)
    c[BLUE] = 255;
    draw_line(0, YRES-1, x+1, 0, s, c);
    draw_line(0, YRES-1, x+1, YRES/2 + x, s, c);
    draw_line(x+1, 0, 0, YRES/2 + x, s, c);
    c[RED] = 255;
    c[GREEN] = 0;
    c[BLUE] = 0;
    draw_line(0, 0, x/2, YRES-1, s, c);
    draw_line(x+1, YRES-1, x/2, 0, s, c);
    c[BLUE] = 255;
    draw_line(0, YRES-1, x/2, 0, s, c);
    draw_line(x+1, 0, x/2, YRES-1, s, c);
    c[BLUE] = 0;
    c[GREEN] = 255;
    draw_line(0, YRES/2 + x, x+1, YRES/2 + x, s, c);
    draw_line(x/2, 0, x/2, YRES-1, s, c);
    x = x + 10

display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')

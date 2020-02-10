from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
	x = int(x0)
	y = int(y0)
	A = y1 - y
	B = -1 * (x1 - x)
	hold = 0
	if (x1-x) == 0:
		hold = 1
	else:
		hold = (x1-x)
	slope = ((y1-y)/hold)
	if (slope < 1):
		d = 2 * A + B #octant 1
		while x <= x1:
        		plot (screen, color, x, y)
        		if d > 0:
            			y = y + 1
            			d = d + 2 * B
        		x = x + 1
        		d = d + 2 * A
	else if (slope > 1):
		d = A + 2 * B #octant 2
		while y <= y1:
        		plot (screen, color, x, y)
        		if d < 0:
            			x = x + 1
           	 		d = d + 2 * A
        		y = y + 1
        		d = d + 2 * B
	else if (slope < -1):
		d = A - 2 * B #octant 7
		while y >= y1:
			plot (screen, color, x, y)
			if d > 0: 
	    			x = x + 1
	    			d = d + 2 * A
			y = y - 1
			d = d - 2 * B
	else:
		d = 2 * A - B #octant 8
		while x <= x1:
			plot (screen, color, x, y)
			if d > 0: 
				y = y - 1
				d = d - 2 * B
			x = x + 1
			d = d + 2 * A


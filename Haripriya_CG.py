from graphics import *
import tkinter as tk
from functools import partial
def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()

cirx=[]
ciry=[]
def midPointCircleDraw(x_centre,y_centre, r):
	x = r
	y = 0	
	print("(", x + x_centre, ", ",y + y_centre, ")",sep = "", end = "")
	cirx.append(x + x_centre)
	ciry.append(y + y_centre)
	if (r > 0) :
		print("(", x + x_centre, ", ",-y + y_centre, ")",sep = "", end = "")
		cirx.append(x + x_centre)
		ciry.append(-y + y_centre)
		print("(", y + x_centre, ", ",x + y_centre, ")",sep = "", end = "")
		cirx.append(y + x_centre)
		ciry.append(x + y_centre)
		print("(", -y + x_centre, ", ",x + y_centre, ")", sep = "")
		cirx.append(-y + x_centre)
		ciry.append(x + y_centre)
	P = 1-r
	while (x > y) :
		y += 1
		if (P <= 0): 
			P = P + 2 * y + 1 
		else: 
			x -= 1 
			P = P + 2 * y - 2 * x + 1 
		if (x < y): 
			break  
		print("(", x + x_centre, ", ", y + y_centre, ")", sep = "", end = "") 
		cirx.append(x + x_centre)
		ciry.append(y + y_centre)
		print("(", -x + x_centre, ", ", y + y_centre, ")", sep = "", end = "") 
		cirx.append(-x + x_centre)
		ciry.append(y + y_centre)
		print("(", x + x_centre, ", ", -y + y_centre, ")", sep = "", end = "")
		cirx.append(x + x_centre)
		ciry.append(-y + y_centre) 
		print("(", -x + x_centre, ", ", -y + y_centre, ")", sep = "") 
		cirx.append(-x + x_centre) 
		ciry.append(-y + y_centre)
		if (x != y) : 
			print("(", y + x_centre, ", ", x + y_centre, ")", sep = "", end = "") 
			cirx.append(y + x_centre)
			ciry.append(x + y_centre)
			print("(", -y + x_centre, ", ", x + y_centre, ")", sep = "", end = "") 
			cirx.append(-y + x_centre) 
			ciry.append(x + y_centre)
			print("(", y + x_centre, ", ", -x + y_centre, ")", sep = "", end = "") 
			cirx.append(y + x_centre)
			ciry.append(-x + y_centre)
			print("(", -y + x_centre, ", ", -x + y_centre, ")", sep = "") 
			cirx.append(-y + x_centre)
			ciry.append(-x + y_centre)

def Circle(x_centre,y_centre, r):
	midPointCircleDraw(x_centre,y_centre, r) 
	win = GraphWin("Circle",400, 400)
	for i in range(len(cirx)):
		pt=Point(cirx[i],ciry[i])
		pt.draw(win)
	pt=Point(200,200)
	pt.draw(win)
	win.getMouse()
	clear(win)
	win.close()

ex=[]
ey=[]
def midptellipse(rx, ry, xc, yc):
	x = 0;
	y = ry;
	d1 = ((ry * ry) - (rx * rx * ry) +(0.25 * rx * rx));
	dx = 2 * ry * ry * x;
	dy = 2 * rx * rx * y;

# For region 1
	while (dx < dy):  
		print("(", x + xc, ",", y + yc, ")"); 
		ex.append(x+xc)
		ey.append(y+yc)
		print("(",-x + xc,",", y + yc, ")"); 
		ex.append(-x+xc)
		ey.append(y+yc)
		print("(",x + xc,",", -y + yc ,")"); 
		ex.append(x+xc)
		ey.append(-y+yc)
		print("(",-x + xc, ",", -y + yc, ")"); 
		ex.append(-x+xc)
		ey.append(-y+yc)
		if (d1 < 0): 
			x += 1; 
			dx = dx + (2 * ry * ry); 
			d1 = d1 + dx + (ry * ry); 
		else: 
			x += 1; 
			y -= 1; 
			dx = dx + (2 * ry * ry); 
			dy = dy - (2 * rx * rx); 
			d1 = d1 + dx - dy + (ry * ry);
		
	d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) + ((rx * rx) * ((y - 1) * (y - 1))) - (rx * rx * ry * ry)); 
	while (y >= 0):

		print("(", x + xc, ",", y + yc, ")");
		ex.append(x+xc)
		ey.append(y+yc)
		print("(", -x + xc, ",", y + yc, ")");
		ex.append(-x+xc)
		ey.append(y+yc)
		print("(", x + xc, ",", -y + yc, ")");
		ex.append(x+xc)
		ey.append(-y+yc)
		print("(", -x + xc, ",", -y + yc, ")");
		ex.append(-x+xc)
		ey.append(-y+yc)
		if (d2 > 0):
			y -= 1;
			dy = dy - (2 * rx * rx);
			d2 = d2 + (rx * rx) - dy;
		else:
			y -= 1;
			x += 1;
			dx = dx + (2 * ry * ry);
			dy = dy - (2 * rx * rx);
			d2 = d2 + dx - dy + (rx * rx);



def Ellipse(rx, ry, xc, yc):
	midptellipse(rx, ry, xc, yc) 
	win = GraphWin("Ellipse",400, 400)
	for i in range(len(ex)):
		pt=Point(ex[i],ey[i])
		pt.draw(win)
	pt=Point(200,200)
	pt.draw(win)
	win.getMouse()
	clear(win)
	win.close()

def ROUND(a):
	return int(a + 0.5)
arrx=[]
arry=[]
def drawDDA(x1,y1,x2,y2):
	x,y = x1,y1
	length = (x2-x1) if (x2-x1) > (y2-y1) else (y2-y1)
	dx = (x2-x1)/float(length)
	dy = (y2-y1)/float(length)
	print('x = %s, y = %s' % (((ROUND(x),ROUND(y)))))
	arrx.append(ROUND(x))
	arry.append(ROUND(y))
	for i in range(length):
		x += dx
		y += dy
		print('x = %s, y = %s' % (((ROUND(x),ROUND(y)))))
		arrx.append(ROUND(x))
		arry.append(ROUND(y))

def Line(x1,y1,x2,y2):
	drawDDA(int(x1),int(y1),int(x2),int(y2))
	win = GraphWin("Line",400, 400)
	for i in range(len(arrx)):
		pt = Point(arrx[i],arry[i])
		pt.draw(win)
	win.getMouse()
	clear(win)
	win.close()

#Circle(200, 200, 50)
#Ellipse(20, 50, 200, 200)
window = tk.Tk()
 
window.title("Welcome to Drawing app")
window.configure(background='yellow')
window.geometry('200x200')
 
lbl = tk.Label(window, text="Choose to draw:",fg="blue")
lbl.configure(background='yellow')
j=0
lbl.grid(column=0, row=j)

def clickedline():
	window = tk.Tk()
	window.geometry('600x100')
	window.configure(background='yellow')
	lb1 = tk.Label(window, text="X1:")
	lb1.grid(column=0, row=2)
	x1 = tk.Entry(window,width=10)
	x1.grid(column=1, row=2)
	lb2 = tk.Label(window, text="Y1:")
	lb2.grid(column=2, row=2)
	x2 = tk.Entry(window,width=10)
	x2.grid(column=3, row=2)
	lb3 = tk.Label(window, text="X2:")
	lb3.grid(column=4, row=2)
	x3 = tk.Entry(window,width=10)
	x3.grid(column=5, row=2)
	lb4 = tk.Label(window, text="Y2:")
	lb4.grid(column=6, row=2)
	x4 = tk.Entry(window,width=10)
	x4.grid(column=7, row=2)
	submit=tk.Button(window, text="Submit",fg="blue", command= lambda: Line(int(x1.get()),int(x2.get()),int(x3.get()),int(x4.get())))
	#partial(Line,int(x1.get()),int(x2.get()),int(x3.get()),int(x4.get())))
	submit.grid(column=0, row=4)
	btnq = tk.Button(window,text="QUIT",fg="red",command=window.destroy)
	btnq.grid(column=0,row=5)
	window.mainloop()

def clickedcircle():
	window = tk.Tk()
	window.geometry('600x100')
	window.configure(background='yellow')
	lb1 = tk.Label(window, text="X_Center:")
	lb1.grid(column=0, row=2)
	x1 = tk.Entry(window,width=10)
	x1.grid(column=1, row=2)
	lb2 = tk.Label(window, text="Y_Center:")
	lb2.grid(column=2, row=2)
	x2 = tk.Entry(window,width=10)
	x2.grid(column=3, row=2)
	lb3 = tk.Label(window, text="Radius:")
	lb3.grid(column=4, row=2)
	x3 = tk.Entry(window,width=10)
	x3.grid(column=5, row=2)
	submit=tk.Button(window, text="Submit",fg="blue", command= lambda: Circle(int(x1.get()),int(x2.get()),int(x3.get())))
	#partial(Line,int(x1.get()),int(x2.get()),int(x3.get()),int(x4.get())))
	submit.grid(column=0, row=4)
	btnq = tk.Button(window,text="QUIT",fg="red",command=window.destroy)
	btnq.grid(column=0,row=5)
	window.mainloop()

def clickedellipse():
	window = tk.Tk()
	window.geometry('600x100')
	window.configure(background='yellow')
	lb1 = tk.Label(window, text="Rx:")
	lb1.grid(column=0, row=2)
	x1 = tk.Entry(window,width=10)
	x1.grid(column=1, row=2)
	lb2 = tk.Label(window, text="Ry:")
	lb2.grid(column=2, row=2)
	x2 = tk.Entry(window,width=10)
	x2.grid(column=3, row=2)
	lb3 = tk.Label(window, text="X_Center:")
	lb3.grid(column=4, row=2)
	x3 = tk.Entry(window,width=10)
	x3.grid(column=5, row=2)
	lb4 = tk.Label(window, text="Y_Center:")
	lb4.grid(column=6, row=2)
	x4 = tk.Entry(window,width=10)
	x4.grid(column=7, row=2)
	submit=tk.Button(window, text="Submit",fg="blue", command= lambda: Ellipse(int(x1.get()),int(x2.get()),int(x3.get()),int(x4.get())))
	#partial(Line,int(x1.get()),int(x2.get()),int(x3.get()),int(x4.get())))
	submit.grid(column=0, row=4)
	btnq = tk.Button(window,text="QUIT",fg="red",command=window.destroy)
	btnq.grid(column=0,row=5)
	window.mainloop()
    #lbl.configure(text= res)
 
btn1 = tk.Button(window, text="Line",fg="blue", command=clickedline)
btn1.grid(column=0, row=j+1)
btn2 = tk.Button(window, text="Circle",fg="blue", command=clickedcircle)
btn2.grid(column=0, row=j+2)
btn3 = tk.Button(window, text="Ellipse",fg="blue", command=clickedellipse)
btn3.grid(column=0, row=j+3)
btnq = tk.Button(window,text="QUIT",fg="red",command=quit)
btnq.grid(column=0,row=j+4)
window.mainloop()


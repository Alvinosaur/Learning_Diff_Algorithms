# oopyDotsDemo.py
# starts with betterDotsDemo and adds:
#   * a dotCounter that counts all the instances of Dot or its subclasses
#   * a MovingDot subclass of Dot that scrolls horizontally
#   * a FlashingMovingDot subclass of MovingDot that flashes and moves

import random
from tkinter import *

class Dot(object):
    dotCount = 0

    def __init__(self, x, y):
        Dot.dotCount += 1
        self.x = x
        self.y = y
        self.r = random.randint(20,50)
        self.fill = random.choice(["pink","orange","yellow","green",
                                   "cyan","purple"])
        self.clickCount = 0

    def containsPoint(self, x, y):
        d = ((self.x - x)**2 + (self.y - y)**2)**0.5
        return (d <= self.r)

    def draw(self, canvas):
        canvas.create_oval(self.x-self.r, self.y-self.r,
                           self.x+self.r, self.y+self.r,
                           fill=self.fill)
        canvas.create_text(self.x, self.y, text=str(self.clickCount))

    def onTimerFired(self, data):
        pass

class MovingDot(Dot):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.dx, self.dy = 5, 5

    def onTimerFired(self, data):
        self.x += self.dx
        self.y += self.dy
        if self.y >= data.height or self.y <= 0: self.dy *= -1
        if self.x >= data.width or self.x <= 0: self.dx *= -1

class FlashingMovingDot(MovingDot):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.flash_count = 0
        self.visible = True
    
    def onTimerFired(self, data):
        # update position like moving dot
        super().onTimerFired(data)
        # toggle visible and not visible
        self.flash_count += 1
        if self.flash_count == 5:
            self.flash_count = 0
            self.visible = not self.visible

    def draw(self, canvas):
        if self.visible: super().draw(canvas)

def init(data):
    data.dots = [ ]

def mousePressed(event, data):
    for dot in reversed(data.dots):
        if (dot.containsPoint(event.x, event.y)):
            dot.clickCount += 1
            return
    dotType = (len(data.dots) % 3)
    if (dotType == 0):
        data.dots.append(Dot(event.x, event.y))
    elif (dotType == 1):
        data.dots.append(MovingDot(event.x, event.y))
    else:
        data.dots.append(FlashingMovingDot(event.x, event.y))

def redrawAll(canvas, data):
    for dot in data.dots:
        dot.draw(canvas)
    canvas.create_text(data.width/2, 10, text="%d Dots" % Dot.dotCount)

def keyPressed(event, data):
    pass

def timerFired(data):
    for dot in data.dots:
        dot.onTimerFired(data)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(400, 200)
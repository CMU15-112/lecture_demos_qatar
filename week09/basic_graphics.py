_module = 'basic_graphics.py version 0.1.3'
# basic_graphics.py for standard Python (and not for browser-based brython)
# by David Kosbie
# version 0.1.3

import inspect
from types import SimpleNamespace
from tkinter import *

def draw(canvas, width, height):
    message = 'Replace this with your draw function'
    canvas.create_rectangle(10, 10, width-10, height-10,
                            fill='lightGreen', width=5, outline='green')
    canvas.create_text(width/2, height/2, text=message, font='Arial 20 bold')

def run(*args, title=None, width=400, height=400, drawFn=None):
    state = SimpleNamespace()
    state.width, state.height = width, height
    state.redrawCount = 0 # number of deferred calls to redrawAll (max of 2)
    root = Tk()
    canvas = Canvas(root, width=state.width, height=state.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack(fill=BOTH, expand=YES)
    callersGlobals = inspect.stack()[1][0].f_globals
    if (drawFn is None):
        if ('draw' not in callersGlobals):
            raise Exception('No draw function defined!')
        drawFn = callersGlobals['draw']
    def redrawAll():
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, state.width, state.height,
                                fill='white', outline='white')
        drawFn(canvas, state.width, state.height, *args)
    def updateTitle():
        name = drawFn.__name__
        root.title(f'{name} ({state.width} x {state.height})')
    def deferredRedrawAll():
        if (state.redrawCount == 2): return # one pending, another after that
        state.redrawCount += 1
        if (state.redrawCount == 1):
            afterDelay = 10
            def afterFnWrapper():
                redrawAll()
                state.redrawCount -= 1
                if (state.redrawCount == 1): root.after(afterDelay, afterFnWrapper)
            root.after(afterDelay, afterFnWrapper)
    def sizeChangedWrapper(event):
        if (event and ((event.width < 2) or (event.height < 2))): return
        newWidth,newHeight,winx,winy = [int(v) for v in root.winfo_geometry().replace('x','+').split('+')]
        if ((state.width != newWidth) or (state.height != newHeight)):
            state.width, state.height = newWidth, newHeight
            updateTitle()
            deferredRedrawAll()
    root.bind('<Configure>', lambda event: sizeChangedWrapper(event))
    updateTitle()
    deferredRedrawAll()
    root.mainloop()
    print("bye!")

if (__name__ == '__main__'):
    run()
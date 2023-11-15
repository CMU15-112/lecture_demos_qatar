from cmu_graphics import *

class TextField:
    def __init__(self, x, y, width, height=100, label=None, value="", ispassword=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.focused = False
        self.value = value
        self.ispassword = ispassword

    def draw(self):
        drawLabel(f'{self.label}:',
                  self.x-self.width//2 - 5, self.y,
                  align='right',
                  size=50)
        borderColor = 'black'
        if self.focused:
            borderColor = 'green'
        drawRect(self.x, self.y, self.width, self.height,
                 align='center', fill=None, border = borderColor, borderWidth=10)
        if len(self.value):
            if self.ispassword:
                drawLabel("*"*len(self.value), self.x, self.y, size=50)
            else:
                drawLabel(self.value, self.x, self.y, size=50)


    def isFocused(self, x, y):
        return self.x - self.width //2 <= x <= self.x + self.width //2 and \
               self.y - self.height //2 <= y <= self.y + self.height // 2



class Button:
    def __init__(self, x, y, width, height, label=None):
        self.width = width
        self.height = height
        self.label = label
        self.x = x
        self.y = y
    def draw(self):
        drawRect(self.x, self.y, self.width,
                 self.height, align='center',
                 fill=None, border='black')
        if self.label:
            drawLabel(self.label, self.x, self.y, size = 50)

    def isClicked(self, x, y):
        return self.x - self.width //2 <= x <= self.x + self.width //2 and \
               self.y - self.height //2 <= y <= self.y + self.height // 2


def onAppStart(app):
    app.userForm = {}
    app.focusedField = None
    app.userForm['username'] = TextField(400, 100, 300, label="Username")
    app.userForm['password'] = TextField(400, 250, 300, label="Password", ispassword=True)
    app.loginBtn = Button(200, 400, 300, 100,  label="Login")
    app.state = 'login'


def onStep(app):
    pass

def onKeyPress(app, key):
    if isinstance(app.userFormFocused, TextField):
        if len(key) == 1 and key.isalnum():
            app.userFormFocused.value += key
        elif key == "backspace":
            app.userFormFocused.value = app.userFormFocused.value[:-1]

""" returns True if password is secret42 """
def checkPassword(username, password):
    return password == 'secret42'

def onMousePress(app, x, y):
    if app.state == 'login':
        app.userFormFocused = None
        for field in app.userForm:
            if app.userForm[field].isFocused(x, y):
                app.userForm[field].focused = True
                app.userFormFocused = app.userForm[field]
            else:
                app.userForm[field].focused = False
        if app.loginBtn.isClicked(x, y):
            if checkPassword(app.userForm['username'].value, app.userForm['password'].value):
                app.state = "welcome"
                app.user = app.userForm['username'].value


def redrawAll(app):
    if app.state == 'login':
        for field in app.userForm:
            app.userForm[field].draw()
        app.loginBtn.draw()
    elif app.state == 'welcome':
        drawRect(0,0,app.width, app.height, fill="blue")
        drawLabel(f"Welcome {app.user}", app.width//2, app.height//2,
                  fill="white", font="Arial", size=20, bold=True)


runApp(width=800, height=800)

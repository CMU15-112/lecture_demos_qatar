from cmu_graphics import *

# A widget only has a position on the window
# and a hidden property (is it visible or not?)
class Widget:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hidden = False
    def draw(self):
        pass
    def isClicked(self,x,y):
        pass
    def onKey(self, key):
        pass
    def onClick(self):
        pass
    
class EntryField(Widget):
    def __init__(self, x, y, width, height=100, label=None, value=""):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.label = label
        self.focused = False
        self.value = value

    def drawBox(self):
        drawLabel(f'{self.label}:',
                  self.x-self.width//2 - 5, self.y,
                  align='right',
                  size=50)
        borderColor = 'black'
        if self.focused:
            borderColor = 'green'
        drawRect(self.x, self.y, self.width, self.height,
                 align='center', fill=None, border = borderColor, borderWidth=10)
    def drawContent(self):
        if len(self.value):
            drawLabel(self.value, self.x, self.y, size=50)
    
    def draw(self):
        self.drawBox()
        self.drawContent()

    def isClicked(self, x, y):
        return self.x - self.width //2 <= x <= self.x + self.width //2 and \
               self.y - self.height //2 <= y <= self.y + self.height // 2
    def onKey(self, key):
        if len(key) == 1 and key.isalnum():
            self.value += key
        elif key == "backspace":
            self.value = self.value[:-1]


class PasswordField(EntryField):
    def drawContent(self):
        if len(self.value):
            drawLabel("*"*len(self.value), self.x, self.y, size=50)
    

class Button(Widget):
    def __init__(self, x, y, width, height, label=None):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.label = label
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
    app.userForm['username'] = EntryField(400, 100, 300, label="Username")
    app.userForm['password'] = PasswordField(400, 250, 300, label="Password")
    app.loginBtn = Button(200, 400, 300, 100,  label="Login")
    app.state = 'login'


def onStep(app):
    pass

def onKeyPress(app, key):
    if app.userFormFocused:
        app.userFormFocused.onKey(key)
   
""" returns True if password is secret42 """
def checkPassword(username, password):
    return password == 'secret42'

def onMousePress(app, x, y):
    if app.state == 'login':
        app.userFormFocused = None
        for field in app.userForm:
            if app.userForm[field].isClicked(x, y):
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

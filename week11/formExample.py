from cmu_112_graphics import *

class TextField:
    def __init__(self, x, y, width, height=50, label=None, value="", ispassword=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.focused = False
        self.value = value
        self.ispassword = ispassword
        
    def draw(self, canvas):
        canvas.create_text(self.x-self.width//2 - 5, self.y,
                           anchor='e', text=f'{self.label}:')
        outlineColor = 'black'
        if self.focused:
            outlineColor = 'green'
        canvas.create_rectangle(self.x - self.width//2, self.y - self.height//2,
                                self.x + self.width//2, self.y + self.height//2,
                                fill=None, outline = outlineColor, width=10)
        if len(self.value):
            if self.ispassword:
                canvas.create_text(self.x, self.y, text="*"*len(self.value))
            else:
                canvas.create_text(self.x, self.y, text=self.value)
            
            
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
    def draw(self, canvas):

        canvas.create_rectangle(self.x - self.width//2, self.y - self.height//2,
                                self.x + self.width//2, self.y + self.height//2,
                                fill=None)
        
        canvas.create_text(self.x, self.y, text=self.label)
    def isClicked(self, x, y):
        return self.x - self.width //2 <= x <= self.x + self.width //2 and \
               self.y - self.height //2 <= y <= self.y + self.height // 2
        

def appStarted(app):
    app.userForm = {}
    app.focusedField = None
    app.loginBtn = Button(200, 300, 150, 50,  label="Login")
    app.userForm['username'] = TextField(400, 100, 300, label="Username")
    app.userForm['password'] = TextField(400, 200, 300, label="Password", ispassword=True)
    app.state = 'login'
 
        
def timerFired(app):
    pass

def keyPressed(app, event):
    if isinstance(app.userFormFocused, TextField):
        if event.key.isalnum():
            app.userFormFocused.value += event.key
    
""" returns True if password is secret42 """
def checkPassword(username, password):
    return password == 'secret42'
    
def mousePressed(app, event):
    if app.state == 'login':
        app.userFormFocused = None
        for field in app.userForm:
            if app.userForm[field].isFocused(event.x, event.y):
                app.userForm[field].focused = True
                app.userFormFocused = app.userForm[field]
            else:
                app.userForm[field].focused = False
        if app.loginBtn.isClicked(event.x, event.y):
            if checkPassword(app.userForm['username'].value, app.userForm['password'].value):
                app.state = "welcome"
                app.user = app.userForm['username'].value
    
    
def redrawAll(app, canvas):
    if app.state == 'login':
        for field in app.userForm:
            app.userForm[field].draw(canvas)
        app.loginBtn.draw(canvas)
    elif app.state == 'welcome':
        canvas.create_rectangle(0,0,app.width, app.height, fill="blue")
        canvas.create_text(app.width//2, app.height//2, text=f"Welcome {app.user}",
                           fill="white", font="Arial 20 bold")
        

runApp(width=800, height=800)

from ppg_runtime.application_context.PySide6 import PPGLifeCycle
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel
from PySide6.QtGui import QPixmap, QPainter

class Label(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.p = QPixmap()

    def setPixmap(self, p):
        self.p = p
        self.update()

    def paintEvent(self, event):
        if not self.p.isNull():
            painter = QPainter(self)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)
            painter.drawPixmap(self.rect(), self.p)

class Auth(QWidget, PPGLifeCycle):
	
	def __init__(self, parent=None, **kwargs):
		super().__init__(parent=parent, objectName="Auth", **kwargs)
		self.parent = parent

		# the life cycle of the component has to be forced manually because QWidget stops the life cycle
		self.force_life_cycle()

	
	def force_life_cycle(self):
		self.allow_bg()
		self.render_()
		self.responsive_UI()

	# allow background color
	def allow_bg(self): self.setAttribute(Qt.WA_StyledBackground, True)

	def render_(self):
		# set a responsive logo
		self.logo = Label(self)
		self.logo.setPixmap(QPixmap(self.parent.get_resource('img/logo.jpg')))
		
		
		self.error_msg = QLabel(text="", objectName="label-danger", parent=self)
		self.user = QLineEdit(parent=self, placeholderText="User", objectName="input-form")
		self.passwd = QLineEdit(parent=self, placeholderText="Password", objectName="input-form", echoMode=QLineEdit.Password)
		self.login = QPushButton(parent=self, text="Login", objectName="button-form", clicked=self.login_)

	def login_(self):
		
		user = self.user.text()
		passwd = self.passwd.text()

		if user == "admin" and passwd == "admin":
			self.parent.stack.setCurrentIndex(1)
		else:
			self.error_msg.setStyleSheet("color: white; background: tomato; padding:10px")
			self.error_msg.setText("Invalid credentials")

	def responsive_UI(self):
		F_WIDTH = self.parent.width()
		F_HEIGHT = self.parent.height()

		# move user input to center
		self.user.resize(self.calc(50, F_WIDTH), 30)
		self.user.move(self.calc(25, F_WIDTH), self.calc(50, F_HEIGHT))
		self.passwd.resize(self.calc(50, F_WIDTH), 30)
		self.passwd.move(self.calc(25, F_WIDTH),self.calc(60, F_HEIGHT))

		self.login.resize(self.calc(50, F_WIDTH), 30)
		self.login.move(self.calc(25, F_WIDTH), self.calc(70, F_HEIGHT))

		self.error_msg.resize(self.calc(50, F_WIDTH), 30)
		# move error message to right
		self.error_msg.move(self.calc(70, F_WIDTH), 0)

		# logo used 100% of width and 25% of height
		self.logo.resize(self.calc(40, F_WIDTH), self.calc(45, F_HEIGHT))
		# move logo to center
		self.logo.move(self.calc(28, F_WIDTH), self.calc(0, F_HEIGHT))
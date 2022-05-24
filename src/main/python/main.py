from asyncio import futures
import sys
from ppg_runtime.application_context.PySide6 import ApplicationContext, PPGLifeCycle
from PySide6.QtWidgets import QMainWindow, QStackedWidget
from views.Auth import Auth
from views.Home import Home

class MyApp(PPGLifeCycle, QMainWindow, ApplicationContext):

	def component_will_mount(self):
		self.setFixedSize(640, 480)

	def render_(self):
		screens = [Auth, Home]
		self.stack = QStackedWidget(self, objectName='stack')

		for screen in screens:
			self.stack.addWidget(screen(self))

		# Cambiar este numero para cambiar la pantalla [0-1]
		self.stack.setCurrentIndex(0)

	def set_CSS(self):
		with open(self.get_resource('css/index.css'), 'r') as f:
			self.setStyleSheet(f.read())

	def responsive_UI(self):
		# Create width and height constants
		FULL_WIDTH, FULL_HEIGHT = self.width(), self.height()

		# set stack 100% of the screen and height should be the same as the screen, finally move it to the right 20%
		self.stack.resize(FULL_WIDTH, FULL_HEIGHT)



if __name__ == '__main__':
	appctxt = ApplicationContext()
	window = MyApp()
	window.show()
	exit_code = appctxt.app.exec()
	sys.exit(exit_code)
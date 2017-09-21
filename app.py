from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

'''
class MainWindow(QMainWindow):
	my_signal=pyqtSignal(str,int)
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setWindowTitle('My First App')
		button=QPushButton('Click me!')
		button.pressed.connect(self._click_button)
		self.my_signal.connect(self._my_func)
		self.setCentralWidget(button)

	def _click_button(self):
		self.my_signal.emit('shinimaa',1)
		
	def _my_func(self,n,s):
		print(n)
		print(s)'''
'''
class MainWindow(QMainWindow):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.setWindowTitle('my first app')
		label=QLabel('welcome to here')
		label.setAlignment(Qt.AlignCenter)
		self.setCentralWidget(label)
		tb=QToolBar('Tool Bar')
		tb.setIconSize(QSize(16,16))
		self.addToolBar(tb)
		button_action=QAction(QIcon('icons/penguin.png'),'Menu button',self)
		button_action.setStatusTip('This is menu button')
		button_action.triggered.connect(self.onButtonClick)
		tb.addAction(button_action)
		button_action2=QAction('C++',self)
		button_action3=QAction('Python',self)
		button_action2.setCheckable(True)
		button_action3.setCheckable(True)
		button_action2.triggered.connect(self.onButtonClick)
		button_action3.triggered.connect(self.onButtonClick)
		mb=self.menuBar()
		mb.setNativeMenuBar(False)
		file_menu=mb.addMenu('&MyFile')
		file_menu.addAction(button_action)
		file_menu.addSeparator()
		build_system_menu=file_menu.addMenu('&build system')
		build_system_menu.addAction(button_action2)
		build_system_menu.addSeparator()
		build_system_menu.addAction(button_action3)
		
		self.setStatusBar(QStatusBar(self))
	def onButtonClick(self,s):
		print(s)'''

'''class MainWindow(QMainWindow):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.setWindowTitle('MyFristApp')
		layout=QVBoxLayout()
		widgets=[QCheckBox,QComboBox,QDateEdit,QDateTimeEdit,QDial,QDoubleSpinBox,QFontComboBox,QLCDNumber,QLineEdit,QProgressBar,QPushButton,
QRadioButton,QSlider,QSpinBox,QTimeEdit]
		for item in widgets:
			layout.addWidget(item())
		widget=QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)'''

'''
class Color(QWidget):
	def __init__(self,color,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.setAutoFillBackground(True)
		palette=self.palette()
		palette.setColor(QPalette.Window,QColor(color))
		self.setPalette(palette)

class MainWindow(QMainWindow):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.setWindowTitle('My First app')
		colors=['red','green','blue','yellow']
		layout=QGridLayout()
		for color in colors:
			layout.addWidget(Color(color))
		widget=QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)'''

class CustomDialog(QDialog):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.setWindowTitle('New Dialog')
		QBtn=QDialogButtonBox.Ok|QDialogButtonBox.Cancel
		buttonBox=QDialogButtonBox(QBtn)
		layout=QVBoxLayout()
		layout.addWidget(buttonBox)
		self.setLayout(layout)

class MainWindow(QMainWindow):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.setWindowTitle('MyFirstApp')
		label=QLabel('Welcome to shiysanlou')
		label.setAlignment(Qt.AlignCenter)	
		self.setCentralWidget(label)	
		button_action=QAction('New dialog',self)
		button_action.triggered.connect(self.onButtonClick)
		mb=self.menuBar()
		mb.setNativeMenuBar(False)
		file_menu=mb.addMenu('&File')
		file_menu.addAction(button_action)

	def onButtonClick(self,s):
		dlg=CustomDialog(self)
		dlg.exec_()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

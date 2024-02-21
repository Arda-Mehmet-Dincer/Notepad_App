from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt
from login import Ui_Form
from notepadPage import notepadPage

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.loginform = Ui_Form()
        self.loginform.setupUi(self)
        self.notepadForm = notepadPage()


        self.loginform.lineEdit_username.returnPressed.connect(self.check_login)
        self.loginform.lineEdit_password.returnPressed.connect(self.check_login)


        self.loginform.pushButton_login.clicked.connect(self.check_login)

    def check_login(self):
        username = self.loginform.lineEdit_username.text()
        password = self.loginform.lineEdit_password.text()
        if username == "admin" and password == "123456":
            self.close()
            self.notepadForm.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        else:
            super().keyPressEvent(event)

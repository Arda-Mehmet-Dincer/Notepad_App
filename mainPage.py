from PyQt5.QtWidgets import QApplication
from loginPage import LoginPage

app = QApplication([])
window = LoginPage()
window.show()
app.exec_()
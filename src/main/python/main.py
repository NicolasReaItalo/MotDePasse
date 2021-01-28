from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2 import QtWidgets
import requests

import sys


class PassWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Générateur de mots de passe")
        self.btn_new = QtWidgets.QPushButton("Nouveau mot de passe")
        self.btn_new.clicked.connect(self.bt_new_push)
        self.btn_copy = QtWidgets.QPushButton('Copier')
        self.btn_copy.clicked.connect(self.bt_copy_push)
        self.text = QtWidgets.QLineEdit('********')
        self.text.setReadOnly(True)
        self.text.setFixedSize(100, 30)
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.btn_new)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.btn_copy)
        self.wid = QtWidgets.QWidget()
        self.wid.setLayout(self.layout)
        self.setCentralWidget(self.wid)
        self.resize(450, 50)

    def bt_new_push(self):
        password = self.get_password()
        self.text.clear()
        self.text.setText(password)
        self.text.repaint()

    def bt_copy_push(self):
        self.text.selectAll()
        self.text.copy()

    def get_password(self):
        r = requests.get('https://api.motdepasse.xyz/create/?include_digits&include_lowercase&include_uppercase'
                         '&password_length=8&quantity=1')
        if r.status_code == 200:
            return r.json().get('passwords')[0]
        else:
            return False


if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = PassWindow()
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)

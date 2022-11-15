from PyQt5.Qt import *
from resource.ui.login import Ui_login
import qdarkstyle


class LoginPanel(QWidget, Ui_login):
    # 自定义信号，判断界面切换
    show_registerPanel_signal = pyqtSignal()

    def __init__(self, parent=None):
        # 调用父类的初始化方法
        super().__init__(parent)
        self.setupUi(self)

    def login_to_register(self):
        self.show_registerPanel_signal.emit()

    def check_login(self):
        userName = self.login_username_text.text()
        passWord = self.login_password_text.text()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    # setup stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    window = LoginPanel()
    window.show()
    sys.exit(app.exec_())

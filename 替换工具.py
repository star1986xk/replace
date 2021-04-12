import sys
from ui import Ui_Form
from PyQt5.QtWidgets import QApplication, QFrame


class MainWindow(QFrame, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)

        self.pushButton.clicked.connect(self.run)

    def run(self):
        text1 = self.textEdit_1.toPlainText().strip()
        text2 = self.textEdit_2.toPlainText().strip()
        if not text1 or not text2: return
        t1_list = text1.split('\n')
        t2_list = text2.split('\n')
        t3_list = []
        count = max(len(t1_list), len(t2_list))

        for t1, t2 in zip(t1_list[:count], t2_list[:count]):
            t3_list.append(t1.replace('*', t2))

        self.textEdit_3.setPlainText('\n'.join(t3_list))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

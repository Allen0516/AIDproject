from PyQt4 import QtGui  
from PyQt4 import QtCore 
import sys  

class MyQt(QtGui.QWidget):
    def __init__(self):
        super(MyQt,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,800,600)
        self.setWindowTitle("测试界面")
        self.show()
def main():
    app = QtGui.QApplication(sys.argv)
    myqt=MyQt()

    sys.exit(app.exec_())
if __name__ == "__main__":
    main()

#安装qt-designer
    sudo apt install qt4-designer
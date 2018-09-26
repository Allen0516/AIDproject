# 事件3要素
#     事件来源（source）
#         状态发生变化的对象，这个变化的对象会产生对象
#     事件对象（object）
#         产生的事件是什么事件
#     事件目标（aim）
#         这个事件希望被通知的对象
# 使用事件：
#     信号槽机制：
#     信号和槽是用来进行对象间的沟通的.当一个特定的事件发生时，一个信号被激发.槽用来接受这个信号，可以是
#     任意的python请求。当和槽想关联的信号被激发时，槽被调用from

from PyQt4 import QtGui,QtCore
class window(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle("事件演示")

        #设置布局
        vbox = QtGui.QVBoxLayout()
        #向布局中添加
        #添加一个lcd显示模块
        lcd = QtGui.QLCDNumber(self)
        
        lcd.setToolTip("显示数据")
        #添加一个水平滑竿
        sld = QtGui.QSlider(QtCore.Qt.Horizontal,self)
        sld.setToolTip("控制数据的变化")
        #移动滑竿，变化的值在lcd上显示
        #事件来源：滑竿sld ，事件对象：值发生变化 valuechanged
        #事件目标：在lcd上显示值 display
        sld.valueChanged.connect(lcd.display)
        #添加一个按钮
        button = QtGui.QPushButton("关闭",self)
        button.setToolTip("关闭窗口")
        button.clicked.connect(self.close)

        #将组件添加到布局
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        #最后设置整体布局
        self.setLayout(vbox)
        self.show()
    def closeEvent(self,event):
        reply = QtGui.QMessageBox.question(self,"事件演示","是否退出",QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)

def main():
    import sys
    app= QtGui.QApplication(sys.argv)
    win = window()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()
#导入pyqt

from PyQt4 import QtGui  
from PyQt4 import QtCore 
import sys  
  
# app=QApplication(sys.argv)  
# b=QPushButton("Hello Kitty!")  
# b.show()
# app.connect(b,SIGNAL("clicked()"),app,SLOT("quit()"))  
# # app.exec_() 

def main():
    app=QtGui.QApplication(sys.argv)#创建qt图形应用
    w = QtGui.QWidget()#创建图形窗口
    w.resize(800,600)#设值窗口大小
   
    w.move(350,350)#设置窗口起始位置
    w.setWindowTitle("测试页面")#设置标题名
    w.show()#显示窗口

    sys.exit(app.exec_())#关闭界面
if __name__ =="__main__":
    main()
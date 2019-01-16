import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from calc36 import Ui_MainWindow
from math import sin, cos, tan, asin, acos, atan, log2, factorial, pi
 
class MyWidget(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ev = []
        #Цифры
        self.Button0.clicked.connect(self.run)
        self.Button1.clicked.connect(self.run)
        self.Button2.clicked.connect(self.run)
        self.Button3.clicked.connect(self.run)
        self.Button4.clicked.connect(self.run)
        self.Button5.clicked.connect(self.run)
        self.Button6.clicked.connect(self.run)
        self.Button7.clicked.connect(self.run)
        self.Button8.clicked.connect(self.run)
        self.Button9.clicked.connect(self.run)
        self.ButtonA.clicked.connect(self.run)
        self.ButtonB.clicked.connect(self.run)
        self.ButtonC.clicked.connect(self.run)
        self.ButtonD.clicked.connect(self.run)
        self.ButtonE.clicked.connect(self.run)
        self.ButtonF_2.clicked.connect(self.run)
        self.ButtonG.clicked.connect(self.run)
        self.ButtonH.clicked.connect(self.run)
        self.ButtonI.clicked.connect(self.run)
        self.ButtonJ.clicked.connect(self.run)
        self.ButtonK.clicked.connect(self.run)
        self.ButtonL.clicked.connect(self.run)
        self.ButtonM.clicked.connect(self.run)
        self.ButtonN.clicked.connect(self.run)
        self.ButtonO.clicked.connect(self.run)
        self.ButtonP.clicked.connect(self.run)
        self.ButtonQ.clicked.connect(self.run)
        self.ButtonR.clicked.connect(self.run)
        self.ButtonS.clicked.connect(self.run)
        self.ButtonT_2.clicked.connect(self.run)
        self.ButtonU.clicked.connect(self.run)
        self.ButtonV.clicked.connect(self.run)
        self.ButtonW.clicked.connect(self.run)
        self.ButtonX.clicked.connect(self.run)
        self.ButtonY.clicked.connect(self.run)
        self.ButtonZ.clicked.connect(self.run)       
        
        #
        self.ButtonBack.clicked.connect(self.run)
        self.ButtonCos.clicked.connect(self.run)
        self.ButtonCube.clicked.connect(self.run)
        self.ButtonDel.clicked.connect(self.run)
        self.ButtonDelenie.clicked.connect(self.run)
        self.ButtonDiv.clicked.connect(self.run)
        self.ButtonMod.clicked.connect(self.run)
        self.ButtonProizvedenie.clicked.connect(self.run)
        self.ButtonRavno.clicked.connect(self.rez)
        self.ButtonRaznica.clicked.connect(self.run)
        self.ButtonSin.clicked.connect(self.run)
        self.ButtonSqrt.clicked.connect(self.run)
        self.ButtonSqrt_2.clicked.connect(self.run)
        self.ButtonSqrt_3.clicked.connect(self.run)
        self.ButtonSquare.clicked.connect(self.run)
        self.ButtonStepen.clicked.connect(self.run)
        self.ButtonSumma.clicked.connect(self.run)
        self.ButtonT.clicked.connect(self.run)
        self.ButtonTg.clicked.connect(self.run)
        self.ButtonS1.clicked.connect(self.run)
        self.ButtonS2.clicked.connect(self.run)        
        self.ButtonF.clicked.connect(self.run)        
        self.Buttonlog2.clicked.connect(self.run)        
        self.ButtonPi.clicked.connect(self.run)        
        self.ButtonASin.clicked.connect(self.run)        
        self.ButtonACos.clicked.connect(self.run)        
        self.ButtonATg.clicked.connect(self.run)        
        
        
    def run(self):
        if self.sender().text() == '<--':
            self.ev = self.ev[:-1]
        elif self.sender().text() == 'С':
            self.ev = []
        elif self.sender().text() == 'x':
            self.ev += ['*']
        elif self.sender().text() == 'mod':
            self.ev += ['%']
        elif self.sender().text() == 'div':
            self.ev += ['//']
        elif self.sender().text() == '√':
            self.ev += ['**0.5']
        elif self.sender().text() == '3√':
            self.ev += ['**(1/3)']
        elif self.sender().text() == 'y√':
            self.ev += ['**(1/']
        elif self.sender().text() == 'x^2':
            self.ev += ['**2']
        elif self.sender().text() == 'x^3':
            self.ev += ['**3']
        elif self.sender().text() == 'x^y':
            self.ev += ['**']
        elif self.sender().text() == 'sin':
            self.ev += ['sin(']
        elif self.sender().text() == 'cos':
            self.ev += ['cos(']
        elif self.sender().text() == 'tan':
            self.ev += ['tan(']
        elif self.sender().text() == 'asin':
            self.ev += ['asin(']
        elif self.sender().text() == 'acos':
            self.ev += ['acos(']
        elif self.sender().text() == 'atan':
            self.ev += ['atan(']      
        elif self.sender().text() == 'log2':
            self.ev += ['log2(']
        elif self.sender().text() == '!':
            self.ev += ['factorial(']
        elif self.sender().text() == 'pi':
            self.ev += [str(pi)]
        else:
            self.ev += [self.sender().text()]
            
        self.label.setText(''.join(self.ev))
        
        
        
            
            
    def rez(self):
        try:
            prim = ''.join(self.ev)
            r = str(eval(prim))
            self.label.setText(r)
            self.ev = list(r)
        except Exception:
            self.label.setText('Error')
            self.ev = []
            
        
 
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec())

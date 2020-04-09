# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'início.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
import sys
# from W_COMBINADA import w_combinada
# from INCERTEZA_EXT import txt_to_csv
# from PERDA_DE_CARGA import perda_de_carga
# from TENSORES_DE_REYNOLDS import tensores_de_reynolds

Form, Window = uic.loadUiType('início.ui')

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Window()
        self.ui.form = Form()
        self.ui.form.setupUi(self)
        self.ui.form.toolButton_reynolds.clicked.connect(self.r_botao)
        self.ui.form.toolButton_lda.clicked.connect(self.lda_botao)
        self.ui.form.toolButton_pd.clicked.connect(self.pd_botao)
        # self.ui.form.ok_button.clicked.connect(self.ok_botao)
        
    def r_botao(self):
         path1 = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a directory')
         if path1:
             self.ui.form.folder_reynolds.setText(path1)
         self.string_path1 = path1
        
    def lda_botao(self):
         path2 = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a directory')
         if path2:
             self.ui.form.file_lda.setText(path2)
         self.string_path2 = path2        
         
    def pd_botao(self):
         path3 = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a directory')
         if path3:
             self.ui.form.file_pd.setText(path3)
         self.string_path3 = path3 
         
app = QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())


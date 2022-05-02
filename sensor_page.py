import sys
import datetime

from PyQt5.QtCore import QTimer,pyqtSlot

import sensor
from PyQt5 import QtCore, QtGui,QtWidgets
import pandas as pd
from openpyxl import Workbook
import var as gv 
import sqlite3


class Sensor(QtWidgets.QMainWindow, sensor.Ui_MainWindow):
   global date
   date = datetime.date.today()
   def __init__(self):
      super(self.__class__,self).__init__()
      self.setupUi(self)
      self.lineEdit.setText(str(date))
      self.pushButton.clicked.connect(self.Log_data)
      self.timer = QTimer()
      self.timer.timeout.connect(self.Log_data)
      self.timer.start(50000)
   def Log_data(self):
      gv.date = datetime.date.today()
      t=datetime.datetime.now()
      gv.cr_time = t.strftime("%H:%M:%S")
      gv.no_of_node=self.lineEdit_2.text()
      gv.temp=self.lineEdit_4.text()
      gv.co=self.lineEdit_3.text()
      gv.AQI= self.lineEdit_7.text()
      gv.Humi= self.lineEdit_5.text()
      gv.NH3= self.lineEdit_6.text()
      gv.co2= self.MQ7_data.text()
      gv.dust=self.MQ7_data_2.text()
      print("save")
      Log_data_db()



def Log_data_db():

   try:
        conn  = sqlite3.connect('H:\Chetan\python\sensor_status\Log_data.db')
        print("Connection is established: Database is created in memory")
        db=conn.cursor()
        db.execute('insert into Logtbl(Date,time,No_node,temp,co,AQI,Humidity,NH3,CO2,Dust) values(?,?,?,?,?,?,?,?,?,?)',(gv.date,gv.cr_time,gv.no_of_node,gv.temp,gv.co,gv.AQI,gv.Humi,gv.NH3,gv.co2,gv.dust))
   except:
        print("error in conn")
   
   conn.commit()          
   conn.close()

def main():
   app = QtWidgets.QApplication(sys.argv)
   GUI = Sensor()
   GUI.show()

   print('running')
   app.exec_()



if __name__ == '__main__':
   main()


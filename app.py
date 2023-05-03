from ui import *
import random
import firebase_admin
from firebase_admin import credentials, firestore
import datetime

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        #Configuraciones firebase
        cred = credentials.Certificate("serviceAccountKey.json")
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        self.sensores_ref = db.collection('sensores')

        self.pushButton.clicked.connect(self.saluda)

    def saluda(self):
        temp = self.sensor_temperatura()
        print(temp)
        self.lcdNumber.display(str(temp))
        self.send_data(temp)

    def sensor_temperatura(self):
        #TODO: Implementar logica del sensor
        return round(random.uniform(14,30),2)
    
    def send_data(self,temp):
        data = {
            'temp': temp,
            'hum': 30,
            'fecha': datetime.datetime.now()
        }
        self.sensores_ref.document().set(data)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
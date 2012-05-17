import PySide.QtCore as QtC
import PySide.QtGui as QtG
import PySide.QtNetwork as QtN
import sys
import urllib.request

class DownloadProgressBar(QtG.QProgressBar):
	def __init__(self,url,parent):
		super(DownloadProgressBar,self).__init__(parent)
		self.mRequest = QtN.QNetworkRequest(url)
		self.mNetwork =QtN.QNetworkAccessManager()
		
	def Start(self):
		self.mReply =self.mNetwork.get(self.mRequest)
		self.mReply.downloadProgress.connect(self.UpdateProgress)
		self.mReply.finished.connect(self.Finished)

	
	
	@QtC.Slot()
	def Finished(self):
		print("end of this!")
	
	@QtC.Slot(int,int)
	def UpdateProgress(self,received,total):
		self.setMaximum(total)
		self.setValue(received)

class MainDialog(QtG.QDialog):
	def __init__(self,title,parent=None):
		super(MainDialog,self).__init__(parent)
		self.setBaseSize(200,300)
		self.setWindowTitle(title)
		self.mButton = QtG.QPushButton("download",self)
		self.mButton.clicked.connect(self.Download)
		address=QtC.QUrl("http://www.kernel.org/pub/linux/kernel/v3.0/linux-3.3.6.tar.bz2")
		self.mLocalFile=QtC.QUrl("local_file.tar.bz2")
		self.mBar = DownloadProgressBar(address,self)
		
		self.mBar.setGeometry(100,0,100,20)
		self.mBar.show()
		self.mButton.show()
		
	@QtC.Slot()
	def Download (self):
		self.mBar.Start()

if __name__ == '__main__':
    # Create the Qt Application
    app = QtG.QApplication(sys.argv)
    # Create and show the main window
    dialog = MainDialog("My app DiaLog")
    dialog.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
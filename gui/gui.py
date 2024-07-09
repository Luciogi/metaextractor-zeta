# This Python file uses the following encoding: utf-8
import sys
import os
from PySide6 import QtWidgets, QtCore
sys.path.append("lib")
from lib import *
from util import *
import pprint

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QtWidgets.QWidget):
    filesList = []

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.btnAdd.clicked.connect(self.openFileDialog)
        self.ui.btnRemove.clicked.connect(self.removeListWidgetItem)
        self.ui.btnClearAll.clicked.connect(self.clearList)
        self.ui.btnExtract.clicked.connect(self.extractFromAll)
        self.ui.listWidget.itemDoubleClicked.connect(self.showFileMetadata)

    def openFileDialog(self):
        files= QtWidgets.QFileDialog.getOpenFileNames(
                                self,
                                "Select one or more files to open",
                                os.path.expanduser("~"))
        self.filesList = list(files[0])
        self.addListWidgetItems()

    # load files into listWidget
    def addListWidgetItems(self):
        self.ui.listWidget.addItems(self.filesList)

    def removeListWidgetItem(self):
        currentRow = self.ui.listWidget.currentRow()
        self.ui.listWidget.takeItem(currentRow)
        if len(self.filesList):
            self.filesList.pop(currentRow)  # Mannual poping item from List is required

    def clearList(self):
        self.ui.listWidget.clear()

    def showFileMetadata(self):
        currentFile = self.ui.listWidget.currentItem().text()
        metadata = extract_metadata_file(currentFile)

        self.window = OutputWindow()
        self.window.setWindowTitle(f"Metadata - {currentFile}")

        self.window.text.setText(pprint.pformat(metadata))
        self.window.show()

    def extractFromAll(self):
        create_result_folder()
        for file in self.filesList:
            metadata = extract_metadata_file(file)
            metadata = add_meta_metadata(metadata, file)
            write_pdf(file, metadata)

        messageBox = QtWidgets.QMessageBox(self)
        messageBox.setWindowTitle("Dialog")
        messageBox.setIcon(QtWidgets.QMessageBox.Information)
        messageBox.setText("Sucessfully Extracted Metadata from files")
        messageBox.setInformativeText(f"Check ./{OUTPUT_DIR}/")
        messageBox.exec()


class OutputWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        layout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel("Metadata")
        self.text = QtWidgets.QTextEdit()
        self.text.setReadOnly(True)

        layout.addWidget(self.label)
        layout.addWidget(self.text)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())

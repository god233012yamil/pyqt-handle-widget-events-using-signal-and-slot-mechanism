import sys
from PyQt5.QtWidgets import \
    QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5 import QtCore


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()

        # Create a push button and connect its signal "clicked"
        # with the Slot "PushButtonSlot"
        self.button1 = QPushButton("Click me")
        self.button1.setFixedSize(80, 25)
        self.button1.setObjectName("button1")
        self.button1.clicked.connect(self.PushButtonSlot)

        # Create a push button and connect its signal "released"
        # with the Slot "PushButtonSlot"
        self.button2 = QPushButton("Release me")
        self.button2.setFixedSize(80, 25)
        self.button2.setObjectName("button2")
        self.button2.released.connect(self.PushButtonSlot)

        # Create a push button and connect its signal "pressed"
        # with the Slot "PushButtonSlot"
        self.button3 = QPushButton("Press me")
        self.button3.setFixedSize(80, 25)
        self.button3.setObjectName("button3")
        self.button3.pressed.connect(self.PushButtonSlot)

        # Create a horizontal layout and add three push buttons to it.
        self.horiz_layout = QHBoxLayout()
        self.horiz_layout.addWidget(self.button1, Qt.AlignCenter)
        self.horiz_layout.addWidget(self.button2, Qt.AlignCenter)
        self.horiz_layout.addWidget(self.button3, Qt.AlignCenter)

        # Create a Window with three push buttons layout horizontally.
        self.widget = QWidget(self)
        self.widget.setLayout(self.horiz_layout)
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Signal and Slot")

    @QtCore.pyqtSlot()
    def PushButtonSlot(self) -> None:
        # Get the object (PushButton) who called this Slot.
        object_sender = self.sender()

        # If the push button 1 was clicked.
        if object_sender.objectName() == "button1":
            # then show in the status bar a message.
            self.statusBar().showMessage("Button was clicked")

        # If the push button 2 was released.
        elif object_sender.objectName() == "button2":
            self.statusBar().showMessage("Button was released")

        # If the push button 3 was pressed.
        elif object_sender.objectName() == "button3":
            self.statusBar().showMessage("Button was pressed")

        else:
            pass


if __name__ == '__main__':
    # Qt requires one QApplication object.
    app = QApplication(sys.argv)

    # Create an instance of the class MainWindow.
    window = MainWindow()

    # Show the window.
    window.show()

    # Start Qt event loop.
    sys.exit(app.exec_())
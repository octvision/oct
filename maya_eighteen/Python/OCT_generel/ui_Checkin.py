# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_Checkin.ui'
#
# Created: Mon Aug 12 10:54:27 2013
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(660, 541)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_1 = QtGui.QHBoxLayout()
        self.horizontalLayout_1.setSpacing(0)
        self.horizontalLayout_1.setObjectName(_fromUtf8("horizontalLayout_1"))
        self.myLabel1 = QtGui.QLabel(self.centralwidget)
        self.myLabel1.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.myLabel1.setMinimumSize(QtCore.QSize(100, 0))
        self.myLabel1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.myLabel1.setObjectName(_fromUtf8("myLabel1"))
        self.horizontalLayout_1.addWidget(self.myLabel1)
        self.sourceLabel = QtGui.QLabel(self.centralwidget)
        self.sourceLabel.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.sourceLabel.setObjectName(_fromUtf8("sourceLabel"))
        self.horizontalLayout_1.addWidget(self.sourceLabel)
        self.horizontalLayout_1.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.myLabel2 = QtGui.QLabel(self.centralwidget)
        self.myLabel2.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.myLabel2.setMinimumSize(QtCore.QSize(100, 0))
        self.myLabel2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.myLabel2.setObjectName(_fromUtf8("myLabel2"))
        self.horizontalLayout_2.addWidget(self.myLabel2)
        self.filenameLabel1 = QtGui.QLabel(self.centralwidget)
        self.filenameLabel1.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.filenameLabel1.setObjectName(_fromUtf8("filenameLabel1"))
        self.horizontalLayout_2.addWidget(self.filenameLabel1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.myLabel3 = QtGui.QLabel(self.centralwidget)
        self.myLabel3.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.myLabel3.setMinimumSize(QtCore.QSize(100, 0))
        self.myLabel3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.myLabel3.setObjectName(_fromUtf8("myLabel3"))
        self.horizontalLayout_3.addWidget(self.myLabel3)
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_3.setLineWidth(1)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frame = QtGui.QFrame(self.frame_3)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setLineWidth(1)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.myLabel4 = QtGui.QLabel(self.frame)
        self.myLabel4.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.myLabel4.setMinimumSize(QtCore.QSize(50, 30))
        self.myLabel4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.myLabel4.setAlignment(QtCore.Qt.AlignCenter)
        self.myLabel4.setObjectName(_fromUtf8("myLabel4"))
        self.horizontalLayout_4.addWidget(self.myLabel4)
        self.myLabel5 = QtGui.QLabel(self.frame)
        self.myLabel5.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.myLabel5.setMinimumSize(QtCore.QSize(210, 30))
        self.myLabel5.setAlignment(QtCore.Qt.AlignCenter)
        self.myLabel5.setObjectName(_fromUtf8("myLabel5"))
        self.horizontalLayout_4.addWidget(self.myLabel5)
        self.myLabel6 = QtGui.QLabel(self.frame)
        self.myLabel6.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.myLabel6.setMinimumSize(QtCore.QSize(75, 30))
        self.myLabel6.setMaximumSize(QtCore.QSize(80, 16777215))
        self.myLabel6.setAlignment(QtCore.Qt.AlignCenter)
        self.myLabel6.setObjectName(_fromUtf8("myLabel6"))
        self.horizontalLayout_4.addWidget(self.myLabel6)
        self.myLabel7 = QtGui.QLabel(self.frame)
        self.myLabel7.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.myLabel7.setMinimumSize(QtCore.QSize(50, 30))
        self.myLabel7.setMaximumSize(QtCore.QSize(60, 16777215))
        self.myLabel7.setAlignment(QtCore.Qt.AlignCenter)
        self.myLabel7.setObjectName(_fromUtf8("myLabel7"))
        self.horizontalLayout_4.addWidget(self.myLabel7)
        self.myLabel8 = QtGui.QLabel(self.frame)
        self.myLabel8.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.myLabel8.setMinimumSize(QtCore.QSize(80, 30))
        self.myLabel8.setMaximumSize(QtCore.QSize(80, 16777215))
        self.myLabel8.setAlignment(QtCore.Qt.AlignCenter)
        self.myLabel8.setObjectName(_fromUtf8("myLabel8"))
        self.horizontalLayout_4.addWidget(self.myLabel8)
        self.myLabel9 = QtGui.QLabel(self.frame)
        self.myLabel9.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.myLabel9.setMinimumSize(QtCore.QSize(60, 30))
        self.myLabel9.setMaximumSize(QtCore.QSize(60, 16777215))
        self.myLabel9.setAlignment(QtCore.Qt.AlignCenter)
        self.myLabel9.setObjectName(_fromUtf8("myLabel9"))
        self.horizontalLayout_4.addWidget(self.myLabel9)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(self.frame_3)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_2.setMidLineWidth(0)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setMargin(0)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.idLabel = QtGui.QLabel(self.frame_2)
        self.idLabel.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.idLabel.setMinimumSize(QtCore.QSize(50, 30))
        self.idLabel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.idLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.idLabel.setObjectName(_fromUtf8("idLabel"))
        self.horizontalLayout_9.addWidget(self.idLabel)
        self.filenameLabel2 = QtGui.QLabel(self.frame_2)
        self.filenameLabel2.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.filenameLabel2.setMinimumSize(QtCore.QSize(210, 30))
        self.filenameLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.filenameLabel2.setObjectName(_fromUtf8("filenameLabel2"))
        self.horizontalLayout_9.addWidget(self.filenameLabel2)
        self.timeLabel = QtGui.QLabel(self.frame_2)
        self.timeLabel.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.timeLabel.setMinimumSize(QtCore.QSize(75, 30))
        self.timeLabel.setMaximumSize(QtCore.QSize(80, 16777215))
        self.timeLabel.setObjectName(_fromUtf8("timeLabel"))
        self.horizontalLayout_9.addWidget(self.timeLabel)
        self.ProgressLabel = QtGui.QLabel(self.frame_2)
        self.ProgressLabel.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.ProgressLabel.setMinimumSize(QtCore.QSize(50, 30))
        self.ProgressLabel.setMaximumSize(QtCore.QSize(60, 16777215))
        self.ProgressLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ProgressLabel.setObjectName(_fromUtf8("ProgressLabel"))
        self.horizontalLayout_9.addWidget(self.ProgressLabel)
        self.CreatorLabel = QtGui.QLabel(self.frame_2)
        self.CreatorLabel.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.CreatorLabel.setMinimumSize(QtCore.QSize(80, 30))
        self.CreatorLabel.setMaximumSize(QtCore.QSize(80, 16777215))
        self.CreatorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CreatorLabel.setObjectName(_fromUtf8("CreatorLabel"))
        self.horizontalLayout_9.addWidget(self.CreatorLabel)
        self.CommentsLlabel = QtGui.QLabel(self.frame_2)
        self.CommentsLlabel.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.CommentsLlabel.setMinimumSize(QtCore.QSize(60, 30))
        self.CommentsLlabel.setMaximumSize(QtCore.QSize(60, 16777215))
        self.CommentsLlabel.setText(_fromUtf8(""))
        self.CommentsLlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CommentsLlabel.setObjectName(_fromUtf8("CommentsLlabel"))
        self.horizontalLayout_9.addWidget(self.CommentsLlabel)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(1)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.myLabel10 = QtGui.QLabel(self.centralwidget)
        self.myLabel10.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.myLabel10.setMinimumSize(QtCore.QSize(100, 0))
        self.myLabel10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.myLabel10.setObjectName(_fromUtf8("myLabel10"))
        self.horizontalLayout_5.addWidget(self.myLabel10)
        self.spinBox = QtGui.QSpinBox(self.centralwidget)
        self.spinBox.setMinimumSize(QtCore.QSize(60, 0))
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout_5.addWidget(self.spinBox)
        self.horizontalSlider = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.horizontalLayout_5.addWidget(self.horizontalSlider)
        self.horizontalLayout_5.setStretch(2, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.myLabel11 = QtGui.QLabel(self.centralwidget)
        self.myLabel11.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.myLabel11.setMinimumSize(QtCore.QSize(100, 0))
        self.myLabel11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.myLabel11.setObjectName(_fromUtf8("myLabel11"))
        self.horizontalLayout_6.addWidget(self.myLabel11)
        self.checkgroupBox = QtGui.QGroupBox(self.centralwidget)
        self.checkgroupBox.setTitle(_fromUtf8(""))
        self.checkgroupBox.setCheckable(False)
        self.checkgroupBox.setObjectName(_fromUtf8("checkgroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.checkgroupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.OptimizeCheckBox = QtGui.QCheckBox(self.checkgroupBox)
        self.OptimizeCheckBox.setChecked(True)
        self.OptimizeCheckBox.setObjectName(_fromUtf8("OptimizeCheckBox"))
        self.verticalLayout.addWidget(self.OptimizeCheckBox)
        self.copyMapsCheckBox = QtGui.QCheckBox(self.checkgroupBox)
        self.copyMapsCheckBox.setChecked(True)
        self.copyMapsCheckBox.setObjectName(_fromUtf8("copyMapsCheckBox"))
        self.verticalLayout.addWidget(self.copyMapsCheckBox)
        self.removeCheckBox = QtGui.QCheckBox(self.checkgroupBox)
        self.removeCheckBox.setChecked(True)
        self.removeCheckBox.setObjectName(_fromUtf8("removeCheckBox"))
        self.verticalLayout.addWidget(self.removeCheckBox)
        self.copyCacheCheckBo = QtGui.QCheckBox(self.checkgroupBox)
        self.copyCacheCheckBo.setObjectName(_fromUtf8("copyCacheCheckBo"))
        self.verticalLayout.addWidget(self.copyCacheCheckBo)
        self.horizontalLayout_6.addWidget(self.checkgroupBox)
        self.horizontalLayout_6.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.myLabel12 = QtGui.QLabel(self.centralwidget)
        self.myLabel12.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.myLabel12.setMinimumSize(QtCore.QSize(100, 0))
        self.myLabel12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.myLabel12.setObjectName(_fromUtf8("myLabel12"))
        self.horizontalLayout_7.addWidget(self.myLabel12)
        self.addVideoPushButton = QtGui.QPushButton(self.centralwidget)
        self.addVideoPushButton.setMinimumSize(QtCore.QSize(80, 30))
        self.addVideoPushButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.addVideoPushButton.setObjectName(_fromUtf8("addVideoPushButton"))
        self.horizontalLayout_7.addWidget(self.addVideoPushButton)
        self.videoPath = QtGui.QLabel(self.centralwidget)
        self.videoPath.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.videoPath.setMinimumSize(QtCore.QSize(0, 30))
        self.videoPath.setAlignment(QtCore.Qt.AlignCenter)
        self.videoPath.setObjectName(_fromUtf8("videoPath"))
        self.horizontalLayout_7.addWidget(self.videoPath)
        self.horizontalLayout_7.setStretch(2, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.myLabel13 = QtGui.QLabel(self.centralwidget)
        self.myLabel13.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.myLabel13.setMinimumSize(QtCore.QSize(100, 0))
        self.myLabel13.setMaximumSize(QtCore.QSize(100, 16777215))
        self.myLabel13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.myLabel13.setObjectName(_fromUtf8("myLabel13"))
        self.horizontalLayout_8.addWidget(self.myLabel13)
        self.addImagePushButton = QtGui.QPushButton(self.centralwidget)
        self.addImagePushButton.setMinimumSize(QtCore.QSize(80, 0))
        self.addImagePushButton.setMaximumSize(QtCore.QSize(80, 1000000))
        self.addImagePushButton.setObjectName(_fromUtf8("addImagePushButton"))
        self.horizontalLayout_8.addWidget(self.addImagePushButton)
        self.imagesViewLabel = QtGui.QLabel(self.centralwidget)
        self.imagesViewLabel.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.imagesViewLabel.setMinimumSize(QtCore.QSize(50, 0))
        self.imagesViewLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.imagesViewLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imagesViewLabel.setObjectName(_fromUtf8("imagesViewLabel"))
        self.horizontalLayout_8.addWidget(self.imagesViewLabel)
        self.horizontalLayout_8.setStretch(2, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.myLabel14 = QtGui.QLabel(self.centralwidget)
        self.myLabel14.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.myLabel14.setMinimumSize(QtCore.QSize(100, 0))
        self.myLabel14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.myLabel14.setObjectName(_fromUtf8("myLabel14"))
        self.horizontalLayout_10.addWidget(self.myLabel14)
        self.myLabel15 = QtGui.QLabel(self.centralwidget)
        self.myLabel15.setFrameStyle(QtGui.QFrame.StyledPanel)
        self.myLabel15.setObjectName(_fromUtf8("myLabel15"))
        self.horizontalLayout_10.addWidget(self.myLabel15)
        self.horizontalLayout_10.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.checkinPushButton = QtGui.QPushButton(self.centralwidget)
        self.checkinPushButton.setObjectName(_fromUtf8("checkinPushButton"))
        self.checkinPushButton.setMinimumSize(QtCore.QSize(150, 35))
        self.horizontalLayout_11.addWidget(self.checkinPushButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_3.setStretch(6, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 660, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtGui.QStatusBar(MainWindow)
        # self.statusbar.setObjectName(_fromUtf8("statusbar"))
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Checkin", None, QtGui.QApplication.UnicodeUTF8))
        self.myLabel1.setText(QtGui.QApplication.translate("MainWindow", "Source: ", None, QtGui.QApplication.UnicodeUTF8))
        self.sourceLabel.setText(QtGui.QApplication.translate("MainWindow", "D:work\Test\scenes\Test.mb", None, QtGui.QApplication.UnicodeUTF8))
        self.myLabel2.setText(QtGui.QApplication.translate("MainWindow", "Filename: ", None, QtGui.QApplication.UnicodeUTF8))
        self.filenameLabel1.setText(QtGui.QApplication.translate("MainWindow", "Test.mb", None, QtGui.QApplication.UnicodeUTF8))
        self.myLabel3.setText(QtGui.QApplication.translate("MainWindow", "History: ", None, QtGui.QApplication.UnicodeUTF8))
        self.myLabel4.setText(QtGui.QApplication.translate("MainWindow", "ID", None, QtGui.QApplication.UnicodeUTF8))
        self.myLabel5.setText(QtGui.QApplication.translate("MainWindow", "Filename", None, QtGui.QApplication.UnicodeUTF8))
        self.myLabel6.setText(QtGui.QApplication.translate("MainWindow", "Time", None, QtGui.QApplication.UnicodeUTF8))
        self.myLabel7.setText(QtGui.QApplication.translate("MainWindow", "Progress", None, QtGui.QApplication.UnicodeUTF8))
        self.myLabel8.setText(QtGui.QApplication.translate("MainWindow", "Creator", None, QtGui.QApplication.UnicodeUTF8))
        self.myLabel9.setText(QtGui.QApplication.translate("MainWindow", "Comments", None, QtGui.QApplication.UnicodeUTF8))
        self.idLabel.setText(QtGui.QApplication.translate("MainWindow", "89451", None, QtGui.QApplication.UnicodeUTF8))
        self.filenameLabel2.setText(QtGui.QApplication.translate("MainWindow", "Test.mb", None, QtGui.QApplication.UnicodeUTF8))
        self.timeLabel.setText(QtGui.QApplication.translate("MainWindow", "08_09 11:00", None, QtGui.QApplication.UnicodeUTF8))
        self.ProgressLabel.setText(QtGui.QApplication.translate("MainWindow", "50", None, QtGui.QApplication.UnicodeUTF8))
        self.CreatorLabel.setText(QtGui.QApplication.translate("MainWindow", u"Peter", None, QtGui.QApplication.UnicodeUTF8))
        self.myLabel10.setText(QtGui.QApplication.translate("MainWindow", "Progress: ", None, QtGui.QApplication.UnicodeUTF8))
        self.myLabel11.setText(QtGui.QApplication.translate("MainWindow", "Optimize: ", None, QtGui.QApplication.UnicodeUTF8))
        self.OptimizeCheckBox.setText(QtGui.QApplication.translate("MainWindow", "Optimize Scene Size", None, QtGui.QApplication.UnicodeUTF8))
        self.copyMapsCheckBox.setText(QtGui.QApplication.translate("MainWindow", "Copy Local Maps", None, QtGui.QApplication.UnicodeUTF8))
        self.removeCheckBox.setText(QtGui.QApplication.translate("MainWindow", "Remove All Image Planes", None, QtGui.QApplication.UnicodeUTF8))
        self.copyCacheCheckBo.setText(QtGui.QApplication.translate("MainWindow", "Copy Cache", None, QtGui.QApplication.UnicodeUTF8))
        self.myLabel12.setText(QtGui.QApplication.translate("MainWindow", "Comments: ", None, QtGui.QApplication.UnicodeUTF8))
        self.addVideoPushButton.setText(QtGui.QApplication.translate("MainWindow", "Add Video", None, QtGui.QApplication.UnicodeUTF8))
        self.videoPath.setText(QtGui.QApplication.translate("MainWindow", "Video Path", None, QtGui.QApplication.UnicodeUTF8))
        self.myLabel13.setText(QtGui.QApplication.translate("MainWindow", "Render Images: ", None, QtGui.QApplication.UnicodeUTF8))
        self.addImagePushButton.setText(QtGui.QApplication.translate("MainWindow", "Add Image", None, QtGui.QApplication.UnicodeUTF8))
        self.imagesViewLabel.setText(QtGui.QApplication.translate("MainWindow", "Images View Area", None, QtGui.QApplication.UnicodeUTF8))
        self.myLabel14.setText(QtGui.QApplication.translate("MainWindow", u"存盘方式提示:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.myLabel15.setText(QtGui.QApplication.translate("MainWindow", u'''Checkin之前先存盘，Checkin之后不要存盘。\n这是因为Checkin过程为：优化场景->另存为临时文件->上传临时文件。\nCheckin之后不存盘，就算万一Checkin的优化程序有误，也不会损坏本机文件。''', None, QtGui.QApplication.UnicodeUTF8))
        self.checkinPushButton.setText(QtGui.QApplication.translate("MainWindow", "CheckIn", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", u"TD:赵志杰、钟文洲", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
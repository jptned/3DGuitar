# -*- coding: utf-8 -*-
 
# Form implementation generated from reading ui file 'v1.ui'
#
#      by: PyQt5 UI code generator
#      WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import Draft, math, Part, Sketcher, FreeCAD, FreeCADGui

class Ui_Dialog(object):
    #def __init__(self):
    #    self.didRun = false;

    def setupUi(self, Dialog):
        #if (self.didRun):
        #    print ("Did run!")
        #else:
        #    print ("Didn't run!")
        Dialog.setObjectName("3D Guitar Designer")
        Dialog.resize(527, 420)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget = QtGui.QWidget(self.tab_2)
        self.widget.setGeometry(QtCore.QRect(20, 20, 461, 221))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_fretboardLength_13 = QtGui.QLabel(self.widget)
        self.label_fretboardLength_13.setObjectName("label_fretboardLength_13")
        self.verticalLayout_2.addWidget(self.label_fretboardLength_13)
        self.bodyLength = QtGui.QDoubleSpinBox(self.widget)
        self.bodyLength.setPrefix("")
        self.bodyLength.setSuffix("")
        self.bodyLength.setDecimals(1)
        self.bodyLength.setMinimum(0.1)
        self.bodyLength.setMaximum(10000.0)
        self.bodyLength.setSingleStep(0.1)
        self.bodyLength.setProperty("value", 800.0)
        self.bodyLength.setObjectName("bodyLength")
        self.verticalLayout_2.addWidget(self.bodyLength)
        self.label_fretboardLength_11 = QtGui.QLabel(self.widget)
        self.label_fretboardLength_11.setObjectName("label_fretboardLength_11")
        self.verticalLayout_2.addWidget(self.label_fretboardLength_11)
        self.bodyWidth = QtGui.QDoubleSpinBox(self.widget)
        self.bodyWidth.setPrefix("")
        self.bodyWidth.setSuffix("")
        self.bodyWidth.setDecimals(1)
        self.bodyWidth.setMinimum(0.1)
        self.bodyWidth.setMaximum(1000.0)
        self.bodyWidth.setSingleStep(0.1)
        self.bodyWidth.setProperty("value", 85.0)
        self.bodyWidth.setObjectName("bodyWidth")
        self.verticalLayout_2.addWidget(self.bodyWidth)
        self.label_fretboardLength_10 = QtGui.QLabel(self.widget)
        self.label_fretboardLength_10.setObjectName("label_fretboardLength_10")
        self.verticalLayout_2.addWidget(self.label_fretboardLength_10)
        self.bodThickness = QtGui.QDoubleSpinBox(self.widget)
        self.bodThickness.setPrefix("")
        self.bodThickness.setSuffix("")
        self.bodThickness.setDecimals(1)
        self.bodThickness.setMinimum(0.1)
        self.bodThickness.setMaximum(1000.0)
        self.bodThickness.setSingleStep(0.1)
        self.bodThickness.setProperty("value", 80.0)
        self.bodThickness.setObjectName("bodThickness")
        self.verticalLayout_2.addWidget(self.bodThickness)
        self.label_fretboardLength_14 = QtGui.QLabel(self.widget)
        self.label_fretboardLength_14.setObjectName("label_fretboardLength_14")
        self.verticalLayout_2.addWidget(self.label_fretboardLength_14)
        self.arcRatio = QtGui.QDoubleSpinBox(self.widget)
        self.arcRatio.setPrefix("")
        self.arcRatio.setSuffix("")
        self.arcRatio.setDecimals(2)
        self.arcRatio.setMinimum(0.1)
        self.arcRatio.setMaximum(1000.0)
        self.arcRatio.setSingleStep(0.1)
        self.arcRatio.setProperty("value", 1.26)
        self.arcRatio.setObjectName("arcRatio")
        self.verticalLayout_2.addWidget(self.arcRatio)
        self.label_fretboardLength_12 = QtGui.QLabel(self.widget)
        self.label_fretboardLength_12.setObjectName("label_fretboardLength_12")
        self.verticalLayout_2.addWidget(self.label_fretboardLength_12)
        self.bodyConnectAngle = QtGui.QDoubleSpinBox(self.widget)
        self.bodyConnectAngle.setPrefix("")
        self.bodyConnectAngle.setSuffix("")
        self.bodyConnectAngle.setDecimals(1)
        self.bodyConnectAngle.setMinimum(0.0)
        self.bodyConnectAngle.setMaximum(360.0)
        self.bodyConnectAngle.setSingleStep(0.1)
        self.bodyConnectAngle.setProperty("value", 30.0)
        self.bodyConnectAngle.setObjectName("bodyConnectAngle")
        self.verticalLayout_2.addWidget(self.bodyConnectAngle)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtGui.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 461, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_fretboardLength = QtGui.QLabel(self.layoutWidget)
        self.label_fretboardLength.setObjectName("label_fretboardLength")
        self.verticalLayout_3.addWidget(self.label_fretboardLength)
        self.fretboardLength = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.fretboardLength.setPrefix("")
        self.fretboardLength.setSuffix("")
        self.fretboardLength.setDecimals(1)
        self.fretboardLength.setMinimum(0.1)
        self.fretboardLength.setMaximum(1000.0)
        self.fretboardLength.setSingleStep(0.1)
        self.fretboardLength.setProperty("value", 500.0)
        self.fretboardLength.setObjectName("fretboardLength")
        self.verticalLayout_3.addWidget(self.fretboardLength)
        self.label_fretboardLength_2 = QtGui.QLabel(self.layoutWidget)
        self.label_fretboardLength_2.setObjectName("label_fretboardLength_2")
        self.verticalLayout_3.addWidget(self.label_fretboardLength_2)
        self.fretboardWidthNarrow = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.fretboardWidthNarrow.setPrefix("")
        self.fretboardWidthNarrow.setSuffix("")
        self.fretboardWidthNarrow.setDecimals(1)
        self.fretboardWidthNarrow.setMinimum(0.1)
        self.fretboardWidthNarrow.setMaximum(1000.0)
        self.fretboardWidthNarrow.setSingleStep(0.1)
        self.fretboardWidthNarrow.setProperty("value", 40.0)
        self.fretboardWidthNarrow.setObjectName("fretboardWidthNarrow")
        self.verticalLayout_3.addWidget(self.fretboardWidthNarrow)
        self.label_fretboardLength_3 = QtGui.QLabel(self.layoutWidget)
        self.label_fretboardLength_3.setObjectName("label_fretboardLength_3")
        self.verticalLayout_3.addWidget(self.label_fretboardLength_3)
        self.fretboardWidthWide = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.fretboardWidthWide.setPrefix("")
        self.fretboardWidthWide.setSuffix("")
        self.fretboardWidthWide.setDecimals(1)
        self.fretboardWidthWide.setMinimum(0.1)
        self.fretboardWidthWide.setMaximum(1000.0)
        self.fretboardWidthWide.setSingleStep(0.1)
        self.fretboardWidthWide.setProperty("value", 15.0)
        self.fretboardWidthWide.setObjectName("fretboardWidthWide")
        self.verticalLayout_3.addWidget(self.fretboardWidthWide)
        self.label_fretboardLength_4 = QtGui.QLabel(self.layoutWidget)
        self.label_fretboardLength_4.setObjectName("label_fretboardLength_4")
        self.verticalLayout_3.addWidget(self.label_fretboardLength_4)
        self.fretboardHeight = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.fretboardHeight.setPrefix("")
        self.fretboardHeight.setSuffix("")
        self.fretboardHeight.setDecimals(1)
        self.fretboardHeight.setMinimum(0.1)
        self.fretboardHeight.setMaximum(1000.0)
        self.fretboardHeight.setSingleStep(0.1)
        self.fretboardHeight.setProperty("value", 15.0)
        self.fretboardHeight.setObjectName("fretboardHeight")
        self.verticalLayout_3.addWidget(self.fretboardHeight)
        self.label_fretboardLength_5 = QtGui.QLabel(self.layoutWidget)
        self.label_fretboardLength_5.setObjectName("label_fretboardLength_5")
        self.verticalLayout_3.addWidget(self.label_fretboardLength_5)
        self.fretboardRoundingRadius = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.fretboardRoundingRadius.setPrefix("")
        self.fretboardRoundingRadius.setSuffix("")
        self.fretboardRoundingRadius.setDecimals(1)
        self.fretboardRoundingRadius.setMinimum(0.1)
        self.fretboardRoundingRadius.setMaximum(1000.0)
        self.fretboardRoundingRadius.setSingleStep(0.1)
        self.fretboardRoundingRadius.setProperty("value", 15.0)
        self.fretboardRoundingRadius.setObjectName("fretboardRoundingRadius")
        self.verticalLayout_3.addWidget(self.fretboardRoundingRadius)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget1 = QtGui.QWidget(self.tab_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 20, 461, 176))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_fretboardLength_8 = QtGui.QLabel(self.layoutWidget1)
        self.label_fretboardLength_8.setObjectName("label_fretboardLength_8")
        self.verticalLayout_4.addWidget(self.label_fretboardLength_8)
        self.headLength = QtGui.QDoubleSpinBox(self.layoutWidget1)
        self.headLength.setPrefix("")
        self.headLength.setSuffix("")
        self.headLength.setDecimals(1)
        self.headLength.setMinimum(0.1)
        self.headLength.setMaximum(1000.0)
        self.headLength.setSingleStep(0.1)
        self.headLength.setProperty("value", 150.0)
        self.headLength.setObjectName("headLength")
        self.verticalLayout_4.addWidget(self.headLength)
        self.label_fretboardLength_6 = QtGui.QLabel(self.layoutWidget1)
        self.label_fretboardLength_6.setObjectName("label_fretboardLength_6")
        self.verticalLayout_4.addWidget(self.label_fretboardLength_6)
        self.headWidth = QtGui.QDoubleSpinBox(self.layoutWidget1)
        self.headWidth.setPrefix("")
        self.headWidth.setSuffix("")
        self.headWidth.setDecimals(1)
        self.headWidth.setMinimum(0.1)
        self.headWidth.setMaximum(1000.0)
        self.headWidth.setSingleStep(0.1)
        self.headWidth.setProperty("value", 80.0)
        self.headWidth.setObjectName("headWidth")
        self.verticalLayout_4.addWidget(self.headWidth)
        self.label_fretboardLength_9 = QtGui.QLabel(self.layoutWidget1)
        self.label_fretboardLength_9.setObjectName("label_fretboardLength_9")
        self.verticalLayout_4.addWidget(self.label_fretboardLength_9)
        self.headHeight = QtGui.QDoubleSpinBox(self.layoutWidget1)
        self.headHeight.setPrefix("")
        self.headHeight.setSuffix("")
        self.headHeight.setDecimals(1)
        self.headHeight.setMinimum(0.1)
        self.headHeight.setMaximum(1000.0)
        self.headHeight.setSingleStep(0.1)
        self.headHeight.setProperty("value", 15.0)
        self.headHeight.setObjectName("headHeight")
        self.verticalLayout_4.addWidget(self.headHeight)
        self.label_fretboardLength_7 = QtGui.QLabel(self.layoutWidget1)
        self.label_fretboardLength_7.setObjectName("label_fretboardLength_7")
        self.verticalLayout_4.addWidget(self.label_fretboardLength_7)
        self.headMarchLength = QtGui.QDoubleSpinBox(self.layoutWidget1)
        self.headMarchLength.setPrefix("")
        self.headMarchLength.setSuffix("")
        self.headMarchLength.setDecimals(1)
        self.headMarchLength.setMinimum(0.0)
        self.headMarchLength.setMaximum(100.0)
        self.headMarchLength.setSingleStep(0.1)
        self.headMarchLength.setProperty("value", 15.0)
        self.headMarchLength.setObjectName("headMarchLength")
        self.verticalLayout_4.addWidget(self.headMarchLength)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.widget1 = QtGui.QWidget(self.tab_4)
        self.widget1.setGeometry(QtCore.QRect(20, 20, 461, 176))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_fretboardLength_15 = QtGui.QLabel(self.widget1)
        self.label_fretboardLength_15.setObjectName("label_fretboardLength_15")
        self.verticalLayout_5.addWidget(self.label_fretboardLength_15)
        self.cutawayType = QtGui.QDoubleSpinBox(self.widget1)
        self.cutawayType.setPrefix("")
        self.cutawayType.setSuffix("")
        self.cutawayType.setDecimals(0)
        self.cutawayType.setMinimum(0.0)
        self.cutawayType.setMaximum(1.0)
        self.cutawayType.setSingleStep(1.0)
        self.cutawayType.setProperty("value", 1.0)
        self.cutawayType.setObjectName("cutawayType")
        self.verticalLayout_5.addWidget(self.cutawayType)
        self.label_fretboardLength_16 = QtGui.QLabel(self.widget1)
        self.label_fretboardLength_16.setObjectName("label_fretboardLength_16")
        self.verticalLayout_5.addWidget(self.label_fretboardLength_16)
        self.cutawayOffset = QtGui.QDoubleSpinBox(self.widget1)
        self.cutawayOffset.setPrefix("")
        self.cutawayOffset.setSuffix("")
        self.cutawayOffset.setDecimals(1)
        self.cutawayOffset.setMinimum(0.1)
        self.cutawayOffset.setMaximum(1000.0)
        self.cutawayOffset.setSingleStep(0.1)
        self.cutawayOffset.setProperty("value", 10.0)
        self.cutawayOffset.setObjectName("cutawayOffset")
        self.verticalLayout_5.addWidget(self.cutawayOffset)
        self.label_fretboardLength_17 = QtGui.QLabel(self.widget1)
        self.label_fretboardLength_17.setObjectName("label_fretboardLength_17")
        self.verticalLayout_5.addWidget(self.label_fretboardLength_17)
        self.cutawayDepth = QtGui.QDoubleSpinBox(self.widget1)
        self.cutawayDepth.setPrefix("")
        self.cutawayDepth.setSuffix("")
        self.cutawayDepth.setDecimals(1)
        self.cutawayDepth.setMinimum(0.1)
        self.cutawayDepth.setMaximum(1000.0)
        self.cutawayDepth.setSingleStep(0.1)
        self.cutawayDepth.setProperty("value", 25.0)
        self.cutawayDepth.setObjectName("cutawayDepth")
        self.verticalLayout_5.addWidget(self.cutawayDepth)
        self.label_fretboardLength_18 = QtGui.QLabel(self.widget1)
        self.label_fretboardLength_18.setObjectName("label_fretboardLength_18")
        self.verticalLayout_5.addWidget(self.label_fretboardLength_18)
        self.cutawayRad = QtGui.QDoubleSpinBox(self.widget1)
        self.cutawayRad.setPrefix("")
        self.cutawayRad.setSuffix("")
        self.cutawayRad.setDecimals(1)
        self.cutawayRad.setMinimum(0.1)
        self.cutawayRad.setMaximum(1000.0)
        self.cutawayRad.setSingleStep(0.1)
        self.cutawayRad.setProperty("value", 100.0)
        self.cutawayRad.setObjectName("cutawayRad")
        self.verticalLayout_5.addWidget(self.cutawayRad)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.widget2 = QtGui.QWidget(self.tab_5)
        self.widget2.setGeometry(QtCore.QRect(20, 20, 461, 266))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.widget2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_fretboardLength_19 = QtGui.QLabel(self.widget2)
        self.label_fretboardLength_19.setObjectName("label_fretboardLength_19")
        self.verticalLayout_6.addWidget(self.label_fretboardLength_19)
        self.pickups = QtGui.QDoubleSpinBox(self.widget2)
        self.pickups.setPrefix("")
        self.pickups.setSuffix("")
        self.pickups.setDecimals(0)
        self.pickups.setMinimum(0.0)
        self.pickups.setMaximum(1.0)
        self.pickups.setSingleStep(1.0)
        self.pickups.setProperty("value", 1.0)
        self.pickups.setObjectName("pickups")
        self.verticalLayout_6.addWidget(self.pickups)
        self.label_fretboardLength_20 = QtGui.QLabel(self.widget2)
        self.label_fretboardLength_20.setObjectName("label_fretboardLength_20")
        self.verticalLayout_6.addWidget(self.label_fretboardLength_20)
        self.pickupWidth = QtGui.QDoubleSpinBox(self.widget2)
        self.pickupWidth.setPrefix("")
        self.pickupWidth.setSuffix("")
        self.pickupWidth.setDecimals(1)
        self.pickupWidth.setMinimum(0.1)
        self.pickupWidth.setMaximum(1000.0)
        self.pickupWidth.setSingleStep(0.1)
        self.pickupWidth.setProperty("value", 130.0)
        self.pickupWidth.setObjectName("pickupWidth")
        self.verticalLayout_6.addWidget(self.pickupWidth)
        self.label_fretboardLength_21 = QtGui.QLabel(self.widget2)
        self.label_fretboardLength_21.setObjectName("label_fretboardLength_21")
        self.verticalLayout_6.addWidget(self.label_fretboardLength_21)
        self.pickupHeight = QtGui.QDoubleSpinBox(self.widget2)
        self.pickupHeight.setPrefix("")
        self.pickupHeight.setSuffix("")
        self.pickupHeight.setDecimals(1)
        self.pickupHeight.setMinimum(0.1)
        self.pickupHeight.setMaximum(1000.0)
        self.pickupHeight.setSingleStep(0.1)
        self.pickupHeight.setProperty("value", 80.0)
        self.pickupHeight.setObjectName("pickupHeight")
        self.verticalLayout_6.addWidget(self.pickupHeight)
        self.label_fretboardLength_22 = QtGui.QLabel(self.widget2)
        self.label_fretboardLength_22.setObjectName("label_fretboardLength_22")
        self.verticalLayout_6.addWidget(self.label_fretboardLength_22)
        self.pickupDepth = QtGui.QDoubleSpinBox(self.widget2)
        self.pickupDepth.setPrefix("")
        self.pickupDepth.setSuffix("")
        self.pickupDepth.setDecimals(1)
        self.pickupDepth.setMinimum(0.1)
        self.pickupDepth.setMaximum(1000.0)
        self.pickupDepth.setSingleStep(0.1)
        self.pickupDepth.setProperty("value", 40.0)
        self.pickupDepth.setObjectName("pickupDepth")
        self.verticalLayout_6.addWidget(self.pickupDepth)
        self.label_fretboardLength_23 = QtGui.QLabel(self.widget2)
        self.label_fretboardLength_23.setObjectName("label_fretboardLength_23")
        self.verticalLayout_6.addWidget(self.label_fretboardLength_23)
        self.pickupNeckPosX = QtGui.QDoubleSpinBox(self.widget2)
        self.pickupNeckPosX.setPrefix("")
        self.pickupNeckPosX.setSuffix("")
        self.pickupNeckPosX.setDecimals(1)
        self.pickupNeckPosX.setMinimum(0.1)
        self.pickupNeckPosX.setMaximum(1000.0)
        self.pickupNeckPosX.setSingleStep(0.1)
        self.pickupNeckPosX.setProperty("value", 240.0)
        self.pickupNeckPosX.setObjectName("pickupNeckPosX")
        self.verticalLayout_6.addWidget(self.pickupNeckPosX)
        self.label_fretboardLength_24 = QtGui.QLabel(self.widget2)
        self.label_fretboardLength_24.setObjectName("label_fretboardLength_24")
        self.verticalLayout_6.addWidget(self.label_fretboardLength_24)
        self.pickupBodyPosX = QtGui.QDoubleSpinBox(self.widget2)
        self.pickupBodyPosX.setPrefix("")
        self.pickupBodyPosX.setSuffix("")
        self.pickupBodyPosX.setDecimals(1)
        self.pickupBodyPosX.setMinimum(0.1)
        self.pickupBodyPosX.setMaximum(1000.0)
        self.pickupBodyPosX.setSingleStep(0.1)
        self.pickupBodyPosX.setProperty("value", 500.0)
        self.pickupBodyPosX.setObjectName("pickupBodyPosX")
        self.verticalLayout_6.addWidget(self.pickupBodyPosX)
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.create = QtGui.QPushButton(Dialog)
        self.create.setObjectName("create")
        self.verticalLayout.addWidget(self.create)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)

        QtCore.QObject.connect(self.create,QtCore.SIGNAL("pressed()"),self.onSubmit)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "3D Guitar Designer"))
        self.label_fretboardLength_13.setText(_translate("Dialog", "Length"))
        self.bodyLength.setToolTip(_translate("Dialog", "<html><head/><body><p>Total length of the body</p></body></html>"))
        self.label_fretboardLength_11.setText(_translate("Dialog", "Width"))
        self.bodyWidth.setToolTip(_translate("Dialog", "<html><head/><body><p>Space between the start of the circles and the center of the body</p></body></html>"))
        self.label_fretboardLength_10.setText(_translate("Dialog", "Thickness"))
        self.bodThickness.setToolTip(_translate("Dialog", "<html><head/><body><p>Thickness of the total body</p></body></html>"))
        self.label_fretboardLength_14.setText(_translate("Dialog", "Arc ratio"))
        self.arcRatio.setToolTip(_translate("Dialog", "<html><head/><body><p>Sets ratio between upper and lower arc (1:arcRatio)</p></body></html>"))
        self.label_fretboardLength_12.setText(_translate("Dialog", "Connect angle (degrees)"))
        self.bodyConnectAngle.setToolTip(_translate("Dialog", "<html><head/><body><p>The size of the middle circle part in degrees</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Body"))
        self.label_fretboardLength.setText(_translate("Dialog", "Length"))
        self.fretboardLength.setToolTip(_translate("Dialog", "<html><head/><body><p>Length between body and end of fretboard</p></body></html>"))
        self.label_fretboardLength_2.setText(_translate("Dialog", "Width narrow side"))
        self.fretboardWidthNarrow.setToolTip(_translate("Dialog", "<html><head/><body><p>Width of fretboard at side of body</p></body></html>"))
        self.label_fretboardLength_3.setText(_translate("Dialog", "Width wide side"))
        self.fretboardWidthWide.setToolTip(_translate("Dialog", "<html><head/><body><p>Width of fretboard at top side</p></body></html>"))
        self.label_fretboardLength_4.setText(_translate("Dialog", "Heigth"))
        self.fretboardHeight.setToolTip(_translate("Dialog", "<html><head/><body><p>Heigth of fretboard</p></body></html>"))
        self.label_fretboardLength_5.setText(_translate("Dialog", "Rounding radius bottom"))
        self.fretboardRoundingRadius.setToolTip(_translate("Dialog", "<html><head/><body><p>Radius for rounding at bottom off fretboard</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Fretboard"))
        self.label_fretboardLength_8.setText(_translate("Dialog", "Length"))
        self.headLength.setToolTip(_translate("Dialog", "<html><head/><body><p>Length of head</p></body></html>"))
        self.label_fretboardLength_6.setText(_translate("Dialog", "Width"))
        self.headWidth.setToolTip(_translate("Dialog", "<html><head/><body><p>Width of head</p></body></html>"))
        self.label_fretboardLength_9.setText(_translate("Dialog", "Height"))
        self.headHeight.setToolTip(_translate("Dialog", "<html><head/><body><p>Height of head</p></body></html>"))
        self.label_fretboardLength_7.setText(_translate("Dialog", "Space until narrowing (%)"))
        self.headMarchLength.setToolTip(_translate("Dialog", "<html><head/><body><p>Space between fretboard and narrowing of head (percentage of head length)</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Head"))
        self.label_fretboardLength_15.setText(_translate("Dialog", "Type"))
        self.cutawayType.setToolTip(_translate("Dialog", "<html><head/><body><p>0 - Nothing<br/>1 - Venetian</p></body></html>"))
        self.label_fretboardLength_16.setText(_translate("Dialog", "Offset"))
        self.cutawayOffset.setToolTip(_translate("Dialog", "<html><head/><body><p>Position from neck</p></body></html>"))
        self.label_fretboardLength_17.setText(_translate("Dialog", "Depth"))
        self.cutawayDepth.setToolTip(_translate("Dialog", "<html><head/><body><p>Position in body</p></body></html>"))
        self.label_fretboardLength_18.setText(_translate("Dialog", "Radius"))
        self.cutawayRad.setToolTip(_translate("Dialog", "<html><head/><body><p>Radius of cutaway</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Cutaway"))
        self.label_fretboardLength_19.setText(_translate("Dialog", "Pickups"))
        self.pickups.setToolTip(_translate("Dialog", "<html><head/><body><p>Enable Pickups:</p><p>0 - No<br/>1 - Yes</p></body></html>"))
        self.label_fretboardLength_20.setText(_translate("Dialog", "Width"))
        self.pickupWidth.setToolTip(_translate("Dialog", "<html><head/><body><p>Width of pickup</p></body></html>"))
        self.label_fretboardLength_21.setText(_translate("Dialog", "Height"))
        self.pickupHeight.setToolTip(_translate("Dialog", "<html><head/><body><p>Height of pickup</p></body></html>"))
        self.label_fretboardLength_22.setText(_translate("Dialog", "Depth"))
        self.pickupDepth.setToolTip(_translate("Dialog", "<html><head/><body><p>Depth of pickup</p></body></html>"))
        self.label_fretboardLength_23.setText(_translate("Dialog", "Position neck pickup"))
        self.pickupNeckPosX.setToolTip(_translate("Dialog", "<html><head/><body><p>Position from top of the body</p></body></html>"))
        self.label_fretboardLength_24.setText(_translate("Dialog", "Position body pickup"))
        self.pickupBodyPosX.setToolTip(_translate("Dialog", "<html><head/><body><p>Position from top of body</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "Pickups"))
        self.label.setText(_translate("Dialog", "Hover over an input field to get a short description"))
        self.create.setText(_translate("Dialog", "Generate"))

    def onSubmit(self):
        self.didRun = True

        try:
            # Variables fretboard
            fretboardLength         = self.fretboardLength.value() # Length between body and end of fretboard - x
            fretboardWidthWide      = self.fretboardWidthWide.value() # Width of fretboard at side of body - x
            fretboardWidthNarrow    = self.fretboardWidthNarrow.value() # Width of fretboard at top side - x
            fretboardHeight         = self.fretboardHeight.value() # Heigth of fretboard - x
            fretboardRoundingRadius = self.fretboardRoundingRadius.value() # Radius for rounding at bottom off fretboard - x

            # Variables head
            headPreset              = 1 # Right now, only option 1 is defined - o
            headLength              = self.headLength.value() # Length of head - x
            headWidth               = self.headWidth.value() # Width of head - x
            headHeight              = self.headHeight.value() # Height of hbead - x
            headMarchLength         = self.headMarchLength.value() / 100 * headLength # Space between fretboard and narrowing - x

            # Variables body
            bodyLength              = self.bodyLength.value() #Total length of the body - x
            bodyWidth               = self.bodyWidth.value() #Space between the start of the circles and the center of the body - x
            bodyThickness           = self.bodThickness.value() #Thickness of the total body - x
            lowerBoutArcRatio       = 0.730875 # - o
            arcRatio                = self.arcRatio.value() #Sets ratio between upper and lower arc (1:arcRatio) User input - x
            bodyOffset              = 0.0 #Space between top/bottem of the body and the arcs # - o
            bodyLowerBoutArcRad     = (bodyLength - lowerBoutArcRatio * bodyLength) / 1.089 #Radius of the lower circle - o
            bodyLowerBoutArcPosY    = bodyLowerBoutArcRad + bodyOffset #Position Y of the lower circle - o
            bodyUpperBoutArcRad     = bodyLowerBoutArcRad / arcRatio #Size of the upper part of the body - o
            bodyUpperBoutArcPosY    = bodyLength - bodyOffset - bodyUpperBoutArcRad #Position Y of the upper circle - o
            bodyCutRad              = (bodyUpperBoutArcRad + bodyLowerBoutArcRad) / 4.5 #Size of the cutout between lower and upper bout arc - o
            bodyCutPosX             = (bodyUpperBoutArcRad + bodyLowerBoutArcRad) / 2 #Position X of the middle circle - o
            bodyCutPosY             = ((bodyLength - 2 * bodyOffset) / 2) * math.sqrt(arcRatio) - bodyOffset #Position Y of the middle circle - o

            #Cutout angle(degree to radian)
            bodyConnectAngle        = 30.000000 #The length of the middle circle part
            bodyConnectAngleRad     = math.radians(bodyConnectAngle)

            # Cutaway
            # Type (0=nothing, 1=venetian
            cutawayType             = int(self.cutawayType.value()) # - x
            cutawayOffset           = self.cutawayOffset.value() #Position from neck - x
            cutawayDepth            = self.cutawayDepth.value() #Position in body - x
            cutawayRad              = self.cutawayRad.value() #Radius - x

            # Pickups
            if (int(self.pickups.value()) == 1):
                pickups             = True # - x
            else:
                pickups             = False # - x
            
            pickupWidth             = self.pickupWidth.value() # - x
            pickupHeight            = self.pickupHeight.value() # - x
            pickupDepth             = self.pickupDepth.value() # - x
            pickupNeckPosX          = self.pickupNeckPosX.value() #Position from top of the body - x
            pickupBodyPosX          = self.pickupBodyPosX.value() #Position from top of the body - x
        except:
            print "Error! Values must be valid numbers!"
        else:
            # Initialize
            doc = FreeCAD.newDocument()
            zero = FreeCAD.Vector(0,0,0)

            # Functions
            def posOnCircleX( radius, angle, posX): #Calculate the X position on a cirlce
                move = math.cos(math.radians(angle)) * radius
                position = posX + move
                return(position)

            def posOnCircleY( radius, angle, posY): #Calculate the Y position on a cirlce
                move = math.sin(math.radians(angle)) * radius
                position = posY - move
                return(position)

            # Neck
            #   Fretboard
            fretboardBase = doc.addObject("Part::Box", "fretboardBase")
            fretboardBase.Length = fretboardLength
            fretboardBase.Width = fretboardWidthWide
            fretboardBase.Height = fretboardHeight
            Draft.move(fretboardBase, zero)

            if (fretboardWidthWide != fretboardWidthNarrow):
                # More narrow at top -> make two blocks to cut out sides
                fretboardCutoutR = doc.addObject("Part::Box", "fretboardCutoutR")
                fretboardCutoutL = doc.addObject("Part::Box", "fretboardCutoutL")
                fretboardCutoutR.Length = fretboardLength * 2
                fretboardCutoutL.Length = fretboardLength * 2
                fretboardCutoutR.Width = fretboardWidthWide
                fretboardCutoutL.Width = fretboardWidthWide
                fretboardCutoutR.Height = fretboardHeight
                fretboardCutoutL.Height = fretboardHeight
                fretboardCutOutAngle = math.degrees(math.atan(((fretboardWidthWide - fretboardWidthNarrow) / 2) / fretboardLength))
                fretboardCutoutR.Placement = FreeCAD.Placement(FreeCAD.Vector(0, fretboardWidthWide, 0), FreeCAD.Rotation(FreeCAD.Vector(0,0,1), -fretboardCutOutAngle))
                fretboardCutoutL.Placement = FreeCAD.Placement(FreeCAD.Vector(0, -fretboardWidthWide, 0), FreeCAD.Rotation(FreeCAD.Vector(0,0,1), fretboardCutOutAngle))
                fretboardHalf = doc.addObject("Part::Cut", "fretboardHalf")
                fretboardHalf.Base = fretboardBase
                fretboardHalf.Tool = fretboardCutoutR
                fretboard = doc.addObject("Part::Cut", "fretboard")
                fretboard.Base = fretboardHalf
                fretboard.Tool = fretboardCutoutL
            else:
                fredboard = fretboardBase

            fretboardR = doc.addObject("Part::Fillet","Fillet")
            fretboardR.Base = fretboard
            __fillets__ = []
            __fillets__.append((4,3.00,3.00))
            __fillets__.append((12,3.00,3.00))
            fretboardR.Edges = __fillets__
            del __fillets__
            fretboard.ViewObject.Visibility = False

            #   Head
            if (headPreset == 1):
                headBase = doc.addObject("Part::Box", "headBase")
                headBase.Length = headLength
                headBase.Width = headWidth
                headBase.Height = headHeight
                Draft.move(headBase, FreeCAD.Vector(fretboardLength, -(headWidth - fretboardWidthWide) / 2, 0))
                headCutout = doc.addObject("Part::Box", "headCutout")
                headCutout.Length = headLength * 2
                headCutout.Width = headWidth
                headCutout.Height = headHeight
                headCutoutAngle = math.degrees(math.atan(headWidth / (headLength - headMarchLength)))
                headCutout.Placement = FreeCAD.Placement(FreeCAD.Vector(fretboardLength + headMarchLength, -(headWidth - fretboardWidthWide) / 2 + headWidth, 0), FreeCAD.Rotation(FreeCAD.Vector(0,0,1), -headCutoutAngle))
                head = doc.addObject("Part::Cut", "head")
                head.Base = headBase
                head.Tool = headCutout

            # Combine fretboard and head to neck
            neck = doc.addObject("Part::MultiFuse", "neck")
            neck.Shapes = [fretboardR, head]

            # Rotate the fretboard 90 degrees to fit body
            neck.Placement=FreeCAD.Placement(FreeCAD.Vector(fretboardWidthWide / 2,bodyLength,bodyThickness - fretboardHeight), FreeCAD.Rotation(FreeCAD.Vector(0,0,1),90), FreeCAD.Vector(0,0,0))


            # Body
            # Create sketch
            FreeCAD.activeDocument().addObject('Sketcher::SketchObject','Body')
            FreeCAD.activeDocument().Body.Placement = FreeCAD.Placement(FreeCAD.Vector(0.000000,0.000000,0.000000),FreeCAD.Rotation(0.000000,0.000000,0.000000,1.000000))

            # Add base line of body
            FreeCAD.ActiveDocument.Body.addGeometry(Part.Line(FreeCAD.Vector(0.000000,0.000000,0),FreeCAD.Vector(0.000000,bodyLength,0)))

            # Draw first arc                                                        pos     x            y            z          orientation     radius                    radians
            FreeCAD.ActiveDocument.Body.addGeometry(Part.ArcOfCircle(Part.Circle(FreeCAD.Vector(0.000000 + bodyWidth,bodyLowerBoutArcPosY,0),FreeCAD.Vector(0,0,1),bodyLowerBoutArcRad),-1.570796,bodyConnectAngleRad))

            # Draw second arc
            FreeCAD.ActiveDocument.Body.addGeometry(Part.ArcOfCircle(Part.Circle(FreeCAD.Vector(0.000000 + bodyWidth,bodyUpperBoutArcPosY,0),FreeCAD.Vector(0,0,1),bodyUpperBoutArcRad),-bodyConnectAngleRad,1.570796))

            # Draw cut arc
            FreeCAD.ActiveDocument.Body.addGeometry(Part.ArcOfCircle(Part.Circle(FreeCAD.Vector(bodyCutPosX + bodyWidth,bodyCutPosY,0),FreeCAD.Vector(0,0,1),bodyCutRad),math.radians(180 - bodyConnectAngle),math.radians(180 + bodyConnectAngle)))

            # Draw connect cut
            FreeCAD.ActiveDocument.Body.addGeometry(Part.Line(FreeCAD.Vector(posOnCircleX( bodyUpperBoutArcRad, bodyConnectAngle, 0) + bodyWidth,posOnCircleY( bodyUpperBoutArcRad, bodyConnectAngle, bodyUpperBoutArcPosY),0),FreeCAD.Vector(posOnCircleX( bodyCutRad, 180 + bodyConnectAngle, bodyCutPosX) + bodyWidth,posOnCircleY( bodyCutRad, 180 + bodyConnectAngle, bodyCutPosY),0)))
            FreeCAD.ActiveDocument.Body.addGeometry(Part.Line(FreeCAD.Vector(posOnCircleX( bodyLowerBoutArcRad, -bodyConnectAngle, 0) + bodyWidth,posOnCircleY( bodyLowerBoutArcRad, -bodyConnectAngle, bodyLowerBoutArcPosY),0),FreeCAD.Vector(posOnCircleX( bodyCutRad, 180 - bodyConnectAngle, bodyCutPosX) + bodyWidth,posOnCircleY( bodyCutRad, 180 - bodyConnectAngle, bodyCutPosY),0)))

            # Connect arcs to baseline
            FreeCAD.ActiveDocument.Body.addGeometry(Part.Line(FreeCAD.Vector( 0,bodyOffset+5,0),FreeCAD.Vector( bodyWidth,bodyOffset,0)))
            FreeCAD.ActiveDocument.Body.addConstraint(Sketcher.Constraint('Coincident',-1,1,6,1))

            FreeCAD.ActiveDocument.Body.addGeometry(Part.Line(FreeCAD.Vector( 0,bodyLength - bodyOffset,0),FreeCAD.Vector( bodyWidth,bodyLength - bodyOffset,0)))
            FreeCAD.ActiveDocument.Body.addConstraint(Sketcher.Constraint('Coincident',7,1,0,2)) 

            # Add al constraints
            FreeCAD.ActiveDocument.Body.addConstraint(Sketcher.Constraint('Coincident',2,2,7,2)) #upper arc - offset
            FreeCAD.ActiveDocument.Body.addConstraint(Sketcher.Constraint('Coincident',4,1,2,1)) #upper arc - line
            FreeCAD.ActiveDocument.Body.addConstraint(Sketcher.Constraint('Coincident',3,1,4,2)) #line - cut arc
            FreeCAD.ActiveDocument.Body.addConstraint(Sketcher.Constraint('Coincident',5,2,3,2)) #cut arc - line
            FreeCAD.ActiveDocument.Body.addConstraint(Sketcher.Constraint('Coincident',5,1,1,2)) #line - lower arc
            FreeCAD.ActiveDocument.Body.addConstraint(Sketcher.Constraint('Coincident',6,2,1,1)) #lower arc - offset

            # Create body depth by padding
            FreeCAD.activeDocument().addObject("PartDesign::Pad","Pad")
            FreeCAD.activeDocument().Pad.Sketch = FreeCAD.activeDocument().Body
            FreeCAD.activeDocument().Pad.Length = bodyThickness
            FreeCAD.ActiveDocument.recompute()
            FreeCADGui.activeDocument().hide("Body")


            # Mirror
            FreeCAD.activeDocument().addObject("PartDesign::Mirrored","bodyMirrored")
            FreeCAD.ActiveDocument.recompute()
            FreeCAD.activeDocument().bodyMirrored.Originals = [FreeCAD.activeDocument().Pad,]
            FreeCAD.activeDocument().bodyMirrored.MirrorPlane = (FreeCAD.activeDocument().Body, ["V_Axis"])
            FreeCADGui.activeDocument().Pad.Visibility=False
            FreeCADGui.ActiveDocument.bodyMirrored.ShapeColor=FreeCADGui.ActiveDocument.Pad.ShapeColor
            FreeCADGui.ActiveDocument.bodyMirrored.DisplayMode=FreeCADGui.ActiveDocument.Pad.DisplayMode
            FreeCAD.ActiveDocument.bodyMirrored.Originals = [FreeCAD.ActiveDocument.Pad,]
            FreeCAD.ActiveDocument.bodyMirrored.MirrorPlane = (FreeCAD.ActiveDocument.Body,["V_Axis"])



            # Create cutaway if chosen
            if cutawayType == 0:
                print "Nothing to do"


            elif cutawayType == 1:
                FreeCAD.ActiveDocument.addObject("Part::Cylinder","Cylinder") #Create cylinder
                FreeCAD.ActiveDocument.ActiveObject.Label = "cutAwayCylinder"
                FreeCAD.ActiveDocument.Cylinder.Placement=FreeCAD.Placement(FreeCAD.Vector(cutawayRad + fretboardWidthWide + cutawayOffset,bodyLength - cutawayDepth,0), FreeCAD.Rotation(FreeCAD.Vector(0,0,1),0), FreeCAD.Vector(0,0,0))
                FreeCAD.ActiveDocument.getObject("Cylinder").Radius = cutawayRad
                FreeCAD.ActiveDocument.getObject("Cylinder").Height = bodyLength * 10

                #Cut
                FreeCADGui.activateWorkbench("PartWorkbench")
                FreeCAD.activeDocument().addObject("Part::Cut","Cut")
                FreeCAD.activeDocument().Cut.Base = FreeCAD.activeDocument().bodyMirrored
                FreeCAD.activeDocument().Cut.Tool = FreeCAD.activeDocument().Cylinder
                FreeCADGui.ActiveDocument.Cut.ShapeColor=FreeCADGui.ActiveDocument.bodyMirrored.ShapeColor
                FreeCADGui.ActiveDocument.Cut.DisplayMode=FreeCADGui.ActiveDocument.bodyMirrored.DisplayMode


            # Cut out space for pickups if chosen    
            if pickups == True:
                FreeCAD.ActiveDocument.addObject("Part::Box","neckPickup")
                FreeCAD.ActiveDocument.ActiveObject.Label = "neckPickup"
                FreeCAD.ActiveDocument.neckPickup.Width = pickupHeight
                FreeCAD.ActiveDocument.neckPickup.Length = pickupWidth
                FreeCAD.ActiveDocument.neckPickup.Height = pickupDepth
                FreeCAD.ActiveDocument.neckPickup.Placement=FreeCAD.Placement(FreeCAD.Vector(-pickupWidth / 2,bodyLength - pickupNeckPosX,bodyThickness - pickupDepth), FreeCAD.Rotation(FreeCAD.Vector(0,0,1),0), FreeCAD.Vector(0,0,0))

                FreeCAD.ActiveDocument.addObject("Part::Box","bodyPickup")
                FreeCAD.ActiveDocument.ActiveObject.Label = "bodyPickup"
                FreeCAD.ActiveDocument.bodyPickup.Width = pickupHeight
                FreeCAD.ActiveDocument.bodyPickup.Length = pickupWidth
                FreeCAD.ActiveDocument.bodyPickup.Height = pickupDepth
                FreeCAD.ActiveDocument.bodyPickup.Placement=FreeCAD.Placement(FreeCAD.Vector(-pickupWidth / 2,bodyLength - pickupBodyPosX,bodyThickness - pickupDepth), FreeCAD.Rotation(FreeCAD.Vector(0,0,1),0), FreeCAD.Vector(0,0,0))

                # Cut the pickups
                FreeCAD.activeDocument().addObject("Part::Cut","CutPickup")
                if cutawayType == 0: #If there is no cutaway selected then the name of the element isn't changed
                    FreeCAD.activeDocument().CutPickup.Base = FreeCAD.activeDocument().bodyMirrored
                    FreeCAD.activeDocument().CutPickup.Tool = FreeCAD.activeDocument().neckPickup
                    FreeCADGui.activeDocument().hide('bodyMirrored')
                    FreeCADGui.activeDocument().hide('neckPickup')

                else:
                    FreeCAD.activeDocument().CutPickup.Base = FreeCAD.activeDocument().Cut
                    FreeCAD.activeDocument().CutPickup.Tool = FreeCAD.activeDocument().neckPickup
                    FreeCADGui.activeDocument().hide('Cut')
                    FreeCADGui.activeDocument().hide('neckPickup')


                FreeCAD.activeDocument().addObject("Part::Cut","FreeCADGuitarBody")
                FreeCAD.activeDocument().FreeCADGuitarBody.Base = FreeCAD.activeDocument().CutPickup
                FreeCAD.activeDocument().FreeCADGuitarBody.Tool = FreeCAD.activeDocument().bodyPickup
                FreeCADGui.activeDocument().hide('CutPickup')
                FreeCADGui.activeDocument().hide('bodyPickup')


            # Render
            doc.recompute()
            FreeCADGui.activeDocument().activeView().viewAxometric()
            FreeCADGui.SendMsgToActiveView("ViewFit")

class guitarInput():
    def __init__(self):
        d = QtGui.QDialog()
        d.ui = Ui_Dialog()
        d.ui.setupUi(d)
        d.exec_()
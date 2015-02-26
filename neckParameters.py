# -*- coding: utf-8 -*-
 
# Form implementation generated from reading ui file 'v1.ui'
#
#      by: PyQt5 UI code generator
#      WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import Draft, math, FreeCAD, FreeCADGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(526, 420)
        self.create = QtGui.QPushButton(Dialog)
        self.create.setGeometry(QtCore.QRect(430, 380, 75, 23))
        self.create.setObjectName("create")
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 176, 264))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_fretboardLength = QtGui.QLabel(self.tab)
        self.label_fretboardLength.setObjectName("label_fretboardLength")
        self.gridLayout_2.addWidget(self.label_fretboardLength, 0, 0, 1, 1)
        self.label_fretboardLength_3 = QtGui.QLabel(self.tab)
        self.label_fretboardLength_3.setObjectName("label_fretboardLength_3")
        self.gridLayout_2.addWidget(self.label_fretboardLength_3, 5, 0, 1, 1)
        self.fretboardWidthWide = QtGui.QLineEdit(self.tab)
        self.fretboardWidthWide.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        #self.fretboardWidthWide.setInputMethodHints(QtCore.Qt.ImhNone)
        self.fretboardWidthWide.setObjectName("fretboardWidthWide")
        self.gridLayout_2.addWidget(self.fretboardWidthWide, 6, 0, 1, 1)
        self.label_fretboardLength_4 = QtGui.QLabel(self.tab)
        self.label_fretboardLength_4.setObjectName("label_fretboardLength_4")
        self.gridLayout_2.addWidget(self.label_fretboardLength_4, 7, 0, 1, 1)
        self.label_fretboardLength_5 = QtGui.QLabel(self.tab)
        self.label_fretboardLength_5.setObjectName("label_fretboardLength_5")
        self.gridLayout_2.addWidget(self.label_fretboardLength_5, 9, 0, 1, 1)
        self.label_fretboardLength_2 = QtGui.QLabel(self.tab)
        self.label_fretboardLength_2.setObjectName("label_fretboardLength_2")
        self.gridLayout_2.addWidget(self.label_fretboardLength_2, 3, 0, 1, 1)
        self.fretboardRoundingRadius = QtGui.QLineEdit(self.tab)
        self.fretboardRoundingRadius.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        #self.fretboardRoundingRadius.setInputMethodHints(QtCore.Qt.ImhNone)
        self.fretboardRoundingRadius.setObjectName("fretboardRoundingRadius")
        self.gridLayout_2.addWidget(self.fretboardRoundingRadius, 10, 0, 1, 1)
        self.fretboardHeight = QtGui.QLineEdit(self.tab)
        self.fretboardHeight.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        #self.fretboardHeight.setInputMethodHints(QtCore.Qt.ImhNone)
        self.fretboardHeight.setObjectName("fretboardHeight")
        self.gridLayout_2.addWidget(self.fretboardHeight, 8, 0, 1, 1)
        self.fretboardWidthNarrow = QtGui.QLineEdit(self.tab)
        self.fretboardWidthNarrow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        #self.fretboardWidthNarrow.setInputMethodHints(QtCore.Qt.ImhNone)
        self.fretboardWidthNarrow.setObjectName("fretboardWidthNarrow")
        self.gridLayout_2.addWidget(self.fretboardWidthNarrow, 4, 0, 1, 1)
        self.fretboardLength = QtGui.QLineEdit(self.tab)
        self.fretboardLength.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        #self.fretboardLength.setInputMethodHints(QtCore.Qt.ImhNone)
        self.fretboardLength.setInputMask("")
        self.fretboardLength.setObjectName("fretboardLength")
        self.gridLayout_2.addWidget(self.fretboardLength, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout = QtGui.QGridLayout(self.tab_3)
        self.gridLayout.setObjectName("gridLayout")
        self.headLength = QtGui.QLineEdit(self.tab_3)
        self.headLength.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        #self.headLength.setInputMethodHints(QtCore.Qt.ImhNone)
        self.headLength.setInputMask("")
        self.headLength.setObjectName("headLength")
        self.gridLayout.addWidget(self.headLength, 1, 0, 1, 1)
        self.headWidth = QtGui.QLineEdit(self.tab_3)
        self.headWidth.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        #self.headWidth.setInputMethodHints(QtCore.Qt.ImhNone)
        self.headWidth.setObjectName("headWidth")
        self.gridLayout.addWidget(self.headWidth, 3, 0, 1, 1)
        self.label_fretboardLength_8 = QtGui.QLabel(self.tab_3)
        self.label_fretboardLength_8.setObjectName("label_fretboardLength_8")
        self.gridLayout.addWidget(self.label_fretboardLength_8, 0, 0, 1, 1)
        self.label_fretboardLength_6 = QtGui.QLabel(self.tab_3)
        self.label_fretboardLength_6.setObjectName("label_fretboardLength_6")
        self.gridLayout.addWidget(self.label_fretboardLength_6, 2, 0, 1, 1)
        self.headHeight = QtGui.QLineEdit(self.tab_3)
        self.headHeight.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        #self.headHeight.setInputMethodHints(QtCore.Qt.ImhNone)
        self.headHeight.setObjectName("headHeight")
        self.gridLayout.addWidget(self.headHeight, 5, 0, 1, 1)
        self.label_fretboardLength_7 = QtGui.QLabel(self.tab_3)
        self.label_fretboardLength_7.setObjectName("label_fretboardLength_7")
        self.gridLayout.addWidget(self.label_fretboardLength_7, 6, 0, 1, 1)
        self.label_fretboardLength_9 = QtGui.QLabel(self.tab_3)
        self.label_fretboardLength_9.setObjectName("label_fretboardLength_9")
        self.gridLayout.addWidget(self.label_fretboardLength_9, 4, 0, 1, 1)
        self.headMarchLength = QtGui.QLineEdit(self.tab_3)
        self.headMarchLength.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        #self.headMarchLength.setInputMethodHints(QtCore.Qt.ImhNone)
        self.headMarchLength.setObjectName("headMarchLength")
        self.gridLayout.addWidget(self.headMarchLength, 7, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.create,QtCore.SIGNAL("pressed()"),self.onSubmit)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.create.setText(_translate("Dialog", "Generate"))
        self.label_fretboardLength.setText(_translate("Dialog", "Fretboard length"))
        self.label_fretboardLength_3.setText(_translate("Dialog", "Fretboard width wide side"))
        self.fretboardWidthWide.setText(_translate("Dialog", "15.0"))
        self.label_fretboardLength_4.setText(_translate("Dialog", "Fretboard heigth"))
        self.label_fretboardLength_5.setText(_translate("Dialog", "Rounding radius fretboard"))
        self.label_fretboardLength_2.setText(_translate("Dialog", "Fretboard width narrow side"))
        self.fretboardRoundingRadius.setText(_translate("Dialog", "15.0"))
        self.fretboardHeight.setText(_translate("Dialog", "15.0"))
        self.fretboardWidthNarrow.setText(_translate("Dialog", "40.0"))
        self.fretboardLength.setText(_translate("Dialog", "500.0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Fretboard"))
        self.headLength.setText(_translate("Dialog", "150"))
        self.headWidth.setText(_translate("Dialog", "80.0"))
        self.label_fretboardLength_8.setText(_translate("Dialog", "Head length"))
        self.label_fretboardLength_6.setText(_translate("Dialog", "Head width"))
        self.headHeight.setText(_translate("Dialog", "15.0"))
        self.label_fretboardLength_7.setText(_translate("Dialog", "Space until narrowing head (%)"))
        self.label_fretboardLength_9.setText(_translate("Dialog", "Head height"))
        self.headMarchLength.setText(_translate("Dialog", "15"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Head"))

    def onSubmit(self):
        try:
            fretboardLength = float(self.fretboardLength.text());

            # Variables fretboard
            fretboardLength = float(self.fretboardLength.text()) # Length between body and end of fretboard
            fretboardWidthWide = float(self.fretboardWidthWide.text()) # Width of fretboard at side of body
            fretboardWidthNarrow = float(self.fretboardWidthNarrow.text()) # Width of fretboard at top side
            fretboardHeight = float(self.fretboardHeight.text()) # Heigth of fretboard
            fretboardRoundingRadius = float(self.fretboardRoundingRadius.text()) # Radius for rounding at bottom of fretboard

            # Variables head
            headPreset = 1 # Right now, only option 1 is defined
            headLength = float(self.headLength.text()) # Length of head
            headWidth = float(self.headWidth.text()) # Width of head
            headHeight = float(self.headHeight.text()) # Height of hbead
            headMarchLength = float(self.headMarchLength.text()) / 100 * headLength # Space between fretboard and narrowing

            if fretboardLength <= 0 or \
               fretboardWidthWide <= 0 or \
               fretboardWidthNarrow <= 0 or \
               fretboardHeight <= 0 or \
               fretboardRoundingRadius <= 0 or \
               headLength <= 0 or \
               headWidth <= 0 or \
               headHeight <= 0 or \
               headMarchLength <= 0:
                raise Exception('Values are not allowed.')
        except:
            print "Error! Values must be valid numbers!"
        else:
            # This script is responsable for building up the neck.

            # Initialize
            doc = FreeCAD.newDocument()
            zero = FreeCAD.Vector(0,0,0)

            # Fretboard
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

            # Head
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
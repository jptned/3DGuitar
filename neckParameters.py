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
        self.label_fretboardLength = QtGui.QLabel(Dialog) # QtWidgets
        self.label_fretboardLength.setGeometry(QtCore.QRect(20, 30, 158, 20))
        self.label_fretboardLength.setObjectName("label_fretboardLength")
        self.fretboardLength = QtGui.QLineEdit(Dialog) # QtWidgets
        self.fretboardLength.setGeometry(QtCore.QRect(20, 50, 158, 20))
        self.fretboardLength.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        #self.fretboardLength.setInputMethodHints(QtCore.Qt.ImhNone)
        self.fretboardLength.setText("")
        self.fretboardLength.setObjectName("fretboardLength")
        self.create = QtGui.QPushButton(Dialog) # QtWidgets
        self.create.setGeometry(QtCore.QRect(420, 370, 75, 23))
        self.create.setObjectName("create")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.create,QtCore.SIGNAL("pressed()"),self.onSubmit)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_fretboardLength.setText(_translate("Dialog", "Fretboard length"))
        self.create.setText(_translate("Dialog", "Genereer"))

    def onSubmit(self):
        try:
            fretboardLength = float(self.fretboardLength.text());
        except:
            print "Error! Values must be valid numbers!"
        else:
            # This script is responsable for building up the neck.

            # Variables fretboard
            #fretboardLength = 500.0 # Length between body and end of fretboard
            fretboardWidthWide = 80.0 # Width of fretboard at side of body
            fretboardWidthNarrow = 40.0 # Width of fretboard at top side
            fretboardHeight = 15.0 # Heigth of fretboard
            fretboardRoundingRadius = 15.0 # Radius for rounding at bottom off fretboard

            # Variables head
            headPreset = 1 # Right now, only option 1 is defined
            headLength = 150.0 # Length of head
            headWidth = 80.0 # Width of head
            headHeight = 15.0 # Height of hbead
            headMarchLength = 0.15 * headLength # Space between fretboard and narrowing

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
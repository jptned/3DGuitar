# This script is responsable for building up the neck.

# Variables fretboard
fretboardLength = 500.0 # Length between body and end of fretboard
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
	fretboardCutoutR.Placement = FreeCAD.Placement(FreeCAD.Vector(0, fretboardWidthWide, 0), FreeCAD.Rotation(App.Vector(0,0,1), -fretboardCutOutAngle))
	fretboardCutoutL.Placement = FreeCAD.Placement(FreeCAD.Vector(0, -fretboardWidthWide, 0), FreeCAD.Rotation(App.Vector(0,0,1), fretboardCutOutAngle))
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
	headCutout.Placement = FreeCAD.Placement(FreeCAD.Vector(fretboardLength + headMarchLength, -(headWidth - fretboardWidthWide) / 2 + headWidth, 0), FreeCAD.Rotation(App.Vector(0,0,1), -headCutoutAngle))
	head = doc.addObject("Part::Cut", "head")
	head.Base = headBase
	head.Tool = headCutout

# Combine fretboard and head to neck
neck = doc.addObject("Part::MultiFuse", "neck")
neck.Shapes = [fretboardR, head]

# Render
doc.recompute()
Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
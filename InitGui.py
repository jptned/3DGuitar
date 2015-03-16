import FreeCAD, FreeCADGui

windowCreated = 0

class NewGuitar:
	"Test command"
	def Activated(self):
		global windowCreated
		global neckParameters
		global neckObject
		if windowCreated == 0:
			import neckParameters
			neckObject = neckParameters.guitarInput()
			neckObject.firstOpen()
		else:
			neckObject.reOpen()
			
		windowCreated = 1

	def GetResources(self):
		return {
			'Pixmap'  : 'Std_Tool1', 
			'MenuText': 'Create new guitar', 
			'ToolTip': 'Create new guitar'
		}

FreeCADGui.addCommand('3D_NewGuitar', NewGuitar())

class TGD ( Workbench ):
	"3D Guitar Design Object"
	Icon = """
			/* XPM */
			static const char *test_icon[]={
			"16 16 2 1",
			"a c #167AC6",
			". c None",
			"................",
			"................",
			"..############..",
			"..############..",
			"..###......###..",
			"..###......###..",
			"..###......###..",
			"..############..",
			"..############..",
			"..###...........",
			"..###...........",
			"..###...........",
			"..###...........",
			"..###...........",
			"................",
			"................"};
			"""
	MenuText = "3D Guitar Design"
	ToolTip = "In development"

	def GetClassName(self):
		return "Gui::PythonWorkbench"

	def Initialize(self):
		self.appendToolbar("3D Guitar Design", ["3D_NewGuitar"])
		self.appendMenu("My Tools", ["3D_NewGuitar"])
		Log ("Loading MyModule... done\n")

	#def Activated(self):
	#	Msg ("TGD.Activated()\n")

	#def Deactivated(self):
	#	Msg ("TGD.Deactivated()\n")
	
FreeCADGui.addWorkbench(TGD)
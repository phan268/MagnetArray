# ----------------------------------------------
# IronPython Script Recorded by Ansys Electronics Desktop Version 2023.2.0
# 14:07:00  May 24, 2024
# Modified for universality and simplicity
# This serves as an example to show how to modify the recorded IronPython script and convert it into a version that can be run in Cpython
# ----------------------------------------------

#MAXWELL_PROJECT_PATH = r"C:\Simulations\Magnet_RadialArray\Magnet_RadialPattern_ObjectCS.aedt" # Define Maxwell project file path
import os
MAXWELL_PROJECT_PATH = os.getcwd() # Set the Maxwell project file path to the current working directory

# Added the three lines below
import sys # Import the sys module containing system-specific functions native to IronPython
# The two lines below need to be changed to the default AnsysEM directories for different versions
sys.path.append(r"C:\Program Files\ANSYS Inc\v252\AnsysEM") # Adds the Electronics Desktop installation path to the list of directories Python searches for modules and files
sys.path.append(r"C:\Program Files\ANSYS Inc\v252\AnsysEM\PythonFiles\DesktopPlugin") # Adds the PythonFiles/DesktopPlugin subfolder to the list of directories Python searches for modules and files

# The two lines below imports ScriptEnv.py from the installation path specified above. ScriptEnv.py performs an operating system check and defines functions used in Electronics Desktop scripts. 
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop.2025.2")
# ScriptEnv.Initialize(NonGraphical=True) # Uncomment this line and comment the line above to run in non-graphical mode

oDesktop.RestoreWindow()
oProject = oDesktop.NewProject()
#oProject = oDesktop.SetActiveProject("Project1") # Remove this line
oProject.InsertDesign("Maxwell 3D", "Maxwell3DDesign1", "Magnetostatic", "")
#oProject.Rename("E:/phan/OneDrive_ANSYS/OneDrive - ANSYS, Inc/Documents/Ansoft/Magnet_RadialPattern_ObjectCS.aedt", True) # Remove this line
oProject.SaveAs(os.path.join(MAXWELL_PROJECT_PATH, "Magnet_RadialPattern_ObjectCS.aedt"), True) # Update Maxwell project file path
oDesign = oProject.SetActiveDesign("Maxwell3DDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")

# Create a single box object
XPosition_Box = "-1mm"
YPosition_Box = "-0.2mm"
ZPosition_Box = "0mm"
XSize_Box = "0.2mm"
YSize_Box = "0.4mm"
ZSize_Box = "0.2mm"

#Num_Clone = 12
Num_Clone = 10
Angular_Space = 360/Num_Clone


oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, XPosition_Box,
		"YPosition:="		, YPosition_Box,
		"ZPosition:="		, ZPosition_Box,
		"XSize:="		, XSize_Box,
		"YSize:="		, YSize_Box,
		"ZSize:="		, ZSize_Box
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"ReferenceTemperature:=", "20cel",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.DuplicateAroundAxis(
	[
		"NAME:Selections",
		"Selections:="		, "Box1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:DuplicateAroundAxisParameters",
		"CreateNewObjects:="	, True,
		"WhichAxis:="		, "Z",
		"AngleStr:="		, str(Angular_Space) + "deg", # Change "30deg" to str(30) + "deg"
		"NumClones:="		, str(Num_Clone) # Change "12" to str(12)
	], 
	[
		"NAME:Options",
		"DuplicateAssignments:=", True
	], 
	[
		"CreateGroupsForNewObjects:=", False
	])

# Create the box list
Box_list = ["Box1"]*Num_Clone
for i in range(Num_Clone):
    if i == 0:
        Box_list[i] = "Box1"
    else:
        Box_list[i] = "Box1_" + str(i)

# Define material property NdFe35_Z+
oDefinitionManager = oProject.GetDefinitionManager()
oDefinitionManager.AddMaterial(
	[
		"NAME:NdFe35_Z+",
		"CoordinateSystemType:=", "Cartesian",
		"BulkOrSurfaceType:="	, 1,
		[
			"NAME:PhysicsTypes",
			"set:="			, ["Electromagnetic","Thermal","Structural"]
		],
		[
			"NAME:AttachedData",
			[
				"NAME:MatAppearanceData",
				"property_data:="	, "appearance_data",
				"Red:="			, 204,
				"Green:="		, 204,
				"Blue:="		, 204
			]
		],
		"permittivity:="	, "1",
		"permeability:="	, "1.0997785406",
		"conductivity:="	, "625000",
		"dielectric_loss_tangent:=", "0",
		"magnetic_loss_tangent:=", "0",
		[
			"NAME:magnetic_coercivity",
			"property_type:="	, "VectorProperty",
			"Magnitude:="		, "-890000A_per_meter",
			"DirComp1:="		, "0",
			"DirComp2:="		, "0",
			"DirComp3:="		, "1"
		],
		"thermal_conductivity:=", "0",
		"saturation_mag:="	, "0gauss",
		"lande_g_factor:="	, "2",
		"delta_H:="		, "0Oe",
		"mass_density:="	, "7400",
		"youngs_modulus:="	, "147000000000",
		[
			"NAME:thermal_expansion_coefficient",
			"property_type:="	, "AnisoProperty",
			"unit:="		, "",
			"component1:="		, "3e-06",
			"component2:="		, "-5e-06",
			"component3:="		, "-5e-06"
		]
	])
# Assign material property to all the objects in the radial pattern
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.AssignMaterial(
	[
		"NAME:Selections",
		"AllowRegionDependentPartSelectionForPMLCreation:=", True,
		"AllowRegionSelectionForPMLCreation:=", True,
#		"Selections:="		, "Box1,Box1_1,Box1_2,Box1_3,Box1_4,Box1_5,Box1_6,Box1_7,Box1_8,Box1_9,Box1_10,Box1_11"
		"Selections:="		, ",".join(Box_list)
	], 
	[
		"NAME:Attributes",
		"MaterialValue:="	, "\"NdFe35_Z+\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "nan ",
		"ReferenceTemperature:=", "nan ",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

# =============================================================================
# # Creating ObjectCS for all the objects in the radial pattern
# List_ENtityIDs = [[12, 24, 13],
#                   [41, 53, 42],
#                   [69, 81, 70],
#                   [97, 109, 98],
#                   [125, 137, 126],
#                   [153, 165, 154],
#                   [181, 193, 182],
#                   [209, 221, 210],
#                   [237, 249, 238],
#                   [265, 277, 266],
#                   [293, 305, 294],
#                   [321, 333, 322]]
# =============================================================================

for i in range(Num_Clone):
    if i == 0:
        Face_ID = 12
        Box_Name = "Box1"
    else:
        Face_ID = 13 + 28*i
        Box_Name = "Box1_" + str(i)
        
    Edge1_ID = Face_ID + 12
    Edge2_ID = Face_ID + 1
    ObjectCS_Name = "ObjectCS" + str(i+1)
    
    oEditor.CreateObjectCS(
    	[
    		"NAME:ObjectCSParameters",
    		[
    			"NAME:Origin",
    			"IsAttachedToEntity:="	, True,
    			"EntityID:="		, Face_ID,
    			"FacetedBodyTriangleIndex:=", -1,
    			"TriangleVertexIndex:="	, -1,
    			"PositionType:="	, "FaceCenter",
    			"UParam:="		, 0,
    			"VParam:="		, 0,
    			"XPosition:="		, "0",
    			"YPosition:="		, "0",
    			"ZPosition:="		, "0"
    		],
    		"MoveToEnd:="		, False,
    		"ReverseXAxis:="	, False,
    		"ReverseYAxis:="	, False,
    		[
    			"NAME:xAxisPos",
    			"IsAttachedToEntity:="	, True,
    			"EntityID:="		, Edge1_ID,
    			"FacetedBodyTriangleIndex:=", -1,
    			"TriangleVertexIndex:="	, -1,
    			"PositionType:="	, "EdgeCenter",
    			"UParam:="		, 0,
    			"VParam:="		, 0,
    			"XPosition:="		, "0",
    			"YPosition:="		, "0",
    			"ZPosition:="		, "0"
    		],
    		[
    			"NAME:yAxisPos",
    			"IsAttachedToEntity:="	, True,
    			"EntityID:="		, Edge2_ID,
    			"FacetedBodyTriangleIndex:=", -1,
    			"TriangleVertexIndex:="	, -1,
    			"PositionType:="	, "EdgeCenter",
    			"UParam:="		, 0,
    			"VParam:="		, 0,
    			"XPosition:="		, "0",
    			"YPosition:="		, "0",
    			"ZPosition:="		, "0"
    		]
    	], 
    	[
    		"NAME:Attributes",
    		"Name:="		, ObjectCS_Name,
    		"PartName:="		, Box_Name
    	])

    # Change magnetization orientation based on ObjectCS
    oEditor = oDesign.SetActiveEditor("3D Modeler")
    oEditor.ChangeProperty(
    	[
    		"NAME:AllTabs",
    		[
    			"NAME:Geometry3DAttributeTab",
    			[
    				"NAME:PropServers", 
    				Box_Name
    			],
    			[
    				"NAME:ChangedProps",
    				[
    					"NAME:Orientation",
    					"Value:="		, ObjectCS_Name
    				]
    			]
    		]
    	])

# Create region in Global CS
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global",
		"RegionDepCSOk:="	, False
	])
oEditor.CreateRegion(
	[
		"NAME:RegionParameters",
		"+XPaddingType:="	, "Percentage Offset",
		"+XPadding:="		, "200",
		"-XPaddingType:="	, "Percentage Offset",
		"-XPadding:="		, "200",
		"+YPaddingType:="	, "Percentage Offset",
		"+YPadding:="		, "200",
		"-YPaddingType:="	, "Percentage Offset",
		"-YPadding:="		, "200",
		"+ZPaddingType:="	, "Percentage Offset",
		"+ZPadding:="		, "1200",
		"-ZPaddingType:="	, "Percentage Offset",
		"-ZPadding:="		, "1200",
		[
			"NAME:BoxForVirtualObjects",
			[
				"NAME:LowPoint", 
				1, 
				1, 
				1
			],
			[
				"NAME:HighPoint", 
				-1, 
				-1, 
				-1
			]
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Region",
		"Flags:="		, "Wireframe#",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "nan ",
		"ReferenceTemperature:=", "nan ",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
# Assign mesh operation
oModule = oDesign.GetModule("MeshSetup")
oModule.AssignLengthOp(
	[
		"NAME:Length_magnets",
		"RefineInside:="	, False,
		"Enabled:="		, True,
#		"Objects:="		, ["Box1","Box1_1","Box1_2","Box1_3","Box1_4","Box1_5","Box1_6","Box1_7","Box1_8","Box1_9","Box1_10","Box1_11"],
		"Objects:="		, Box_list,
		"RestrictElem:="	, False,
		"NumMaxElem:="		, "1000",
		"RestrictLength:="	, True,
		"MaxLength:="		, "0.05mm"
	])
oModule.InitialMeshSettings(
	[
		"NAME:MeshSettings",
		[
			"NAME:GlobalSurfApproximation",
			"CurvedSurfaceApproxChoice:=", "UseSlider",
			"SliderMeshSettings:="	, 5
		],
		[
			"NAME:GlobalCurvilinear",
			"Apply:="		, True
		],
		[
			"NAME:GlobalModelRes",
			"UseAutoLength:="	, True
		],
		"MeshMethod:="		, "AnsoftTAU",
		"UseLegacyFaceterForTauVolumeMesh:=", False,
		"DynamicSurfaceResolution:=", True,
		"UseFlexMeshingForTAUvolumeMesh:=", False,
		"UseAlternativeMeshMethodsAsFallBack:=", True,
		"AllowPhiForLayeredGeometry:=", False
	])
# Set up analysis
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("Magnetostatic", 
	[
		"NAME:Setup1",
		"Enabled:="		, True,
		[
			"NAME:MeshLink",
			"ImportMesh:="		, False
		],
		"MaximumPasses:="	, 10,
		"MinimumPasses:="	, 2,
		"MinimumConvergedPasses:=", 1,
		"PercentRefinement:="	, 30,
		"SolveFieldOnly:="	, False,
		"PercentError:="	, 1,
		"SolveMatrixAtLast:="	, True,
		"UseNonLinearIterNum:="	, False,
		"UseIterativeSolver:="	, False,
		"RelativeResidual:="	, 1E-06,
		"NonLinearResidual:="	, 0.001,
		"SmoothBHCurve:="	, False,
		[
			"NAME:MuOption",
			"MuNonLinearBH:="	, True
		]
	])
# Save project before solving
oProject.Save()
# Solve the project
oDesign.Analyze("Setup1")

# Create field plots
oModule = oDesign.GetModule("FieldsReporter")
oModule.CreateFieldPlot(
	[
		"NAME:Mag_B1",
		"SolutionName:="	, "Setup1 : LastAdaptive",
		"UserSpecifyName:="	, 1,
		"UserSpecifyFolder:="	, 1,
		"QuantityName:="	, "Mag_B",
		"PlotFolder:="		, "B",
		"StreamlinePlot:="	, False,
		"AdjacentSidePlot:="	, False,
		"FullModelPlot:="	, False,
		"IntrinsicVar:="	, "",
#		"PlotGeomInfo:="	, [1,"Surface","FacesList",12,"Box1","Box1_1","Box1_2","Box1_3","Box1_4","Box1_5","Box1_6","Box1_7","Box1_8","Box1_9","Box1_10","Box1_11"],
#		"PlotGeomInfo:="	, [1,"Surface","FacesList",12,",".join(f'"{w}"' for w in Box_list)],
#		"PlotGeomInfo:="	, [1,"Surface","FacesList",12," ".join(f'"{w}"' for w in Box_list)],
		"PlotGeomInfo:="	, [1,"Surface","FacesList",12, "Box1"],
		"FilterBoxes:="		, [0],
		[
			"NAME:PlotOnSurfaceSettings",
			"Filled:="		, False,
			"IsoValType:="		, "Tone",
			"AddGrid:="		, False,
			"MapTransparency:="	, True,
			"Refinement:="		, 0,
			"Transparency:="	, 0,
			"SmoothingLevel:="	, 0,
			"ShadingType:="		, 0,
			[
				"NAME:Arrow3DSpacingSettings",
				"ArrowUniform:="	, True,
				"ArrowSpacing:="	, 0,
				"MinArrowSpacing:="	, 0,
				"MaxArrowSpacing:="	, 0
			],
			"GridColor:="		, [255,255,255]
		],
		"EnableGaussianSmoothing:=", False,
		"SurfaceOnly:="		, True
	], "Field")

#ScriptEnv.Shutdown() #commented out to show the AEDT gui. We can include this line in the script to automatically close aedt.

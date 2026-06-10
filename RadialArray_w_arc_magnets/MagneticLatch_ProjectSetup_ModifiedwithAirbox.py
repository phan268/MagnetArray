# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2026.1.0
# 10:28:24  Jun 08, 2026
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Qi2_MagnetLatch_MagneticForce_26R1")
oDesign = oProject.SetActiveDesign("Maxwell3DDesign2")
oEditor = oDesign.SetActiveEditor("3D Modeler")

def removeprefix(s, prefix):
    """Remove the given prefix from string s if it exists."""
    if prefix and s.startswith(prefix):
        return s[len(prefix):]
    return s

magnet1_id_list = oEditor.GetObjectsInGroup("Magnet1_Group")
num_magnet1 = len(magnet1_id_list)
    
for magnet_id in magnet1_id_list:
    oEditor.SetWCS(
        [
            "NAME:SetWCS Parameter",
            "Working Coordinate System:=", "Global",
            "RegionDepCSOk:="	, False
        ])
    if not "_" in magnet_id:
        oEditor.CreateRelativeCS(
            [
                "NAME:RelativeCSParameters",
                "Mode:="		, "Axis/Position",
                "OriginX:="		, "0mm",
                "OriginY:="		, "0mm",
                "OriginZ:="		, "0mm",
                "XAxisXvec:="		, "cos(-2*pi/" + str(num_magnet1) + "*0) mm",
                "XAxisYvec:="		, "-sin(-2*pi/" + str(num_magnet1) + "*0) mm",
                "XAxisZvec:="		, "0mm",
                "YAxisXvec:="		, "sin(-2*pi/" + str(num_magnet1) + "*0) mm",
                "YAxisYvec:="		, "cos(-2*pi/" + str(num_magnet1) + "*0) mm",
                "YAxisZvec:="		, "0mm"
            ], 
            [
                "NAME:Attributes",
                "Name:="		, "RelativeCS_{magnet_id}".format(magnet_id = magnet_id)
            ])
        AddWarningMessage("RelativeCS for Magnet1_Group have been created")
    else:
        label_magnet = removeprefix(magnet_id, "Rectangle1_")
        oEditor.CreateRelativeCS(
            [
                "NAME:RelativeCSParameters",
                "Mode:="		, "Axis/Position",
                "OriginX:="		, "0mm",
                "OriginY:="		, "0mm",
                "OriginZ:="		, "0mm",
                "XAxisXvec:="		, "cos(-2*pi/" + str(num_magnet1) + "*{label_magnet}) mm".format(label_magnet = label_magnet),
                "XAxisYvec:="		, "-sin(-2*pi/" + str(num_magnet1) + "*{label_magnet}) mm".format(label_magnet = label_magnet),
                "XAxisZvec:="		, "0mm",
                "YAxisXvec:="		, "sin(-2*pi/" + str(num_magnet1) + "*{label_magnet}) mm".format(label_magnet = label_magnet),
                "YAxisYvec:="		, "cos(-2*pi/" + str(num_magnet1) + "*{label_magnet}) mm".format(label_magnet = label_magnet),
                "YAxisZvec:="		, "0mm"
            ], 
            [
                "NAME:Attributes",
                "Name:="		, "RelativeCS_{magnet_id}".format(magnet_id = magnet_id)
            ])
            
    oEditor.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:Geometry3DAttributeTab",
                [
                    "NAME:PropServers", 
                    magnet_id
                ],
                [
                    "NAME:ChangedProps",
                    [
                        "NAME:Orientation",
                        "Value:="		, "RelativeCS_{magnet_id}".format(magnet_id = magnet_id)
                    ]
                    ]
                ]
            ])

#oEditor.SetWCS(
#	[
#		"NAME:SetWCS Parameter",
#		"Working Coordinate System:=", "Global",
#		"RegionDepCSOk:="	, False
#	])
    
magnet2_id_list = oEditor.GetObjectsInGroup("Magnet2_Group")
num_magnet2 = len(magnet2_id_list)
    
for magnet_id in magnet2_id_list:
    oEditor.SetWCS(
        [
            "NAME:SetWCS Parameter",
            "Working Coordinate System:=", "Global",
            "RegionDepCSOk:="	, False
        ])
    if not "_" in magnet_id:
        oEditor.CreateRelativeCS(
            [
                "NAME:RelativeCSParameters",
                "Mode:="		, "Axis/Position",
                "OriginX:="		, "0mm",
                "OriginY:="		, "0mm",
                "OriginZ:="		, "0mm",
                "XAxisXvec:="		, "cos(-2*pi/" + str(num_magnet2) + "*0 + pi) mm",
                "XAxisYvec:="		, "-sin(-2*pi/" + str(num_magnet2) + "*0 + pi) mm",
                "XAxisZvec:="		, "0mm",
                "YAxisXvec:="		, "sin(-2*pi/" + str(num_magnet2) + "*0 + pi) mm",
                "YAxisYvec:="		, "cos(-2*pi/" + str(num_magnet2) + "*0 + pi) mm",
                "YAxisZvec:="		, "0mm"
            ], 
            [
                "NAME:Attributes",
                "Name:="		, "RelativeCS_{magnet_id}".format(magnet_id = magnet_id)
            ])
        AddWarningMessage("RelativeCS for Magnet2_Group have been created")
    else:
        label_magnet = removeprefix(magnet_id, "Rectangle2_")
        oEditor.CreateRelativeCS(
            [
                "NAME:RelativeCSParameters",
                "Mode:="		, "Axis/Position",
                "OriginX:="		, "0mm",
                "OriginY:="		, "0mm",
                "OriginZ:="		, "0mm",
                "XAxisXvec:="		, "cos(-2*pi/" + str(num_magnet2) + "*{label_magnet} + pi) mm".format(label_magnet = label_magnet),
                "XAxisYvec:="		, "-sin(-2*pi/" + str(num_magnet2) + "*{label_magnet} + pi) mm".format(label_magnet = label_magnet),
                "XAxisZvec:="		, "0mm",
                "YAxisXvec:="		, "sin(-2*pi/" + str(num_magnet2) + "*{label_magnet} + pi) mm".format(label_magnet = label_magnet),
                "YAxisYvec:="		, "cos(-2*pi/" + str(num_magnet2) + "*{label_magnet} + pi) mm".format(label_magnet = label_magnet),
                "YAxisZvec:="		, "0mm"
            ], 
            [
                "NAME:Attributes",
                "Name:="		, "RelativeCS_{magnet_id}".format(magnet_id = magnet_id)
            ])
            
    oEditor.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:Geometry3DAttributeTab",
                [
                    "NAME:PropServers", 
                    magnet_id
                ],
                [
                    "NAME:ChangedProps",
                    [
                        "NAME:Orientation",
                        "Value:="		, "RelativeCS_{magnet_id}".format(magnet_id = magnet_id)
                    ]
                    ]
                ]
            ])

#oEditor.SetWCS(
#	[
#		"NAME:SetWCS Parameter",
#		"Working Coordinate System:=", "Global",
#		"RegionDepCSOk:="	, False
#	])

magnet3_id_list = oEditor.GetObjectsInGroup("Magnet3_Group")
num_magnet3 = len(magnet3_id_list)

oEditor.SetWCS(
        [
            "NAME:SetWCS Parameter",
            "Working Coordinate System:=", "Global",
            "RegionDepCSOk:="	, False
        ])
        
oEditor.CreateRelativeCS(
    [
        "NAME:RelativeCSParameters",
        "Mode:="		, "Axis/Position",
        "OriginX:="		, "0mm",
        "OriginY:="		, "0mm",
        "OriginZ:="		, "0mm",
        "XAxisXvec:="		, "0mm",
        "XAxisYvec:="		, "0mm",
        "XAxisZvec:="		, "1mm",
        "YAxisXvec:="		, "0mm",
        "YAxisYvec:="		, "1mm",
        "YAxisZvec:="		, "0mm"
    ], 
    [
        "NAME:Attributes",
        "Name:="		, "RelativeCS_Magnet3_Group"
    ])
AddWarningMessage("RelativeCS for Magnet3_Group have been created")
    
for magnet_id in magnet3_id_list:
    oEditor.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:Geometry3DAttributeTab",
                [
                    "NAME:PropServers", 
                    magnet_id
                ],
                [
                    "NAME:ChangedProps",
                    [
                        "NAME:Orientation",
                        "Value:="		, "RelativeCS_Magnet3_Group"
                    ]
                    ]
                ]
            ])

magnet4_id_list = oEditor.GetObjectsInGroup("Magnet4_Group")
num_magnet4 = len(magnet4_id_list)

oEditor.SetWCS(
        [
            "NAME:SetWCS Parameter",
            "Working Coordinate System:=", "Global",
            "RegionDepCSOk:="	, False
        ])
        
oEditor.CreateRelativeCS(
    [
        "NAME:RelativeCSParameters",
        "Mode:="		, "Axis/Position",
        "OriginX:="		, "0mm",
        "OriginY:="		, "0mm",
        "OriginZ:="		, "0mm",
        "XAxisXvec:="		, "0mm",
        "XAxisYvec:="		, "0mm",
        "XAxisZvec:="		, "-1mm",
        "YAxisXvec:="		, "0mm",
        "YAxisYvec:="		, "-1mm",
        "YAxisZvec:="		, "0mm"
    ], 
    [
        "NAME:Attributes",
        "Name:="		, "RelativeCS_Magnet4_Group"
    ])
AddWarningMessage("RelativeCS for Magnet4_Group have been created")
    
for magnet_id in magnet4_id_list:
    oEditor.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:Geometry3DAttributeTab",
                [
                    "NAME:PropServers", 
                    magnet_id
                ],
                [
                    "NAME:ChangedProps",
                    [
                        "NAME:Orientation",
                        "Value:="		, "RelativeCS_Magnet4_Group"
                    ]
                    ]
                ]
            ])
            
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global",
		"RegionDepCSOk:="	, False
	])
    
oModule = oDesign.GetModule("MaxwellParameterSetup")

magnet_id_list = magnet1_id_list + magnet2_id_list + magnet3_id_list + magnet4_id_list

for magnet_id in magnet_id_list:   
    oModule.AssignForce(
        [
            "NAME:Force1",
            "Reference CS:="	, "Global",
            "Is Virtual:="		, True,
            "Objects:="		, [magnet_id]
        ])

    oDesign.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:Maxwell3D",
                [
                    "NAME:PropServers", 
                    "MaxwellParameterSetup:Force1"
                ],
                [
                    "NAME:ChangedProps",
                    [
                        "NAME:Name",
                        "Value:="		, "Force_{magnet_id}".format(magnet_id = magnet_id)
                    ]
                ]
            ]
        ])
# Assign force parameters for the 4 magnet groups -- Magnet1_Group, Magnet2_Group, Magnet3_Group and Magnet4_Group

oModule = oDesign.GetModule("MaxwellParameterSetup")

magnet_group_list = [magnet1_id_list, magnet2_id_list, magnet3_id_list, magnet4_id_list]

for i in range(4):
    oModule.AssignForce(
        [
            "NAME:Force1",
            "Reference CS:="	, "Global",
            "Is Virtual:="		, True,
            "Objects:="		, magnet_group_list[i]
    ])
    oDesign.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:Maxwell3D",
                [
                    "NAME:PropServers", 
                    "MaxwellParameterSetup:Force1"
                ],
                [
                    "NAME:ChangedProps",
                    [
                        "NAME:Name",
                        "Value:="		, "Force_Magnet" + str(i+1) + "_Group"
                    ]
                ]
            ]
        ])
    AddWarningMessage("Force parameter assignment has been completed for Magnet{i}_Group".format(i=i+1))


for magnet_id in magnet_id_list:   
    oModule.AssignForce(
        [
            "NAME:Force1",
            "Reference CS:="	, "Global",
            "Is Virtual:="		, True,
            "Objects:="		, [magnet_id, "Airbox_" + magnet_id]
        ])

    oDesign.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:Maxwell3D",
                [
                    "NAME:PropServers", 
                    "MaxwellParameterSetup:Force1"
                ],
                [
                    "NAME:ChangedProps",
                    [
                        "NAME:Name",
                        "Value:="		, "Force_w_Airbox_{magnet_id}".format(magnet_id = magnet_id)
                    ]
                ]
            ]
        ])
# Assign force parameters for the 4 magnet groups -- Magnet1_Group, Magnet2_Group, Magnet3_Group and Magnet4_Group

oEditor = oDesign.SetActiveEditor("3D Modeler")
airbox_magnet1_id_list = oEditor.GetObjectsInGroup("Airbox_Magnet1_Group")
airbox_magnet2_id_list = oEditor.GetObjectsInGroup("Airbox_Magnet2_Group")
airbox_magnet3_id_list = oEditor.GetObjectsInGroup("Airbox_Magnet3_Group")
airbox_magnet4_id_list = oEditor.GetObjectsInGroup("Airbox_Magnet4_Group")

oModule = oDesign.GetModule("MaxwellParameterSetup")
magnet_group_list = [magnet1_id_list + airbox_magnet1_id_list, magnet2_id_list + airbox_magnet2_id_list, magnet3_id_list + airbox_magnet3_id_list, magnet4_id_list + airbox_magnet4_id_list]

for i in range(4):
    oModule.AssignForce(
        [
            "NAME:Force1",
            "Reference CS:="	, "Global",
            "Is Virtual:="		, True,
            "Objects:="		, magnet_group_list[i]
    ])
    oDesign.ChangeProperty(
        [
            "NAME:AllTabs",
            [
                "NAME:Maxwell3D",
                [
                    "NAME:PropServers", 
                    "MaxwellParameterSetup:Force1"
                ],
                [
                    "NAME:ChangedProps",
                    [
                        "NAME:Name",
                        "Value:="		, "Force_w_Airbox_Magnet" + str(i+1) + "_Group"
                    ]
                ]
            ]
        ])
    AddWarningMessage("Force parameter assignment has been completed for Magnet{i}_Group + Airbox_Magnet{i}_Group".format(i=i+1))
        
oProject.Save()

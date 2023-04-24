#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 15:45:37 2023

@author: tfu
"""

from datetime import datetime
from sdRDM import DataModel

#PorousPy = DataModel.from_markdown("/home/tfu/Documents/Kooperationen/RDM_project_JanRange/porous-media-flow-model/specifications/model.md")
PorousPy = DataModel.from_git("https://github.com/SimTech-Research-Data-Management/porous-media-flow-model.git")
PorousPy.Root.visualize_tree()

dataset = PorousPy.Root(
    id = "test_82_140722_Re21300_m4_hill_70_5Hz",
    description = "Time-averaged PIV-Data of a triply periodic minimal surface topology as porous medium adjascent to a free flow at Reynolds number Re=21300",
    name = "Time -resolved hill-alignment (@ centerline) @ Re=21300",
    date = datetime.today(),
    subjects = ["Coupling between free flow and porous medium", "highly spatiotemporal Particle Image Velocimetry", "Flow visualisation"],
    keywords = ["Turbulent FLow","Turbulent Pumping", "Porous Media", "highly spatiotemporal measurements","Highly space- and time-resolved", "Particle Image Velocimetry", "PIV", "Heat Transfer", "Triply Periodic Minimal Surface"]
    
    
)

dataset.add_to_authors(
    name = "Tobias Fuhrmann",
    affiliation = "Institute of Aerospace Thermodynamics (ITLR)",
    email = "tobias.fuhrmann@itlr.uni-stuttgart.de",
    phone = +4971168562438
)

dataset.add_to_authors(
    name = "Julian Härter",
    affiliation = "Institute of Aerospace Thermodynamics (ITLR)",
    email = "julian.haerter@itlr.uni-stuttgart.de",
    phone = +4971168562438
)

model = PorousPy.Model(type = "Porous Media Model", location = "Adjascent to a turbulent free stream")
model.porous_media = PorousPy.PorousMediaParameters(
    topology = "'Schwarz P' Triply Periodic Minimal Surface",
    height = 0.1,
    width = 0.34,
    depth = 0.14,
    porosity = 0.92,
    periodicity_x = 0.04,
    periodicity_y = 0.04,
    wall_thickness = 0.0001
)

devices = PorousPy.Hardware()
devices.add_to_camera(
    manufacturer = "LaVision",
    model = "Imager SX6M",
    lens = "Nikon AF NIKKOR 50mm 1:1.8D, Notchfilter (532 nm)",
    sensor = "CCD (charge-coupled devic)e"
)

# Adding Model to the Root-Dataset
dataset.model = model


print(">> Root parameters", dataset, sep="\n", end="\n\n")

#export to YAML
# with open("./dataset.yaml","w") as file:
#     file.write(dataset.yaml())
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

#### Dataset ####

dataset = PorousPy.Root(
    id = "test_73_260422_Re21300_m4",
    description = "Time-averaged PIV-Data of a triply periodic minimal surface topology as porous medium adjascent to a free flow at Reynolds number Re=21300",
    name = "Time-averaged hill-alignment (@ centerline) @ Re=21300",
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

#### Devices ####

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

devices.add_to_optics(
    manufacturer = "LaVision",
    model = "Laser Guiding Arm, Item-Numbers: 1108453, 1108375",    
)
devices.add_to_optics(
    manufacturer = "LaVision",
    model = "Sheet Optics (divergent), f=-20mm, Item-Numbers: 1108405, 1108516, 1108406",    
)

devices.add_to_camera(
    manufacturer = "Photron",
    model = "FASTCAM SA-X2",
    lens = "Nikon AF NIKKOR 50mm 1:1.8D, Notchfilter (532 nm)",
    sensor = "20 m pixel size, 12-bit ADC (Bayer system color, single sensor ) (CMOS)"
)

devices.add_to_laser(
    manufacturer = "Edgewave",
    model = "Innoslab IS200-2-L",
    wavelength = 532,
    type = "Nd:YAG pulsed",
    power = 35    
)

seeding = PorousPy.Seeding(manufacturer = "LaVision", model = "Aerosol Generator, Item-Number: 1108926")
seeding.particles = PorousPy.SeedingParameters(
    material = "Bis (2-ethylhexyl) sebacate (DEHS)",
    type = "Liquid",
    density = 910,
    particle_size = 0.00000016
)

PorousPy.Triggering(
    recording_mode = "cyclic time-based"
)

#### Free Flow ####

freeflow = PorousPy.FreeFlow(
    shape = "square duct flow",
    hydraulic_diameter = 0.14,
    height = 0.14,
    width = 0.14,
    depth = 0.14,
)
freeflow.fluid = PorousPy.FlowParameters(
    fluid = "Dry air",
    temperature = 1,
    pressure = 1,
    density = 1,
    kinematic_viscosity = 1,
    flow_velocity = 1,
    mass_flux = 1,
    #reynolds_number = 1, # not working
)

#### Measurement ####

measurements = PorousPy.Measurement(name = "test_73_260422_Re21300_m4")
measurements.recordings = PorousPy.Recording(
    
)

# Adding Model to the Root-Dataset
dataset.model = model


print(">> Root parameters", dataset, sep="\n", end="\n\n")

#export to YAML
# with open("./dataset.yaml","w") as file:
#     file.write(dataset.yaml())
# Dataset EXC2075 PN1-3

- [Dataset EXC2075 PN1-3](#dataset-exc2075-pn1-3)
  - [General information](#general-information)
    - [PorousMediaDocument](#porousmediadocument)
    - [Author](#author)
  - [Model specifications](#model-specifications)
    - [FreeFlow](#freeflow)
    - [FlowParameters](#flowparameters)
    - [Model](#model)
    - [PorousMediaParameters](#porousmediaparameters)
  - [Experimental setup](#experimental-setup)
    - [Hardware](#hardware)
    - [Device](#device)
    - [Camera \[_Device_\]](#camera-device)
    - [Laser \[_Device_\]](#laser-device)
    - [Seeding \[_Device_\]](#seeding-device)
    - [SeedingParameters](#seedingparameters)
    - [Triggering \[_Device_\]](#triggering-device)
  - [Methods](#methods)
    - [Measurement](#measurement)
    - [ProcessStep](#processstep)
    - [Software](#software)
    - [Recording](#recording)

This is the preliminary Markdown-file of EXC2075 PN1-3. The main goal of this document is to define a data storage standard for Particle Image Velocimetry (PIV) recordings. The data model is still under developement.

## General information

### PorousMediaDocument

This is a container for general information about the dataset. Please describe your dataset in detail here.

- __grant_information__
  - Type: string
  - Description: Hello
- __description__
  - Type: string
  - Description: Describes the content of the dataset
- __name__
  - Type: string
  - Description: Descriptive name of the dataset / ID
- __date__
  - Type: datetime
  - Description: Date/time when the dataset was created
- __authors__
  - Type: [Author](#author)
  - Multiple: True
  - Description: Persons who worked on the dataset
- __subjects__
  - Type: string
  - Multiple: True
  - Description: Research subjects covered by the dataset
- model
  - Type: Model
  - Description: Porous media model investigated in this dataset
- __keywords__
  - Type: string
  - Multiple: True
  - Description: Descriptive keywords to describe the datase (examples:PIV, time-resolved, time-averaged)
- __devices__
  - Type: [Hardware](#hardware)
  - Description: Devices used in this experiment
  - Multiple: True
- free_flow
  - Type: [FreeFlow](#freeflow)
  - Description: Free flow of the measurement
- measurements
  - Type: [Measurement](#measurement)
  - Description: Contains all measurements done in this experiment
  - Multiple: True

### Author

This is a container for information regarding persons who worked on the dataset or created it.

- __name__
  - Type: string
  - Description: Full name of the author
- __affiliation__
  - Type: string
  - Description: Organisation the author is affiliated with
- __email__
  - Type: string
  - Description: Contact e-mail adress of the author
- phone
  - Type: int
  - Description: Contact phone number of the author

## Model specifications

### FreeFlow

This is a container for information about the free flow channel and the working fluid.

- __shape__
  - Type: string
  - Description: Shape of the flow channels cross section
- __hydraulic_diameter__
  - Type: float
  - Description: Value of the hydraulic diameter in m
- height
  - Type: float
  - Description: Value of the flow channel height in m
- width
  - Type: float
  - Description: Value of the flow channel width in m
- depth
  - Type: float
  - Description: Value of the flow channel depth in m
- diameter
  - Type: float
  - Description: Value of the flow channel diameter in m
- __fluid__
  - Type: [FlowParameters](#flowparameters)
  - Description: Description of flow parameters

### FlowParameters

This is a container for information about the flow parameters.

- __fluid__
  - Type: string
  - Description: Name of the free flow fluid
- __temperature__
  - Type: float
  - Description: Value of the fluid temperature in K
- __pressure__
  - Type: float
  - Description: Value of the fluid pressure in bar
- __density__
  - Type: float
  - Description: Value of the fluid density in kg/m^3
- __kinematic_viscosity__
  - Type: float
  - Description: Value of the fluid kinematic viscosity in m^2/s
- __flow_velocity__
  - Type: float
  - Description: Value of the fluid flow velocity in m/s
- __mass_flux__
  - Type: float
  - Description:  Value of the fluid mass flux in kg/s
- __reynolds_number__
  - Type: float
  - Multiple: True
  - Description: Value(s) of investigated Reynolds number(s)

### Model

This is a container for information about a possible object in/adjascent to the free flow

- __type__
  - Type: string
  - Description: What kind of object is located inside the flow channel? (porous media model, cylinder, ...)

- __location__
  - Type: string
  - Description: Where is the object located inside the flow channel? (in, adjascent to, ... the free flow)

- porous_media
  - Type: [PorousMediaParameters](#porousmediaparameters)
  - Description: Description of porous media parameters

### PorousMediaParameters

This is a container for information about parameters of the used porous media model

- __topology__
  - Type: string
  - Description: Definition of the porous media model topology (rods, cylinders, minimal surface, ...)
- __height__
  - Type: float
  - Description: Value of the porous media model height in m
- __width__
  - Type: float
  - Description: Value of the porous media model width in m
- __depth__
  - Type: float
  - Description: Value of the porous media model depth in m
- __porosity__
  - Type: float
  - Description: Value of the porous media model porosity
- periodicity_x
  - Type: float
  - Description: Value of the porous media model periodicity in x-direction in m
- periodicity_y
  - Type: float
  - Description: Value of the porous media model periodicity in y-direction in m
- wall_thickness
  - Type: float
  - Description: Value of the porous media model wall thickness in m

## Experimental setup

### Hardware

This is a container for general information about the hardware which was used to capture the PIV data.

- __camera__
  - Type : [Camera](#camera-device)
  - Multiple: True
  - Description: Description of the used camera system
- __laser__
  - Type: [Laser](#laser-device)
  - Multiple: True
  - Description: Description of the used laser system
- __seeding__
  - Type: [Seeding](#seeding-device)
  - Description: Description of the used seeding device and seeding material
- optics
  - Type: [Device](#device)
  - Multiple: True
  - Description: Description of the used optical devices (laserarm, lenses, beamsplitter, sheet optics, ...)
- triggering
  - Type: [Triggering](#triggering-device)
  - Description: Description of the used triggering devices

### Device

This is a container for information regarding of general devices. For now it only applies to "Hardware-optics" but it could be for more.

- __manufacturer__
  - Type: string
  - Description: Name of the device's manufacturer
- __model__
  - Type: string
  - Description: Name of the device's model

### Camera [_Device_]

This is a container for information regarding cameras which were used within the dataset.

- lens
  - Type: string
  - Description: Name of the camera lens
- sensor
  - Type: string
  - Description: Description of the camera sensor

### Laser [_Device_]

This is a container for information regarding lasers which were used within the dataset.

- __wavelength__
  - Type: float
  - Description: Value of the used wavelength
- type
  - Type: string
  - Description: Pulsed or continous wave laser?
- power
  - Type: float
  - Description: value of the laser power

### Seeding [_Device_]

This is a container for information regarding of the seeding device which was used within the dataset.

- __particles__
  - Type: [SeedingParameters](#seedingparameters)
  - Description: Seeding parameters of the used seeding material

### SeedingParameters

This is a container for information regarding of the used seeding particles.

- __material__
  - Type: string
  - Description: Name of the seeding material
- __type__
  - Type: string
  - Description: Solid or liquid particles?
- __density__
  - Type: float
  - Description: Value of the seeding particle density in kg/m^3
- __particle_size__
  - Type: float
  - Description: Value or span of the seeding particle diameter in m
- kinematic_viscosity
  - Type: float
  - Description: Value of the seeding particle kinematic viscosity in m^2/s

### Triggering [_Device_]

This is a container for information regarding of the used triggering system.

- __recording_mode__
  - Type: string
  - Description: Type of recording mode (time-based, cyclic time-based, ...)

## Methods

### Measurement

- __name__
  - Type: string
  - Description: Name of the experiment
- recordings
  - Type: [Recording](#recording)
  - Description: Recordings that have been done in the course of the experiment
  - Multiple: True
- processing_steps
  - Type: [ProcessStep](#processstep)
  - Description: Processed video data of the flow measurement
  - Multiple: True

### ProcessStep

- __name__
  - Type: string
  - Description: Name of the processing step
- __processed_recording__
  - Type: [Recording](#recording)
  - Description: Resulting video from the processing
- __software__
  - Type: [Software](#software)
  - Description: Software that has been used to perform the processing step

### Software

This is a container for general information about the used software.

- __manufacturer__
  - Type: string
  - Description: Name of the used recording software manufacturer
- __name__
  - Type: string
  - Description: Name of the used recording software
- __version__
  - Type: string
  - Description: Version of the used recording software

### Recording

This is a container for information about the recording parameters

- __camera_id__
  - Type: @Camera.id
  - Description: ID of the camera that has been used
- __time__
  - Type: float
  - Description: Value of the investigated time period in s
- __repetition_rate__
  - Type: float
  - Description: Value of the recording repetition rate in Hz
- __field_of_view__
  - Type: string
  - Description: Value of the field of view in m x m
- height
  - Type: PositiveInt
  - Description: Height of the image
- width
  - Type: PositiveInt
  - Description: Width of the image
- n_frames
  - Type: integer
  - Description: Number of frames found in this video
- frames
  - Type: NDArray
  - Description: Videoframes

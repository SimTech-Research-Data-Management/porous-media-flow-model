- [Dataset EXC2075 PN1-3](#dataset-exc2075-pn1-3)
    - [Root](#root)
    - [Author](#author)
    - [Measurement](#measurement)
    - [ProcessStep](#processstep)
    - [Hardware](#hardware)
    - [Device](#device)
    - [Camera [_Device_]](#camera-device)
    - [Laser [_Device_]](#laser-device)
    - [Seeding [_Device_]](#seeding-device)
    - [SeedingParameters](#seedingparameters)
    - [Triggering [Device]](#triggering-device)
    - [Software](#software)
    - [FreeFlow](#freeflow)
    - [FlowParameters](#flowparameters)
    - [Model](#model)
    - [PorousMediaParameters](#porousmediaparameters)
    - [Recording](#recording)

# Dataset EXC2075 PN1-3

This is the preliminary Markdown-file of EXC2075 PN1-3. The main goal of this document is to define a data storage standard for Particle Image Velocimetry (PIV) recordings. The data model is still under developement.


### Root

This is a container for general information about the dataset. Please describe your dataset in detail here.

- __description*__
  - Type: string
  - Description: Describes the content of the dataset
- __name*__
  - Type: string
  - Description: Descriptive name of the dataset / ID
- __date*__
  - Type: date
  - Description: Date/time when the dataset was created
- __authors*__
  - Type: [Author](#author)
  - Multiple: True
  - Description: Persons who worked on the dataset
- __subjects*__
  - Type: string
  - Multiple: True
  - Description: Research subjects covered by the dataset
- __model__
  - Type: Model
  - Description: Porous media model investigated in this dataset
- __keywords*__
  - Type: string
  - Multiple: True
  - Description: Descriptive keywords to describe the datase (examples:PIV, time-resolved, time-averaged)
- __devices*__
  - Type: [Hardware](#hardware)
  - Description: Devices used in this experiment
  - Multiple: True
- __free_flow__
  - Type: [FreeFlow](#freeflow)
  - Description: Free flow of the measurement
- __measurements__
  - Type: [Measurement](#measurement)
  - Description: Contains all measurements done in this experiment
  - Multiple: True


### Author

This is a container for information regarding persons who worked on the dataset or created it.

- __name*__
    - Type: string
    - Description: Full name of the author
- __affiliation*__
    - Type: string
    - Description: Organisation the author is affiliated with
- __email*__
    - Type: string
    - Description: Contact e-mail adress of the author
- __phone__
    - Type: int
    - Description: Contact phone number of the author

### Measurement

- __name*__
  - Type: string
  - Description: Name of the experiment
- __recordings__
  - Type: [Recording](#recording)
  - Description: Recordings that have been done in the course of the experiment
  - Multiple: True
- __processing_steps__
  - Type: [ProcessStep](#processstep)
  - Description: Processed video data of the flow measurement
  - Multiple: True

### ProcessStep

- __name*__
  - Type: string
  - Description: Name of the processing step
- __processed_recording*__
  - Type: [Recording](#recording)
  - Description: Resulting video from the processing
- __software*__
  - Type: [Software](#software)
  - Description: Software that has been used to perform the processing step

### Hardware

This is a container for general information about the hardware which was used to capture the PIV data.

- __camera*__
    - Type : [Camera](#camera)
    - Multiple: True
    - Description: Description of the used camera system
- __laser*__
    - Type: [Laser](#laser)
    - Multiple: True
    - Description: Description of the used laser system
- __seeding*__
    - Type: [Seeding](#seeding)
    - Description: Description of the used seeding device and seeding material
- __optics__
    - Type: [Device](#device)
    - Multiple: True
    - Description: Description of the used optical devices (laserarm, lenses, beamsplitter, sheet optics, ...)
- __triggering__
    - Type: [Triggering](#triggering)
    - Description: Description of the used triggering devices

### Device

This is a container for information regarding of general devices. For now it only applies to "Hardware-optics" but it could be for more.

- __manufacturer*__
    - Type: string
    - Description: Name of the device's manufacturer
- __model*__
    - Type: string
    - Description: Name of the device's model   

### Camera [_Device_]

This is a container for information regarding cameras which were used within the dataset.

- __lens__
    - Type: string
    - Description: Name of the camera lens
- __sensor__
    - Type: string
    - Description: Description of the camera sensor


### Laser [_Device_]

This is a container for information regarding lasers which were used within the dataset.

- __wavelength*__
    - Type: float
    - Description: Value of the used wavelength
- __type__
    - Type: string
    - Description: Pulsed or continous wave laser?
- __power__
    - Type: float
    - Description: value of the laser power


### Seeding [_Device_]

This is a container for information regarding of the seeding device which was used within the dataset.

- __particles*__
    - Type: [SeedingParameters](#seedingparameters)
    - Description: Seeding parameters of the used seeding material


### SeedingParameters

This is a container for information regarding of the used seeding particles.

- __material*__
    - Type: string
    - Description: Name of the seeding material
- __type*__
    - Type: string
    - Description: Solid or liquid particles?
- __density*__
    - Type: float
    - Description: Value of the seeding particle density in kg/m^3
- __particle_size*__
    - Type: float
    - Description: Value or span of the seeding particle diameter in m
- __kinematic_viscosity__
    - Type: float
    - Description: Value of the seeding particle kinematic viscosity in m^2/s


### Triggering [Device]

This is a container for information regarding of the used triggering system.

- __recording_mode*__
    - Type: string
    - Description: Type of recording mode (time-based, cyclic time-based, ...) 


### Software

This is a container for general information about the used software.

- __manufacturer*__
    - Type: string
    - Description: Name of the used recording software manufacturer
- __name*__
    - Type: string
    - Description: Name of the used recording software
- __version*__
    - Type: string
    - Description: Version of the used recording software


### FreeFlow

This is a container for information about the free flow channel and the working fluid.

- __shape*__
    - Type: string
    - Description: Shape of the flow channels cross section
- __hydraulic_diameter*__
    - Type: float
    - Description: Value of the hydraulic diameter in m
- __height__
    - Type: float
    - Description: Value of the flow channel height in m 
- __width__
    - Type: float
    - Description: Value of the flow channel width in m 
- __depth__
    - Type: float
    - Description: Value of the flow channel depth in m 
- __diameter__
    - Type: float
    - Description: Value of the flow channel diameter in m 
- __fluid*__
    - Type: [FlowParameters](#flowparameters)
    - Description: Description of flow parameters


### FlowParameters 

This is a container for information about the flow parameters.

- __fluid*__
    - Type: string
    - Description: Name of the free flow fluid
- __temperature*__
    - Type: float
    - Description: Value of the fluid temperature in K
- __pressure*__
    - Type: float
    - Description: Value of the fluid pressure in bar
- __density*__
    - Type: float
    - Description: Value of the fluid density in kg/m^3
- __kinematic_viscosity*__
    - Type: float
    - Description: Value of the fluid kinematic viscosity in m^2/s
- __flow_velocity*__
    - Type: float
    - Description: Value of the fluid flow velocity in m/s
- __mass_flux*__
    - Type: float
    - Description:  Value of the fluid mass flux in kg/s
- __reynolds_number*__
    - Type: float
    - Multiple: True
    - Description: Value(s) of investigated Reynolds number(s)


### Model   

This is a container for information about a possible object in/adjascent to the free flow

- __type*__
    - Type: string
    - Description: What kind of object is located inside the flow channel? (porous media model, cylinder, ...)

- __location*__
    - Type: string
    - Description: Where is the object located inside the flow channel? (in, adjascent to, ... the free flow)

- __porous_media__
    - Type: [PorousMediaParameters](#porousmediaparameters)
    - Description: Description of porous media parameters


### PorousMediaParameters

This is a container for information about parameters of the used porous media model

- __topology*__
    - Type: string
    - Description: Definition of the porous media model topology (rods, cylinders, minimal surface, ...)
- __height*__
    - Type: float
    - Description: Value of the porous media model height in m 
- __width*__
    - Type: float
    - Description: Value of the porous media model width in m 
- __depth*__
    - Type: float
    - Description: Value of the porous media model depth in m 
- __porosity*__
    - Type: float
    - Description: Value of the porous media model porosity
- __periodicity_x__
    - Type: float
    - Description: Value of the porous media model periodicity in x-direction in m
- __periodicity_y__
    - Type: float
    - Description: Value of the porous media model periodicity in y-direction in m
- __wall_thickness__
    - Type: float
    - Description: Value of the porous media model wall thickness in m


### Recording

This is a container for information about the recording parameters

- __camera_id*__
  - Type: @Camera.id
  - Description: ID of the camera that has been used
- __height__
  - Type: PositiveInt
  - Description: Height of the image
- __width__
  - Type: PositiveInt
  - Description: Width of the image
- __n_frames__
  - Type: integer
  - Description: Number of frames found in this video
- __frames__
  - Type: NDArray
  - Description: Videoframes
- __time*__
  - Type: float
  - Description: Value of the investigated time period in s
- __repetition_rate*__
  - Type: float
  - Description: Value of the recording repetition rate in Hz
- __field_of_view*__
  - Type: string
  - Description: Value of the field of view in m x m
# Dataset EXC2075 PN1-3

- [Dataset EXC2075 PN1-3](#dataset-exc2075-pn1-3)
  - [General information](#general-information)
    - [Metadata](#metadata)
    - [Author](#author)
  - [Model specifications](#model-specifications)
    - [FreeFlow](#freeflow)
    - [FlowParameters](#flowparameters)
    - [Model](#model)
    - [PorousMedia](#porousmedia)
  - [Experimental setup](#experimental-setup)
    - [Hardware](#hardware)
    - [Device](#device)
    - [Camera \[*Device*\]](#camera-device)
    - [Laser \[*Device*\]](#laser-device)
    - [Seeding \[*Device*\]](#seeding-device)
    - [SeedingParameters](#seedingparameters)
    - [Triggering \[*Device*\]](#triggering-device)
  - [Methods](#methods)
    - [Measurement](#measurement)
    - [Calibration](#calibration)
    - [ProcessStep](#processstep)
    - [Software](#software)
    - [Recording](#recording)

This is the preliminary Markdown-file of EXC2075 PN1-3. The main goal of this document is to define a data storage standard for highly spatiotemporal Particle Image Velocimetry (PIV) recordings. The data model is still under development.

PIV is an optical, particle-based measurement technique used to measure fluid flow velocities. By illuminating small particles in the flow field with a laser sheet and analyzing their displacement between two consecutive images, PIV provides highly time and space resolved data on velocity profiles and flow structures.
EXC2075 PN1-3 focuses on understanding the turbulent pumping mechanisms in different porous structures topologies with different characteristic porous scales.
These fluid flow interactions between energy, mass and momentum transfer need to be further understood to improve engineering applications such as transpiration cooling, filtration processes and heat exchangers.
To that aim time-resolved and time-averaged velocity measurements were performed at the interface between a turbulent free flow and various porous structures.

## General information

*In this section the most important general information on the stored data set is listed here including for example a brief description, the ID of the dataset, the research subjects covered by the dataset.
It also provides the name of the author who worked on the dataset and the corresponding e-mail address as well as the affiliation.*

### Metadata

*The Metadata summarizes key information about the following dataset. It includes a description of the dataset's content, a descriptive name or ID of the dataset, and the date of creation. It also lists the contributors, highlights the research areas which are covered and specifies the specific porous media model investigated. Descriptive keywords help categorize the dataset and the the hardware used in the experiment is also stored. Free flow conditions of the turbulent air flow are also stored. The Metadata provides detailed information about the measurements conducted in the experiment.*

* **description**
  * Type: string
  * Description: Summary of the content and background of the dataset described in 3-5 sentences.
* **ID**
  * Type: string
  * Description: Descriptive name of the dataset or ID of the dataset.
* **date**
  * Type: datetime
  * Description: Date & time when the dataset was created.
* **authors**
  * Type: [Author](#author)
  * Multiple: True
  * Description: Persons who worked on the dataset.
* **subjects**
  * Type: string
  * Multiple: True
  * Description: Research subjects covered by the dataset.
* model
  * Type: Model
  * Description: Define the actual model which was investigated with the dataset.
* **keywords**
  * Type: string
  * Multiple: True
  * Description: Descriptive keywords to describe the dataset.
* **devices**
  * Type: [Hardware](#hardware)
  * Description: Experimental devices used in the dataset.
  * Multiple: True
* free\_flow
  * Type: [FreeFlow](#freeflow)
  * Description: Free flow conditions during the experiment
* measurements
  * Type: [Measurement](#measurement)
  * Description: Contains all measurements & recordings which were conducted during the experiment
  * Multiple: True

### Author

*The Author section provides information about the persons involved in working on or creating the dataset.
These information helps providing the identity and contact details of the authors associated with the dataset.*

* **name**
  * Type: string
  * Description: Full name of the author or the experimenter.
* **affiliation**
  * Type: string
  * Description: Organisation to which the author belongs.
* **email**
  * Type: string
  * Description: E-Mail adress of the author.
* phone
  * Type: int
  * Description: Phone number of the author.

## Model specifications

*The Model specifications provide information about the shape, dimensions, and working fluid of the free flow channel.
It includes details such as the hydraulic diameter of the channel as well as the height, width and depth of the channel.
Furthermore, fluid parameters and porous media parameters are listed, which allows a comprehensive understanding of the experimental setup.*

### FreeFlow

*The Free Flow section contains information about the shape, dimensions, and working fluid of the free flow channel.
It provides details such as the shape of the flow channel's cross-section, the hydraulic diameter, height, width and depth of the channel and a description of the flow parameters of the working fluid.*

* **shape**
  * Type: string
  * Description: Shape of the flow channel's cross section (e.g. rectangular, round, ...)
* **hydraulic\_diameter**
  * Type: float
  * Description: Value of the channel's hydraulic diameter. \[m]
* height
  * Type: float
  * Description: Value of the channel height, assuming a rectangular channel. \[m]
* width
  * Type: float
  * Description: Value of the flow channel width, assuming a rectangular channel. \[m]
* depth
  * Type: float
  * Description: Value of the flow channel depth, assuming a rectangular channel. \[m]
* diameter
  * Type: float
  * Description: Value of the flow channel diameter, assuming a round channel. \[m]
* **fluid**
  * Type: [FlowParameters](#flowparameters)
  * Description: Description of the free flow parameters during the dataset.

### FlowParameters

*The Flow Parameters encompasses crucial details about the flow parameters of the working fluid used in the present dataset.
These parameters provide a comprehensive understanding of the fluid's properties and flow conditions within the experiment.*

* **fluid**
  * Type: string
  * Description: Name of the free flow fluid (e.g. dry air, water, ...)
* **temperature**
  * Type: float
  * Description: Value of the fluid temperature at the inlet. \[K]
* **pressure**
  * Type: float
  * Description: Value of the fluid pressure at the outlet. \[bar]
* **density**
  * Type: float
  * Description: Value of the fluid density \[kg/m^3]
* **kinematic\_viscosity**
  * Type: float
  * Description: Value of the fluid kinematic viscosity \[m^2/s]
* **dynamic\_viscosity**
  * Type: float
  * Description: Value of the dynamic fluid viscosity \[mPas]
* **mass\_flux**
  * Type: float
  * Description:  Value of the fluid mass flux \[kg/s]
* **reynolds\_number**
  * Type: float
  * Multiple: True
  * Description: Value(s) of investigated channel Reynolds number(s). \[ - ]

### Model

*The Model section contains information about the location of the object in the flow channel.
It provides details regarding the type of the present porous media model, its location relative to the free flow and if applicable, detailed parameters related to the model which was used.*

* **type**
  * Type: string
  * Description: What kind of object is located inside the flow channel? (porous media model, cylinder, ...)
* **location**
  * Type: string
  * Description: Where is the object located inside the flow channel? (in, adjascent to, ... the free flow)
* porous_media
  * Type: [PorousMedia](#porousmediaparameters)
  * Description: Description of porous media parameters
* cad_model
  * Type: bytes
  * Description: CAD drawing of the used model (e.g. stored as a '.stl'-File)

### PorousMedia

*The Porous Media contains information regarding the parameters associated with the utilized porous media model.
They include the topology of the porous media model, the dimensions and other relevant material properties.*

* **topology**
  * Type: string
  * Description: Definition of the porous media model topology.
* **height**
  * Type: float
  * Description: Value of the porous media model height. \[m]
* **width**
  * Type: float
  * Description: Value of the porous media model width. \[m]
* **depth**
  * Type: float
  * Description: Value of the porous media model depth. \[m]
* **porosity**
  * Type: float
  * Description: Value of the porous media model porosity. \[ - ]
* periodicity\_x
  * Type: float
  * Description: Value of the porous media model periodicity in x-direction. \[m]
* periodicity\_y
  * Type: float
  * Description: Value of the porous media model periodicity in y-direction. \[m]
* wall\_thickness
  * Type: float
  * Description: Value of the porous media model wall thickness. \[m]

## Experimental setup

*The Experimental setup provides detailed information about the hardware devices used for capturing the PIV data of the present dataset.
The Hardware container includes descriptions of the camera systems, laser systems, seeding devices and materials, optical devices, and triggering systems utilized during the experiment.*

### Hardware

*The Hardware includes descriptions of the camera systems, laser systems, seeding devices and materials, optical devices, and triggering systems utilized during the experiment.*

* **camera**
  * Type : [Camera](#camera-device)
  * Multiple: True
  * Description: Description of the used camera system.
* **laser**
  * Type: [Laser](#laser-device)
  * Multiple: True
  * Description: Description of the used laser system.
* **seeding**
  * Type: [Seeding](#seeding-device)
  * Multiple: True
  * Description: Description of the used seeding device and seeding material.
* optics
  * Type: [Device](#device)
  * Multiple: True
  * Description: Description of the used optical devices (e.g. laserarms, lenses, beamsplitter, sheet optics, ...).
* triggering
  * Type: [Triggering](#triggering-device)
  * Multiple: True
  * Description: Description of the used triggering devices.

### Device

*The Device provides general information about the manufacturer and model of the used devices such as cameras, lasers, optics, triggering and seeding systems.*

* **manufacturer**
  * Type: string
  * Description: Name of the device's manufacturer.
* model
  * Type: string
  * Description: Name of the device's model.

### Camera \[*Device*]

*It specifies details about the camera lenses and sensors which were used during the experiment.*

* lens
  * Type: string
  * Description: Name of the camera lens which were used.
* sensor
  * Type: string
  * Description: Description of the camera sensor which were used.

### Laser \[*Device*]

*The Laser provides information about the laser wavelength, either the laser is pulsed or continuous as well as the laser power.*

* **wavelength**
  * Type: float
  * Description: Value of the used wavelength of the laser. \[nm]
* type
  * Type: string
  * Description: Type of the used laser (e.g. pulsed or continuous wave laser, ...)
* power
  * Type: float
  * Description: Value of the laser power. \[W]

### Seeding \[*Device*]

*The Seeding describes the material of the seeding particles, the type of them as well as their density, particle size, and kinematic viscosity.*

* **particles**
  * Type: [SeedingParameters](#seedingparameters)
  * Description: Seeding parameters of the used seeding material during the experiment.

### SeedingParameters

*The Seeding Parameters contains crucial information about the seeding material used in the experiment.
It includes details such as the material name, particle type, density, particle size and the kinematic viscosity of the seeding particles.
These parameters provide valuable insights into the characteristics of the seeding material and its influence on the fluid flow behavior within the experimental setup.*

* **material**
  * Type: string
  * Description: Name of the seeding material.
* **phase**
  * Type: string
  * Description: Phase of the seeding material which was used (e.g. solid, liquid, ...).
* **density**
  * Type: float
  * Description: Value of the seeding particle density. \[kg/m^3]
* **particle\_size**
  * Type: float
  * Description: Value or span of the seeding particle diameter. \[m]
* kinematic\_viscosity
  * Type: float
  * Description: Value of the seeding particle kinematic viscosity \[m^2/s]

### Triggering \[*Device*]

*The Triggering explains the recording mode employed during the experiment.*

* **recording\_mode**
  * Type: string
  * Description: Type of recording mode during the experiment (e.g. time-based, cyclic time-based, ...).

## Methods

*The Methods present a detailed account of the experimental approach and procedures used.
It includes information about the experiment's name, the amount of recordings made during the study, and the processing steps applied to the flow measurement video data (.lvs-files).
The section also provides insights into the software used for processing and the recording parameters of the utilized camera system.*

### Measurement

*The Measurement encompasses key details about the conducted experiment and its calibration.*

* **name**
  * Type: string
  * Description: Name of the experiment.It should contain all relevant information about the expe.
* calibration
  * Type: [Calibration](#calibration)
  * Description: Calibration that has been done before the actual experiment.
  * Multiple: True
* recordings
  * Type: [Recording](#recording)
  * Description: Recordings that have been done in the course of the experiment.
  * Multiple: True
* processing\_steps
  * Type: [ProcessStep](#processstep)
  * Description: Processing steps and processed video data of the experiment
  * Multiple: True

### Calibration

*The Calibration contains information about the parameters used during the recording process.
The parameters are providing insights into the camera position relative to the experiment for correcting possible misalignments.*

* **calibration\_type**
  * Type: string
  * Description: Specify the calibration plate and/or the calibration facility which was used for calibration.
* camera\_position\_translation
  * Type: float
  * Description: Value of the translation of the camera position relative to the calibration plate. \[m]
* camera\_position\_rotation
  * Type: float
  * Description: Value of the rotation of the camera position relative to the calibration plate. \[°]
* **scale\_factor**
  * Type: float
  * Description: Value of the scale factor of the recordings.The amount of pixels corresponding to the length of 1 mm. \[px/mm]
* calibration\_image
  * Type: bytes
  * Description: The actual calibration image which was used.

### ProcessStep

*The Process Step outlines the specific processing steps applied to the flow measurement video data.
It includes the name of each processing step, the resulting video from the processing, and the software used to post-process the data.
Additionally, files with the extension ".lvs" from the Davis 10 software can be embedded within this section, providing a comprehensive record of the processing workflow and ensuring the availability of relevant files for reference and replication.*

* **name**
  * Type: string
  * Description: Full name of the processing step.
* **processed\_recording**
  * Type: [Recording](#recording)
  * Description: Resulting video after applying the process steps and the raw video.
  * Multiple: True
* **software**
  * Type: [Software](#software)
  * Description: Software that has been used to perform the processing steps.
  * Multiple: True

### Software

*The Software section serves as a container for general information about the software utilized in the experiment.
It includes details such as the name of the manufacturer, the specific software name, and the version used to generate the dataset.
These details provide important context for the experiment, allowing for reproducibility and facilitating a clear understanding of the software environment in which the data analysis and processing were performed.*

* **manufacturer**
  * Type: string
  * Description: Name of the used recording or processing software manufacturer.
* **name**
  * Type: string
  * Description: Name of the used recording or processing software.
* version
  * Type: string
  * Description: Version of the used recording or processing software.

### Recording

*The Recording contains crucial information about the parameters used during the recording process.
These parameters offer valuable insights into the experimental setup, facilitating accurate analysis and interpretation of the recorded data.
The inclusion of the video frames allows for a visual reference and further examination of the recorded footage.*

* **time**
  * Type: float
  * Description: Value of the investigated time period. \[s]
* **repetition\_rate**
  * Type: float
  * Description: Value of the recording repetition rate. \[Hz]
* **field\_of\_view**
  * Type: string
  * Description: Value of the field of view. \[m x m]
* n\_frames
  * Type: integer
  * Description: Number of frames found in this video.
* frames
  * Type: bytes
  * Description: The actual Videoframes of the raw video
* location
  * Type: string
  * Description: Specify the local filepath to the location of the recordings.

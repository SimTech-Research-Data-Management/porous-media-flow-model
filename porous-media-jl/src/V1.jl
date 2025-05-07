# This file contains Julia type definitions with JSON serialization.
#
# WARNING: This is an auto-generated file.
# Do not edit directly - any changes will be overwritten.

module Porousmedia

using JSON3
using StructTypes

#=
  Type Definitions
  ---------------
  Main struct definitions with their fields and JSON serialization support.
=#
"""
The Recording contains crucial information about the parameters used
during the recording process.These parameters offer valuable insights
integero the experimental setup, facilitating accurate analysis and
integererpretation of the recorded data. The inclusion of the video
frames allows for a visual reference and further examination of the
recorded footage.
"""
Base.@kwdef mutable struct Recording
    """
    Value of the investigated time period. (s)
    """
    time::Float64

    """
    Value of the recording repetition rate. (Hz)
    """
    repetition_rate::Float64

    """
    Value of the field of view. (m x m)
    """
    field_of_view::String

    """
    Number of frames found in this video.
    """
    n_frames::Union{Int64, Nothing} = nothing

    """
    The actual Videoframes of the raw video
    """
    frames::Union{bytes, Nothing} = nothing

    """
    Specify the local filepath to the location of the recordings.
    """
    location::Union{String, Nothing} = nothing

end

export Recording

"""
The Software section serves as a container for general information
about the software utilized in the experiment.It includes details
such as the name of the manufacturer, the specific software name,
and the version used to generate the dataset.These details provide
important context for the experiment, allowing for reproducibility
and facilitating a clear understanding of the software environment in
which the data analysis and processing were performed.
"""
Base.@kwdef mutable struct Software
    """
    Name of the used recording or processing software manufacturer.
    """
    manufacturer::String

    """
    Name of the used recording or processing software.
    """
    name::String

    """
    Version of the used recording or processing software.
    """
    version::Union{String, Nothing} = nothing

end

export Software

"""
The Parameter section defines the specific parameters used in various
operations during the data processing. It includes the name of the
parameter and its corresponding value, which can be a float, string,
or boolean. This information is crucial for understanding the exact
configuration of each operation and ensuring reproducibility of the
processing steps.
"""
Base.@kwdef mutable struct Parameter
    """
    Name of the parameter.
    """
    name::String

    """
    Value of the parameter.
    """
    value::Union{
    ParameterValueType, Nothing} = nothing

end

export Parameter

"""
The Operation section defines the specific operations performed
during the data processing.It includes the name of the operation, its
description, and the parameters used in the operation.
"""
Base.@kwdef mutable struct Operation
    """
    Name of the operation.
    """
    name::String

    """
    Description of the operation.
    """
    description::Union{String, Nothing} = nothing

    """
    Parameters of the operation.
    """
    parameters::Union{Vector{
    Parameter}, Nothing} = nothing

end

export Operation

"""
The Process Step outlines the specific processing steps applied
to the flow measurement video data.It includes the name of each
processing step, the resulting video from the processing, and the
software used to post-process the data.Additionally, files with the
extension ".lvs" from the Davis 10 software can be embedded within
this section, providing a comprehensive record of the processing
workflow and ensuring the availability of relevant files for reference
and replication.
"""
Base.@kwdef mutable struct ProcessStep
    """
    Full name of the processing step.
    """
    name::String

    """
    List of processing steps carried out with the processing software.
    """
    operation_list::Union{Vector{
    Operation}, Nothing} = nothing

    """
    Resulting video after applying the process steps and the raw video.
    """
    processed_recording::Union{Vector{
    Recording}, Nothing} = nothing

    """
    Software that has been used to perform the processing steps.
    """
    software::Vector{
    Software}

end

export ProcessStep

"""
The Calibration contains information about the parameters used during
the recording process.The parameters are providing insights integero
the camera position relative to the experiment for correcting possible
misalignments.
"""
Base.@kwdef mutable struct Calibration
    """
    Specify the calibration plate and/or the calibration facility which
    was used for calibration.
    """
    calibration_type::String

    """
    Value of the scale factor of the recordings.The amount of pixels
    corresponding to the length of 1 mm. (px/mm)
    """
    scale_factor::Float64

    """
    Value of the translation of the camera position relative to the
    calibration plate. (m)
    """
    camera_position_translation::Union{Float64, Nothing} = nothing

    """
    Value of the rotation of the camera position relative to the
    calibration plate. (°)
    """
    camera_position_rotation::Union{Float64, Nothing} = nothing

    """
    The actual calibration image which was used.
    """
    calibration_image::Union{bytes, Nothing} = nothing

end

export Calibration

"""
The Measurement encompasses key details about the conducted experiment
and its calibration.
"""
Base.@kwdef mutable struct Measurement
    """
    Name of the experiment.It should contain all relevant information
    about the experiment.
    """
    name::String

    """
    Calibration that has been done before the actual experiment.
    """
    calibration::Union{Vector{
    Calibration}, Nothing} = nothing

    """
    Recordings that have been done in the course of the experiment.
    """
    recordings::Union{Vector{
    Recording}, Nothing} = nothing

    """
    Processing steps and processed video data of the experiment
    """
    processing_steps::Union{Vector{
    ProcessStep}, Nothing} = nothing

end

export Measurement

"""
The Triggering explains the recording mode employed during the
experiment.
"""
Base.@kwdef mutable struct Triggering
    """
    Name of the device's manufacturer.
    """
    manufacturer::String

    """
    Type of recording mode during the experiment (e.g. time-based, cyclic
    time-based, ...).
    """
    recording_mode::String

    """
    Name of the device's model.
    """
    model::Union{String, Nothing} = nothing

end

export Triggering

"""
The Seeding Parameters contains crucial information about the seeding
material used in the experiment.It includes details such as the
material name, particle type, density, particle size and the kinematic
viscosity of the seeding particles.These parameters provide valuable
insights integero the characteristics of the seeding material and its
influence on the fluid flow behavior within the experimental setup.
"""
Base.@kwdef mutable struct SeedingParameters
    """
    Name of the seeding material.
    """
    material::String

    """
    Phase of the seeding material which was used (e.g. solid,
    liquid, ...).
    """
    phase::String

    """
    Value of the seeding particle density. (kg/m^3)
    """
    density::Float64

    """
    Value or span of the seeding particle diameter. (m)
    """
    particle_size::Float64

    """
    Value of the seeding particle kinematic viscosity (m^2/s)
    """
    kinematic_viscosity::Union{Float64, Nothing} = nothing

end

export SeedingParameters

"""
The Seeding describes the material of the seeding particles, the
type of them as well as their density, particle size, and kinematic
viscosity.
"""
Base.@kwdef mutable struct Seeding
    """
    Name of the device's manufacturer.
    """
    manufacturer::String

    """
    Seeding parameters of the used seeding material during the experiment.
    """
    particles::
    SeedingParameters

    """
    Name of the device's model.
    """
    model::Union{String, Nothing} = nothing

end

export Seeding

"""
The Laser provides information about the laser wavelength, either the
laser is pulsed or continuous as well as the laser power.
"""
Base.@kwdef mutable struct Laser
    """
    Name of the device's manufacturer.
    """
    manufacturer::String

    """
    Value of the used wavelength of the laser. (nm)
    """
    wavelength::Float64

    """
    Name of the device's model.
    """
    model::Union{String, Nothing} = nothing

    """
    Type of the used laser (e.g. pulsed or continuous wave laser, ...)
    """
    type::Union{String, Nothing} = nothing

    """
    Value of the laser power. (W)
    """
    power::Union{Float64, Nothing} = nothing

end

export Laser

"""
It specifies details about the camera lenses and sensors which were
used during the experiment.
"""
Base.@kwdef mutable struct Camera
    """
    Name of the device's manufacturer.
    """
    manufacturer::String

    """
    Name of the device's model.
    """
    model::Union{String, Nothing} = nothing

    """
    Name of the camera lens which were used.
    """
    lens::Union{String, Nothing} = nothing

    """
    Description of the camera sensor which were used.
    """
    sensor::Union{String, Nothing} = nothing

end

export Camera

"""
The Device provides general information about the manufacturer and
model of the used devices such as cameras, lasers, optics, triggering
and seeding systems.
"""
Base.@kwdef mutable struct Device
    """
    Name of the device's manufacturer.
    """
    manufacturer::String

    """
    Name of the device's model.
    """
    model::Union{String, Nothing} = nothing

end

export Device

"""
The Hardware includes descriptions of the camera systems, laser
systems, seeding devices and materials, optical devices, and
triggering systems utilized during the experiment.
"""
Base.@kwdef mutable struct Hardware
    """
    Description of the used camera system.
    """
    camera::Vector{
    Camera}

    """
    Description of the used laser system.
    """
    laser::Vector{
    Laser}

    """
    Description of the used seeding device and seeding material.
    """
    seeding::Vector{
    Seeding}

    """
    Description of the used optical devices (e.g. laserarms, lenses,
    beamsplitter, sheet optics, ...).
    """
    optics::Union{Vector{
    Device}, Nothing} = nothing

    """
    Description of the used triggering devices.
    """
    triggering::Union{Vector{
    Triggering}, Nothing} = nothing

end

export Hardware

"""
The Porous Media contains information regarding the parameters
associated with the utilized porous media model.They include the
topology of the porous media model, the dimensions and other relevant
material properties.
"""
Base.@kwdef mutable struct PorousMedia
    """
    Definition of the porous media model topology.
    """
    topology::String

    """
    Value of the porous media model height. (m)
    """
    height::Float64

    """
    Value of the porous media model width. (m)
    """
    width::Float64

    """
    Value of the porous media model depth. (m)
    """
    depth::Float64

    """
    Value of the porous media model porosity. ( - )
    """
    porosity::Float64

    """
    Value of the porous media model permeability. (m^2)
    """
    permeability::Union{Float64, Nothing} = nothing

    """
    Value of the porous media model periodicity in x-direction. (m)
    """
    periodicity_x::Union{Float64, Nothing} = nothing

    """
    Value of the porous media model periodicity in y-direction. (m)
    """
    periodicity_y::Union{Float64, Nothing} = nothing

    """
    Value of the porous media model wall thickness. (m)
    """
    wall_thickness::Union{Float64, Nothing} = nothing

end

export PorousMedia

"""
The Model section contains information about the location of the
object in the flow channel.It provides details regarding the type
of the present porous media model, its location relative to the free
flow and if applicable, detailed parameters related to the model which
was used.
"""
Base.@kwdef mutable struct Model
    """
    What kind of object is located inside the flow channel? (porous media
    model, cylinder, ...)
    """
    type::String

    """
    Where is the object located inside the flow channel? (in, adjascent
    to, ... the free flow)
    """
    location::String

    """
    Description of porous media parameters
    """
    porous_media::Union{
    PorousMedia, Nothing} = nothing

    """
    CAD drawing of the used model (e.g. stored as a '.stl'-File)
    """
    cad_model::Union{bytes, Nothing} = nothing

end

export Model

"""
The Flow Parameters encompasses crucial details about the flow
parameters of the working fluid used in the present dataset. These
parameters provide a comprehensive understanding of the fluid's
properties and flow conditions within the experiment.
"""
Base.@kwdef mutable struct FlowParameters
    """
    Name of the free flow fluid (e.g. dry air, water, ...)
    """
    fluid::String

    """
    Value of the fluid temperature at the inlet. (K)
    """
    temperature::Float64

    """
    Value of the fluid pressure at the outlet. (Pa)
    """
    pressure::Float64

    """
    Value of the fluid density (kg/m^3)
    """
    density::Float64

    """
    Value of the fluid kinematic viscosity (m^2/s)
    """
    kinematic_viscosity::Float64

    """
    Value of the dynamic fluid viscosity (mPas)
    """
    dynamic_viscosity::Float64

    """
    Value of the fluid mass flux (kg/s)
    """
    mass_flux::Vector{Float64}

    """
    Value(s) of investigated channel Reynolds number(s). ( - )
    """
    reynolds_number::Vector{Float64}

end

export FlowParameters

"""
The Free Flow section contains information about the shape,
dimensions, and working fluid of the free flow channel.It provides
details such as the shape of the flow channel's cross-section, the
hydraulic diameter, height, width and depth of the channel and a
description of the flow parameters of the working fluid.
"""
Base.@kwdef mutable struct FreeFlow
    """
    Shape of the flow channel's cross section (e.g. rectangular,
    round, ...)
    """
    shape::String

    """
    Value of the channel's hydraulic diameter (m)
    """
    hydraulic_diameter::Float64

    """
    Description of the free flow parameters during the dataset.
    """
    fluid::
    FlowParameters

    """
    Value of the channel height, assuming a rectangular channel. (m)
    """
    height::Union{Float64, Nothing} = nothing

    """
    Value of the flow channel width, assuming a rectangular channel. (m)
    """
    width::Union{Float64, Nothing} = nothing

    """
    Value of the flow channel depth, assuming a rectangular channel. (m)
    """
    depth::Union{Float64, Nothing} = nothing

    """
    Value of the flow channel diameter, assuming a round channel. (m)
    """
    diameter::Union{Float64, Nothing} = nothing

end

export FreeFlow

"""
The Author section provides information about the persons involved in
working on or creating the dataset.These information helps providing
the identity and contact details of the authors associated with the
dataset.
"""
Base.@kwdef mutable struct Author
    """
    Full name of the author or the experimenter.
    """
    name::String

    """
    Organisation to which the author belongs.
    """
    affiliation::String

    """
    E-Mail adress of the author.
    """
    email::String

    """
    Phone number of the author.
    """
    phone::Union{Int64, Nothing} = nothing

end

export Author

"""
The Metadata summarizes key information about the following dataset.
It includes a description of the dataset's content, a descriptive
name or ID of the dataset, and the date of creation. It also lists
the contributors, highlights the research areas which are covered and
specifies the specific porous media model investigated. Descriptive
keywords help categorize the dataset and the the hardware used in the
experiment is also stored. Free flow conditions of the turbulent air
flow are also stored. The Metadata provides detailed information about
the measurements conducted in the experiment.
"""
Base.@kwdef mutable struct Metadata
    """
    Summary of the content and background of the dataset described in 3-
    5 sentences.
    """
    description::String

    """
    Descriptive name of the dataset or ID of the dataset.
    """
    dataset_id::String

    """
    Date & time when the dataset was created.
    """
    date::String

    """
    Persons who worked on the dataset.
    """
    authors::Vector{
    Author}

    """
    Research subjects covered by the dataset.
    """
    subjects::Vector{String}

    """
    Define the actual model which was investigated with the dataset.
    """
    model::Union{
    Model, Nothing} = nothing

    """
    Descriptive keywords to describe the dataset.
    """
    keywords::Vector{String}

    """
    Experimental devices used in the dataset.
    """
    devices::Vector{
    Hardware}

    """
    Free flow conditions during the experiment
    """
    free_flow::Union{
    FreeFlow, Nothing} = nothing

    """
    Contains all measurements & recordings which were conducted during
    the experiment
    """
    measurements::Union{Vector{
    Measurement}, Nothing} = nothing

end

export Metadata


#=
  Union Type Definitions
  ---------------------
  Custom union types for fields that can accept multiple types.
=#

"""
Union type for Parameter.value
"""
abstract type ParameterValueType end
struct ParameterValueFloat <: ParameterValueType
    value::Float64
end
struct ParameterValueString <: ParameterValueType
    value::String
end
struct ParameterValueBoolean <: ParameterValueType
    value::Bool
end

end # module porousmedia
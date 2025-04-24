//! This file contains Rust struct definitions with serde serialization.
//!
//! WARNING: This is an auto-generated file.
//! Do not edit directly - any changes will be overwritten.

use derive_builder::Builder;
use schemars::JsonSchema;
use serde::{Deserialize, Serialize};

//
// Type definitions
//
/// The Metadata summarizes key information about the following dataset.
/// It includes a description of the dataset's content, a descriptive
/// name or ID of the dataset, and the date of creation. It also
/// lists the contributors, highlights the research areas which
/// are covered and specifies the specific porous media model
/// investigated. Descriptive keywords help categorize the dataset and
/// the the hardware used in the experiment is also stored. Free flow
/// conditions of the turbulent air flow are also stored. The Metadata
/// provides detailed information about the measurements conducted in
/// the experiment.
#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema, Builder, Default)]
#[allow(non_snake_case)]
pub struct Metadata {
    /// Summary of the content and background of the dataset described in 3-
    /// 5 sentences.
    ///
    #[builder(setter(into))]
    pub description: String,

    /// Descriptive name of the dataset or ID of the dataset.
    ///
    #[builder(setter(into))]
    pub dataset_id: String,

    /// Date & time when the dataset was created.
    ///
    #[builder(setter(into))]
    pub date: String,

    /// Persons who worked on the dataset.
    ///
    #[builder(default, setter(into, each(name = "to_authors")))]
    pub authors: Vec<Author>,

    /// Research subjects covered by the dataset.
    ///
    #[builder(default, setter(into, each(name = "to_subjects")))]
    pub subjects: Vec<String>,

    /// Define the actual model which was investigated with the dataset.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub model: Option<Model>,

    /// Descriptive keywords to describe the dataset.
    ///
    #[builder(default, setter(into, each(name = "to_keywords")))]
    pub keywords: Vec<String>,

    /// Experimental devices used in the dataset.
    ///
    #[builder(default, setter(into, each(name = "to_devices")))]
    pub devices: Vec<Hardware>,

    /// Free flow conditions during the experiment
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub free_flow: Option<FreeFlow>,

    /// Contains all measurements & recordings which were conducted during
    /// the experiment
    #[serde(default, skip_serializing_if = "Vec::is_empty")]
    #[builder(default, setter(into, each(name = "to_measurements")))]
    pub measurements: Vec<Measurement>,
}

/// The Author section provides information about the persons involved
/// in working on or creating the dataset.These information helps
/// providing the identity and contact details of the authors
/// associated with the dataset.
#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema, Builder, Default)]
#[allow(non_snake_case)]
pub struct Author {
    /// Full name of the author or the experimenter.
    ///
    #[builder(setter(into))]
    pub name: String,

    /// Organisation to which the author belongs.
    ///
    #[builder(setter(into))]
    pub affiliation: String,

    /// E-Mail adress of the author.
    ///
    #[builder(setter(into))]
    pub email: String,

    /// Phone number of the author.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub phone: Option<i64>,
}

/// The Free Flow section contains information about the shape,
/// dimensions, and working fluid of the free flow channel.It provides
/// details such as the shape of the flow channel's cross-section, the
/// hydraulic diameter, height, width and depth of the channel and a
/// description of the flow parameters of the working fluid.
#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema, Builder, Default)]
#[allow(non_snake_case)]
pub struct FreeFlow {
    /// Shape of the flow channel's cross section (e.g. rectangular,
    /// round, ...)
    ///
    #[builder(setter(into))]
    pub shape: String,

    /// Value of the channel's hydraulic diameter (m)
    ///
    #[builder(setter(into))]
    pub hydraulic_diameter: f64,

    /// Value of the channel height, assuming a rectangular channel. (m)
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub height: Option<f64>,

    /// Value of the flow channel width, assuming a rectangular channel. (m)
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub width: Option<f64>,

    /// Value of the flow channel depth, assuming a rectangular channel. (m)
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub depth: Option<f64>,

    /// Value of the flow channel diameter, assuming a round channel. (m)
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub diameter: Option<f64>,

    /// Description of the free flow parameters during the dataset.
    ///
    #[builder(setter(into))]
    pub fluid: FlowParameters,
}

/// The Flow Parameters encompasses crucial details about the flow
/// parameters of the working fluid used in the present dataset. These
/// parameters provide a comprehensive understanding of the fluid's
/// properties and flow conditions within the experiment.
#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema, Builder, Default)]
#[allow(non_snake_case)]
pub struct FlowParameters {
    /// Name of the free flow fluid (e.g. dry air, water, ...)
    ///
    #[builder(setter(into))]
    pub fluid: String,

    /// Value of the fluid temperature at the inlet. (K)
    ///
    #[builder(setter(into))]
    pub temperature: f64,

    /// Value of the fluid pressure at the outlet. (Pa)
    ///
    #[builder(setter(into))]
    pub pressure: f64,

    /// Value of the fluid density (kg/m^3)
    ///
    #[builder(setter(into))]
    pub density: f64,

    /// Value of the fluid kinematic viscosity (m^2/s)
    ///
    #[builder(setter(into))]
    pub kinematic_viscosity: f64,

    /// Value of the dynamic fluid viscosity (mPas)
    ///
    #[builder(setter(into))]
    pub dynamic_viscosity: f64,

    /// Value of the fluid mass flux (kg/s)
    ///
    #[builder(default, setter(into, each(name = "to_mass_flux")))]
    pub mass_flux: Vec<f64>,

    /// Value(s) of investigated channel Reynolds number(s). ( - )
    ///
    #[builder(default, setter(into, each(name = "to_reynolds_number")))]
    pub reynolds_number: Vec<f64>,
}

/// The Model section contains information about the location of the
/// object in the flow channel.It provides details regarding the type
/// of the present porous media model, its location relative to the
/// free flow and if applicable, detailed parameters related to the
/// model which was used.
#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema, Builder, Default)]
#[allow(non_snake_case)]
pub struct Model {
    /// What kind of object is located inside the flow channel? (porous media
    /// model, cylinder, ...)
    ///
    #[serde(rename = "type")]
    #[builder(setter(into))]
    pub type_: String,

    /// Where is the object located inside the flow channel? (in, adjascent
    /// to, ... the free flow)
    ///
    #[builder(setter(into))]
    pub location: String,

    /// Description of porous media parameters
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub porous_media: Option<PorousMedia>,

    /// CAD drawing of the used model (e.g. stored as a '.stl'-File)
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub cad_model: Option<Vec<u8>>,
}

/// The Porous Media contains information regarding the parameters
/// associated with the utilized porous media model.They include
/// the topology of the porous media model, the dimensions and other
/// relevant material properties.
#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema, Builder, Default)]
#[allow(non_snake_case)]
pub struct PorousMedia {
    /// Definition of the porous media model topology.
    ///
    #[builder(setter(into))]
    pub topology: String,

    /// Value of the porous media model height. (m)
    ///
    #[builder(setter(into))]
    pub height: f64,

    /// Value of the porous media model width. (m)
    ///
    #[builder(setter(into))]
    pub width: f64,

    /// Value of the porous media model depth. (m)
    ///
    #[builder(setter(into))]
    pub depth: f64,

    /// Value of the porous media model porosity. ( - )
    ///
    #[builder(setter(into))]
    pub porosity: f64,

    /// Value of the porous media model permeability. (m^2)
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub permeability: Option<f64>,

    /// Value of the porous media model periodicity in x-direction. (m)
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub periodicity_x: Option<f64>,

    /// Value of the porous media model periodicity in y-direction. (m)
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub periodicity_y: Option<f64>,

    /// Value of the porous media model wall thickness. (m)
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub wall_thickness: Option<f64>,
}

/// The Hardware includes descriptions of the camera systems, laser
/// systems, seeding devices and materials, optical devices, and
/// triggering systems utilized during the experiment.
#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema, Builder, Default)]
#[allow(non_snake_case)]
pub struct Hardware {
    /// Description of the used camera system.
    ///
    #[builder(default, setter(into, each(name = "to_camera")))]
    pub camera: Vec<Camera>,

    /// Description of the used laser system.
    ///
    #[builder(default, setter(into, each(name = "to_laser")))]
    pub laser: Vec<Laser>,

    /// Description of the used seeding device and seeding material.
    ///
    #[builder(default, setter(into, each(name = "to_seeding")))]
    pub seeding: Vec<Seeding>,

    /// Description of the used optical devices (e.g. laserarms, lenses,
    /// beamsplitter, sheet optics, ...).
    #[serde(default, skip_serializing_if = "Vec::is_empty")]
    #[builder(default, setter(into, each(name = "to_optics")))]
    pub optics: Vec<Device>,

    /// Description of the used triggering devices.
    #[serde(default, skip_serializing_if = "Vec::is_empty")]
    #[builder(default, setter(into, each(name = "to_triggering")))]
    pub triggering: Vec<Triggering>,
}

/// The Device provides general information about the manufacturer
/// and model of the used devices such as cameras, lasers, optics,
/// triggering and seeding systems.
#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema, Builder, Default)]
#[allow(non_snake_case)]
pub struct Device {
    /// Name of the device's manufacturer.
    ///
    #[builder(setter(into))]
    pub manufacturer: String,

    /// Name of the device's model.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub model: Option<String>,
}

/// It specifies details about the camera lenses and sensors which were
/// used during the experiment.
#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema, Builder, Default)]
#[allow(non_snake_case)]
pub struct Camera {
    /// Name of the device's manufacturer.
    ///
    #[builder(setter(into))]
    pub manufacturer: String,

    /// Name of the device's model.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub model: Option<String>,

    /// Name of the camera lens which were used.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub lens: Option<String>,

    /// Description of the camera sensor which were used.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub sensor: Option<String>,
}

/// The Laser provides information about the laser wavelength, either the
/// laser is pulsed or continuous as well as the laser power.
#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema, Builder, Default)]
#[allow(non_snake_case)]
pub struct Laser {
    /// Name of the device's manufacturer.
    ///
    #[builder(setter(into))]
    pub manufacturer: String,

    /// Name of the device's model.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub model: Option<String>,

    /// Value of the used wavelength of the laser. (nm)
    ///
    #[builder(setter(into))]
    pub wavelength: f64,

    /// Type of the used laser (e.g. pulsed or continuous wave laser, ...)
    #[serde(default, rename = "type", skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub type_: Option<String>,

    /// Value of the laser power. (W)
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub power: Option<f64>,
}

/// The Seeding describes the material of the seeding particles, the type
/// of them as well as their density, particle size, and kinematic
/// viscosity.
#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema, Builder, Default)]
#[allow(non_snake_case)]
pub struct Seeding {
    /// Name of the device's manufacturer.
    ///
    #[builder(setter(into))]
    pub manufacturer: String,

    /// Name of the device's model.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub model: Option<String>,

    /// Seeding parameters of the used seeding material during the experiment.
    ///
    #[builder(setter(into))]
    pub particles: SeedingParameters,
}

/// The Seeding Parameters contains crucial information about the seeding
/// material used in the experiment.It includes details such as the
/// material name, particle type, density, particle size and the
/// kinematic viscosity of the seeding particles.These parameters
/// provide valuable insights integero the characteristics of the
/// seeding material and its influence on the fluid flow behavior
/// within the experimental setup.
#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema, Builder, Default)]
#[allow(non_snake_case)]
pub struct SeedingParameters {
    /// Name of the seeding material.
    ///
    #[builder(setter(into))]
    pub material: String,

    /// Phase of the seeding material which was used (e.g. solid,
    /// liquid, ...).
    ///
    #[builder(setter(into))]
    pub phase: String,

    /// Value of the seeding particle density. (kg/m^3)
    ///
    #[builder(setter(into))]
    pub density: f64,

    /// Value or span of the seeding particle diameter. (m)
    ///
    #[builder(setter(into))]
    pub particle_size: f64,

    /// Value of the seeding particle kinematic viscosity (m^2/s)
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub kinematic_viscosity: Option<f64>,
}

/// The Triggering explains the recording mode employed during the
/// experiment.
#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema, Builder, Default)]
#[allow(non_snake_case)]
pub struct Triggering {
    /// Name of the device's manufacturer.
    ///
    #[builder(setter(into))]
    pub manufacturer: String,

    /// Name of the device's model.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub model: Option<String>,

    /// Type of recording mode during the experiment (e.g. time-based, cyclic
    /// time-based, ...).
    ///
    #[builder(setter(into))]
    pub recording_mode: String,
}

/// The Measurement encompasses key details about the conducted experiment
/// and its calibration.
#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema, Builder, Default)]
#[allow(non_snake_case)]
pub struct Measurement {
    /// Name of the experiment.It should contain all relevant information
    /// about the experiment.
    ///
    #[builder(setter(into))]
    pub name: String,

    /// Calibration that has been done before the actual experiment.
    #[serde(default, skip_serializing_if = "Vec::is_empty")]
    #[builder(default, setter(into, each(name = "to_calibration")))]
    pub calibration: Vec<Calibration>,

    /// Recordings that have been done in the course of the experiment.
    #[serde(default, skip_serializing_if = "Vec::is_empty")]
    #[builder(default, setter(into, each(name = "to_recordings")))]
    pub recordings: Vec<Recording>,

    /// Processing steps and processed video data of the experiment
    #[serde(default, skip_serializing_if = "Vec::is_empty")]
    #[builder(default, setter(into, each(name = "to_processing_steps")))]
    pub processing_steps: Vec<ProcessStep>,
}

/// The Calibration contains information about the parameters used during
/// the recording process.The parameters are providing insights
/// integero the camera position relative to the experiment for
/// correcting possible misalignments.
#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema, Builder, Default)]
#[allow(non_snake_case)]
pub struct Calibration {
    /// Specify the calibration plate and/or the calibration facility which
    /// was used for calibration.
    ///
    #[builder(setter(into))]
    pub calibration_type: String,

    /// Value of the translation of the camera position relative to the
    /// calibration plate. (m)
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub camera_position_translation: Option<f64>,

    /// Value of the rotation of the camera position relative to the
    /// calibration plate. (°)
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub camera_position_rotation: Option<f64>,

    /// Value of the scale factor of the recordings.The amount of pixels
    /// corresponding to the length of 1 mm. (px/mm)
    ///
    #[builder(setter(into))]
    pub scale_factor: f64,

    /// The actual calibration image which was used.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub calibration_image: Option<Vec<u8>>,
}

/// The Process Step outlines the specific processing steps applied to
/// the flow measurement video data.It includes the name of each
/// processing step, the resulting video from the processing, and the
/// software used to post-process the data.Additionally, files with
/// the extension ".lvs" from the Davis 10 software can be embedded
/// within this section, providing a comprehensive record of the
/// processing workflow and ensuring the availability of relevant
/// files for reference and replication.
#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema, Builder, Default)]
#[allow(non_snake_case)]
pub struct ProcessStep {
    /// Full name of the processing step.
    ///
    #[builder(setter(into))]
    pub name: String,

    /// List of processing steps carried out with the processing software.
    #[serde(default, skip_serializing_if = "Vec::is_empty")]
    #[builder(default, setter(into, each(name = "to_operation_list")))]
    pub operation_list: Vec<String>,

    /// Resulting video after applying the process steps and the raw video.
    #[serde(default, skip_serializing_if = "Vec::is_empty")]
    #[builder(default, setter(into, each(name = "to_processed_recording")))]
    pub processed_recording: Vec<Recording>,

    /// Software that has been used to perform the processing steps.
    ///
    #[builder(default, setter(into, each(name = "to_software")))]
    pub software: Vec<Software>,
}

/// The Software section serves as a container for general information
/// about the software utilized in the experiment.It includes details
/// such as the name of the manufacturer, the specific software name,
/// and the version used to generate the dataset.These details provide
/// important context for the experiment, allowing for reproducibility
/// and facilitating a clear understanding of the software environment
/// in which the data analysis and processing were performed.
#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema, Builder, Default)]
#[allow(non_snake_case)]
pub struct Software {
    /// Name of the used recording or processing software manufacturer.
    ///
    #[builder(setter(into))]
    pub manufacturer: String,

    /// Name of the used recording or processing software.
    ///
    #[builder(setter(into))]
    pub name: String,

    /// Version of the used recording or processing software.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub version: Option<String>,
}

/// The Recording contains crucial information about the parameters used
/// during the recording process.These parameters offer valuable
/// insights integero the experimental setup, facilitating accurate
/// analysis and integererpretation of the recorded data. The
/// inclusion of the video frames allows for a visual reference and
/// further examination of the recorded footage.
#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema, Builder, Default)]
#[allow(non_snake_case)]
pub struct Recording {
    /// Value of the investigated time period. (s)
    ///
    #[builder(setter(into))]
    pub time: f64,

    /// Value of the recording repetition rate. (Hz)
    ///
    #[builder(setter(into))]
    pub repetition_rate: f64,

    /// Value of the field of view. (m x m)
    ///
    #[builder(setter(into))]
    pub field_of_view: String,

    /// Number of frames found in this video.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub n_frames: Option<i64>,

    /// The actual Videoframes of the raw video
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub frames: Option<Vec<u8>>,

    /// Specify the local filepath to the location of the recordings.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    #[builder(default, setter(into))]
    pub location: Option<String>,
}

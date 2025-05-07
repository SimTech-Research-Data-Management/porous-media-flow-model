/**
 * This file contains Zod schema definitions for data validation.
 *
 * Zod is a TypeScript-first schema declaration and validation library.
 * It allows you to create schemas that validate data at runtime while
 * providing static type inference.
 *
 * Usage example:
 * ```typescript
 * import { TestSchema } from './schemas';
 *
 * // Validates data at runtime
 * const result = TestSchema.parse(data);
 *
 * // Type-safe - result has correct TypeScript types
 * console.log(result.name);
 *
 * // Will throw error if validation fails
 * try {
 *   TestSchema.parse(invalidData);
 * } catch (err) {
 *   console.error(err);
 * }
 * ```
 *
 * @see https://github.com/colinhacks/zod
 *
 * WARNING: This is an auto-generated file.
 * Do not edit directly - any changes will be overwritten.
 */


import { z } from 'zod';

// JSON-LD Types
export const JsonLdContextSchema = z.record(z.any());

export const JsonLdSchema = z.object({
  '@context': JsonLdContextSchema.optional(),
  '@id': z.string().optional(),
  '@type': z.string().optional(),
});

// PorousMedia Type definitions
// The Metadata summarizes key information about the following
// dataset. It includes a description of the dataset's content, a
// descriptive name or ID of the dataset, and the date of creation.
// It also lists the contributors, highlights the research areas
// which are covered and specifies the specific porous media model
// investigated. Descriptive keywords help categorize the dataset and
// the the hardware used in the experiment is also stored. Free flow
// conditions of the turbulent air flow are also stored. The Metadata
// provides detailed information about the measurements conducted in
// the experiment.
export const MetadataSchema = z.lazy(() => JsonLdSchema.extend({
  description: z.string().describe(`
    Summary of the content and background of the dataset described in 3-
    5 sentences.
  `),
  dataset_id: z.string().describe(`
    Descriptive name of the dataset or ID of the dataset.
  `),
  date: z.string().describe(`
    Date & time when the dataset was created.
  `),
  authors: z.array(AuthorSchema).describe(`
    Persons who worked on the dataset.
  `),
  subjects: z.array(z.string()).describe(`
    Research subjects covered by the dataset.
  `),
  model: ModelSchema.nullable().describe(`
    Define the actual model which was investigated with the dataset.
  `),
  keywords: z.array(z.string()).describe(`
    Descriptive keywords to describe the dataset.
  `),
  devices: z.array(HardwareSchema).describe(`
    Experimental devices used in the dataset.
  `),
  free_flow: FreeFlowSchema.nullable().describe(`
    Free flow conditions during the experiment
  `),
  measurements: z.array(MeasurementSchema).describe(`
    Contains all measurements & recordings which were conducted during
    the experiment
  `),
}));

export type Metadata = z.infer<typeof MetadataSchema>;

// The Author section provides information about the persons involved
// in working on or creating the dataset.These information helps
// providing the identity and contact details of the authors
// associated with the dataset.
export const AuthorSchema = z.lazy(() => JsonLdSchema.extend({
  name: z.string().describe(`
    Full name of the author or the experimenter.
  `),
  affiliation: z.string().describe(`
    Organisation to which the author belongs.
  `),
  email: z.string().describe(`
    E-Mail adress of the author.
  `),
  phone: z.number().nullable().describe(`
    Phone number of the author.
  `),
}));

export type Author = z.infer<typeof AuthorSchema>;

// The Free Flow section contains information about the shape,
// dimensions, and working fluid of the free flow channel.It provides
// details such as the shape of the flow channel's cross-section, the
// hydraulic diameter, height, width and depth of the channel and a
// description of the flow parameters of the working fluid.
export const FreeFlowSchema = z.lazy(() => JsonLdSchema.extend({
  shape: z.string().describe(`
    Shape of the flow channel's cross section (e.g. rectangular,
    round, ...)
  `),
  hydraulic_diameter: z.number().describe(`
    Value of the channel's hydraulic diameter (m)
  `),
  fluid: FlowParametersSchema.describe(`
    Description of the free flow parameters during the dataset.
  `),
  height: z.number().nullable().describe(`
    Value of the channel height, assuming a rectangular channel. (m)
  `),
  width: z.number().nullable().describe(`
    Value of the flow channel width, assuming a rectangular channel. (m)
  `),
  depth: z.number().nullable().describe(`
    Value of the flow channel depth, assuming a rectangular channel. (m)
  `),
  diameter: z.number().nullable().describe(`
    Value of the flow channel diameter, assuming a round channel. (m)
  `),
}));

export type FreeFlow = z.infer<typeof FreeFlowSchema>;

// The Flow Parameters encompasses crucial details about the flow
// parameters of the working fluid used in the present dataset. These
// parameters provide a comprehensive understanding of the fluid's
// properties and flow conditions within the experiment.
export const FlowParametersSchema = z.lazy(() => JsonLdSchema.extend({
  fluid: z.string().describe(`
    Name of the free flow fluid (e.g. dry air, water, ...)
  `),
  temperature: z.number().describe(`
    Value of the fluid temperature at the inlet. (K)
  `),
  pressure: z.number().describe(`
    Value of the fluid pressure at the outlet. (Pa)
  `),
  density: z.number().describe(`
    Value of the fluid density (kg/m^3)
  `),
  kinematic_viscosity: z.number().describe(`
    Value of the fluid kinematic viscosity (m^2/s)
  `),
  dynamic_viscosity: z.number().describe(`
    Value of the dynamic fluid viscosity (mPas)
  `),
  mass_flux: z.array(z.number()).describe(`
    Value of the fluid mass flux (kg/s)
  `),
  reynolds_number: z.array(z.number()).describe(`
    Value(s) of investigated channel Reynolds number(s). ( - )
  `),
}));

export type FlowParameters = z.infer<typeof FlowParametersSchema>;

// The Model section contains information about the location of the
// object in the flow channel.It provides details regarding the type
// of the present porous media model, its location relative to the
// free flow and if applicable, detailed parameters related to the
// model which was used.
export const ModelSchema = z.lazy(() => JsonLdSchema.extend({
  type: z.string().describe(`
    What kind of object is located inside the flow channel? (porous media
    model, cylinder, ...)
  `),
  location: z.string().describe(`
    Where is the object located inside the flow channel? (in, adjascent
    to, ... the free flow)
  `),
  porous_media: PorousMediaSchema.nullable().describe(`
    Description of porous media parameters
  `),
  cad_model: z.bytes().nullable().describe(`
    CAD drawing of the used model (e.g. stored as a '.stl'-File)
  `),
}));

export type Model = z.infer<typeof ModelSchema>;

// The Porous Media contains information regarding the parameters
// associated with the utilized porous media model.They include
// the topology of the porous media model, the dimensions and other
// relevant material properties.
export const PorousMediaSchema = z.lazy(() => JsonLdSchema.extend({
  topology: z.string().describe(`
    Definition of the porous media model topology.
  `),
  height: z.number().describe(`
    Value of the porous media model height. (m)
  `),
  width: z.number().describe(`
    Value of the porous media model width. (m)
  `),
  depth: z.number().describe(`
    Value of the porous media model depth. (m)
  `),
  porosity: z.number().describe(`
    Value of the porous media model porosity. ( - )
  `),
  permeability: z.number().nullable().describe(`
    Value of the porous media model permeability. (m^2)
  `),
  periodicity_x: z.number().nullable().describe(`
    Value of the porous media model periodicity in x-direction. (m)
  `),
  periodicity_y: z.number().nullable().describe(`
    Value of the porous media model periodicity in y-direction. (m)
  `),
  wall_thickness: z.number().nullable().describe(`
    Value of the porous media model wall thickness. (m)
  `),
}));

export type PorousMedia = z.infer<typeof PorousMediaSchema>;

// The Hardware includes descriptions of the camera systems, laser
// systems, seeding devices and materials, optical devices, and
// triggering systems utilized during the experiment.
export const HardwareSchema = z.lazy(() => JsonLdSchema.extend({
  camera: z.array(CameraSchema).describe(`
    Description of the used camera system.
  `),
  laser: z.array(LaserSchema).describe(`
    Description of the used laser system.
  `),
  seeding: z.array(SeedingSchema).describe(`
    Description of the used seeding device and seeding material.
  `),
  optics: z.array(DeviceSchema).describe(`
    Description of the used optical devices (e.g. laserarms, lenses,
    beamsplitter, sheet optics, ...).
  `),
  triggering: z.array(TriggeringSchema).describe(`
    Description of the used triggering devices.
  `),
}));

export type Hardware = z.infer<typeof HardwareSchema>;

// The Device provides general information about the manufacturer
// and model of the used devices such as cameras, lasers, optics,
// triggering and seeding systems.
export const DeviceSchema = z.lazy(() => JsonLdSchema.extend({
  manufacturer: z.string().describe(`
    Name of the device's manufacturer.
  `),
  model: z.string().nullable().describe(`
    Name of the device's model.
  `),
}));

export type Device = z.infer<typeof DeviceSchema>;

// It specifies details about the camera lenses and sensors which were
// used during the experiment.
export const CameraSchema = z.lazy(() => JsonLdSchema.extend({
  manufacturer: z.string().describe(`
    Name of the device's manufacturer.
  `),
  model: z.string().nullable().describe(`
    Name of the device's model.
  `),
  lens: z.string().nullable().describe(`
    Name of the camera lens which were used.
  `),
  sensor: z.string().nullable().describe(`
    Description of the camera sensor which were used.
  `),
}));

export type Camera = z.infer<typeof CameraSchema>;

// The Laser provides information about the laser wavelength, either the
// laser is pulsed or continuous as well as the laser power.
export const LaserSchema = z.lazy(() => JsonLdSchema.extend({
  manufacturer: z.string().describe(`
    Name of the device's manufacturer.
  `),
  wavelength: z.number().describe(`
    Value of the used wavelength of the laser. (nm)
  `),
  model: z.string().nullable().describe(`
    Name of the device's model.
  `),
  type: z.string().nullable().describe(`
    Type of the used laser (e.g. pulsed or continuous wave laser, ...)
  `),
  power: z.number().nullable().describe(`
    Value of the laser power. (W)
  `),
}));

export type Laser = z.infer<typeof LaserSchema>;

// The Seeding describes the material of the seeding particles, the type
// of them as well as their density, particle size, and kinematic
// viscosity.
export const SeedingSchema = z.lazy(() => JsonLdSchema.extend({
  manufacturer: z.string().describe(`
    Name of the device's manufacturer.
  `),
  particles: SeedingParametersSchema.describe(`
    Seeding parameters of the used seeding material during the experiment.
  `),
  model: z.string().nullable().describe(`
    Name of the device's model.
  `),
}));

export type Seeding = z.infer<typeof SeedingSchema>;

// The Seeding Parameters contains crucial information about the seeding
// material used in the experiment.It includes details such as the
// material name, particle type, density, particle size and the
// kinematic viscosity of the seeding particles.These parameters
// provide valuable insights integero the characteristics of the
// seeding material and its influence on the fluid flow behavior
// within the experimental setup.
export const SeedingParametersSchema = z.lazy(() => JsonLdSchema.extend({
  material: z.string().describe(`
    Name of the seeding material.
  `),
  phase: z.string().describe(`
    Phase of the seeding material which was used (e.g. solid,
    liquid, ...).
  `),
  density: z.number().describe(`
    Value of the seeding particle density. (kg/m^3)
  `),
  particle_size: z.number().describe(`
    Value or span of the seeding particle diameter. (m)
  `),
  kinematic_viscosity: z.number().nullable().describe(`
    Value of the seeding particle kinematic viscosity (m^2/s)
  `),
}));

export type SeedingParameters = z.infer<typeof SeedingParametersSchema>;

// The Triggering explains the recording mode employed during the
// experiment.
export const TriggeringSchema = z.lazy(() => JsonLdSchema.extend({
  manufacturer: z.string().describe(`
    Name of the device's manufacturer.
  `),
  recording_mode: z.string().describe(`
    Type of recording mode during the experiment (e.g. time-based, cyclic
    time-based, ...).
  `),
  model: z.string().nullable().describe(`
    Name of the device's model.
  `),
}));

export type Triggering = z.infer<typeof TriggeringSchema>;

// The Measurement encompasses key details about the conducted experiment
// and its calibration.
export const MeasurementSchema = z.lazy(() => JsonLdSchema.extend({
  name: z.string().describe(`
    Name of the experiment.It should contain all relevant information
    about the experiment.
  `),
  calibration: z.array(CalibrationSchema).describe(`
    Calibration that has been done before the actual experiment.
  `),
  recordings: z.array(RecordingSchema).describe(`
    Recordings that have been done in the course of the experiment.
  `),
  processing_steps: z.array(ProcessStepSchema).describe(`
    Processing steps and processed video data of the experiment
  `),
}));

export type Measurement = z.infer<typeof MeasurementSchema>;

// The Calibration contains information about the parameters used
// during the recording process.The parameters are providing insights
// integero the camera position relative to the experiment for
// correcting possible misalignments.
export const CalibrationSchema = z.lazy(() => JsonLdSchema.extend({
  calibration_type: z.string().describe(`
    Specify the calibration plate and/or the calibration facility which
    was used for calibration.
  `),
  scale_factor: z.number().describe(`
    Value of the scale factor of the recordings.The amount of pixels
    corresponding to the length of 1 mm. (px/mm)
  `),
  camera_position_translation: z.number().nullable().describe(`
    Value of the translation of the camera position relative to the
    calibration plate. (m)
  `),
  camera_position_rotation: z.number().nullable().describe(`
    Value of the rotation of the camera position relative to the
    calibration plate. (°)
  `),
  calibration_image: z.bytes().nullable().describe(`
    The actual calibration image which was used.
  `),
}));

export type Calibration = z.infer<typeof CalibrationSchema>;

// The Process Step outlines the specific processing steps applied
// to the flow measurement video data.It includes the name of each
// processing step, the resulting video from the processing, and the
// software used to post-process the data.Additionally, files with the
// extension ".lvs" from the Davis 10 software can be embedded within
// this section, providing a comprehensive record of the processing
// workflow and ensuring the availability of relevant files for
// reference and replication.
export const ProcessStepSchema = z.lazy(() => JsonLdSchema.extend({
  name: z.string().describe(`
    Full name of the processing step.
  `),
  operation_list: z.array(OperationSchema).describe(`
    List of processing steps carried out with the processing software.
  `),
  processed_recording: z.array(RecordingSchema).describe(`
    Resulting video after applying the process steps and the raw video.
  `),
  software: z.array(SoftwareSchema).describe(`
    Software that has been used to perform the processing steps.
  `),
}));

export type ProcessStep = z.infer<typeof ProcessStepSchema>;

// The Operation section defines the specific operations performed during
// the data processing.It includes the name of the operation, its
// description, and the parameters used in the operation.
export const OperationSchema = z.lazy(() => JsonLdSchema.extend({
  name: z.string().describe(`
    Name of the operation.
  `),
  description: z.string().nullable().describe(`
    Description of the operation.
  `),
  parameters: z.array(ParameterSchema).describe(`
    Parameters of the operation.
  `),
}));

export type Operation = z.infer<typeof OperationSchema>;

// The Parameter section defines the specific parameters used in various
// operations during the data processing. It includes the name of
// the parameter and its corresponding value, which can be a float,
// string, or boolean. This information is crucial for understanding
// the exact configuration of each operation and ensuring
// reproducibility of the processing steps.
export const ParameterSchema = z.lazy(() => JsonLdSchema.extend({
  name: z.string().describe(`
    Name of the parameter.
  `),
  value: z.union([z.number(), z.string(), z.boolean()]).nullable().describe(`
    Value of the parameter.
  `),
}));

export type Parameter = z.infer<typeof ParameterSchema>;

// The Software section serves as a container for general information
// about the software utilized in the experiment.It includes details
// such as the name of the manufacturer, the specific software name,
// and the version used to generate the dataset.These details provide
// important context for the experiment, allowing for reproducibility
// and facilitating a clear understanding of the software environment
// in which the data analysis and processing were performed.
export const SoftwareSchema = z.lazy(() => JsonLdSchema.extend({
  manufacturer: z.string().describe(`
    Name of the used recording or processing software manufacturer.
  `),
  name: z.string().describe(`
    Name of the used recording or processing software.
  `),
  version: z.string().nullable().describe(`
    Version of the used recording or processing software.
  `),
}));

export type Software = z.infer<typeof SoftwareSchema>;

// The Recording contains crucial information about the parameters
// used during the recording process.These parameters offer valuable
// insights integero the experimental setup, facilitating accurate
// analysis and integererpretation of the recorded data. The inclusion
// of the video frames allows for a visual reference and further
// examination of the recorded footage.
export const RecordingSchema = z.lazy(() => JsonLdSchema.extend({
  time: z.number().describe(`
    Value of the investigated time period. (s)
  `),
  repetition_rate: z.number().describe(`
    Value of the recording repetition rate. (Hz)
  `),
  field_of_view: z.string().describe(`
    Value of the field of view. (m x m)
  `),
  n_frames: z.number().nullable().describe(`
    Number of frames found in this video.
  `),
  frames: z.bytes().nullable().describe(`
    The actual Videoframes of the raw video
  `),
  location: z.string().nullable().describe(`
    Specify the local filepath to the location of the recordings.
  `),
}));

export type Recording = z.infer<typeof RecordingSchema>;
# KiCad 3D Models
This repository contains 3D models for rendering and MCAD integration, for use with [KiCAD EDA](http://kicad-pcb.org/) software.
The model needs a source file (a manually-modelled or script-generated); its WRL counterpart file must be obtained as a conversion from the MCAD model.

## Supported File Formats
The 3D model library supports two file formats:

### STEP
STEP files are used for integration with MCAD software packages.

STEP models must be a solid single object (a union of parts) for size and loading optimization. KiCad supports STEP file integration and can export board and component models into an integrated STEP file. This file can then be imported by a MCAD package.

### WRL
WRL files must be exported from its mechanical model counterpart. WRL files are used for photo-realistic rendering using KiCad's raytracing rendering engine. This format supports more complex material properties, allowing various common component materials to be accurately rendered. 

## Source Files
Source files for generated models should be submitted to (https://github.com/kicad/packages3d-source). This includes generator scripts, or native model files from source software (e.g. [FreeCAD](https://www.freecadweb.org/)).

## Preferred method to create 3D models
The model has to be created in a mechanical program able to generate STEP export. The model can be created by automatic scripts or manually.

[FreeCAD](https://www.freecadweb.org/) is the preferred software because it is open source and anyone can rework the model for future improvements, but other proprietary MCAD software is allowed.

In case the model is generated by scripts, the scripts should be linked to the PR stating software and version used to run the scripts;
when the model is manually created, the MCAD source file should be added to the PR as well as STEP file.

Nominal component dimensions must be used when creating models, not minimum or maximum dimensions.

Text is not suggested on models to maintain a small file size, but if text is used the fonts must be licensed free as the word.

WRL models should be exported from its mechanical counterpart and, when possible, have the suggested material properties as in this document [WRL Material Properties](https://cld.pt/dl/download/64e39e99-c5b6-451b-accd-9e25331ceafe/KiCad_3D-Viewer_component-materials-reference-list_MarioLuzeiro.pdf?download=true).  

A simple method to export a fully compliant WRL model from a mechanical STEP model is through [KiCad StepUp](https://sourceforge.net/projects/kicadstepup/).

A tutorial video can be found [here](https://youtu.be/O6vr8QFnYGw) and a good starting point to learn how to create models by script is this github repo [kicad-3d-models-in-freecad](https://github.com/easyw/kicad-3d-models-in-freecad).

The scripts are made in Python and run in FreeCAD with the [CadQuery module](https://github.com/jmwright/cadquery-freecad-module) add-on.  

### Model Alignment
The 3D models in this library are aligned (placed at the same origin and with the same rotation) with the footprints in the KiCad footprint libraries.

### Model Scaling
The STEP file format includes model scaling information, and so the 3D model must always be scaled 1:1 in mm units.

The WRL file format does not specify absolute dimensions. KiCad normalizes WRL model dimension to units of *0.1 inches*, and the internal units of the WRL files should be scaled accordingly.

## Contributing
Refer to the Wiki page on [Contributing](https://github.com/KiCad/packages3D/wiki/Contributing).

## Model Licencing
See the KiCad [Libraries License](http://kicad-pcb.org/libraries/license/) for details.

## External Model Libraries
In addition to the 3D model data provided in this library, there are other sources that designers may use to source 3D models.

Many manufacturers provide accurate 3D models for specific components.

Online repositories:
    * [FreeCAD Electric Library](https://github.com/FreeCAD/FreeCAD-library/tree/master/Electrical%20Parts)
    * [FreeCAD Electronic Library](https://github.com/FreeCAD/FreeCAD-library/tree/master/Electrical%20Parts/electronic-components)
    * [GrabCAD](https://grabcad.com/)
    * [3D ContentCentral](http://www.3dcontentcentral.com/)
    * [traceparts](http://www.traceparts.com/)

Ensure that the license of any 3D data used is compatible with the KiCad project.

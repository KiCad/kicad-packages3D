# KiCad 3D Models
This repository contains 3D models for rendering and MCAD integration, for use with [KiCAD EDA](http://kicad-pcb.org/) software.

## License
These models are script generated and are free to use and distribute (refer to LICENSE file).

## Supported File Formats
The 3D model library supports two file formats:

### STEP 
STEP files are used for integration with MCAD software packages. KiCad supports STEP file integration and can export board and component models into an integrated STEP file. This file can then be imported by an MCAD package.

### WRL
WRL files are used for photo-realistic rendering using KiCad's raytracing rendering engine. WRL supports more complex material properties, allowing various common component materials to be accurately rendered.

## Model Alignment
The 3D models in this library are aligned with the footprints available in the KiCad footprint libraries.

## Model Scaling
* The STEP file format includes model scaling information, and so the 3D model scaling parameter must always be set to 1:1
* The WRL file format does not specify absolute dimensions. KiCad normalizes model parameters to units of *Inches*, and some WRL files may be scaled accordingly.

## Contributing
TODO

## External Model Libraries
In addition to the 3D model data provided in this library, there are other sources that designers may use to source 3D models.

* Many manufacturers provide accurate 3D models for specific components.
* Online repositories, e.g.
    * [smisioto](http://smisioto.no-ip.org/elettronica/kicad/kicad-en.htm)
    * [GrabCAD](https://grabcad.com/)
    * [3D ContentCentral](http://www.3dcontentcentral.com/)
    * [traceparts](http://www.traceparts.com/)
    
Ensure that the LICENSE of any 3D data used is compatible with the intended use-case of the project.
    

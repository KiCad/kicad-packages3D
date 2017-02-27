# KiCad 3D Models
This repository contains 3D models for rendering and MCAD integration, for use with [KiCAD EDA](http://kicad-pcb.org/) software.

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
* The WRL file format does not specify absolute dimensions. KiCad normalizes model parameters to units of *Inches*, and the internal units of the WRL files should be scaled accordingly

## Contributing
TODO

## A word about Licensing on 3d model files.
All software components of KiCAD are released under the GNU General
Public License (GPL) version 2 or later. However, some confusion exists
about the 3d models distributed in this library. What license do they use? Will GPL 3d models
“infect” your design, thereby requiring you to release your design to
the public? If you modify the 3d models, must you release the modified
versions under the GPL?

The goal of the KiCAD Project is to provide an open-source EDA Suite
which may be used for non-commercial as well as commercial projects. Our
tools are aimed for use by students, hobbyists, educators, consultants,
and - yes - corporate engineers. We are not interested in exerting any
control over your designs, or forcing you to reveal proprietary
information contained in your designs.

3d models are similar to the font files used in document processing
software – they are graphical objects used to express your ideas. We
want you to retain control of your own ideas (your design), while the
KiCAD Project retains a say in how you redistribute the 3d models themselves.

There are three ways a 3d models might be distributed:

  1. As part of a 3d model library, or individually as a .step or .wrl files
     (i.e. as a 3d model itself).
  2. Embedded in a 3d file exported generated from your project. (i.e. part of the soft, or editable copy of a design).
  3. The resulting rendering created from your printed circuit board using these 3d models (i.e. as
     part of the hard, or non-editable copy of a design).

There is a distinction between cases 1 and (2, 3). In case 1, the object
of interest is the 3d model library (or individual 3d models) itself. In case
(2, 3), the object of interest is the design. Some label case 1
“distribution”, and case (2, 3) “use” of the 3d model.

Our goals for the 3d models are:

  * We wish to distribute the 3d models under a licencing scheme which
    encourages that you give back to the community if you redistribute
    the the 3d models themselves - whether modified or unmodified. This is
    case 1 distribution. The GPL ensures this.

  * We wish to specifically prohibit anybody from building KiCAD's
    3d models into their *software* products, and then place restrictions
    on how the resulting product may be used. If you bundle KiCAD 3d models
    - whether modified or unmodified - into your software and then
    distribute it, then you must allow for the software's (and 3d models')
    continued redistribution under the GPL. Again, this is case 1
    distribution; the GPL ensures this.

  * However, we do not wish to “infect” your *electronic* design, or
    force you to release your proprietary design information if you use
    or embed KiCAD 3d models in your design. This is case (2, 3) use.

The Free Software Foundation has recognized a possible conflict of the
base GPL with the use of fonts - and, by analogy, 3d models used in the cases
(2, 3). Their solution is to use an exemption clause in the GPL which
you explicitly insert for fonts. Read about it here:

http://www.fsf.org/licensing/licenses/gpl-faq.html#FontException

Therefore, using this as a template, all 3d models released with KiCAD
are covered under the GPL with the following exception clause:

"As a special exception, if you create a design which uses this 3d model,
and embed this 3d model or unaltered portions of this 3d model into the
design, this 3d model does not by itself cause the resulting design to
be covered by the GNU General Public License. This exception does not
however invalidate any other reasons why the design itself might be
covered by the GNU General Public License. If you modify this
3d model, you may extend this exception to your version of the
3d model, but you are not obligated to do so. If you do not
wish to do so, delete this exception statement from your version."

The idea is that case 1 redistribution is covered under the GPL, but
distribution of your design (case (2, 3) is exempt from the GPL. This is
the scheme which the KiCAD Project wishes to use for 3d model distribution
and use.

## External Model Libraries
In addition to the 3D model data provided in this library, there are other sources that designers may use to source 3D models.

* Many manufacturers provide accurate 3D models for specific components.
* Online repositories, e.g.
    * [smisioto](http://smisioto.no-ip.org/elettronica/kicad/kicad-en.htm)
    * [GrabCAD](https://grabcad.com/)
    * [3D ContentCentral](http://www.3dcontentcentral.com/)
    * [traceparts](http://www.traceparts.com/)

Ensure that the LICENSE of any 3D data used is compatible with the intended use-case of the project.

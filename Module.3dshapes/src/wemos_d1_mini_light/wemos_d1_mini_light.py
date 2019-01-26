# This is a CadQuery script template
# Add your script code below
import cadquery as cq

in2mm = 25.4

pcb_x = 26
pcb_y = 34.5
pcb_z = 1.6
pcb_r = 3

pins = 16
pin_pitch = 0.1 * in2mm
pin_diameter = 1.0
#
pin_1_x = (pcb_x - (0.9 * in2mm)) / 2
pin_1_y = 9 + (pins/2 - 1) * pin_pitch
#
pin_points = []
for i in range(pins):
    if i < pins/2:
        pin_points.append((pin_1_x, pin_1_y - i * pin_pitch))
    else:
        pin_points.append((pin_1_x + 0.9 * in2mm, pin_1_y - (i-8) * pin_pitch))

pcb_rst_notch_x = 2.2
pcb_rst_notch_y = 7.6
pcb_rst_notch_r = 1.5
#
pcb_usb_notch_x = 9
pcb_usb_notch_y = 1.4
pcb_usb_notch_offset_x = 5.6 + 2.2

usb_x = 7.85
usb_y = 5.6
usb_z = 2.85
#
usb_offset_x = 9.7
usb_offset_y = 0.9

esp_pcb_x = 16
esp_pcb_y = 24
esp_pcb_z = 1.2

esp_can_x = 12
esp_can_y = 15
esp_can_z = 2.3
esp_can_offset_x = 2
esp_can_offset_y = 1.2

pcb = cq.Workplane("XY")\
    .box(pcb_x, pcb_y, pcb_z)\
    .faces(">Y").edges("|Z").fillet(pcb_r)


pcb_pin_holes = pcb.faces(">Z").vertices("<XY").workplane()\
    .moveTo(pin_1_x, pin_1_y)\
    .pushPoints(pin_points)\
    .circle(pin_diameter/2).extrude(-pcb_z, combine=False)

rst_notch = pcb.faces(">Z").vertices("<XY").workplane()\
    .rect(pcb_rst_notch_x, pcb_rst_notch_y, centered=False)\
    .extrude(-pcb_z, combine=False)\
    .faces(">Y").edges("|Z").edges(">X").fillet(pcb_rst_notch_r)

usb_notch = pcb.faces(">Z").vertices("<XY").workplane()\
    .moveTo(pcb_usb_notch_offset_x)\
    .rect(pcb_usb_notch_x, pcb_usb_notch_y, centered=False)\
    .extrude(-pcb_z, combine=False)\
    .faces(">Y").edges("|Z").fillet(pcb_usb_notch_y/1.1)

usb_plug = pcb.faces("<Z").vertices(">X").vertices("<Y").workplane()\
    .moveTo(-usb_offset_x , usb_offset_y)\
    .rect(-usb_x, usb_y, centered=False)\
    .extrude(-usb_z, combine=False)\

esp = pcb.faces(">Z").vertices("<XY").workplane()\
    .moveTo(pcb_x/2 - esp_pcb_x/2, pcb_y-esp_pcb_y)\
    .rect(esp_pcb_x, esp_pcb_y, centered=False)\
    .extrude(esp_pcb_z, combine=False)

esp_can = esp.faces(">Z").vertices("<XY").workplane()\
    .moveTo(esp_can_offset_x, esp_can_offset_y)\
    .rect(esp_can_x, esp_can_y, centered=False)\
    .extrude(esp_can_z)

pcb = pcb.cut(rst_notch)
pcb = pcb.cut(usb_notch)
pcb = pcb.cut(pcb_pin_holes)

show_object(pcb, options={"rgba":(4,93,142, 0)})
show_object(esp, options={"rgba":(100, 100, 100, 0.0)})
show_object(usb_plug, options={"rgba":(200, 200, 200, 0)})
#show_object(rst_notch, options={"rgba":(255, 50, 50, 0.9)})
#show_object(usb_notch, options={"rgba":(50, 127, 127, 0.9)})
#show_object(pcb_pin_holes, options={"rgba":(255, 255, 100, 0.5)})

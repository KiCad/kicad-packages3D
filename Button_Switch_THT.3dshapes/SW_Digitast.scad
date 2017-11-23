// All dimensions in mm
// Author: Robert Loos

module prism4(l1,w1,l2,w2,h) {
    dl=(l1-l2)/2;
    dw=(w1-w2)/2;
    polyhedron(
    points=[[0,0,0],[l1,0,0],[l1,w1,0],[0,w1,0],
    [dl,dw,h],[dl+l2,dw,h],[dl+l2,dw+w2,h],[dl,dw+w2,h]],
    faces=[[0,1,2,3],[4,5,1,0],[5,6,2,1],[6,7,3,2],[7,4,0,3],[7,6,5,4]]);
}

module button_mount() {
    union() {
        cube(size=[1.4,3.8,3.8]);
        translate([0,1.9,0]) rotate (a=[0,90,0]) linear_extrude(1.4) circle(d=3.8,$fn=18);
    };
}

module led_hole(x,y) {
    translate([x,y,-2]) cylinder(d=3.5,h=10,$fn=18);
}

module led(x,y,z) {
    translate([x,y,-2.4+z]) color([1,0,0]) union() {
        cylinder(d=3,h=4,$fn=18);
        translate([0,0,4]) sphere(d=3,$fn=18);
    }
    pin(-1.27+x,y,90);
    pin(1.27+x,y,90);
}

// num_leds bust be 0, 1 or 2
// w is 12.3 for normal width and 17.3 for wide
module button(num_leds,w) {
    color([0.4,0.4,0.4]) translate ([0,0,10.5]) difference() {
        union() {
            cube(size=[w+.01,17.1,3],center=true);
            translate([-w/2,-8.55,1.5]) prism4(w,10,w-1.5,8.5,1.5);
            translate ([-6.15,8.55-3.8,-1.5-3.7]) button_mount();
            translate ([6.15-1.4,8.55-3.8,-1.5-3.7]) button_mount();
        }
        if (num_leds==1) {
            led_hole(0,5.08);
            led(0,5.08);
        }
        else if (num_leds==2)
        {
            led_hole(-2.54,5.08);
            led_hole(2.54,5.08);
        }
    }
    if (num_leds==1) {
        led(0,5.08,10.5);
    }
    if (num_leds==2) {
        led(-2.54,5.08,10.5);
        led(2.54,5.08,10.5);
    }
}

module nose() {
    color([0.8,0.8,0.8]) translate([0,0,-2]) cylinder(h=2,d=1,$fn=18);
}
module switch_base() {
    union() {
        difference() {
            color([.8,.8,.8]) cube(size=[12.3,17.5,8],center=true);
            translate ([4.65,8.55-3.95,1]) scale([1.1,1.1,1.1]) button_mount();
            translate ([-6.16,8.55-3.95,1]) scale([1.1,1.1,1.1]) button_mount();
        translate([10,0,4.01]) rotate([270,180,90]) linear_extrude(height=22) polygon(points=[[0,0],[9,0],[9,-1]]);
        }
        translate([3.81,7.62,-4]) nose();
        translate([-3.81,-7.62,-4]) nose();
    }
}

module pin(x,y,rot) {
    color([0.5,0.5,0.1]) translate([x,y,-.1]) rotate([0,0,rot]) translate([-.1,-.35,-3.6]) cube([0.2,0.7,3.6]);
}


translate([0,0,4]) switch_base();
// Set number of LEDs and Width to generate different types
button(0,17.3); // w=12.3 for normal, 17.3 for wide
pin(-3.81,0,90);
pin(3.81,0,90);
pin(-3.81,-5.08,0);
pin(3.81,-5.08,0);

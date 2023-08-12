"""

Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2012 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""
import math
class Point(object):
    """Represents a point in 2-D space."""


def print_point(p):
    """Print a Point object in human-readable format."""
    print ('(%g, %g)' % (p.x, p.y))


class Rectangle(object):
    """Represents a rectangle. 

    attributes: width, height, corner.
    """


def find_center(rect):
    """Returns a Point at the center of a Rectangle."""
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p


def grow_rectangle(rect, dwidth, dheight):
    """Modify the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight

class Circle():
    """Represents a circle. 

    attributes: center and radius.
    """
def point_in_circle(circle, point):
    """Returns True if point in circle"""
    distance_of_pt_from_center = math.sqrt((point.x - circle.center.x)**2 +(point.y - circle.center.y)**2)
    if distance_of_pt_from_center>circle.radius:
        return False
    return True

def corners_rect(rectangle):
    """Return corners of rectangle , format: clockwise starting from
    left top, given a rectangle object considering
    the column given with rectange as top left corner"""
    corner_lt = rectangle.corner
    width = rectangle.width
    height = rectangle.height
    corner_lb = Point()
    corner_lb.x = corner_lt.x
    corner_lb.y = corner_lt.y - rectangle.height
    corner_rb = Point()
    corner_rb.x = corner_lt.x + rectangle.width
    corner_rb.y = corner_lt.y - rectangle.height
    corner_rt = Point()
    corner_rt.x = corner_lt.x + rectangle.width
    corner_rt.y = corner_lt.y 
    return corner_lt, corner_rt, corner_rb, corner_lb

def rect_in_circle(circle,rectangle):
    """Returns true if Rectange lies entirely in circle"""
    corner_lt, corner_rt, corner_rb, corner_lb = corners_rect(rectangle)
    if not point_in_circle(circle, corner_lt):
        return False
    if not point_in_circle(circle, corner_rt):
        return False
    if not point_in_circle(circle, corner_rb):
        return False
    if not point_in_circle(circle, corner_lb):
        return False
    return True

def rect_circle_overlap(circle,rectangle):
    """Returns true if any corner of lies in circle"""
    corner_lt, corner_rt, corner_rb, corner_lb = corners_rect(rectangle)
    if  point_in_circle(circle, corner_lt):
        return True
    if point_in_circle(circle, corner_rt):
        return True
    if point_in_circle(circle, corner_rb):
        return True
    if point_in_circle(circle, corner_lb):
        return True
    return False

def rect_circle_overlap_complex(circle,rectangle):
    """Returns true if any overlap between rectangle and circle
    idea is to check for left, right, botton and top overlap"""
    corner_lt, corner_rt, corner_rb, corner_lb = corners_rect(rectangle)
    center_c = circle.center
    radius_c = circle.radius
    # checking for inside circle
    if rect_in_circle(circle,rectangle):
        return True
    # top of rectangle overlaps with circle bottom
    if (center_c.y - radius_c)<corner_lt.y and corner_lt.x < center_c.x  and corner_rt.x > center_c.x:
        return True
    # bottom of rectangle overlaps with circle top
    if (center_c.y + radius_c)<corner_lt.y and corner_lb.x < center_c.x and corner_rb.x > center_c.x:
        return True
    # left of rectange overlaps with circle right
    if (center_c.x + radius_c)<corner_lt.x and corner_lb.y < center_c.y and corner_lt.x > center_c.y:
        return True
    if (center_c.x - radius_c)<corner_rt.x and corner_rb.y < center_c.y and corner_rt.x > center_c.y:
        return True
    return False


def main():
    ## for point inside circle
    c1 = Circle()
    print(c1)
    c1.center = Point()
    c1.center.x = 150
    c1.center.y = 100
    c1.radius = 75
    
    # point on circle
    p1 = Point()
    p1.x =225
    p1.y =100
    # point outside circle
    p2 = Point()
    p2.x =225
    p2.y = 172
    print(point_in_circle(c1,p1))
    print(point_in_circle(c1,p2))

    
    print("for rectangle inside circle")
    # definig  a rectangle
    r1 = Rectangle()
    r1.corner = Point()
    r1.corner.x = 150
    r1.corner.y = 100
    r1.width = 100
    r1.height = 10
    print(rect_in_circle(c1,r1))

    print("for rectangle corner inside circle")
    print(rect_circle_overlap(c1,r1))

    print("for rectangle circle overlap")
    print(rect_circle_overlap_complex(c1,r1))
if __name__ == '__main__':
    main()

length=int(input("enter the length of cuboid"))
breadth=int(input("enter the breadth of cuboid"))
height=int(input("enter the height of cuboid"))
def cuboid_TSA(length,breadth,height):
    print("the total surface area of the cuboid is",2*((length*breadth)+(length*height)+(breadth*height)))
def cuboid_perimeter(length,breadth,height):
    print("the perimeter of the cuboid is",4*(length+breadth+height))
def cuboid_volume(length,breadth,height):
    print("the volume of the cuboid is",length*breadth*height)
cuboid_TSA(length,breadth,height)
cuboid_perimeter(length,breadth,height)
cuboid_volume(length,breadth,height)

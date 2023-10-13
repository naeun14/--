def cube(edge_length):
    volume = edge_length ** 3
    return volume

def box(length, width, height):
    volume = length * width * height
    return volume

def cone(radius, height):
    volume = (1/3) * 3.14 * radius ** 2 * height
    return volume

def sphere(radius):
    volume = (4/3) * 3.14 * radius ** 3
    return volume

def cylinder(radius, height):
    volume = 3.14 * radius ** 2 * height
    return volume

cube_volume = cube(12)
print("정육면체 부피:", cube_volume)
box_volume = box(3, 5, 6)
print("직육면체 부피:", box_volume)
cone_volume = cone(20, 10)
print("원뿔 부피:", cone_volume)
sphere_volume = sphere(15)
print("구 부피:", sphere_volume)
cylinder_volume = cylinder(20, 10)
print("원기둥 부피:", cylinder_volume)
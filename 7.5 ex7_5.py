import math as m
for i in range(0,181,10):
    angle = m.radians(i)  # 각도를 라디안으로 변환
    print("sin ({:3d}) = {:.3f}, cos ({:3d}) = {:.3f}, tan({:3d}) = {:.3f}".format(i,m.sin(angle),i,m.cos(angle),i,m.tan(angle)))
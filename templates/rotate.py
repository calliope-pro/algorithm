# ABC197 D
import math
def rotate(x, y, theta, x_center=0, y_center=0):
    # x,yは中心からの相対座標, thetaは回転角
    x_res = x*math.cos(theta) - y*math.sin(theta) + x_center
    y_res = x*math.sin(theta) + y*math.cos(theta) + y_center
    return x_res, y_res
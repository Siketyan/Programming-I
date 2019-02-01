# coding: utf-8
# 円柱の体積を求める


# Constants
PI = 3.141592

# Inputs
radius = float(input("円柱の半径は? "))
height = float(input("円柱の高さは? "))

# Results
surface = radius * radius * PI
volume = surface * height

# Output
print("円柱の体積は %14.5f" %volume)

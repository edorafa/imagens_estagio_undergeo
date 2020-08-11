f = open("pvgrid_original.txt", "r")

for x in f:
  a = x.split(', ')
  
print(a)

g = open("Cesium_Air.txt", "r")

for z in g:
  b = z.split(', ')
  
print(b)
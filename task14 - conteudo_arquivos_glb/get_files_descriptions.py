from pygltflib import GLTF2

glb_filename1 = "pvgrid.glb"
glb2 = GLTF2().load(glb_filename1)
glb2.scene

description1 = str(glb2)

glb_filename2 = "Cesium_Air.glb"
glb = GLTF2().load(glb_filename2)
glb.scene

description2 = str(glb)

split_description1 = description1.split(', ')
split_description2 = description2.split(', ')

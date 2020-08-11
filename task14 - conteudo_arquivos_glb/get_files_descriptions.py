from pygltflib import GLTF2
glb_filename = "Cesium_Air.glb"
glb = GLTF2().load(glb_filename)
glb.scene


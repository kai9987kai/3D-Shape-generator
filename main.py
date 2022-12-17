import bpy
import random

# Set the number of shapes to generate
num_shapes = 10

# Set the dimensions of the shapes
min_size = 0.5
max_size = 2.0

# Set the range of colors for the shapes
min_color = (0.0, 0.0, 0.0)
max_color = (1.0, 1.0, 1.0)

# Set the range of rotation angles for the shapes
min_rotation = (0.0, 0.0, 0.0)
max_rotation = (360.0, 360.0, 360.0)

# Set the range of positions for the shapes
min_position = (-5.0, -5.0, -5.0)
max_position = (5.0, 5.0, 5.0)

# Generate the shapes
for i in range(num_shapes):
    # Create a random size for the shape
    size = random.uniform(min_size, max_size)
    
    # Create a random color for the shape
    color = (random.uniform(min_color[0], max_color[0]),
             random.uniform(min_color[1], max_color[1]),
             random.uniform(min_color[2], max_color[2]))
    
    # Create a random rotation for the shape
    rotation = (random.uniform(min_rotation[0], max_rotation[0]),
                random.uniform(min_rotation[1], max_rotation[1]),
                random.uniform(min_rotation[2], max_rotation[2]))
    
    # Create a random position for the shape
    position = (random.uniform(min_position[0], max_position[0]),
                random.uniform(min_position[1], max_position[1]),
                random.uniform(min_position[2], max_position[2]))
    
    # Generate a random shape
    if random.randint(0, 1) == 0:
        # Create a cube
        bpy.ops.mesh.primitive_cube_add(size=size, location=position, rotation=rotation)
    else:
        # Create a sphere
        bpy.ops.mesh.primitive_uv_sphere_add(size=size, location=position, rotation=rotation)
    
    # Set the color of the shape
    bpy.context.object.active_material.diffuse_color = color

# Render the scene
bpy.ops.render.render()

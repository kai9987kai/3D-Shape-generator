
# 3D-Shape-generator

A tiny **Blender (Python / `bpy`) script** that procedurally generates a batch of random 3D primitives (cubes or UV spheres), randomizes their transform + color, and triggers a render. :contentReference[oaicite:0]{index=0}

---

## What it does

`main.py`:
- Generates `num_shapes` random shapes (default: **10**) :contentReference[oaicite:1]{index=1}
- For each shape:
  - Random **size** within `[min_size, max_size]` :contentReference[oaicite:2]{index=2}
  - Random **position** within a 3D bounding box :contentReference[oaicite:3]{index=3}
  - Random **rotation** (degrees, 0–360 per axis) :contentReference[oaicite:4]{index=4}
  - Random **color** (RGB in 0–1 range) :contentReference[oaicite:5]{index=5}
  - Randomly chooses **cube** or **UV sphere** :contentReference[oaicite:6]{index=6}
- Calls `bpy.ops.render.render()` at the end (rendering the current scene setup). :contentReference[oaicite:7]{index=7}

---

## Requirements

- **Blender** (any version with `bpy` and the operators used)
- Run via Blender’s **Scripting** workspace (Text Editor) or CLI.

> This will *not* run in standard Python without Blender, because it depends on `bpy`. :contentReference[oaicite:8]{index=8}

---

## How to run (Blender UI)

1. Open Blender
2. Go to **Scripting** workspace
3. Open `main.py` in the Text Editor
4. Press **Run Script**

You should see multiple primitives appear in the scene at random locations, and Blender will trigger a render. :contentReference[oaicite:9]{index=9}

---

## How to run (CLI)

From a terminal:

```bash
blender --background --python main.py
````

This runs Blender headless and executes the script.

---

## Customization

Edit the parameters at the top of `main.py`:

* `num_shapes` — how many objects to create ([GitHub][1])
* `min_size`, `max_size` — primitive size range ([GitHub][1])
* `min_color`, `max_color` — RGB randomization bounds ([GitHub][1])
* `min_rotation`, `max_rotation` — rotation bounds (degrees) ([GitHub][1])
* `min_position`, `max_position` — spawn volume bounds ([GitHub][1])

---

## Notes / gotchas

* The script sets `bpy.context.object.active_material.diffuse_color = color`. If the created object has **no active material**, this can error or do nothing depending on Blender version/settings. A common improvement is to create/assign a new material per object before setting its color. ([GitHub][1])
* The script currently renders using **whatever render settings** are already configured in the `.blend` scene (engine, camera, resolution, output path, etc.). ([GitHub][1])

---

## Repo contents

* `main.py` — the Blender Python generator script ([GitHub][2])

---

## License

No license file is currently present in the repository. If you want others to reuse it cleanly, add a LICENSE (e.g., MIT). ([GitHub][2])

```
::contentReference[oaicite:19]{index=19}
```

[1]: https://raw.githubusercontent.com/kai9987kai/3D-Shape-generator/main/main.py "raw.githubusercontent.com"
[2]: https://github.com/kai9987kai/3D-Shape-generator "GitHub - kai9987kai/3D-Shape-generator"

# PILTools
Additional tools for python Pillow library

## documentation
### want convert PIL image into python array?
```python
from PILTools import PILTools
from PIL import Image

img = Image.open("picture.png")
array = PILTools.conv_img_array(img)

print(array)
```

### want compress your PIL image?
```python
from PILTools import PILTools
from PIL import Image

img = Image.open("picture.png")
img_compressed = PILTools(img, 2) # 1920 -> 960; 1080 -> 540

img_compressed.save("picture_.png")
```

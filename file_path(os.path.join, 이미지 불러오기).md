```python
import os
test_filepath = os.path.join(os.getcwd(), 'titanic.csv')

def get_images(filepath):
# 2. Obtain paths of images (.png used for example)
  path = os.path.join(filepath, '*.jpg') #가운데에 슬래시 쓰면 안 됨! 얘가 알아서 생성해줌
  print(path)
  img_list = sorted(glob.glob(path))

  # 3. Read images & convert to numpy arrays
  ## create placeholding numpy arrays
  IMG_SIZE = 256 #(image resolution of 256 x 256 used for example)
  x_data = np.empty((len(img_list), IMG_SIZE, IMG_SIZE, 3), dtype=np.float32) #1은 뭐지?? 일단 rgb니까 3으로 바꿨음

  ## read and convert to arrays
  for i, img_path in enumerate(img_list):
      # read image
      img = imread(img_path)
      # resize image (1 channel used for example; 1 for gray-scale, 3 for RGB-scale)
      img = resize(img, output_shape=(IMG_SIZE, IMG_SIZE, 3), preserve_range=True)
      # save to numpy array
      x_data[i] = img
  return x_data
  ```
zipfile 부터 불러오기
```python
import zipfile  # unziping 
import glob  # finding image paths
import numpy as np  # creating numpy arrays
from skimage.io import imread  # reading images
from skimage.transform import resize  # resizing images

# 1. Unzip images
'''
path = 'your zip file path'
with zipfile.ZipFile(path, 'r') as zip_ref:
    zip_ref.extractall('path for extracted images')
'''
# 2. Obtain paths of images (.png used for example)

img_list = sorted(glob.glob('mountainForest/train/forest/*.jpg'))

# 3. Read images & convert to numpy arrays
## create placeholding numpy arrays
IMG_SIZE = 256 #(image resolution of 256 x 256 used for example)
x_data = np.empty((len(img_list), IMG_SIZE, IMG_SIZE, 3), dtype=np.float32) #1은 뭐지?? 일단 rgb니까 3으로 바꿨음

## read and convert to arrays
for i, img_path in enumerate(img_list):
    # read image
    img = imread(img_path)
    # resize image (1 channel used for example; 1 for gray-scale, 3 for RGB-scale)
    img = resize(img, output_shape=(IMG_SIZE, IMG_SIZE, 3), preserve_range=True)
    # save to numpy array
    x_data[i] = img
```

간단하게 디렉토리로 불러오기
```python
file_extension = "*.jpg"

train_forest_ic = io.imread_collection(os.path.join(train_forest_dir, file_extension))
```



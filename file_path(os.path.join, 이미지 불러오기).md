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

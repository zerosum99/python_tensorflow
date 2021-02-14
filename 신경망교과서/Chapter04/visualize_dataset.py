import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import os
import random

src = 'Dataset/PetImages/'

# 데이터셋이 있는지 먼저 확인한다. 없다면 내려 받아야 한다.
if not os.path.isdir(src):
    print("""
          Dataset not found in your computer.
          Please follow the instructions in the link below to download the dataset:
          https://raw.githubusercontent.com/PacktPublishing/Neural-Network-Projects-with-Python/master/chapter4/how_to_download_the_dataset.txt
          """)
    quit()

# 파일명 리스트를 가져온다
_, _, cat_images = next(os.walk('Dataset/PetImages/Cat'))

# 가로 3개, 세로 3개(총 9개)짜리 차트를 준비한다
fig, ax = plt.subplots(3,3, figsize=(20,10))

# 무작위로 선택한 이미지를 그린다
for idx, img in enumerate(random.sample(cat_images, 9)):
    img_read = plt.imread('Dataset/PetImages/Cat/'+img)
    ax[int(idx/3), idx%3].imshow(img_read)
    ax[int(idx/3), idx%3].axis('off')
    ax[int(idx/3), idx%3].set_title('Cat/'+img)

plt.show()


# 파일명 리스트를 가져온다
_, _, dog_images = next(os.walk('Dataset/PetImages/Dog'))

# 가로 3개, 세로 3개(총 9개)짜리 차트를 준비한다
fig, ax = plt.subplots(3,3, figsize=(20,10))

# 무작위로 선택한 이미지를 그린다
for idx, img in enumerate(random.sample(dog_images, 9)):
    img_read = plt.imread('Dataset/PetImages/Dog/'+img)
    ax[int(idx/3), idx%3].imshow(img_read)
    ax[int(idx/3), idx%3].axis('off')
    ax[int(idx/3), idx%3].set_title('Dog/'+img)

plt.show()

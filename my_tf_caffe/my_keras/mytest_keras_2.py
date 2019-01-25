''''''
'''
https://blog.csdn.net/baimafujinji/article/details/80743814
迁移学习
'''

'''制作图片'''
from keras.preprocessing.image import ImageDataGenerator,img_to_array,load_img

datagen = ImageDataGenerator(rotation_range=40,
                             width_shift_range=0.2,
                             height_shift_range=0.2,
                             rescale=1. / 255,
                             shear_range=0.2,
                             zoom_range=0.2,
                             horizontal_flip=True,
                             fill_mode='nearest')
img = load_img('cat.jpg')  # this is a PIL image
x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
x = x.reshape((1,) + x.shape)  # a Numpy array with shape (1, 3, 150, 150)：一张图，三个通道，图像的尺寸（宽与高）

# the .flow() command below generates batches of randomly transformed images
# and saves the results to the `preview/` directory
i = 0
for batch in datagen.flow(x, batch_size=1,
                          save_to_dir='preview',
                          save_prefix='cat',
                          save_format='jpg'):
    i += 1
    if i > 20:
        break  # otherwise the generator would loop indefinitely


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def adjust_gamma(image, gamma=1.0):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255) ** invGamma) * 255 
                      for i in np.arange(0, 256)]).astype("uint8")
    return (cv2.LUT(image,table))

def norm(val):
    return val * 12.92 if val <= 0.0031308 else 1.055 * val**(1.0/2.4) - 0.055

def openEXR_RGB_to_mat(path):
    image = OpenEXR.InputFile(path)
    x=224
    y=224
    im = np.zeros((x,y,3))

    im[:,:,0] = np.frombuffer(image.channel('R'), dtype=np.float32).reshape((x,y))
    im[:,:,1] = np.frombuffer(image.channel('G'), dtype=np.float32).reshape((x,y))
    im[:,:,2] = np.frombuffer(image.channel('B'), dtype=np.float32).reshape((x,y))

    im = np.clip(im, 0, 1)
    return norm(im)

def category_label(labels, dims, n_labels):
    x = np.zeros([dims[0], dims[1], n_labels])
    for i in range(dims[0]):
        for j in range(dims[1]):
            x[i, j, labels[i][j]] = 1
    x = x.reshape(dims[0] * dims[1], n_labels)
    return x

def preprocess_exr(image,gamma):
    img=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img=((img/np.max(img))*255).astype("uint8")
    img=adjust_gamma(img,gamma)
    img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def data_gen_small(img_dir, mask_dir,depth_dir,liste, batch_size, dims=(224,224), n_labels=5):
    while True:
        ix = np.random.choice(liste, batch_size)
        imgs = []
        labels = []
        for i in ix:
            # images
            img_path = img_dir + str('{0:04}'.format(i)) + ".exr"
            original_img = openEXR_RGB_to_mat(img_path)
            depth_path= depth_dir + str('{0:04}'.format(i)) + ".exr"
            depth_img=openEXR_RGB_to_mat(depth_path)
            array_img = img_to_array(original_img)
            depth_channel=depth_img[:,:,0]
            array_depth=img_to_array(depth_channel)
            rgb_depth=np.dstack((array_img,array_depth))
            imgs.append(rgb_depth)
            # masks
            original_mask = cv2.imread(mask_dir + str('{0:04}'.format(i)) + ".exr")
            internoeuds = cv2.imread(inter_dir + str('{0:04}'.format(i)) + ".exr")
            array_mask = category_label(original_mask[:, :, 0], dims, n_labels)
            array_inter = img_to_array(internoeuds[:, :, 0])
            array_inter = array_inter.reshape(dims[0]*dims[1],1)
            all_masks = np.concatenate((array_mask,array_inter),axis=1)
            labels.append(all_masks)
        imgs = np.array(imgs)
        labels = np.array(labels)
        yield imgs, labels

def class_pixels(img):
    w=img.shape[0]
    h=img.shape[1]
    z=img.shape[2]
    l=np.zeros((w,h,z))
    for i in range(w):
        for j in range(h):
            for f in range(z-1):
                if img[i,j,f]==np.max([img[i,j,0],img[i,j,1],img[i,j,2],img[i,j,3],img[i,j,4]]):
                    l[i,j,f]=1
    return l


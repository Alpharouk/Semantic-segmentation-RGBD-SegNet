#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# defining the parameters of the model
model = segnet(shape, n_labels ,kernel, pool_size, output_mode)
print(model.summary())

# setting the train, val and test generator bacthes
train_gen = data_gen_small(img_dir
,mask_dir,depth_dir,liste=train_list,batch_size,dims,n_labels)
val_gen=data_gen_small(img_dir
,mask_dir,depth_dir,liste=val_list,batch_size,dims,n_labels)
test_gen = data_gen_small(img_dir
,mask_dir,depth_dir,liste=test_list,batch_size,dims,n_labels)

# training
model.compile(loss, optimizer, metrics)
history=parallel_model.fit_generator(
        train_gen,
        steps_per_epoch,
        epochs,
        validation_data,
        validation_steps)
print(history.history.keys())

import matplotlib.pyplot as plt

# plotting of training and validation accuracy curves
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()
# plotting of training and validation loss curves
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()

# inference
evaluation=model.evaluate_generator(test_gen, steps=1)
print('test score is:',evaluation[0])
print('test accuracy is:',"{0:.0f}%".format(evaluation[1]*100))


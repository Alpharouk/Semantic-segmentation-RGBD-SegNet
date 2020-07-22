#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tensorflow as tf
from keras.backend.tensorflow_backend import set_session

os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="x,y,z,.." #numbers of GPUs
config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
config.gpu_options.per_process_gpu_memory_fraction = #0.5 #0.8 
config.log_device_placement=False
config.allow_soft_placement=True

def _get_available_gpus():
    """Get a list of available gpu devices (formatted as strings).

    # Returns
        A list of available GPU devices.
    """
    #global _LOCAL_DEVICES
    if tfback._LOCAL_DEVICES is None:
        devices = tf.config.list_logical_devices()
        tfback._LOCAL_DEVICES = [x.name for x in devices]
    return [x for x in tfback._LOCAL_DEVICES if 'device:gpu' in x.lower()]

tfback._get_available_gpus = _get_available_gpus

parallel_model = multi_gpu_model(model,#total number of GPUs)


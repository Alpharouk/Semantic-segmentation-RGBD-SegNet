# Semantic segmentation of plant organs using Encoder/Decoder network and RGB-D images



This project is about semantic segmentation of 4 classes of plant organs (stem, petiole, leaf and fruit) from RGB-D images using Pyhton 3, Tensorflow 2.0 and Keras. I worked with synthetic data, randomly generated and annotated with Blender and used an Encoder/Decoder architecture trained from Scratch with 10000 images.








<img width="931" alt="Capture d’écran 2020-07-19 à 11 33 46" src="https://user-images.githubusercontent.com/62508367/87871785-c46c9200-c9b3-11ea-8ae5-21af796d4697.png">



The model was trained on 10000 images of size 224x224 on 4x12Go GPU, the curves of accuracy and loss were good as shown below:

<img width="1023" alt="Capture d’écran 2020-07-20 à 23 01 32" src="https://user-images.githubusercontent.com/62508367/87986152-ffb6b000-cadc-11ea-9552-5ed4d089f65f.png">

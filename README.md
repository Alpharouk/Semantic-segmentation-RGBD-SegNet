# Semantic segmentation of plant organs using Encoder/Decoder network and RGB-D images



This project is about semantic segmentation of 4 classes of plant organs (stem, petiole, leaf and fruit) from RGB-D images using Pyhton 3, Tensorflow 2.0 and Keras. I worked with synthetic data, randomly generated and annotated with Blender and used an Encoder/Decoder architecture trained from Scratch with 10000 images.








<img width="931" alt="Capture d’écran 2020-07-19 à 11 33 46" src="https://user-images.githubusercontent.com/62508367/87871785-c46c9200-c9b3-11ea-8ae5-21af796d4697.png">


## 1.Training & Evaluation

The model was trained on 10000 images ( 8000 images for training, 1000 images for validation and 1000 for test ) of size 224x224 on 4x12Go GPU, the curves of accuracy and loss were as follows :
**Training accuracy = 99%** and **Validation accuracy = 98%** . The curves of accuracy and loss are shown below :

<img width="1023" alt="Capture d’écran 2020-07-20 à 23 05 22" src="https://user-images.githubusercontent.com/62508367/87986532-87042380-cadd-11ea-9d1e-9a0828ace184.png">



## 2.Inference

The model was tested on 1000 RGBD images and with a **test accuracy = 97,8%** , here is some results: 


  
<img width="1026" alt="Capture d’écran 2020-07-21 à 16 59 19" src="https://user-images.githubusercontent.com/62508367/88070952-8ddd7580-cb73-11ea-8274-df32a56828a6.png">



## 3.Architecture

I used a deep Convolutional Neural Network with Encoder blocs as a features extractor and Decoder blocs as a mask generator (please go to the model.py file for the implementation of the full architecture). Here is a screenshot of one Encoder bloc visualised in Tensorboard :

<img width="1678" alt="Capture d’écran 2020-07-21 à 17 57 34" src="https://user-images.githubusercontent.com/62508367/88078060-45768580-cb7c-11ea-8c70-3f4e29f08044.png">


## Conclusion

This project was about segmentation of plant organs first in synthetic data and after in real data by doing transfert learning and generalizing the knowledge of the model ( I did only talk about the first part in this repository, the second part is confidential to the company in which I did my internship.)

## Contact

>Farouk EL BAHA
>
> Junior ML & DL Engineer
>
> e-mail: elbaha-farouk@live.fr
>
> linkedin: www.linkedin.com/in/farouk-el-baha-74803b188

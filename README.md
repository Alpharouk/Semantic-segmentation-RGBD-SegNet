# Semantic segmentation of plant organs using SegNet network and RGB-D images



This project is about semantic segmentation of 4 classes of plant organs (stem, petiole, leaf and fruit) from RGB-D images using Pyhton 3, Tensorflow 2.0 and Keras. I worked with synthetic data, randomly generated and annotated with Blender and used a SegNet architecture trained from Scratch with 10000 images.








<img width="931" alt="Capture d’écran 2020-07-19 à 11 33 46" src="https://user-images.githubusercontent.com/62508367/87871785-c46c9200-c9b3-11ea-8ae5-21af796d4697.png">



## Dataset
I published the Dataset in Dryad, here is the citation and the link of the Dataset.

Alfarouk, El Baha (2020), Synthetic HDR dataset of RGB-D images of plants and their masks for semantic and instance segmentation, Dryad, Dataset, https://doi.org/10.5061/dryad.ht76hdrd7

## 1.Training & Evaluation

The model was trained on 10000 images ( 8000 images for training, 1000 images for validation and 1000 for test ) of size 224x224 on 4x12Go GPU, the curves of accuracy and loss were as follows :
>
**Training accuracy = 99%** 
>
**Validation accuracy = 98%** 
>
The curves of accuracy and loss are shown below :

<img width="1023" alt="Capture d’écran 2020-07-20 à 23 05 22" src="https://user-images.githubusercontent.com/62508367/87986532-87042380-cadd-11ea-9d1e-9a0828ace184.png">



## 2.Inference

The model was tested on 1000 RGBD images and with a **test accuracy = 97,8%** , here is some results: 


  
<img width="1026" alt="Capture d’écran 2020-07-21 à 16 59 19" src="https://user-images.githubusercontent.com/62508367/88070952-8ddd7580-cb73-11ea-8274-df32a56828a6.png">



## 3.Architecture

Here is a screenshot of one bloc of SegNet visualised in Tensorboard :

<img width="1678" alt="Capture d’écran 2020-07-21 à 17 57 34" src="https://user-images.githubusercontent.com/62508367/88078060-45768580-cb7c-11ea-8c70-3f4e29f08044.png">


## Conclusion

This project is about semantic segmentation of plant organs into 4 classes + Background using synthetic RGB-D images.

## References

- Alfarouk, El Baha (2020), Synthetic HDR dataset of RGB-D images of plants and their masks for semantic and instance segmentation, Dryad, Dataset, https://doi.org/10.5061/dryad.ht76hdrd7

- SegNet: A Deep Convolutional Encoder-Decoder Architecture for Image Segmentation by Vijay Badrinarayanan, Alex Kendall, Roberto Cipolla, Senior Member, IEEE

## Contact

>Farouk EL BAHA
>
> Junior ML & DL Engineer
>
> e-mail: alfarouk.elbaha@gmail.com
>
> linkedin: www.linkedin.com/in/farouk-el-baha-74803b188

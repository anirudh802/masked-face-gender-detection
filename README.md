# Detecting gender of people in face masks

#### Finding the dataset

finding a dataset was pretty hard for this one because most were categorized in people with masks and people without masks

Now the first dataset i got was unlabelled but it had like a 10000 images of people in masks but they were unlabelled
now to get them labelled i tried to use the roboflow api and save the detections in text.txt file

what i planned did not work out that well because roboflow api allows only 1000 hosted inferences which i had exhausted.
now using this data i tried to train a convolutional network (this was a mistake as it almost always overfit and also the results from the roboflow inference were not fully accurate)
next i tried to search for some architectures built for detecting faces and i got to know about MTCNN

MTCNN works like magic on faces without masks but it fails on faces with masks as that was what it was trained for
i tried to search how to custom train MTCNN but i had no luck

I also tried to search more on face classification and detection models and came to know about vggFace and InceptionNet.
I tried to implement both but again with no luch the libraries were not working

Now i tried to implement this again by using a new dataset that i found which was pretty awesome as it had properly labelled images
but this time the dataset was skewed towards males i.e. it had a lot of male images and very few female ones

this time i custom trained a resnet model on the both the dataset.

on the second dataset i got an accuracy on the test imgs of 75% 
and decided to use that as the final model.


the two datasets i used are stored in 
1. halfFace_A face covering mask dataset of South Asian people
2. face (its labels are stored in text.txt file)

also the two ipynb files are for the two different datasets
1. the facetask is the first attempt with face dataset
2. the final facetask is the next attempt with the halfface dataset

#### model in action

![img](https://github.com/anirudh802/masked-face-gender-detection/blob/main/Screenshot%20from%202024-05-23%2021-48-47.png)

#### running the model

to run the model, clone the repository in your computer and run the run.py file
give it the path to the imege you want to classify and it will give back the results

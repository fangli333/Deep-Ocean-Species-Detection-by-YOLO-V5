# Project member

Fang Li @ UIUC
Yu Liu @ UIUC
Haoran Zhang @ UIUC

# Project Description

Directed by Professor Volodymyr Kindratenko @ NCSA, UIUC and Reseach Scientist Aiman S Soliman @ NCSA, UIUC.

@ National Center for Supercomputing Applications, University of Illinois at Urbana-Champaign.

This project was developed to detect species in deep ocean including shark, squid etc. During training, we chose to take camera as one class to         reduce the probability that the camera will be wrongly detected as other species. In this way, the accuracy of species can also be improved. 

A tool takes raw video in and outputs an excel file containing the numbers of species corresponding to timestamps and the video with bounding boxes     of different species showing the results of detection.

YOLO v5 | roboflow | histogram | opencv 

According to the agreement reached, the private raw videos cannot be accessed by ohters. The new private datasets established by ourselves are also     cannot accessed by others.

# How to Run

## Set up the environment
```
git clone https://github.com/fangli333/Deep-Ocean-Species-Detection-by-YOLO-V5.git Fish
cd Fish
conda create -n <MyEnv> python=3.9
conda activate <MyEnv>
pip install -r requirements.txt
```

## Detect your videos
1. Drag your video(s) into `videos` folder
2. run `bash run.sh`
3. The generated excels and videos with bbox are under `outputs` folder

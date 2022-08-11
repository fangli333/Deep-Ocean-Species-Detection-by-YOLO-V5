# Project member

Fang Li
Yu Liu
Haoran Zhang

# Project Description
This project aims to detect deep ocean species including shark, squid etc. given a set of video series. Specifically, we design a tool which takes raw videos as input, and ouput a excel file for each video indicating the number of shark, squid, etc and the timestamp for each video frame, as well as the processed video containing bbox. 

# How to Run

## Set up the environment
```
git clone https://github.com/LYZJU2019/fish_project.git Fish
cd Fish
conda create -n <MyEnv> python=3.9
conda activate <MyEnv>
pip install -r requirements.txt
```

## Detect your videos
1. Drag your video(s) into `videos` folder
2. run `bash run.sh`
3. The generated excels and videos with bbox are under `outputs` folder

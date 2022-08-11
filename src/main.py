# entrance of our project
import argparse
import os

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_path', type=str, default= './videos', help='path of the video')
    parser.add_argument('--save_dir', type=str, default="./outputs", help='path of generated excel')
    parser.add_argument('--start_t', type=str, default="00:00:00")
    parser.add_argument('--end_t', type=str, default="00:00:00")
    opt = parser.parse_args()
    return opt

def get_cmd(opt):
    cmds = []
    for vids in os.listdir(opt.video_path):
        cmds.append(r"python ./src/detect_new.py --weights ./src/best.pt --source ./videos/" + vids +  " --save_dir " + opt.save_dir + "/" + vids + ".csv --start_time " + opt.start_t + " --end_time " + opt.end_t)
    return cmds

if __name__ == "__main__":
    cmds = get_cmd(parse_opt())
    for cmd in cmds:
        print(cmd)
        os.system(cmd)
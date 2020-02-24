import cv2
import os
import shutil

def machade(file, t_s):
    cap = cv2.VideoCapture('./data/{0}.mp4'.format(file))
    dir = './results/{0}/'.format(file)
    try:
        os.mkdir(dir)
    except:
        print('Detected a folder with the same name. Deleteting it.')
        shutil.rmtree(dir)
        os.mkdir(dir)

    for i in range(len(t_s)):
        t_s[i] = t_s[i] - 0.4

    #GETTING VIDEO DETAILS
    fps = cap.get(cv2.CAP_PROP_FPS)
    dur = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    time = dur / fps

    ind = 0
    temp_j = 1
    while True:
        cur = (cap.get(cv2.CAP_PROP_POS_MSEC) / 1000)
        ret, frame = cap.read()
        if not ret:
            break
        if ind < len(t_s) and t_s[ind] - cur <= 0.05:
            print(ind + 1, cur, t_s[ind])
            h, w, c = frame.shape
            #out = cv2.VideoWriter('{0}/{1}.avi'.format(dir, str(ind)),cv2.VideoWriter_fourcc('M','J','P','G'), fps, (w, h)) 
            temp_j = 0
            for temp in range(40):
                ret, frame = cap.read()
                if not ret:
                    out.release()
                    break
                out.write(frame)
                cv2.imwrite('{0}/{1}/{2}.jpg'.format(dir, str(ind), temp_j), frame)
                temp_j+=1
            out.release()
            ind+=1

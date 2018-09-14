#encoding=utf8
import sys
import time
import math
import json
import random
import os
from PIL import Image
reload(sys)
sys.setdefaultencoding('utf8')

# split verify_code image
def split_img(nosplit_dir,save_dir):
    files=os.listdir(nosplit_dir)
    for file in files:
        #print nosplit_dir+file
        img_abdir=nosplit_dir+file
        img = Image.open(img_abdir)  #size:(85,26)
        img_id=file.split('-')[0]
        img_name=file.split('-')[1]
        region = [(0,0,20,26),(16,0,38,26),(34,0,56,26),(52,0,74,26)]
        for i in range(0,len(region)):
            cropimg=img.crop(region[i])
            crop_dir=save_dir+img_id+str(i)+'-'+img_name[i:i+1]+'.jpg'
            print crop_dir
            cropimg.save(crop_dir)
        
if __name__=="__main__":
    train_nosplit_dir="data/train_nosplit/"
    train_split_dir="data/train_split/"
    test_nosplit_dir="data/test_nosplit/"
    test_split_dir="data/test_split/"
    split_img(train_nosplit_dir,train_split_dir)
    split_img(test_nosplit_dir,test_split_dir)

import sys
import os
import wget
import time

libdir = os.path.join(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))), 'lib')
rawdir = os.path.join(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))), 'raw')


def download():
    try:
        down_data = []
        with open(os.path.join(libdir, 'data_record.txt'), 'r', encoding='UTF-8') as f:
            for line in f:
                temp = line.strip('\n')
                if(len(temp) > 0):
                    down_data.append(temp)
        down_lenth = len(down_data)
        rawdata = []
        with open(os.path.join(libdir, 'metadata.txt'), 'r', encoding='UTF-8') as f:
            for line in f:
                temp = line.strip('\n').strip('?')
                if temp.startswith('!') or temp.startswith('[') \
                        or temp.startswith('raw') or len(temp) == 0:
                    continue
                else:
                    rawdata.append(temp.strip('&'))
        raw_lenth = len(rawdata)
        for i in range(0, raw_lenth):
            if os.path.exists(os.path.join(rawdir, rawdata[i])):
                os.remove(os.path.join(rawdir, rawdata[i]))
            else:
                continue
        for i in range(0, down_lenth):
            down_txt = wget.download(down_data[i], rawdir)
        return 1

    except Exception as e:
        return 0

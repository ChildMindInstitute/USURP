#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mxf_to_wav.py

Script to quickly convert an mp3 file to a waveform file.

Author:
        – Jon Clucas, 2016 (jon.clucas@childmind.org)

© 2016, Child Mind Institute, Apache v2.0 License

Created on Fri Dec 23 12:43:40 2016

@author: jon.clucas
"""
import argparse, subprocess
from os import path

def mxf_to_wav(in_file):
    # make an output filename
    out_file = path.join(path.dirname(in_file), ''.join([path.basename(
               in_file).strip('.mxf').strip('.MXF'), '.wav']))
    # do the conversion verbosely
    print(''.join(["Converting ", in_file, " to ", out_file]))
    to_convert = ''.join(["ffmpeg -i ", in_file, " -ac 2 -acodec pcm_s32le ", out_file])
    subprocess.call(to_convert, shell = True)

def main():
    # script can be run from the command line
    parser = argparse.ArgumentParser(description='get mxf')
    parser.add_argument('in_file', metavar='in_file', type=str)
    arg = parser.parse_args()
    mxf_to_wav(arg.in_file)

# ============================================================================
if __name__ == '__main__':
    main()
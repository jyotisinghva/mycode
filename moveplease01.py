#!/usr/bin/env python3
import shutil
import os

def main():
    os.chdir('/home/student/mycode/')
    os.chdir('/home/student/mycode/')
    xname = input('What is the new name for kerrigan.obj? ')
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()

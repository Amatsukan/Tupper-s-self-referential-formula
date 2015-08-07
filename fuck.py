#!/usr/bin/python
# -*- coding: utf-8 -*-

from numpy import *
import sys
import argparse

def main():
    #k = (len(sys.argv) > 1) ? ((sys.argv[1] != 0) ? sys.argv[1] : n ): n 
    K = 960939379918958884971672962127852754715004339660129306651505519271702802395266424689642842174350718121267153782770623355993237280874144307891325963941337723487857735749823926629715517173716995165232890538221612403238855866184013235585136048828693337902491454229288667081096184496091705183454067827731551705405381627380967602565625016981482083418783163849115590225610003652351370343874461848378737238198224849863465033159410054974700593138339226497249461751545728366702369745461014655997933798537483143786841806593422227898388722980000748404719
    X = 106
    Y = 17

    parser = argparse.ArgumentParser(description='Tupper\'s self referential formula.')
    parser.add_argument('--width', '-x', type=int, default=X,
                       help='Defines x range, default is 106 pixels\n ex: -x 106')
    parser.add_argument('--height', '-y',type=int, default=Y,
                       help='Defines x range, default is 17 pixels\n ex: -y 17')
    parser.add_argument('--number', '-n',type=int, default=K,
                       help='A number to generate the image, default is K of Tupper\'s formula')
    args = parser.parse_args()
   
    X=args.width
    Y=args.height
    K=args.number

    printF(X,Y,K)


def func(x, y, K, X, Y):
    return ((K + y)//Y//2**(Y*int(x) + int(y)%Y))%2 > 0.5

def printF(X,Y,K):
    values = [[func(x, y, K, X, Y) for x in range(X)] for y in range(Y)]
    for row in values:
        a=''
        for value in row[::-1]: 
            if value:
                a = a+'█'
            else:
                a = a+' '
        print(a)



if __name__ == '__main__':
    main()

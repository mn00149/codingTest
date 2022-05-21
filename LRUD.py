#!/usr/bin/env python
# -*- coding: utf-8 -*-

import doctest
import os
import sys


def LRUD(n, list):
    '''
    nXn크기의 정사각형 공간을 만든다
    list(L,R,U,D)를 받아 움직인다
    정사각형을 넘어가는 경우는 무시
    list의 지시에 따른 최종 위치를 구할 것


    Parameters:
            list: 1차원 list(방향을 나타냄)
            n:int 이차원 배영의 크기를 결정
    Return:
            x: int x죄표
            y: int y좌표

    Test cases:
        >>> n=5 
        >>> list = [R,R,R,U,D,D]
        >>> LRUD(n, list)
        [3,4]
    Approach:
            1. 입력 리스트에 따라 움직일 방향 리스트 설정(처음 위치는 (1,1))
            1-1: L[-1, 0, 0, 0], R[0, 1, 0, 0], U[0, 0, 1, 0], D[0, 0, 0, -1]
            2. 정사각형의 크기는 nXn, (1,1)~(n,n)까지 좌표 설정
            3. 현제의 위치: x, y로 설정하고 방향 지시에 따른 위치 변화를 x= x+dx, y=y+dy로 설정
            4. for문을 이용하여 input list를 돌리고, 3의 조건에 따라 x, y의 위치를 변화시킨다
            4. 설정된 공간 배열을 넘어가는 경우 ex(0,0)이되는 경우 continue(1<=x<=n, 1<=y<=n)
            5. 최종 좌표의 위치 출력
    '''
    x, y = 1, 1
    dx = [0, 0, -1, +1]
    dy = [-1, 1, 0, 0]
    move = ["L", "R", "U", "D"]
    for i in list:
        for j in range(0, len(move)):
            if i == move[j]:
                x, y = x+dx[j], y+dy[j]
            if x < 1 or x > n or y < 1 or y > n:
                x, y = x-dx[j], y-dy[j]

    return [x, y]


if __name__ == '__main__':
    doctest.testmod()

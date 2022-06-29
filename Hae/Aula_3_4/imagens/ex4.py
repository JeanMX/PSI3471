import cv2
import queue
import numpy as np
import math

def distEuclidiana(a, b):
    return math.dist(a,b)

def pintaVermelho(a, ls, cs, t):
    b = a.copy()
    cormatriz = a[ls,cs,:]
    q = queue.Queue()
    q.put(ls)
    q.put(cs)
    while not q.empty():
        l = q.get()
        c = q.get()
        if (distEuclidiana(b[l, c,:], cormatriz) < t):
            b[l,c] = [0,0,255]
            q.put(l-1); q.put(c)
            q.put(l+1); q.put(c)
            q.put(l); q.put(c+1)
            q.put(l); q.put(c-1)
    return b


if __name__ == "__main__":
    a = cv2.imread('elefante.jpg', cv2.IMREAD_COLOR)
    b = pintaVermelho(a, 100, 110, 100)
    cv2.imwrite('ex4.jpg',b)
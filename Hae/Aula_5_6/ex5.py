import cv2
import queue
import numpy as np
import math

if __name__ == "__main__":
    a = cv2.imread('quadrado.png')
    sx = cv2.Scharr(a, cv2.CV_64F, 1,0); ver_esq = sx/4.0+0.5; cv2.imwrite('ver_esq.png',ver_esq)
    sy = cv2.Scharr(a, cv2.CV_64F, 0, 1); hor_sup = sy/4.0+0.5; cv2.imwrite('hor_sup.png',hor_sup)
    todo_hor = np.abs(hor_sup); cv2.imwrite('todo_hor.png', todo_hor)
    todo_ver = np.abs(ver_esq); cv2.imwrite('todo_ver.png', todo_ver)
    ver_dir = -sx; cv2.imwrite('ver_dir.png', ver_dir)
    hor_inf = -sy; cv2.imwrite('hor_inf.png', hor_inf)

    gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
    grad_x = cv2.Sobel(a,-1, 1, 0)
    ox = grad_x/4.0+0.5
    cv2.imwrite('ox.png', ox)
    # teste = cv2.Sobel(a, -1, 1, 0,[teste[3]]); ox=teste/4.0+0.5; cv2.imwrite('ox.png', ox)
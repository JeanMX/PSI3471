import cv2
import numpy as np
import sys

def dcReject(a, dontcare=-1e-10):
    # Elimina nivel DC (subtrai media) com dontcare. Array a deve ser numpy float32
    if dontcare==-1e-10:
        a=a-cv2.mean(a)
    else:
        naodontcare = (a!=dontcare).astype("uint8")
        media=cv2.mean(a,naodontcare)
        b=cv2.subtract(a,media,None,naodontcare)
        a=b.reshape(a.shape)
    return a
def matchTemplateSame(a, q, method, backg=0.0):
    p=np.full( a.shape, backg, dtype=np.float32 )
    p[(q.shape[0]-1)//2 : ((q.shape[0]-1)//2)+(a.shape[0]-q.shape[0]+1), (q.shape[1]-1)//2 : ((q.shape[1]-1)//2)+(a.shape[1]-q.shape[1]+1) ] = cv2.matchTemplate(np.array(a,'float32')/255,q, method)
    return p

def somaAbsDois(a):
    soma=np.sum(np.abs(a))
    a = a/(soma/2.0)
    return a

if __name__ == "__main__":
    a = cv2.imread('a.png', 0)
    q = cv2.imread('q.png', 0)
    a = np.array(a,'float32')/255
    q = np.array(q,'float32')/255
    p2 = cv2.matchTemplate(a,q, cv2.TM_CCOEFF_NORMED)
    a = cv2.cvtColor(a, cv2.COLOR_GRAY2BGR)
    p2 = np.abs(p2)
    for i in range(len(p2)):
        for j in range(len(p2[0])):
            if p2[i][j] >0.9:
                a[i][j] = [0,1,0]
    a = np.array(255*a,'uint8')
    cv2.imwrite("q_tratado.png",a)
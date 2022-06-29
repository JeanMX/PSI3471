import cv2

a = cv2.imread('mickey.bmp',0)

for l in range(a.shape[0]-1): #Percorre as linhas
    for c in range(a.shape[1]): #Percorre as colunas
        if a[l,c] == 255 and a[l,c-1] == 0 and a[l-1,c] == 0 and a[l+1, c] == 0: #Verifica se em volta do pixel branco há pixels pretos
            a[l,c]=0 #Transforma o pixel branco em preto

cv2.imwrite('mickey_elimina_ruido_branco.png',a)
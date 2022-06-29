//knearest_v3.cpp - pos2020
//Linkar com opencv3 (compila knearest_v3 -c -v3)
#include <cekeikon.h>
int main() {
    MNIST mnist(7, true, true);
    mnist.le("/cekeikon5/tiny_dnn/data");

    Mat_<FLT> axnew(mnist.ax.rows*3,49); //declaracao do valor muda conforme mais entradas forem acrescentadas
    Mat_<FLT> aynew(mnist.ay.rows*3,1);

    //Translacao para a direita
    Mat_<FLT> src_d = (Mat_<FLT>(3,2) <<
        0,0,
        7,0,
        7,7);

    Mat_<FLT> dst_d = (Mat_<FLT>(3,2) <<
        0,5,
        7,5,
        7,13);


    TimePoint t1=timePoint();
    Ptr<ml::KNearest> knn(ml::KNearest::create());
    // knn->train(mnist.ax, ml::ROW_SAMPLE, mnist.ay);
    knn->train(axnew, ml::ROW_SAMPLE, aynew);
    TimePoint t2=timePoint();
    Mat_<FLT> dist;
    knn->findNearest(mnist.qx, 1, noArray(), mnist.qp, dist);
    TimePoint t3=timePoint();
    printf("Erros=%10.2f%%\n",100.0*mnist.contaErros()/mnist.nq);
    printf("Tempo de treinamento: %f\n",timeSpan(t1,t2));
    printf("Tempo de predicao: %f\n",timeSpan(t2,t3));
}

 augmentario(data, resp):
    desloc_n = np.empty((data.shape))
    desloc_s = np.empty((data.shape))
    desloc_l = np.empty((data.shape))
    desloc_o = np.empty((data.shape))
    
    desloc_n = np.float32([[1,0,-1], [0,1,0]])
    desloc_s = np.float32([[1,0,1], [0,1,0]])
    desloc_l = np.float32([[1,0,0], [0,1,1]])
    desloc_o = np.float32([[1,0,0], [0,1,-1]])
    
    for i in range(data.shape[0]):
        desloc_n[i] = cv2.warpAffine(data[i], desloc_n, (data.shape[1], data.shape[2]))
        desloc_s[i] = cv2.warpAffine(data[i], desloc_n, (data.shape[1], data.shape[2]))
        desloc_l[i] = cv2.warpAffine(data[i], desloc_n, (data.shape[1], data.shape[2]))
        desloc_o[i] = cv2.warpAffine(data[i], desloc_n, (data.shape[1], data.shape[2]))
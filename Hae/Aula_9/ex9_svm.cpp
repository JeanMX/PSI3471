#include <cekeikon.h>
int main(int argc, char** argv) {
    MNIST mnist(7, true, false); //10x10 e sem Bounding Box
    mnist.le("/cekeikon5/tiny_dnn/data");
    CvSVM ind; //Ind as a support vector machine
    TimePoint t1=timePoint();
    
    Mat_<FLT> axnew(mnist.ax.rows*2,49); //declaracao do valor muda conforme mais entradas forem acrescentadas
    Mat_<FLT> aynew(mnist.ay.rows*2,1); 

    //Translacao para a direita
    Mat_<FLT> src_d = (Mat_<FLT>(3,2) <<
        0,0,
        7,0,
        7,7);

    Mat_<FLT> dst_d = (Mat_<FLT>(3,2) <<
        0,5,
        7,5,
        7,13);

    for (int i=0; i <60000; i++){
        for (int j=0; j<49; j++){
            axnew(i,j) = mnist.ax(i,j);
            aynew(i) = mnist.ay(i);
        }
    }

    for (int i=60000; i <120000; i++){ //subindo um pixel 
        for (int j=0; j<49; j++){
            if (j <= 41){
                axnew(i,j) = mnist.ax(i-60000,j+7);
            }
            else{
                axnew(i,j) = 0;
            }
            aynew(i) = mnist.ay(i-60000);
        }
    }

    ind.train(axnew, aynew); // Treinamento da SVM
    TimePoint t2=timePoint();
    for (int l=0; l<mnist.nq; l++) {
        mnist.qp(l)=ind.predict(mnist.qx.row(l));
    }
    TimePoint t3=timePoint();
    printf("Erros=%10.2f%%\n",100.0*mnist.contaErros()/mnist.nq);
    printf("Tempo de treinamento: %f\n",timeSpan(t1,t2));
    printf("Tempo de predicao: %f\n",timeSpan(t2,t3));
}
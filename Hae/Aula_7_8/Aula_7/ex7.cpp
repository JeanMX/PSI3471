//Lição de casa Aula 7
//Jean Carlos Mello Xavier Faria - 11259628
//Leonardo Alves Amaral Torres   - 11261002

#include <cekeikon.h>
int main() {
    Mat_<FLT> src = (Mat_<FLT>(4,2) <<
        140,44,   //Superior esquerda
        322,34,   //Superior Direita
        354,296,  //Inferior direita
        108,296); //Inferior esquerda  - ref
    Mat_<FLT> dst = (Mat_<FLT>(4,2) <<
        108,34,  //Superior esquerda
        354,34,  
        354,296,
        108,296); 
    Mat_<double> m=getPerspectiveTransform(src,dst);
    cout << m << endl;
    //Corrige a perspectiva
    Mat_<COR> a; le(a,"calib_result.jpg");
    Mat_<COR> b;
    warpPerspective(a,b,m,a.size());
    imp(b,"tabuleiro_alinhado.jpg");
}
// Especifica fatores de ampliacao
#include <cekeikon.h>
int main(int argc, char** argv)
{ if (argc!=5) {
 printf("vizinho: Muda resolucao de imagem usando interpolacao vizinho+px.\n");
 printf("vizinho ent.pgm sai.pgm fatorl fatorc\n");
 erro("Erro: Numero de argumentos invalido");
 }
 Mat_<GRY> a; le(a,argv[1]);
 float fatorl,fatorc;
 if (sscanf(argv[3],"%f",&fatorl)!=1) erro("Erro: Leitura fatorl");
 if (sscanf(argv[4],"%f",&fatorc)!=1) erro("Erro: Leitura fatorc");
 int nl=cvRound(a.rows*fatorl);
 int nc=cvRound(a.cols*fatorc);
 Mat_<GRY> b(nl,nc);
 for (int l=0; l<b.rows; l++)
 for (int c=0; c<b.cols; c++)
 b(l,c) = a(cvRound(l/fatorl),cvRound(c/fatorc));
 imp(b,argv[2]);
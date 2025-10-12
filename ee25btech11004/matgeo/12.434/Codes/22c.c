#include<math.h>

int crossx (int a2, int b3, int a3, int b2){

   int answerx = a2*b3 - a3*b2;
   return answerx;
}

int crossy (int a1, int b3, int a3, int b1){

   int answery = -(a1*b3 - a3*b1);
   return (answery);
}

int crossz (int a1, int b2, int a2, int b1){

   int answerz = a1*b2 - a2*b1;
   return answerz;
}



float norm(float a, float b, float c){

float answer;
answer = pow(a,2) + pow(b,2) + pow(c,2);
answer = sqrt(answer);

return answer;

}
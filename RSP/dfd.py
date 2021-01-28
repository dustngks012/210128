#include <stdio.h>
#include <wiringPi.h>

#define LED 1
#define SWITHCH 4

int main(){
    if(wiringPiSetup() == -1)
        return -1;

    //mode
    pinMode(LED, INPUT);
    pinMode(SWITHCH, INPUT);
    int cnt=0;  //cnt :반복횟수
    while(1){

        if(digitalRead(SWITHCH) ==1){
            cnt++;
            printf("cnt:%d\n",cnt);
            if ((cnt%3) == 1){
                digitalWrite(LED,1);
                delay(200);
    }
    else if ((cnt %3) == 2){
        for (int i = 0; i < 5; i++){
            digitalWrite(LED, 0);
            delay(200);
            digitalWrite(LED, 1);
            delay(200);
        }
    }
    else if ((cnt % 3) == 0){
        digitalWrite(LED, 0);
        delay(200);
         }
        }
    }     return 0;
}
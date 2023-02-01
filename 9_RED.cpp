#include<bits/stdc++.h>
using namespace std;

int main(){
    int maxPac = 20;
    int queSize = 10;

    double maxPro = 0.7;
    double minPro = 0.3;

    int queLen = 0;
    double dropPro = minPro;
    srand(time(0));
    for(int i = 0; i<maxPac; ++i){
        if ( queLen == queSize ){
            cout << "Packet dropped ( Queue Full ) " << endl;
            dropPro = minPro;
        }
        else if ( (double)rand()/RAND_MAX < dropPro ){
            cout << "Packet dropped ( Random ) " << endl;
            dropPro += (maxPro - minPro)/(maxPac -1);
        }
        else{
            cout << "Packet Accepted" << endl;
            queLen++;
            dropPro = minPro;
        }
    }

    return 0;
}
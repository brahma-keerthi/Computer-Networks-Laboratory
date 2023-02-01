#include <bits/stdc++.h>
using namespace std;

int main(){
    int tokens = 1, capacity = 100, request, rate = 10;

    for(int i = 0; i<10; ++i){
        tokens = min(tokens + rate, capacity);
        request = 23;

        if ( tokens >= request ){
            tokens -= request;
            cout << " Request granted -> tokens remaining >> " << tokens << endl;
        }
        else
            cout << " Request denied -> tokens remaining >> " << tokens << endl;
    }

    return 0;
}
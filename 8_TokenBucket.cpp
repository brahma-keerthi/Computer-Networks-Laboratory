#include <bits/stdc++.h>
#include<unistd.h>

using namespace std;

int main(){
    int tokens = 1, capacity = 100, request, rate = 10;

    while (true) {
        sleep(1);
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
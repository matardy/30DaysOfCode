#include<iostream> 
#include<stdlib.h>
#include<vector>

using namespace std ;

bool validate_creditcard(vector<int> credit_card){
    vector <int> validation_method;
    int sum = 0;

    for(int i=0; i<credit_card.size(); i=i+2){

        if(2*credit_card[i] > 9){
            validation_method.push_back(2*credit_card[i] - 9);
        }else{
            validation_method.push_back(2*credit_card[i]);
        }
            validation_method.push_back(credit_card[i+1]);
    }
    
    for(int i=0; i<validation_method.size(); i++){
        sum += validation_method[i];
    }

    return (sum%10 == 0);
}


int main(){
    vector<int> credit_card = {4,5,3,9,3,1,9,5,0,3,4,3,6,4,6,7};

    if(validate_creditcard(credit_card)){
        cout<< "Tarjeta valida" <<endl;
    }else{
        cout<< "Tarjeta no valida" <<endl;
    }
    

    return 0;
}
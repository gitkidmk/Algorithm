package concept;

class Parent {

    int method1(){
        int a = 1;
        int b = 2;
        return a+b;
    }
    
}

class Child extends Parent{

    // overloading
    int method1(int param1){ 
        return param1;
    }

    // overriding
    int method1(){
        int a = 1;
        int b = 2;
        int c = 3;
        return a+b+c;
    }
}

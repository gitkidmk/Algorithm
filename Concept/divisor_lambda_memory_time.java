package Concept;

@FunctionalInterface
interface MyFunction{
    // run method is always public abstract void
    void run();
}

class Divisor {
    int divisor1(int number){
        int count = 0;
        for(int i=1; i<=number; i++){
            if(number%i == 0) count += 1;
        }
        return count;
    }
    int divisor2(int number){
        int count = 0;
        for(int i=1; i*i<=number; i++){
            if(i*i==number) count += 1;
            else if(number%i == 0) count += 2;
        }
        return count;
    }

    void checkEfficiency(MyFunction f, String name) {
        Runtime runTime = Runtime.getRuntime();
        // Garbage Collection으로 메모리 초기화
		System.gc();
        // 시간 체크
        long start = System.currentTimeMillis();
        //method work
        f.run();
        long end = System.currentTimeMillis();

        float usedMemory = runTime.totalMemory() - runTime.freeMemory(); 
        System.out.printf("%s spendTime = %f %n%s usedMemory = %f%n", name, (double)(end - start)/1000.0, name, usedMemory);

    }

    public static void main(String[] args){
        MyFunction f1 = ()-> new Divisor().divisor1(1000000000);
        MyFunction f2 = ()-> new Divisor().divisor2(1000000000);

        new Divisor().checkEfficiency(f1, "divisor1");
        new Divisor().checkEfficiency(f2, "divisor2");
    }

    /* -----실행결과
        divisor1 spendTime = 2.054000 
        divisor1 usedMemory = 1152312.000000
        divisor2 spendTime = 0.000000 
        divisor2 usedMemory = 683496.000000
    */
    
}

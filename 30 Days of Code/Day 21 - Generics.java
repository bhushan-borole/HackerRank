// https://www.hackerrank.com/challenges/30-generics/problem

/**
*    Method Name: printArray
*    Print each element of the generic array on a new line. Do not return anything.
*    @param A generic array
**/

public <T> void printArray(T arr[]){
    for(T t: arr){
        System.out.println(t);
    }
}
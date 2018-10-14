// https://www.hackerrank.com/challenges/30-queues-stacks/problem

public class Solution {
    // Write your code here.
    static Queue<Character> queue = new LinkedList<>(); 
    static Stack<Character> stack = new Stack<Character>();
    void pushCharacter(char ch){
        stack.push(ch);
    }
    
    void enqueueCharacter(char ch) {
        queue.add(ch);
    }
    char popCharacter() {
        return stack.pop();
    }
    char dequeueCharacter() {
        retuarn queue.remove();
    }
}    

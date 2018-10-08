// https://www.hackerrank.com/challenges/30-inheritance/problem

class Student extends Person{
	private int[] testScores;

    /*	
    *   Class Constructor
    *   
    *   @param firstName - A string denoting the Person's first name.
    *   @param lastName - A string denoting the Person's last name.
    *   @param id - An integer denoting the Person's ID number.
    *   @param scores - An array of integers denoting the Person's test scores.
    */
    String firstname;
    String lastname;
    int id;
    
    // Write your constructor here
    public Student(String firstname, String lastname, int id, int[] testScores){
        super(firstname, lastname, id);
        this.firstname = firstname;
        this.lastname = lastname;
        this.id = id;
        this.testScores = testScores;
    }
    /*	
    *   Method Name: calculate
    *   @return A character denoting the grade.
    */
    // Write your method here
    public char calculate(){
        int sum = 0;
        for(int i=0; i<testScores.length; i++)
            sum += testScores[i];
        float avg = sum/testScores.length;
        if(avg>=90 && avg<=100)
            return 'O';
        if(avg>=80 && avg<90)
            return 'E';
        if(avg>=70 && avg<80)
            return 'A';
        if(avg>=55 && avg<70)
            return 'P';
        if(avg>=40 && avg<55)
            return 'D';
        else
            return 'T';
    }
}
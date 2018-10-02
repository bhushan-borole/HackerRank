/*
 * Determine the original side lengths and return an array:
 * - The first element is the length of the shorter side
 * - The second element is the length of the longer side
 * 
 * Parameter(s):
 * literals: The tagged template literal's array of strings.
 * expressions: The tagged template literal's array of expression values (i.e., [area, perimeter]).
 */
function sides(literals, ...expressions) {
     let A = expressions[0];
    let P = expressions[1];
    var answers = [];
    var s1 = (P+Math.sqrt(Math.pow(P, 2)-16*A))/4;
    var s2 = (P-Math.sqrt(Math.pow(P, 2)-16*A))/4;
    
    answers.push(s1);
    answers.push(s2);
    
    return answers.sort();
}
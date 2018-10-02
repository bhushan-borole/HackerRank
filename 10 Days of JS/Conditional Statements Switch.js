function getLetter(s1) {
    let s = s1.charAt(0);
    const set1 = new Set(['a', 'e', 'i', 'o', 'u']);
    const set2 = new Set(['b', 'c', 'd', 'f', 'g']);
    const set3 = new Set(['h', 'j', 'k', 'l', 'm']);
    const set4 = new Set(['n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']);
    if(set1.has(s))
        return "A";
    if(set2.has(s))
        return "B";
    if(set3.has(s))
        return "C";
    if(set4.has(s))
        return "D";
}
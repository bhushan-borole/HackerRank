function getGrade(score) {
    return 'FFEDCBA'[Math.ceil(score/5.0)];
}
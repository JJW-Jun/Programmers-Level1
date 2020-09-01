# Python Code
def solution(n):
    word = "수박" * n
    answer = word[:n]
    return answer






# Java Code
class Solution {
    public String solution(int n) {
        String answer = "";
        for (int i=1; i<=n; i++) {
            if (i%2 !=0){
                answer += "수";
            } else {
                answer += "박";
            }
        }return answer;
    }
}

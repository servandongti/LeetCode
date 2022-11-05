import Foundation

class Solution {

    func generateParenthesis(_ n: Int) -> [String] {
        var ans = [String]()
        addParenthesis(0, open: n, close: n, ans: &ans, cur: "")
        return ans
    }

    private func addParenthesis(_ index: Int, open: Int, close: Int, ans: inout [String], cur: String) {
        guard open != 0 || close != 0 else {
            ans.append(cur)
            return
        }

        if open > 0 {
            addParenthesis(index + 1, open: open - 1, close: close, ans: &ans, cur: "\(cur)(")
        }

        if close > 0, close > open {
            addParenthesis(index + 1, open: open, close: close - 1, ans: &ans, cur: "\(cur))")
        }
    }

}
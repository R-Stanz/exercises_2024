class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ls = []
        def generate_sequences(open_count = 0, close_count = 0, sequence = ""):
            if (open_count < n):
                generate_sequences(open_count + 1, close_count, sequence + "(")
            if (close_count < open_count):
                generate_sequences(open_count, close_count + 1, sequence + ")")
            if (close_count == n):
                ls.append(sequence)

        generate_sequences()
        return ls

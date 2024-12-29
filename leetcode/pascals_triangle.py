class Solution:
    def generate(self, num_rows: int) -> list[list[int]]:
        # We start with the first row, which is always [1]
        result = [[1]]

        # Loop through num_rows - 1 since the first row is already initialized
        for _ in range(num_rows - 1):
            # The current row is built by adding 0's to the start and end of the previous row
            temp_list = [0] + result[-1] + [0]
            next_row = []
            for j in range(len(result[-1]) + 1):
                # The next value is the sum of two adjacent values from the previous row
                next_row.append(temp_list[j] + temp_list[j + 1])
            result.append(next_row)

        return result
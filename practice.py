# class Solution:
#     def pattern5(self, n):
#         for row in range(0, n):
#             for col in range(0, n-row):
#                 print("*", end="")
#             print()
#
# sol = Solution()
# sol.pattern5(n=4)

def is_prime(num):
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

print(is_prime(10))
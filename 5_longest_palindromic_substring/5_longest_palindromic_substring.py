#!/usr/bin/python3

class Solution:
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		special_symb = '$'
		new_s = ''.join(map(str, [special_symb+char for char in s])) + special_symb
		z = []
		z.append(1) ##default, z[0] = 1

		R = M = 0

		for i, x in enumerate(new_s):
			mirror_x_idx = M - (i - M) #the index of mirror i
			x_right_length = R + 1 - idx

			if i > R:
				# i is not in z value which is already ready
				pass
			elif z[mirror_x_idx] == x_right_length:
				# current i's longest length hit the rigtest of palindromix of M
        # need to compare the next (i+z[mirror_x_idx], i-z[mirror_x_idx]) and then
				pass
			else:
				# i is in the palindromic of M
				pass


print(Solution().longestPalindrome('test'))

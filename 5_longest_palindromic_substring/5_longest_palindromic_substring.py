#!/usr/local/bin/python3

class Solution:
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		special_symb = '$'
		new_s = ''.join(map(str, [special_symb+char for char in s])) + special_symb
		new_s_length = len(new_s)

		def extend(left, right):
			palindromic_len = 0
			while left - palindromic_len >= 0 and right + palindromic_len < new_s_length and new_s[left - palindromic_len] == new_s[right + palindromic_len]:
				palindromic_len = palindromic_len + 1
			return palindromic_len

		z = []
		z.append(1) ##default, z[0] = 1
		##R: the rightest index of palindromic of M, M: the middle index of longest palindromic
		R = M = 0  

		for i, x in enumerate(new_s):
			mirror_x_idx = M - (i - M) #the index of mirror i
			x_max_palindromic_leng = R + 1 - i

			if i > R:
				# i is not in z value which is already ready
				z.append(extend(i, i))
				M = i
				R = i + z[i] - 1				
			elif z[mirror_x_idx] == x_max_palindromic_leng:
				# current i's longest length hit the rigtest of palindromix of M
				# need to compare the next (i+z[mirror_x_idx], i-z[mirror_x_idx]) and then
				if i > 0:  #special case for i == 0 since z[0] is 1 already
					z.append(z[mirror_x_idx] + extend(i-x_max_palindromic_leng, i+x_max_palindromic_leng))
				M = i
				R = i + z[i] - 1
			else:
				# (i+z[mirror_i]>R and i<R) or i + z[mirror_i] < R
				z.append(min(z[mirror_x_idx], x_max_palindromic_leng))

		# print([x for x in new_s])
		# print([str(x) for x in z])
		max_len = max(z)
		max_idx = z.index(max_len)
		max_len = max_len - 1 #real length

		longest_palindromic = ''.join(char for char in list(filter(lambda x: (x != special_symb), new_s[max_idx-max_len:max_idx+max_len])))
		# print("max_len: %s, max_idx: %s" % (max_len, max_idx))
		# print(longest_palindromic)
		return longest_palindromic

sample='babad'
print(Solution().longestPalindrome(sample))

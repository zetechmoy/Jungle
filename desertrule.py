

class DesertRule:

	def __init__(self, str_to_replace, replace_with):
		self.str_to_replace = str_to_replace
		self.replace_with = replace_with

	def apply(self, body_string):
		encoded_str = body_string.replace(self.str_to_replace, self.replace_with)
#		for letter in body_string:
#			if letter == self.str_to_replace:
#				encoded_str = encoded_str + self.replace_with
#			else:
#				encoded_str = encoded_str + letter
		return encoded_str

	def apply_back(self, body_string):
		decoded_str = ""
		for letter in body_string:
			if letter == self.replace_with:
				decoded_str = decoded_str + self.str_to_replace
			else:
				decoded_str = decoded_str + letter
		return decoded_str

	def applyOneTime(self, body_string):
		encoded_str = ""
		replaced = False
		for letter in body_string:
			if letter == self.str_to_replace and not replaced:
				encoded_str = encoded_str + self.replace_with
				replaced = True
			else:
				encoded_str = encoded_str + letter
		return encoded_str

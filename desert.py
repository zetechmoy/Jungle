import argparse

from desertrule import DesertRule

class Desert:

	def __init__(self, input_key):
		self.input_key = input_key
		self.key = ""
		self.vowels_index = [[], [], [], [], [], []]#[[index of all a in key], [index of all e in key], ...]
		self.vowels = "aeiouy"
		self.consonants = "zrtpqsdfghjklmwxcvbn"

		self.computeKey(input_key)

		self.current_a_index = 0
		self.current_e_index = 0
		self.current_i_index = 0
		self.current_o_index = 0
		self.current_u_index = 0
		self.current_y_index = 0

	def encode(self, str_to_encode):
		self.verifyKey()

		encoded_str = str_to_encode

		for i in range(0, len(self.vowels)):
			vowel = self.vowels[i]
			vowel_index = self.vowels_index[i]
			vowel_index_i = 0

			while(vowel in encoded_str):
				vowel_rule = DesertRule(vowel, str(vowel_index[vowel_index_i]))
				encoded_str = vowel_rule.applyOneTime(encoded_str)
				vowel_index_i += 1
				if vowel_index_i == len(vowel_index):
					vowel_index_i = 0


		for cons in self.consonants:
			rule = DesertRule(cons, cons+"a")
			encoded_str = rule.apply(encoded_str)

		space_rule = DesertRule(" ", "e")
		encoded_str = space_rule.apply(encoded_str)
		apo_rule = DesertRule("'", "i")
		encoded_str = apo_rule.apply(encoded_str)
		q_rule = DesertRule("?", "o")
		encoded_str = q_rule.apply(encoded_str)
		point_rule = DesertRule(".", "y")
		encoded_str = q_rule.apply(encoded_str)

		return encoded_str

	def decode(self, str_to_decode):
		self.verifyKey()

		decoded_str = str_to_decode

		decoded_str = decoded_str.replace("a", "")

		space_rule = DesertRule(" ", "e")
		decoded_str = space_rule.apply_back(decoded_str)
		apo_rule = DesertRule("'", "i")
		decoded_str = apo_rule.apply_back(decoded_str)
		q_rule = DesertRule("?", "o")
		decoded_str = q_rule.apply_back(decoded_str)
		point_rule = DesertRule(".", "y")
		decoded_str = q_rule.apply_back(decoded_str)

		for i in range(len(self.vowels)-1, -1, -1):
			vowel = self.vowels[i]
			vowel_index = self.vowels_index[i]
			for j in range(len(vowel_index)-1, -1, -1):
				vowel_rule = DesertRule(str(vowel_index[j]), vowel)
				decoded_str = vowel_rule.apply(decoded_str)

		return decoded_str

	def verifyKey(self):
		if(self.input_key == ""):
			raise ValueError("input_key is empty")
		if(self.key == ""):
			raise ValueError("key is empty")
		if(len(self.input_key) < 124):
			raise ValueError("key length is not enough, must be >= 124")

	def printConfig(self):
		print("input_key : "+self.input_key)
		print("key : "+self.key)

	def setKey(self, key):
		self.input_key = key
		self.computeKey(key)

	def computeKey(self, key):
		key = key.lower()
		if("a" in key and "e" in key and "i" in key and "o" in key and "u" in key and "y" in key):
			k = ""
			while(len(k) < 257):
				k = k + key
			self.key = k[:256]
			self.vowels_index = []
			for v in self.vowels:
				self.vowels_index.append(self.letterIndex(self.key, v))
		else:
			raise ValueError("All vowels (AEIOUY) are not in the key")

	def letterIndex(self, body_text, a):
		start = 0
		count = 0
		counlist = []
		length=len(body_text)
		body_text_length = len(body_text)
		index=body_text.find(a,start,length)
		while index<>-1:
			start=index+1
			count=count+1
			index=body_text.find(a,start,length)
			if(index != -1):
				counlist.append(index)
		return counlist

if __name__ == "__main__":
	parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter, add_help=False)
	parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.0', help="Show program's version number and exit.")
	parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Show this help message')
	parser.add_argument("-k", "--key", type=str, help='This is the key you want to encode/decode your string')
	parser.add_argument("-e", "--encode", type=str, help='Encode string')
	parser.add_argument("-d", "--decode", type=str, help='Decode string')

	args = parser.parse_args()
	key = args.key

	if args.key == None:
		key = "THISISAVERYLONGKEYWITHALLVOWELSYOUWILLNOTFINDANDIDONTREALLYKNOWHOWTOFINISHTHISSENTENCECAUSEIMADESTUPIDRULESBUTTHISISFORSECURITYPURPOSE"

	desert = Desert(key)

	if args.encode != None:
		print(desert.encode(args.encode))

	if args.decode != None:
		print(desert.decode(args.decode))

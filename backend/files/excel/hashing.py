import hashlib


def hashing(path):
	hasher = hashlib.md5()
	path = input('enter file path')
	print(path)
	with open(path, 'rb') as afile:
		buf = afile.read()
		hasher.update(buf)
		print(hasher.hexdigest())

hashing('./File.sol')


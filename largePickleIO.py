class largePickleIO(object):

	def __init__(self, f):
		self.f = f

	def __getattr__(self, item):
		return getattr(self.f, item)

	def read(self, n):
		if n >= (1 << 31):
			buffer = bytearray(n)
			idx = 0
			while idx < n:
				batch_size = min(n - idx, 1 << 31 - 1)
				buffer[idx:idx + batch_size] = self.f.read(batch_size)
				idx += batch_size
			return buffer
		return self.f.read(n)

	def write(self, buffer):
		n = len(buffer)
		print("Writing total bytes: {}...".format(n), flush=True)
		idx = 0
		while idx < n:
			batch_size = min(n - idx, 1 << 31 - 1)
			print("Writing bytes: [{0}, {1})... \r".format(idx, idx + batch_size), end="", flush=True)
			self.f.write(buffer[idx:idx + batch_size])
			print("Done.", flush=True)
			idx += batch_size


def loadPickle(path):
	try:
		with open(file_path, "rb") as file:
			pickle.load(largePickleIO(file))
		print('Load Sucessfully!')
	except Exception as e:
		print(e)
		return None

def savePickle(obj, file_path):
	try:
		with open(file_path, "wb") as file:
			pickle.dump(obj, largePickleIO(file), protocol=pickle.HIGHEST_PROTOCOL)
		print('Save Sucessfully!')
	except Exception as e:
		print(e)
		return None

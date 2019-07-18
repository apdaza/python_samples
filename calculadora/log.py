def save_to_log(fn):
	def wrapper(self, txt):
		fn(self, txt)
		print("Write {}".format(txt))

	return wrapper

def save_to_log(fn):
	def wrapper():
		log_info = fn()
		print("Open Log File")
		print("Write {}".format(log_info))
		print("Close File")
	return wrapper

@save_to_log
def response1():
	return "hola"

@save_to_log
def response2():
	return "chao"

response1()

response2()

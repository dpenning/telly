import telnetlib
class Telly:
	"""This class wraps the telnetlib object and allows for simpler
	printing and command management. This was originally built to
	deal with networking equipment, and the different ways they respond
	to different signals"""

	tn = None # tn is the telnetlib.Telnet object

	def __init__(self,host):
		tn = telnetlib.Telnet(host)

	def respond(self,cmd,prompt):
		"""takes a command, telnet session, and a prompt
		and returns the output of the code"""
		self.tn.write(cmd)
		return wait(t,prompt)

	def wait(self,prompt):
		"""takes a telnet session, and a prompt"""
		output_list = []
		c = ''
		d = ''
		while p not in d:
			c = self.tn.read_very_eager()
			if len(c) > 0:
				d += c
				print c
				output_list.append(c)
			if "Press any key to continue" in c or "--More--" in c:
				self.tn.write(" ")
		output_list = ((''.join(output_list)).replace('\r\n','\n')).split('\n')
		return output_list
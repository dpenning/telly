#This File is the old file that I actually used to improve on telnetid
#with this file I would insert a telnet session using the parameters on a function
#This will be fixed when I start building the real package


def respond(cmd,t,p):
	"""takes a command, telnet session, and a prompt
	and returns the output of the code"""
	t.write(cmd)
	return wait(t,p)
def wait(t,p):
	"""takes a telnet session, and a prompt"""
	output_list = []
	c = ''
	d = ''
	while p not in d:
		c = t.read_very_eager()
		if len(c) > 0:
			d += c
			print c
			output_list.append(c)
		if "Press any key to continue" in c or "--More--" in c:
			t.write(" ")
	output_list = ((''.join(output_list)).replace('\r\n','\n')).split('\n')
	return output_list

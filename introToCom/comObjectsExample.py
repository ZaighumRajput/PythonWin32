#SimpleComServer.py - A sample COM Server

# We expose a single method in a Python COM object. class PythonUtilities
import pythoncom
class PythonUtilities:
	_reg_clsctx_ = pythoncom.CLSCTX_LOCAL_SERVER
	_public_methods = [ 'SplitString']
	_reg_progid_ = "PythonString"

	# Use "print pythoncom.CreateGuid()" to make a new one.
	_reg_clsid_ = "{41E24E95-D45A-11D2-852C-204C4F4F5020}"

	def SplitString(self, val, item=None):
		import string
		if item != None: item = str(item)
		return string.split(str(val), item)
		
	# Add code so that when this script is run by
	# Python.exe it self-registers
if __name__== '__main__':
	print "Registering COM Server..."
	import win32com.server.register
	win32com.server.register.UseCommandLine(PythonUtilities)
		
	
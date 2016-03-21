# -*- coding: utf-8 -*-

# standard libs
import sys
import os
import subprocess

# custom libs
from shell_script_colors import ShellColor


# The base shell script object to be extended by real scripts
# We're extending Popen().wait()'s errorcodes into
# -1 for default and -2 for 'command doesn't exist'
class ShellScriptCore(object):
	scripts = {}
	env = os.environ

	def __init__(self, env_vars = {}, new_scripts = {}):
		for var, val in env_vars.iteritems():
			env[var] = val
		self.scripts = new_scripts

	def run(self, cmd = None):
		errorcode = None
		if cmd:
			script = self.scripts.get(cmd)
			if(script != None):
				errorcode = self.run_script(script)
			else:
				errorcode = self.cmd_does_not_exist()
		else:
			errorcode = self.default()
		return errorcode

	def default(self):
		print ShellColor.yellow + "There are no scripts to run." + ShellColor.default
		return -1

	def run_script(self, script):
		if "msg" in script:
			print ShellColor.yellow + script["msg"] + ShellColor.default
		errorcode = None
		for process in script["processes"]:
			errorcode = self.execute(process)
			if errorcode > 0:
				break
		return errorcode

	def cmd_does_not_exist(self):
		print ShellColor.red + "The command you called does not exist." + ShellColor.default
		return -2

	def execute(self, process):
		print process
		return subprocess.Popen(process, shell=True, env=self.env).wait()

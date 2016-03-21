# -*- coding: utf-8 -*-

import sys

from shell_script_assistant import ShellScriptAssistant

class Program:

	@staticmethod
	def main(args, env_vars, scripts):
		shellScript = ShellScriptAssistant(env_vars, scripts)
		if len(args) > 1:
			shellScript.run(args[1])
		else:
			shellScript.run()

# -*- coding: utf-8 -*-

import sys

from shell_script_core import ShellScriptCore
from shell_script_colors import ShellColor

# ここに実行したいスクリプトを用意する。
class ShellScriptAssistant(ShellScriptCore):

	def all(self):
		print "Good morning!"
		print "Did you remember to check these files? " + \
			ShellColor.cyan + "fuel/app/config/sandbox/db.php" + \
			ShellColor.default + " and " + ShellColor.cyan + \
			"fuel/app/config/sandbox/config.php" + ShellColor.default
		input = raw_input(ShellColor.magenta +
			"Shall I reinstall the database for you? " + ShellColor.default)
		if input.lower() == "y" or input.lower() == "yes":
			self.run_script(self.scripts["db"])
		input = raw_input(ShellColor.magenta +
			"How about your stylesheets? Recompile? " + ShellColor.default)
		if input.lower() == "y" or input.lower() == "yes":
			self.run_script(self.scripts["css"])
		print "Thank you for coming by!"

	# Override default.
	def default(self):
		self.all()

# -*- coding: utf-8 -*-
import sys
from shell_program import Program

env_vars = {
	"FUEL_ENV": "production"
}

scripts = {
	"db": {
		"msg": "Cleaning database...",
		"processes": [
			"php oil refine dinglebop",
			"php oil refine shleem",
			"php oil refine crumbo",
			"php oil refine migrate"
		]
	},
	"css": {
		"msg": "Recompiling CSS...",
		"processes": [
			"compass clean",
			"compass compile"
		]
	}
}

if __name__ == "__main__":
	Program.main(sys.argv, env_vars, scripts)

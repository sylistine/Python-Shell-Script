import sys
import unittest

from shell_script_core import ShellScriptCore

class ShellScriptCoreTest(unittest.TestCase):

    def test_init(self):
        coreInstance = ShellScriptCore()
        self.assertTrue(coreInstance.env != None)
        self.assertTrue(coreInstance.scripts == {})
        extensionInstance = TestSimpleShellScript()
        self.assertTrue(extensionInstance.env != None)
        self.assertTrue("good_process_test" in extensionInstance.scripts)

    def test_default(self):
        coreInstance = ShellScriptCore()
        self.assertEquals(coreInstance.run(), -1)

    def test_fail(self):
        coreInstance = ShellScriptCore()
        self.assertEquals(coreInstance.run("test"), -2)

    def test_success(self):
        extensionInstance = TestSimpleShellScript()
        self.assertEquals(extensionInstance.run("good_process_test"), 0)
        self.assertTrue(extensionInstance.run("bad_process_test") > 0)
        self.assertEquals(extensionInstance.run(), 0)


class TestSimpleShellScript(ShellScriptCore):

    def __init__(self):
        self.scripts = {
            "good_process_test": {
                "msg": "Running good process test.",
                "processes": [
                    "ls -la"
                ]
            },
            "bad_process_test": {
                "msg": "Running bad process test.",
                "processes": [
                    "glip glop"
                ]
            }
        }

    def default_override_test(self):
        return self.run("good_process_test")

    def default(self):
        return self.default_override_test()


if __name__ == '__main__':
    unittest.main()

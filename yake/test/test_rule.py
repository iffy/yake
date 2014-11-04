from twisted.trial.unittest import TestCase
from twisted.python.filepath import FilePath

from yake.rule import fromYAML, runRule


class RuleTest(TestCase):


    def runRule(self, rule):
        tmpdir = FilePath(self.mktemp())
        tmpdir.makedirs()
        result = runRule(rule, tmpdir.path)
        return tmpdir, result


    def test_fromYaml(self):
        """
        You can read a rule from YAML
        """
        rules = fromYAML(
            'dst.o:\n'
            '  echo foo > dst.o')
        self.assertEqual(len(rules), 1)
        tmpdir, result = self.runRule(rules[0])
        self.assertTrue(tmpdir.child('dst.o').exists(),
            "Should create dst.o")
        self.assertEqual(tmpdir.child('dst.o').getContent(),
            'foo\n')

import yaml
import commands


class Rule(object):
    
    
    def __init__(self, targets, commands):
        self.targets = targets
        self.commands = commands



def fromYAML(yaml_string):
    """

    """
    data = yaml.load(yaml_string)
    ret = []
    for key, value in data.items():
        ret.append(Rule([key], [value]))
    return ret


def runRule(rule, workdir):
    """
    Run a rule in a directory.
    """
    for command in rule.commands:
        output = commands.getoutput(command)
        print output
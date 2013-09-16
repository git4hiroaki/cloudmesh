import yaml
from jinja2 import Template
from cloudmesh.util.util import path_expand
class cm_template():

    def __init__(self, filename):

        self.filename = path_expand(filename)
        self.content = open(self.filename, 'r').read()

    def variables(self):
        vars = list()
        lines = self.content.splitlines()
        for line in lines:
            if "{{" in line:
                words = line.split("{{")
                for word in words:
                    if "}}" in word:
                        name = word.split("}}")[0].strip()
                        vars.append(name)
        return vars

    def _variables(self):
        env = Environment()
        parsed_content = env.parse(self.content)
        print meta.find_undeclared_variables(parsed_content)

    def replace(self, format="text", **d):
        template = Template(self.content)
        if format == "text":
            self.result = template.render(d)
        elif format == "dict":
            self.result = yaml.safe_load(template.render(d))
        return self.result

if __name__ == "__main__":
    d = {
      "portalname": "gvonlasz"
    }
    filename = "etc/cloudmesh.yaml"

    t = cm_template(filename)
    print t.variables()

    print t.replace(d, format="dict")

#    if not t.complete():
#       print "ERROR: undefined variables"
#       print t.variables()




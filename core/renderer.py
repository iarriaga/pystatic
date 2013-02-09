import sys

from jinja2 import Environment, PackageLoader

sys.path.append('..')


class TemplateRenderer(object):


    def __init__(self):
        self.env = Environment(loader=PackageLoader('core', 'templates'))

    def render(self, template_name, template_context = {}, target_path = None):
        template_object = self.env.get_template(template_name)
        render_result = template_object.render(template_context)
        if target_path:
            self.to_file(target_path, render_result)
        return render_result

    def to_file(self, target_path, result):
        target_file = open(target_path, 'w')
        target_file.write(result)
        target_file.close()

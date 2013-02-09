import unittest
from renderer import TemplateRenderer
from jinja2 import TemplateNotFound


class TestTemplateRenderer(unittest.TestCase):


    def setUp(self):
        self.template_renderer = TemplateRenderer()
        self.correct_template = 'test.html'
        self.template_context = { 'macanudo': '2' }
        self.target_path = '/tmp/test.html'

    def test_correct_template(self):
        result = self.template_renderer.render(self.correct_template, self.template_context)
        self.assertEquals(result, 'Test template 2')

    def test_unexisting_template(self):
        try:
            result = self.template_renderer.render('testnotexisting.html')
            self.fail()
        except TemplateNotFound:
            pass

    def test_correct_template_with_file(self):
        self.template_renderer.render(self.correct_template, template_context \
                                          = self.template_context, target_path=self.target_path)
        target_file = open(self.target_path,'r')
        self.assertEquals(target_file.read(), 'Test template 2')

if __name__ == '__main__':
    unittest.main()

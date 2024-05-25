from jinja2 import Environment, FileSystemLoader, select_autoescape

import config

def render_file(filename):
    loader = FileSystemLoader(config.app_config.website_template_path())
    environment = Environment(loader=loader, autoescape=select_autoescape())
    template = environment.get_template(filename)
    return template.render()

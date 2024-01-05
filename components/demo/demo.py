from django_components import component


@component.register("demo")
class Demo(component.Component):
    template_name = "demo/demo.html"

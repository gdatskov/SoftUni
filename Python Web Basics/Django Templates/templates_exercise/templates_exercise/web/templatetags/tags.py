from django.template import Library

from templates_exercise.web.views import Student

register = Library()


@register.simple_tag(name='student_info')
def student_info(student: Student):
    return f'This is {student.name} and is {student.age} years old'


@register.simple_tag(name='sample_tag')
def sample_tag(*args, **kwargs):
    return ', '.join(str(x) for x in (list(args) + list(kwargs.items())))


@register.inclusion_tag('tags/nav.html', name='tag_nav', takes_context=True)
def generate_nav(context, *args):
    other_context = {
        'url_names': args,
    }
    return other_context

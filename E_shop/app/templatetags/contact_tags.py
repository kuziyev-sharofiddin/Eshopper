from django import template
from app.forms import MailForm

register=template.Library()
@register.inclusion_tag('contact/tags/mail.html')

def mail_form():
    return {'mail_form':MailForm()}
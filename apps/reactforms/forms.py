from django import forms
from django.template.context_processors import csrf

class ReactForm(object):
    '''
    Must be used with objects that implement the Django forms API
    ex. ModelForm, Form
    '''

    def as_json(self, method, csrftoken):
        return {
                'csrftoken': str(csrftoken),
                'method': method,
                'fields': {
                    name: {
                        'type': field.__class__.__name__,
                    } for name, field in self.fields.items()
                }
            }

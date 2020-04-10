from django import forms

class ReactForm(object):
    '''
    Must be used with objects that implement the Django forms API
    ex. ModelForm, Form
    '''

    def as_json(self, method):
        return {
                'method': method,
                'fields': {
                    name: {
                        'type': field.__class__.__name__,
                    } for name, field in self.fields.items()
                }
            }

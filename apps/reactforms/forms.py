from django import forms

class ReactForm(object):
    '''
    Must be used with objects that implement the Django forms API
    ex. ModelForm, Form
    '''

    def as_json(self):
        print(self.fields)

from django.forms import Form,fields,widgets

class CustomerForm(Form):
    first_name = fields.CharField(max_length=100)
    last_name = fields.CharField(max_length=100)
    phon_number = fields.CharField(max_length=100)
    addres = fields.CharField(widget=widgets.Textarea)
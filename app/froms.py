from django import forms


class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()


class Appointform(forms.Form):
    name = forms.CharField(max_length=100, initial='Noname')
    email = forms.EmailField(help_text='Введите Email')
    phone = forms.CharField(max_length=15, widget=forms.PasswordInput, initial='+7 ### ### ## ##')
    select_service = forms.CharField(max_length=150)
    comments = forms.Textarea()
    fieled_order = ['email', 'name', 'phone']

class DelivForm(forms.Form):
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    email = forms.EmailField()
    street = forms.CharField(max_length=100)
    house = forms.IntegerField()
    flat = forms.IntegerField()
    agree = forms.BooleanField()
    # languages = forms.ChoiceField(choices=((1, 'English'), (2, 'Germany'), (3, 'Franch')) 

class NewsForm(forms.Form):
    title = forms.CharField(label='title', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), min_length=10)
    content = forms.CharField(max_length=300, required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    is_published = forms.BooleanField(label='published', initial=True)
    category = forms.ChoiceField(choices=((1, 'sport'), (2, 'health'), (3, 'idk')), label='category',
                                 widget=forms.Select(attrs={'class': 'form-control'})) 




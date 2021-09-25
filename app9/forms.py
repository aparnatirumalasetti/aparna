from django import forms
some_choices=[
("dosa","dosa"),
("idly","idly")
]
gender=[
("male","male"),
("female","female"),
("other","other")
]
class supermarket(forms.Form):
    name=forms.CharField(max_length=100)
    text=forms.CharField(initial="aparna",widget=forms.Textarea(attrs={"rows":4,"cols":10}))
    Roll=forms.IntegerField()
    present=forms.BooleanField(required=False)
    email=forms.EmailField(required=False)
    food_menu=forms.CharField(widget=forms.Select(choices=some_choices))
    gender=forms.CharField(label="Gender",widget=forms.RadioSelect(choices=gender))
    quantity=forms.IntegerField()
    price=forms.IntegerField()
    profile_pic=forms.ImageField(required=False)
class regs(forms.Form):
    username=forms.CharField(max_length=100)
    firstname=forms.CharField(max_length=100)
    lastname=forms.CharField(max_length=100)
    email=forms.EmailField(widget=forms.EmailInput)
    password1=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput)

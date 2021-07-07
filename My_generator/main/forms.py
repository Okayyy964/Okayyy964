
from django import forms



class Post_check(forms.Form):
	text_code = forms.CharField(label='code',max_length=20)


class Post_generate_code(forms.Form):
	group_name = forms.CharField(label='group',max_length=20)
	number_codes = forms.IntegerField(label='number')
from django import forms

class AddBlog(forms.Form):
    title = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title...'}))
    author = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Author...'}))
    blog_content = forms.CharField(widget = forms.Textarea(attrs = {'class':'form-control', 'placeholder':'Content of blog...'}))
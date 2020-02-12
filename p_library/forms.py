from django import forms  
from p_library.models import Author, Book
from django.forms import formset_factory
  
class AuthorForm(forms.ModelForm):  
    full_name = forms.CharField(widget=forms.TextInput) #Теперь вместо стандартного виджета будет использоваться виджет input type=text! 
    class Meta:  
        model = Author
        fields = '__all__' #будет обрабатывать все поля (full_name, birth_year, country)
class BookForm(forms.ModelForm):  
    class Meta:  
        model = Book  
        fields = '__all__'

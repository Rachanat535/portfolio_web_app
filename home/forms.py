from django import forms
from .models import Subscription, Banner
from blog.models import Blog

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = '__all__'
class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = '__all__'

class PopularBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
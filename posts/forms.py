from django import forms
from tinymce.widgets import TinyMCE
from posts.models import Post, Tag


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class CreatePostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    post_image = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control'}))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())

    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Post
        fields = ('title', 'post_image', 'content', 'tags')
        # fields = '__all__'

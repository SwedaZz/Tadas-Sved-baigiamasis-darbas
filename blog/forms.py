from django import forms

from blog.models import BlogPost, Tag


class CreateTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['label', 'owner']

class UpdateTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['label', 'owner']

    def save(self, commit=True):
        tag = self.instance
        tag.label = self.cleaned_data['label']

        if commit:
            tag.save()
        return tag

class CreateBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image', 'tag']


class UpdateBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image', 'tag']

    def save(self, commit=True):
        blog_post = self.instance
        blog_post.title = self.cleaned_data['title']
        blog_post.body = self.cleaned_data['body']
        blog_post.tag = self.cleaned_data['tag']

        if self.cleaned_data['image']:
            blog_post.image = self.cleaned_data['image']

        if commit:
            blog_post.save()
        return blog_post

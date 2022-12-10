from django import forms

from mymusic.mymusicapp.models import Profile, Album


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username:'
                }
            ),
            'age': forms.TextInput(
                attrs={
                    'placeholder': 'Age:'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'E-mail:'
                }
            ),
        }


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name:'
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist:'
                }
            ),
            # TODO: Fix placeholders
            # 'genre': forms.ChoiceField(
            #     attrs={
            #         'placeholder': 'Choose genre...'
            #     }
            # ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description:'
                }),
            # 'image_url': forms.URLField(
            #     attrs={
            #         'placeholder': 'Image URL:'
            #     }),
            # 'price': forms.DecimalField(
            #     attrs={
            #         'placeholder': 'Price:'
            #     }),
        }


class AlbumCreateForm(AlbumBaseForm):
    pass


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumDeleteForm(AlbumBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

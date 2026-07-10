from django import forms


class MediaUploadForm(forms.Form):
    
    youtube_url = forms.URLField(
        required=False,
        label="YouTube URL",
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter YouTube video link'
        }) 
    )

    video_file = forms.FileField(
        required=False,
        label="Upload Video",
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'accept': 'video/*'
        })
    )

    audio_file = forms.FileField(
        required=False,
        label="Upload Audio",
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'accept': 'audio/*'
        })
    )

    def clean(self):
        cleaned_data = super().clean()

        youtube_url = cleaned_data.get("youtube_url")
        video_file = cleaned_data.get("video_file")
        audio_file = cleaned_data.get("audio_file")
        if not youtube_url and not video_file and not audio_file:
            raise forms.ValidationError(
                "Please provide a YouTube link or upload a video/audio file."
            )

        return cleaned_data
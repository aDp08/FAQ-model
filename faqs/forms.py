from django import forms
from .models import FAQ

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'question_hi', 'question_bn', 'answer']

    def clean(self):
        cleaned_data = super().clean()
        question_en = cleaned_data.get("question")
        question_hi = cleaned_data.get("question_hi")
        question_bn = cleaned_data.get("question_bn")

        # Logic to allow any of the fields (English, Hindi, Bengali) to be valid
        if not question_en and not question_hi and not question_bn:
            raise forms.ValidationError("At least one question must be filled (English, Hindi, or Bengali).")

        
        if not question_en and (question_hi or question_bn):
            cleaned_data["question"] = question_hi or question_bn  # Auto-fill the English field if other fields are filled
            

        return cleaned_data

from django.contrib import admin
from .models import FAQ, UserQuestion  
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'question_hi', 'question_bn']
    search_fields = ['question']

from django.contrib import admin
from .models import FAQ, UserQuestion

class UserQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at', 'is_approved')
    actions = ['approve_question']

    def approve_question(self, request, queryset):
        for question in queryset:
            if question.is_approved:
                # Check if FAQ already exists.
                if not FAQ.objects.filter(question=question.question).exists():
                    FAQ.objects.create(question=question.question, answer="Answer to be added")
                    # Mark the question.
                    question.is_approved = True  
                    question.save()
                else:
                    self.message_user(request, f"FAQ for question '{question.question}' already exists.")
            else:
                self.message_user(request, f"Question '{question.question}' is not approved yet.")
        
        self.message_user(request, "Selected questions have been approved and added to FAQ.")

    approve_question.short_description = "Approve selected questions and add to FAQ"


admin.site.register(UserQuestion, UserQuestionAdmin)

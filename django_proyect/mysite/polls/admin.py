from django.contrib import admin

# Register your models here.

from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
            ('Date Information', {'fields': ['publish_date']}), ]
    inlines = [ChoiceInLine]
    
admin.site.register(Question,QuestionAdmin)
from django.contrib import admin
from .models import Planet, Jedi, Tests, Questions


# Register your models here.
admin.site.register(Planet)
admin.site.register(Jedi)

class TestsInline(admin.StackedInline):
    model = Questions
    extra = 0

@admin.register(Tests)
class QuestionsAdmin(admin.ModelAdmin):
    inlines = [
        TestsInline,
    ]


from django.contrib import admin
from .models import Student, Options, Bet
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Publication date' ,{'fields': ['pub_dt']}),
        ('Student information',{'fields':['name', 'desc']})
         ]

class ChoiceInLine(admin.StackedInline):
    model = Options
    extra = 3

class BetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Betting object', {'fields': ['bet_object']}),
        ('Betting details', {'fields': ['bet_desc'], 'classes' :['collapse']})
    ]
    inlines = [ChoiceInLine]

admin.site.register(Student,StudentAdmin)
admin.site.register(Bet, BetAdmin)
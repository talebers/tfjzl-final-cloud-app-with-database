from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, CourseInstructor, \
                    Enrollment, Question, Choice, Submission


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]


class LessonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
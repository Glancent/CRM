from django.contrib import admin
from django.shortcuts import render, HttpResponse, redirect

from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from crm import models
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'qq', 'name', 'source', 'consultant', 'content', 'status', 'date')
    list_filter = ('source', 'consultant', 'date')
    search_fields = ('qq', 'name')
    raw_id_fields = ('consult_course',)
    filter_horizontal = ('tags',)
    list_editable = ('status',)
    list_per_page = 5

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = models.UserProfile
        fields = ('email', 'name')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = models.UserProfile
        fields = ('email', 'password', 'name')

    def clean_password(self):
        return self.initial["password"]

class UserProfileAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'name')
    list_filter = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal', {'fields': ('name',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ("user_permissions", "groups")


class CourseRecordAdmin(admin.ModelAdmin):
    list_display = ['from_class', 'day_num', 'teacher', 'has_homework', 'homework_title', 'date']

    def initialize_studyrecords(self, request, queryset):
        print('--->initialize_studyrecords', self, request, queryset[0])
        for i in queryset:
            print("queryset:", i, type(i))

        if len(queryset) > 1:
            return HttpResponse("只能选择一个班级")
        print(queryset[0].from_class.enrollment_set.all())
        new_obj_list = []
        for enroll_obj in queryset[0].from_class.enrollment_set.all():
            # models.StudyRecord.objects.get_or_create(
            #     student=enroll_obj,
            #     course_record=queryset[0],
            #     attendance=0,
            #     score=0,
            # )

            new_obj_list.append(models.StudyRecord(
                student=enroll_obj,
                course_record=queryset[0],
                attendance=0,
                score=0,
            ))

        try:
            models.StudyRecord.objects.bulk_create(new_obj_list)  # 批量创建

        except Exception as e:
            return HttpResponse("批量初始化学习记录失败，请检查该节课是否已经有对应的学习记录")
        return redirect("/admin/crm/studyrecord/?course_record__id__exact=%s" % queryset[0].id)

    initialize_studyrecords.short_description = "初始化本节所有学员的上课记录"
    actions = ['initialize_studyrecords', ]


# Now register the new UserAdmin...

class StudyRecordAdmin(admin.ModelAdmin):
    list_display = ['student', 'course_record', 'attendance', 'score', 'date', ]
    list_filter = ['course_record', 'score', 'attendance', 'course_record__from_class', 'student', ]
    list_editable = ['score', 'attendance', ]


admin.site.register(models.UserProfile, UserProfileAdmin)

admin.site.register(models.CourseRecord, CourseRecordAdmin)
admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.CustomerFollowUp)
admin.site.register(models.Enrollment)
admin.site.register(models.Course)
admin.site.register(models.ClassList)

admin.site.register(models.Branch)
# admin.site.register(models.Role)
admin.site.register(models.Payment)
admin.site.register(models.ContractTemplate)
admin.site.register(models.StudyRecord, StudyRecordAdmin)
admin.site.register(models.Tag)
# admin.site.register(models.Menu)

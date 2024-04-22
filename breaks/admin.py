from django.contrib import admin

from breaks.models.organisations import Organisation
from breaks.models.groups import Group
from breaks.models.replacements import (
    Replacement,
    ReplacementStatus,
    ReplacementEmployee,
)

###############################
# INLINES
###############################


class ReplacementEmployeeInline(admin.TabularInline):
    model = ReplacementEmployee
    fields = (
        "employee",
        "status",
    )
    extra = 2


###############################
# MODELS
###############################
@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "director",
    )


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "manager",
        "min_active",
    )


@admin.register(Replacement)
class ReplacementAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "group",
        "date",
        "break_start",
        "break_end",
        "break_max_duration",
    )


@admin.register(ReplacementStatus)
class ReplacementStatusAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "name",
        "sort",
        "is_active",
    )
    inlines = (ReplacementEmployeeInline,)

from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html

from breaks.models.organisations import Organisation
from breaks.models.groups import Group
from breaks.models.replacements import (
    Replacement,
    ReplacementEmployee,
)
from breaks.models.breaks import Break
from breaks.models.dicts import ReplacementStatus, BreakStatus


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
    filter_horizontal = ("employees",)
    # fields = ("name",)
    # exclude = ("director",)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "manager", "min_active", "replacement_count")
    list_display_links = (
        "name",
        "min_active",
    )
    # search_fields = ("name__istartswith",)
    search_fields = ("name",)

    def replacement_count(self, obj):
        return obj.replacement_count

    replacement_count.short_description = "Количетсов смен"
    # replacement_count.empty_value_display = "Unknown"

    def get_queryset(self, request):
        queryset = Group.objects.annotate(replacement_count=Count("replacements__id"))
        return queryset


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
    autocomplete_fields = ("group",)


@admin.register(ReplacementStatus)
class ReplacementStatusAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "name",
        "sort",
        "is_active",
    )
    inlines = (ReplacementEmployeeInline,)


@admin.register(BreakStatus)
class BreakStatusAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "name",
        "sort",
        "is_active",
    )


@admin.register(Break)
class BreakAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "replacement_link",
        "break_start",
        "break_start",
    )
    # list_display_links = ("__str__", "replacement")

    def replacement_link(self, obj):
        link = reverse("admin:breaks_replacement_change", args=[obj.replacement.id])
        return format_html('<a href="{}">{}</a>', link, obj.replacement)

    replacement_link.short_description = "Смена"
    replacement_link.allow_tags = True
    list_filter = ("status__name",)
    empty_value_display = "Нет данных"
    radio_fields = {"status": admin.VERTICAL}
    # radio_fields = {"status": admin.HORIZONTAL}

    # readonly_fields = ("break_start",)
    # list_filter = ("status",)

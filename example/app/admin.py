from django.contrib import admin

from example.app.models import LevelOne, LevelThree, LevelTwo, TopLevel
from nested_inline.admin import NestedModelAdmin, NestedStackedInline


class LevelThreeInline(NestedStackedInline):
    model = LevelThree
    extra = 1
    fk_name = 'level'


class LevelTwoInline(NestedStackedInline):
    model = LevelTwo
    extra = 1
    fk_name = 'level'
    inlines = [LevelThreeInline]


class LevelOneInline(NestedStackedInline):
    model = LevelOne
    extra = 1
    fk_name = 'level'
    inlines = [LevelTwoInline]


class TopLevelAdmin(NestedModelAdmin):
    model = TopLevel
    inlines = [LevelOneInline]


admin.site.register(TopLevel, TopLevelAdmin)

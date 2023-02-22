from django.contrib import admin

from example.app.models import Foo, LevelOne, LevelThree, LevelTwo, TopLevel
from nested_inline.admin import NestedModelAdmin, NestedStackedInline


class FooAdmin(admin.ModelAdmin):
    model = Foo
    search_fields = ['name']


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
    autocomplete_fields = ['foos']


admin.site.register(Foo, FooAdmin)
admin.site.register(TopLevel, TopLevelAdmin)

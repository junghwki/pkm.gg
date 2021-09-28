from django.contrib import admin

# Register your models here.

from .models import Skill, Item, Pkm_item, Pokemon, Pkm_battle_item, Battle_item, Evolution, News

class Pkm_itemAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'pkm_id', 'count')
    search_fields = ['pkm_id__name_text']


admin.site.register(Skill)
admin.site.register(Item)
admin.site.register(Pkm_item, Pkm_itemAdmin)
admin.site.register(Pokemon)
admin.site.register(Pkm_battle_item)
admin.site.register(Battle_item)
admin.site.register(Evolution)
admin.site.register(News)



######################################
# pokemon item build modify
#from .models import Pkm_item_test
#
#class Pkm_item_test_admin(admin.ModelAdmin):
#    list_display = ('pkm_id', 'count', 'item_id_1', 'item_id_2', 'item_id_3')
#    search_fields = ['pkm_id__name_text']
#admin.site.register(Pkm_item_test, Pkm_item_test_admin)

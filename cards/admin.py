from django.contrib import admin

# Register your models here.
from cards.models import Cards


def report(modeladmin, request, queryset):
    ids = [x.id for x in queryset.all()]
    # count = queryset.update(is_reported=False)
    print('HERE:', ids)


@admin.register(Cards)
class CardsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'contents', 'created_at', 'is_reported', 'color', '_user',)
    date_hierarchy = 'created_at'       # 생성날짜별로 모아보기
    list_filter = ('is_reported', 'color',)      # 정형화된 값(boolean choice)의 필터를 만들수 있음
    search_fields = ('title', 'color', 'user__username',)     # 검색, or, contain 조건으로 검색하므 속도가 느려질 수 있음

    raw_id_fields = ('user',)
    # autocomplete_fields = ('user',)

    actions = (report, )

    def _user(self, obj):
        return obj.user.username

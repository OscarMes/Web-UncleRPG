from django.contrib import admin
# from .models import Cls_juegos
from .models import Tbl_juegos,Tbl_motor,Tbl_tres_populares

# admin.site.register(Cls_juegos)

admin.site.register(Tbl_juegos)
admin.site.register(Tbl_motor)
admin.site.register(Tbl_tres_populares)
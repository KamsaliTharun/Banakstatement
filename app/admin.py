from django.contrib import admin
from app.models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Wallet)
admin.site.register(Transaction)
admin.site.register(TransactionFee)
admin.site.register(SuperUser)
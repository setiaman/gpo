from mobile.models import Kebaktian
from mobile.models import KebaktianItem
from mobile.models import Anggota

from django.contrib import admin

class KebaktianItemInline(admin.TabularInline):
    model = KebaktianItem
    extra = 2

class KebaktianAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General',        {'fields': ['tanggal','remark','tataIbadah']}),
        ('Renungan',    {'fields': ['renungan'], 'classes': ['collapse']}),
     ]

    list_display = ('tanggal','remark')
    inlines = [KebaktianItemInline]

class AnggotaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General',        {'fields': [('HomeBase','NoAng'),('Nama','Gender'),('DOB', 'TempatLahir'), 'Pekerjaan', 'Remarks'], 'classes':['wide','extrapretty']}),
        ('Alamat/Komunikasi', {'fields': ['Alamat1', 'Kodepos',('Wilayah','Kota','Negara'),('TelHome','TelMobile','TelpdiLN','Email'),'Alamat2'], 'classes': ['wide','collapse']}),
        ('Keanggotaan',    {'fields': ['StatusAnggota', 'GerejaAsal','AtestasiMasuk', 'AtestasiKeluar','StatusBaptis','TanggalBaptis','TanggalSidi','SIDIdiGereja'], 'classes': ['wide','collapse']}),
        ('Keluarga',    {'fields': ['Ayah', 'Ibu','MaritalStatus','NamaSuamiIstri','Anak1','Anak2', 'Anak3','Anak4'], 'classes': ['wide','collapse']}),
        ('Pelayanan',    {'fields': ['Kategorial', 'Pelayanan','Talenta','Groupinterest'], 'classes': ['wide','collapse']}),
        
     ]    

    list_display = ('HomeBase', 'NoAng','Nama','DOB')
    search_fields = ['NoAng','Nama']
    date_hierarchy = 'DOB'
    
admin.site.register(Kebaktian, KebaktianAdmin)
admin.site.register(Anggota, AnggotaAdmin)
#admin.site.register(KebaktianItem)

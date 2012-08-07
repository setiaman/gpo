from django.db import models

class Kebaktian(models.Model):
    tanggal = models.DateTimeField()
    remark = models.CharField(max_length=30)
    tataIbadah = models.TextField()
    renungan = models.TextField()

    class Meta:
        db_table = "Kebaktian"

    def __unicode__(self):
        return self.remark

class KebaktianItem(models.Model):

    ITEM_TYPE = ( ('A','Ayat'), ('P','Pujian') )

    type = models.CharField(max_length=2, choices=ITEM_TYPE)
    title = models.CharField(max_length=60)
    detail = models.TextField()
    sortOrder = models.IntegerField()
    kebaktian = models.ForeignKey(Kebaktian)

    class Meta:
        db_table = "KebaktianItem"

    def __unicode__(self):
        return self.title

    
from django.db import models

class Anggota(models.Model):
    HOME_BASE = ( ('GPO','GPO'), ('GPBB','GPBB') )
    GENDER = ( ('P','Pria'), ('W','Wanita') )
    STATUS = ( ('A','Aktif'), ('TA','Tidak Aktif') )
    MARITAL_STATUS = ( ('M','Married'), ('S','Single') )
    
#    AwaldiGPO = models.IntegerField()
    NoAng = models.CharField('No. Anggota',max_length=10)
    DOB = models.DateField("Tanggal Lahir", blank=True, null=True)
    AtestasiMasuk = models.DateField(blank=True, null=True)
    AtestasiKeluar = models.DateField(blank=True, null=True)
    TanggalBaptis = models.DateField(blank=True, null=True)
    TanggalSidi = models.DateField(blank=True, null=True)
    Tglverifikasi = models.DateField(blank=True, null=True)
    Nama = models.CharField(max_length=45)
    Gender = models.CharField('Jenis Kelamin',max_length=6, choices=GENDER, blank=True)
    HomeBase = models.CharField(max_length=4, choices=HOME_BASE)
    TempatLahir = models.CharField('Tempat Lahir', max_length=50, blank=True, null=False)
    StatusAnggota = models.CharField(max_length=50, choices=STATUS, blank=True, null=False)
    Pekerjaan = models.CharField(max_length=30, blank=True, null=False)
    Alamat1 = models.TextField('Alamat SIN',max_length=45, blank=True, null=False)
    Alamat2 = models.TextField('Alamat LN',max_length=45, blank=True, null=False)
    Kota = models.CharField(max_length=20, blank=True, null=False)
    Negara = models.CharField(max_length=30, blank=True, null=False)
    Kodepos = models.CharField(max_length=6, blank=True, null=False)
    Kategorial = models.CharField(max_length=20, blank=True, null=False)
    Verifyoleh = models.CharField(max_length=45, blank=True, null=False)
    CatatanbukuGPO = models.CharField(max_length=50, blank=True, null=False)
    Groupinterest = models.CharField(max_length=15, blank=True, null=False)
    PasPhotoFile = models.CharField(max_length=255, blank=True, null=False)
    KodeposdiLN = models.CharField(max_length=6, blank=True, null=False)
    NegaradiLN = models.CharField(max_length=30, blank=True, null=False)
    TelpdiLN = models.CharField('Tlp Luar Negri',max_length=15, blank=True, null=False)
    Remarks = models.TextField(blank=True, null=False)
    verified = models.CharField(max_length=10, blank=True, null=False)
    Yangperludiverifikasi = models.CharField(max_length=80, blank=True, null=False)
    MaritalStatus = models.CharField(max_length=15, choices=MARITAL_STATUS, blank=True, null=False)
    Wilayah = models.CharField(max_length=10, blank=True, null=False)
    Nomorlama = models.CharField(max_length=5, blank=True, null=False)
    AlamatdiLN1 = models.CharField(max_length=40, blank=True, null=False)
    AlamatdiLN2 = models.CharField(max_length=30, blank=True, null=False)
    KotadiLN = models.CharField(max_length=20, blank=True, null=False)
    Anak2 = models.CharField(max_length=45, blank=True, null=False)
    NomorAnak2 = models.CharField(max_length=5, blank=True, null=False)
    Anak3 = models.CharField(max_length=45, blank=True, null=False)
    NomorAnak3 = models.CharField(max_length=5, blank=True, null=False)
    Anak4 = models.CharField(max_length=45, blank=True, null=False)
    NomorAnak4 = models.CharField(max_length=5, blank=True, null=False)
    NamaSuamiIstri = models.CharField('Nama Suami/Istri:',max_length=45, blank=True, null=False)
    NomorSuamiistri = models.CharField(max_length=5, blank=True, null=False)
    Ayah = models.CharField(max_length=45, blank=True, null=False)
    Ibu = models.CharField(max_length=45, blank=True, null=False)
    Anak1 = models.CharField(max_length=45, blank=True, null=False)
    NomorAnak1 = models.CharField(max_length=5, blank=True, null=False)
    SIDIdiGereja = models.CharField(max_length=100, blank=True, null=False)
    Kewarganegaraan = models.CharField(max_length=30, blank=True, null=False)
    Kewarganegaraanlain = models.CharField(max_length=30, blank=True, null=False)
    LamadiGPOGPBB = models.CharField(max_length=10, blank=True, null=False)
    Pelayanan = models.CharField(max_length=255, blank=True, null=False)
    Talenta = models.CharField(max_length=255, blank=True, null=False)
    TelHome = models.CharField('Tlp Rumah',max_length=15, blank=True, null=False)
    TelMobile = models.CharField('HP',max_length=15, blank=True, null=False)
    Email = models.CharField(max_length=100, blank=True, null=False)
    GerejaAsal = models.CharField(max_length=70, blank=True, null=False)
    StatusBaptis = models.CharField(max_length=50, blank=True, null=False)
    BaptisdiGereja = models.CharField(max_length=100, blank=True, null=False)
    StatusKeanggotaan = models.CharField(max_length=10, blank=True, null=False)
    
    class Meta:
        db_table = "Anggota"

    def __unicode__(self):
        return self.Nama


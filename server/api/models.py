from django.db import models


class Field(models.Model):
    """Oil field model"""

    name = models.CharField(max_length=70, unique=True)
    type = models.CharField(max_length=70, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'Field {self.name}'

    class Meta:
        db_table = 'fields'


class Project(models.Model):
    field = models.OneToOneField(
        Field, on_delete=models.CASCADE)
    name = models.TextField(unique=True)
    number = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Project {self.name}'

    class Meta:
        db_table = 'projects'


class FieldCoordinate(models.Model):
    field = models.ForeignKey(
        Field, related_name='coordinates', on_delete=models.CASCADE)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    x = models.FloatField(null=True, blank=True)
    y = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'field_coordinates'

    def __str__(self):
        return f'lat={self.lat} lng={self.lng}  x={self.x}  y={self.y}'


class Well(models.Model):
    """Well model"""
    name = models.CharField(max_length=70)
    field = models.ForeignKey(
        Field, related_name='wells', on_delete=models.CASCADE)
    pad = models.CharField(max_length=70, null=True)
    type = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True)
    alt = models.FloatField(null=True)
    bottom = models.FloatField(null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    x = models.FloatField(null=True)
    y = models.FloatField(null=True)

    def __str__(self):
        return f'Well {self.name} bottom={self.bottom}'

    class Meta:
        unique_together = ('name', 'field',)
        db_table = 'wells'


class Inclinometry(models.Model):
    """Inclinometry model"""

    well = models.ForeignKey(
        Well, related_name='inc', on_delete=models.CASCADE)
    md = models.FloatField()
    inc = models.FloatField(null=True)
    azi = models.FloatField(null=True)

    class Meta:
        db_table = 'inclinometry'

    def __str__(self):
        return f'md={self.md}   inc={self.inc}  azi={self.azi}'


class AbstractRateModel(models.Model):
    """Generic production data"""

    well = models.ForeignKey(
        Well, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=50, null=True)
    rate = models.FloatField(null=True)

    def __str__(self):
        return f'date={self.date}   rate={self.rate}'

    class Meta:
        abstract = True


class Mer(AbstractRateModel):
    """Month production report model"""

    production = models.FloatField(null=True)
    work_days = models.IntegerField(null=True)

    class Meta:
        db_table = 'mer'
        unique_together = ('well', 'date',)


class Rate(AbstractRateModel):
    """Daily production model"""

    pressure = models.FloatField(null=True)
    dynamic_level = models.FloatField(null=True)
    static_level = models.FloatField(null=True)

    class Meta:
        db_table = 'rates'


class Zone(models.Model):
    """Geological Zone/Layer model"""

    well = models.ForeignKey(Well, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    top_md = models.FloatField(null=True)
    bot_md = models.FloatField(null=True)
    top_tvd = models.FloatField(null=True)
    bot_tvd = models.FloatField(null=True)
    h = models.FloatField(null=True)

    class Meta:
        db_table = 'zones'
        unique_together = ('name', 'well',)

    def __str__(self):
        return f'Zone: {self.name}  top_md={self.top_md}    bot_md={self.bot_md}'


class WellCase(models.Model):
    """Inclinometry model"""

    well = models.ForeignKey(
        Well, related_name='cases', on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    diameter = models.FloatField()
    length = models.FloatField(null=True)
    top_md = models.FloatField(null=True)
    bot_md = models.FloatField(null=True)
    cemented = models.BooleanField(null=True)
    cement_top = models.FloatField(null=True)

    def __str__(self):
        return f'Case: {self.name}  diameter={self.diameter}'

    class Meta:
        db_table = 'cases'
        unique_together = ('name', 'well',)


class WellPerforation(models.Model):
    """Inclinometry model"""

    well = models.ForeignKey(
        Well, related_name='perforations', on_delete=models.CASCADE)
    perforator_type = models.CharField(max_length=70, null=True)
    hole_diameter = models.FloatField(null=True)
    holes_per_meter = models.FloatField(null=True)
    top_md = models.FloatField()
    bot_md = models.FloatField()

    def __str__(self):
        return f'Perforation: top_md={self.top_md}  bot_md={self.bot_md}'

    class Meta:
        db_table = 'perforations'


class WellPump(models.Model):
    """Inclinometry model"""

    well = models.OneToOneField(
        Well, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    md = models.FloatField(null=True)
    rate = models.FloatField(null=True)
    diameter = models.FloatField(null=True)

    def __str__(self):
        return f'Pump: {self.name}  md={self.md}'

    class Meta:
        db_table = 'pumps'

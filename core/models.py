from django.db import models


class Trem(models.Model):
    tue = models.CharField('tue', max_length=4, blank=True, null=True)

    def __str__(self):
        return f'{self.tue}'

    class Meta:
        verbose_name = ('TUE')
        verbose_name_plural = ('TUEs')


class Carro(models.Model):
    CMC_LUZ = 'CMC_LUZ'
    CR1_LUZ = 'CR1_LUZ'
    CR2_LUZ = 'CR2_LUZ'
    CM_LUZ = 'CM_LUZ'
    CMC_EST = 'CMC_EST'
    CR1_EST = 'CR1_EST'
    CR2_EST = 'CR2_EST'
    CM_EST = 'CM_EST'
    TIPOS = (
        (CMC_LUZ, 'CMC_LUZ'),
        (CR1_LUZ, 'CR1_LUZ'),
        (CR2_LUZ, 'CR2_LUZ'),
        (CM_LUZ , 'CM_LUZ'),
        (CMC_EST, 'CMC_EST'),
        (CR1_EST, 'CR1_EST'),
        (CR2_EST, 'CR2_EST'),
        (CM_EST, 'CM_EST')
    )
    nome = models.CharField('carro', max_length=4, blank=True, null=True)
    tipo = models.CharField('tipo', max_length=7, choices=TIPOS, blank=True, null=True)
    trem = models.ForeignKey('Trem',
                               verbose_name=('trem'),
                               related_name='carros',
                               on_delete=models.DO_NOTHING,
                               blank=True,
                               null=True)

    def __str__(self):
        return f'{self.trem} - {self.nome}'

    class Meta:
        verbose_name = ('carro')
        verbose_name_plural = ('carros')


class Falha(models.Model):
    osm = models.CharField('osm', max_length=6, blank=True, null=True)
    saf = models.CharField('saf', max_length=6, blank=True, null=True)
    descricao = models.CharField('descricao', max_length=300, blank=True, null=True)
    data = models.DateField('data', blank=True, null=True)
    hora = models.TimeField('horário', blank=True, null=True)
    ocorrencia = models.CharField('ocorrência', max_length=300, blank=True, null=True)
    trem = models.ForeignKey('Trem',
                               verbose_name=('trem'),
                               related_name='falhas',
                               on_delete=models.DO_NOTHING,
                               blank=True,
                               null=True)
    carros = models.ManyToManyField('Carro', verbose_name=('carros'), blank=True)

    def __str__(self):
        return f'{self.osm}'

    class Meta:
        verbose_name = ('falha')
        verbose_name_plural = ('falhas')


class Atuacao(models.Model):
    descricao = models.CharField('descricao', max_length=300, blank=True, null=True)
    data = models.DateField('data', blank=True, null=True)
    hora = models.TimeField('horário', blank=True, null=True)
    funcionarios = models.CharField('funcionarios', max_length=300, blank=True, null=True)
    empresas = models.CharField('empresas', max_length=300, blank=True, null=True)
    falha = models.ForeignKey('Falha',
                               verbose_name=('falha'),
                               related_name='atuacao',
                               on_delete=models.DO_NOTHING,
                               blank=True,
                               null=True)
    trem = models.ForeignKey('Trem',
                               verbose_name=('trem'),
                               related_name='atuacao',
                               on_delete=models.DO_NOTHING,
                               blank=True,
                               null=True)

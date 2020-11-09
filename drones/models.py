from django.db import models


class DroneCategoria(models.Model):
    nome = models.CharField(max_length=250)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome


class Drone(models.Model):
    nome = models.CharField(max_length=250)
    drone_categoria = models.ForeignKey(DroneCategoria,
                                        related_name='drone', on_delete=models.CASCADE)
    data = models.DateTimeField()
    competindo = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome


class Piloto(models.Model):
    MASCULINO = 'M'
    FEMININO = 'F'
    GENDER_CHOICES = (
        (MASCULINO, 'Masculino'),
        (FEMININO, 'Feminino'),
    )
    nome = models.CharField(max_length=150, blank=False, default='')
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=MASCULINO,
    )
    quant_corridas = models.IntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome


class Competicao(models.Model):
    piloto = models.ForeignKey(Piloto, related_name='competicoes',
                               on_delete=models.CASCADE)
    altura_em_pes = models.IntegerField()
    distancia_na_data = models.DateTimeField()

    class Meta:
        ordering = ('-altura_em_pes',)



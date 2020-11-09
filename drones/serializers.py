from rest_framework import serializers

from drones.models import DroneCategoria, Drone, Competicao, Piloto


class DroneCategoriaSerializer(serializers.HyperlinkedModelSerializer):
    drone = serializers.HyperlinkedIdentityField(
        many=True,
        read_only=True,
        view_none='drone-detail')

    class Meta:
        model = DroneCategoria
        fields = (
            'url',
            'pk',
            'nome',
            'drone')


class DroneSerializer(serializers.HyperlinkedModelSerializer):
    drone_categoria = serializers.SlugRelatedField(queryset=DroneCategoria.objects.all(), slug_fiels='nome')

    class Meta:
        modelo = Drone
        fields = (
            'url',
            'nome',
            'drone_categoria',
            'manufacturing_date',
            'has_it_competed')


class CompeticaoSerializer(serializers.HyperlinkedModelSerializer):
    drone = DroneSerializer()

    class Meta:
        model = Competicao
        fields = (
            'url',
            'pk',
            'altura_em_pes',
            'distancia_na_data',
            'drone')


class PilotoSerializer(serializers.HyperlinkedModelSerializer):
    competicao = CompeticaoSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(
        choices=Piloto.GENDER_CHOICES)
    gender_descricao = serializers.CharField(
        source='get_gender_display',
        read_only=True)

    class Meta:
        model = Piloto
        fields = (
            'url',
            'nome',
            'gender',
            'gender_descricao',
            'quant_corridas',
            'criado_em',
            'competicao')


class PilotoCompeticaoSerializers(serializers.ModelSerializer):
    piloto = serializers.SlugRelatedField(queryset=Piloto.objects.all(), slug_field='nome')
    drone = serializers.SlugRelatedField(queryset=Drone.objects.all(), slug_field='nome')

    class Meta:
        model = Competicao
        fields = (
            'url',
            'pk',
            'altura_em_pes',
            'distancia_na_data',
            'piloto',
            'drone')

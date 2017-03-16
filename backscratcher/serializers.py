from rest_framework import serializers

from .models import Backscratcher, Size


class SizeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Size
        fields = ('name',)


class BackscratcherSerializer(serializers.HyperlinkedModelSerializer):

    size = SizeSerializer(many=True, read_only=True)

    class Meta:
        model = Backscratcher
        fields = ('id', 'name', 'description', 'size', 'price')

    def create(self, validated_data):
        instance = Backscratcher.objects.create(**validated_data)
        sizes = Size.objects.filter(name__in=self.initial_data['size']).all()
        instance.size.add(*sizes)

        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        sizes_names = [s['name'] for s in self.initial_data.get('size', [])]
        sizes = Size.objects.filter(name__in=sizes_names).all()
        bs_sizes = instance.size.all()

        for size in bs_sizes:
            if size not in sizes:
                instance.size.remove(size)

        instance.size.add(*sizes)

        return instance

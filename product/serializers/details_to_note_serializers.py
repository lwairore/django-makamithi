from rest_framework.fields import IntegerField
from rest_framework.serializers import Serializer


class DetailToNoteSerializer(Serializer):
    loop_index_for_fr_updating = IntegerField(required=False)
    id = IntegerField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

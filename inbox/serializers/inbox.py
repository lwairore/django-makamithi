from custom_utils.iterable_object_is_not_empty import iterable_object_is_not_empty
from custom_utils.string_is_not_empty import string_is_not_empty
from custom_utils.check_key_util import check_key
from inbox.models import InboxModel
from rest_framework.serializers import ModelSerializer


class AddNewMessageModelSerializer(ModelSerializer):
    @classmethod
    def format_request_data(cls, request_data):
        new_message = {}

        if check_key(request_data, 'name'):
            name = request_data.get('name')

            if string_is_not_empty(name):
                new_message['name'] = name

        if check_key(request_data, 'email'):
            email = request_data.get('email')

            if string_is_not_empty(email):
                new_message['email'] = email

        if check_key(request_data, 'phone_number'):
            phone_number = request_data.get('phone_number')

            if string_is_not_empty(phone_number):
                new_message['phone_number'] = phone_number

        if check_key(request_data, 'subject'):
            subject = request_data.get('subject')

            if string_is_not_empty(subject):
                new_message['subject'] = subject

        if check_key(request_data, 'message'):
            message = request_data.get('message')

            if string_is_not_empty(message):
                new_message['message'] = message

        return new_message if iterable_object_is_not_empty(new_message) else None

    class Meta:
        model = InboxModel
        fields = ('name', 'email', 'phone_number',
                  'subject', 'message',)

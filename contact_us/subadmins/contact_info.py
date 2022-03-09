from contact_us.models import ContactInfoModel
from django.contrib.admin import ModelAdmin, register
from django.utils.html import format_html


@register(ContactInfoModel)
class ContactInfoModelAdmin(ModelAdmin):
    list_display = ('address_title',
                    'address', 'call_us_at', 'email_us_at', 'can_appear_on_footer',)
    list_editable = ('can_appear_on_footer',)
    list_filter = ('can_appear_on_footer', 'modified_date', 'created_at',)
    readonly_fields = ('modified_date', 'created_at',)
    date_hierarchy = 'created_at'
    search_fields = ('address_title',
                     'address', 'email', 'phone_number',)

    def call_us_at(self, obj: ContactInfoModel):
        phone_number = obj.phone_number

        if phone_number:
            return format_html(f"<a href='tel:{phone_number}'>{phone_number}</a>")
        return '-'

    call_us_at.short_description = 'Call us at'

    def email_us_at(self, obj: ContactInfoModel):
        email = obj.email

        if email:
            return format_html(f"<a href='mailto:{email}'>{email}</a>")
        return '-'

    email_us_at.short_description = 'Email us at'

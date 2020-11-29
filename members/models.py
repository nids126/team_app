from django.db import models


# Create your models here.


class Members(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    phone_number = models.IntegerField()
    email = models.EmailField()
    role = models.CharField(
        max_length=7,
        choices=(
            ('ADMIN', 'Admin'),
            ('REGULAR', 'Regular')),
        default='REGULAR',
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "team_members"

    @staticmethod
    def get_formatted_member_object(member):
        return {
            "memberId": member.id,
            "firstName": member.first_name,
            "lastName": member.last_name,
            "phoneNumber": member.phone_number,
            "email": member.email,
            "role": member.role
        }

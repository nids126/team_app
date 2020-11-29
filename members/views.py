import json

from django import views
from django.http import HttpResponse

from members.models import Members
from members.utils.common_utils import *


class TeamMembers(views.View):
    """
    View Function to fetch all the team members
    """
    @staticmethod
    def fetch_all(request):
        if request.method != "GET":
            return HttpResponse(content="Method not allowed. Please use GET", status=405)

        try:
            members_list = Members.objects.all()
            members = []
            for member in members_list:
                members.append({
                    "memberId": member.id,
                    "firstName": member.first_name,
                    "lastName": member.last_name,
                    "phoneNumber": member.phone_number,
                    "email": member.email,
                    "role": member.role
                })
            return HttpResponse(content=json.dumps({'team_members': members}), status=200, content_type="application/json")
        except Exception as e:
            return HttpResponse(content="Unable to fetch content. Please try again.", status=500)

    @staticmethod
    def fetch_id(request, member_id):
        if request.method != "GET":
            return HttpResponse(content="Method not allowed. Please use GET", status=400)

        try:
            member = Members.objects.get(id=member_id)
            member_json = Members.get_formatted_member_object(member)
            return HttpResponse(content=json.dumps(member_json), status=200, content_type="application/json")
        except Exception as e:
            return HttpResponse(content="Unable to fetch content. Please try again.", status=500)
        pass

    @staticmethod
    def create(request):
        if request.method != "POST":
            return HttpResponse(content="Method not allowed. Please use POST with the correct request body", status=405)
        try:
            request_json = json.loads(request.body)
        except Exception as e:
            return HttpResponse(content="Invalid Json.", status=400)
        try:
            # Check if all the required fields are present to create a record
            missing_fields = check_required_fields(request_json, ["firstName", "lastName", "phoneNumber", "email"])
            if len(missing_fields):
                return HttpResponse(content=f"Missing required fields: {','.join(missing_fields)}", status=400)

            # Validate the incoming phone number
            phone_number = request_json["phoneNumber"]
            if not is_valid_phone_number(str(phone_number)):
                return HttpResponse(content="Please enter a valid 10 digit mobile number", status=400)

            # Validate the email address
            email = request_json["email"]
            if not is_valid_email(email):
                return HttpResponse(content="Please enter a valid email address", status=400)

            role = request_json.get("role")
            if role and role not in ["ADMIN", "REGULAR"]:
                return HttpResponse(content="Allowed role: [ADMIN, REGULAR]", status=400)

            first_name = request_json["firstName"]
            last_name = request_json["lastName"]
            if role is not None:
                new_member = Members(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email, role=role)
            else:
                new_member = Members(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email)
            new_member.save()
            member_json = Members.get_formatted_member_object(new_member)
            return HttpResponse(status=201, content=json.dumps(member_json), content_type="application/json")
        except Exception as e:
            return HttpResponse(status=500, content=f"Error while adding member: {e}")

    @staticmethod
    def update(request, member_id):
        if request.method != "POST":
            return HttpResponse(content="Method not allowed. Please use POST with the correct request body", status=405)

        try:
            existing_member = Members.objects.get(id=member_id)
        except:
            return HttpResponse(content=f"No member with id: {member_id} found", status=404)

        try:
            request_json = json.loads(request.body)
        except Exception as e:
            return HttpResponse(content="Invalid Json.", status=400)

        try:
            if "firstName" in request_json and request_json["firstName"]:
                existing_member.first_name = request_json["firstName"]

            if "lastName" in request_json and request_json["lastName"]:
                existing_member.last_name = request_json["lastName"]

            if "phoneNumber" in request_json and request_json["phoneNumber"]:
                if not is_valid_phone_number(str(request_json["phoneNumber"])):
                    return HttpResponse(content="Please enter a valid 10 digit mobile number", status=400)
                existing_member.phone_number = request_json["phoneNumber"]
            if "email" in request_json and request_json["email"]:
                if not is_valid_email(request_json["email"]):
                    return HttpResponse(content="Please enter a valid email address", status=400)
                existing_member.email = request_json["email"]

            if "role" in request_json and request_json["role"]:
                if request_json["role"] not in ["ADMIN", "REGULAR"]:
                    return HttpResponse(content="Allowed role: [ADMIN, REGULAR]", status=400)
                existing_member.role = request_json["role"]

            existing_member.save()
        except Exception as e:
            return HttpResponse(status=500, content=f"Error while adding member: {e}")
        member_json = Members.get_formatted_member_object(existing_member)
        return HttpResponse(status=200, content=json.dumps(member_json), content_type="application/json")

    @staticmethod
    def delete(request, member_id):
        if request.method != "DELETE":
            return HttpResponse(content="Method not allowed", status=405)

        try:
            response = Members.objects.filter(id=member_id).delete()
        except Exception as e:
            return HttpResponse(content=f"Unable to delete member: {member_id}.\n {e}", status=500)
        return HttpResponse(status=200)

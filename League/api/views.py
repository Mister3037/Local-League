from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from liga.models import Team, Contact, News, Players
from users.models import CustomUser


# Create your views here.

class TeamAPIView(APIView):
    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)


class ContactAPIView(APIView):

    def post(self, request):
        data = request.data
        contact_serializer = ContactSerializer(data)

        if contact_serializer.is_valid():
            contact_serializer.save()
            data = {
                "success": "Successfully created message",
                "contact": data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {
                    "success": False,
                    "message": contact_serializer.errors
                }
            )


class TeamDetailAPIView(APIView):
    def get(self, request, pk):
        try:

            team_detail = Team.objects.get(id=pk)
            serializer = TeamSerializer(team_detail).data
            data = {
                "success": True,
                "detail": serializer
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {
                    "success": False,
                    "message": "does not exists"
                }
            )


class ProfileAPIView(APIView):
    def get(self, request, pk):
        try:

            profile = CustomUser.objects.get(id=pk)
            serializer = CustomUserSerializer(profile).data

            data = {
                "success": True,
                "profile_detail": serializer
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {
                    "success": False,
                    "message": "does not exists"
                }
            )


class NewsAPIView(APIView):
    def get(self, request):
        try:

            news = News.objects.all()
            serializer = NewsSerializer(news, many=True).data

            data = {
                "success": True,
                "news": serializer
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {
                    "success": False,
                    "message": "does not exists"
                }
            )


class NewsDetailAPIView(APIView):
    def get(self, request, pk):
        try:

            news_detail = News.objects.get(id=pk)
            serializer = NewsSerializer(news_detail).data
            data = {
                "success": True,
                "news_detail": serializer
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {
                    "success": False,
                    "message": "does not exists"
                }
            )


class PlayerAPIView(APIView):
    def get(self, request, pk):
        try:
            player = Players.objects.get(id=pk)
            serializer = PlayersSerializer(player).data

            data = {
                "success": True,
                "players": serializer
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {
                    "success": False,
                    "message": "does not exists"
                }
            )

from rest_framework import status, viewsets
from rest_framework.response import Response
from.serializers import LoanSerializer
from.models import Loan
from.permissions import IsAuthenticatedOrReadOnly
from.authentication import CustomJWTAuthentication

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [CustomJWTAuthentication]
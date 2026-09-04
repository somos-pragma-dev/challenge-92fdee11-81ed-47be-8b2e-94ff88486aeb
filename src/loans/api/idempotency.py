import uuid
from django.core.cache import cache

def idempotent_create_loan(request, data):
    idempotency_key = request.headers.get('Idempotency-Key', uuid.uuid4())
    cached_response = cache.get(idempotency_key)
    if cached_response:
        return cached_response
    else:
        # Logic to create loan and save to cache
        pass
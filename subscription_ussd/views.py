from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import parse_qs
from .ussd_logic import ussd_menu

# Mock session store
SESSION_STORE = {}

@csrf_exempt
def ussd_callback(request):
    if request.method == "POST":
        # Print incoming request body for debugging
        print("=======================CHECKING REQUEST==================", request.body)
        
        # Parse the URL-encoded data
        data = parse_qs(request.body.decode('utf-8'))
        
        # Extract values from the parsed data (returns a list, so we take the first item)
        session_id = data.get("sessionId", [None])[0]
        phone_number = data.get("phoneNumber", [None])[0]
        text = data.get("text", [""])[0]

        print("This is a text =====================",text)
        # Get or create session
        session = SESSION_STORE.get(session_id, {})

        # Call USSD logic
        response_text, end_session = ussd_menu(session, text)

        # Save session
        SESSION_STORE[session_id] = session

        # Build USSD response
        response_type = "END" if end_session else "CON"
        response = f"{response_type} {response_text}"

        return HttpResponse(response, content_type="text/plain")

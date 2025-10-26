def notify_supervisor(help_request):
    print(f"[Supervisor Notification] Need help answering: '{help_request.question}' (Request ID: {help_request.id})")

def notify_customer(help_request):
    print(f"[Customer Follow-up] Hello! The answer to your question '{help_request.question}' is: {help_request.answer}")

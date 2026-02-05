import re

def get_response(user_input: str) -> str:
    """Return a library-style response based on simple rule-based checks."""
    text = user_input.lower().strip()

    # Exit conditions
    if text in ["bye", "exit", "quit", "goodbye"]:
        return "Thank you for using the Library Assistant. Goodbye!"

    # Greetings
    if re.search(r"\b(hello|hi|hey|good morning|good afternoon|good evening)\b", text):
        return "Hello! How can I help you with library information today?"

    # Library timings
    if re.search(r"\b(timings|hours|library open|library timings)\b", text):
        return "The library is open from 9:00 AM to 6:00 PM from Monday to Saturday."

    # Book availability
    if re.search(r"\b(book availability|available books|find book)\b", text):
        return "You can search for available books using the library catalog at the counter or online portal."

    # Issue books
    if re.search(r"\b(issue book|borrow book|book issue)\b", text):
        return "To issue a book, please bring your library card to the circulation desk."

    # Return books
    if re.search(r"\b(return book|book return)\b", text):
        return "Books must be returned within 14 days to avoid late fines."

    # Membership
    if re.search(r"\b(membership|library card|join library)\b", text):
        return "Library membership can be obtained by submitting an ID proof and registration form."

    # Fines
    if re.search(r"\b(fine|late fee|penalty)\b", text):
        return "A fine of Rs. 2 per day is charged for late returns."

    # Default response
    return (
        "I'm not sure about that. You may ask about library timings, book availability, "
        "membership, issuing or returning books."
    )


def library_chatbot():
    print("LibraryBot: Welcome! I am your rule-based library assistant.")
    print("LibraryBot: Type 'bye', 'exit', or 'quit' to end the chat.\n")

    while True:
        user = input("You: ")
        response = get_response(user)
        print("LibraryBot:", response)

        if user.lower().strip() in ["bye", "exit", "quit", "goodbye"]:
            break


# Run the chatbot
library_chatbot()

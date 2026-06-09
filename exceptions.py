# Error handling
class BaseProjectError(Exception):
    """Base exception for this project."""
    pass

class BookNotFoundError(BaseProjectError):
    """Raised when a book is not found in the library."""
    pass


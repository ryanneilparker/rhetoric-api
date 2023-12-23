from pydantic import BaseModel

class Payload(BaseModel):
    """
    Captures key parameters for constructing a comprehensive blog prompt.
    """

    tone: str  # Desired tone of the text (e.g., informative, persuasive, humorous)
    structure: str  # Preferred structure of the text (e.g., listicle, how-to guide, narrative)
    style: str  # Intended writing style (e.g., formal, informal, conversational)
    voice: str  # Narrator's voice or perspective (e.g., first-person, third-person)
    purpose: str  # Main goal or objective of the text (e.g., to inform, to persuade, to entertain)
    promptText: str  # Core prompt text, serving as the starting point for the generated content

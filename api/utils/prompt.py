def generate_prompt(payload):
    """
    Construct a comprehensive blog prompt by extracting and combining essential elements from the request payload.

    Args:
        payload (dict): A dictionary containing key-value pairs representing blog prompt specifications:

    Returns:
        str: A well-formatted blog prompt string, combining all specified elements for clarity and comprehensiveness.
    """

    # Extract prompt elements from the payload
    tone = payload.tone
    structure = payload.structure
    style = payload.style
    voice = payload.voice
    purpose = payload.purpose
    prompt_text = payload.promptText

    # Construct the prompt string with clear formatting and explicit metadata
    prompt = (
        f"### Blog Prompt\n\n"
        f"Tone: {tone}\n"
        f"Structure: {structure}\n"
        f"Style: {style}\n"
        f"Voice: {voice}\n"
        f"Purpose: {purpose}\n\n"
        f"{prompt_text}\n"
    )

    return prompt

from google.cloud import texttospeech


def text_to_speech(message):
    # Initialize the client
    client = texttospeech.TextToSpeechClient()

    # where we put the python prompt
    message = "Your text here."

    # Set the text input and voice parameters
    input_text = texttospeech.SynthesisInput(text=message)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )

    # Set the audio configuration
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.OGG_OPUS
    )

    # Make the API call
    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    #return audio
    return response.audio_content



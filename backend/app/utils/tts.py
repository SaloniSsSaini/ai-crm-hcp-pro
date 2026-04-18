from fastapi.responses import StreamingResponse
import io
from openai import OpenAI

client = OpenAI()


def generate_tts_audio(text: str):
    response = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=text
    )

    audio_bytes = response.read()

    return audio_bytes


def stream_tts_audio(text: str):
    audio_bytes = generate_tts_audio(text)

    return StreamingResponse(
        io.BytesIO(audio_bytes),
        media_type="audio/mpeg"
    )
from http.client import ResponseNotReady
from google.cloud import speech_v1 as speech
import os
import requests
import json

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"d:\UPES\Project\translation project\Local_to_GCP\upheld-beach-360516-95be0c166639.json"

def speech_to_text(config, audio):
    client = speech.SpeechClient()
    response = client.recognize(config=config, audio=audio)
    print_sentences(response)
    f= open("transcribe.txt","w+")
    f=response
    # for line in response.results:
    #     f.write("This is line \n",{line})

def print_sentences(response):
    for result in response.results:
        best_alternative = result.alternatives[0]
        transcript = best_alternative.transcript
        confidence = best_alternative.confidence
        print("-" * 80)
        print(f"Transcript: {transcript}")
        print(f"Confidence: {confidence:.0%}")
        print_word_offsets(best_alternative)


def print_word_offsets(alternative):
    for word in alternative.words:
        confidence = word.confidence
        start_s = word.start_time.total_seconds()
        end_s = word.end_time.total_seconds()
        word = word.word
        print(f"{start_s:>7.3f} | {end_s:>7.3f} | {word} |{confidence:.0%}")
        

config = dict(
    language_code="en-US",
    enable_automatic_punctuation=True,
    enable_word_time_offsets=True,
    audio_channel_count = 2,
    enable_word_confidence=True)

audio = dict(uri="gs://flac_file111/how-to-speak-so-that-people-want-to-listen-julian-treasure_RRYwKciD.flac")

speech_to_text(config, audio)
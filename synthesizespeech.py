import azure.cognitiveservices.speech as speechsdk

# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = "94132667f47a4a7a85ade21ebf33c65d", "westus"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

def speech_to_text_service():
	# Creates a recognizer with the given settings
	speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
	print("Say something...")

	# Starts speech recognition, and returns after a single utterance is recognized. The end of a
	# single utterance is determined by listening for silence at the end or until a maximum of 15
	# seconds of audio is processed.  The task returns the recognition text as result. 
	# Note: Since recognize_once() returns only a single utterance, it is suitable only for single
	# shot recognition like command or query. 
	# For long-running multi-utterance recognition, use start_continuous_recognition() instead.
	result = speech_recognizer.recognize_once()
	# Checks result.
	if result.reason == speechsdk.ResultReason.RecognizedSpeech:
		return result.text
	elif result.reason == speechsdk.ResultReason.NoMatch:
		return result.no_match_details
	elif result.reason == speechsdk.ResultReason.Canceled:
	    cancellation_details = result.cancellation_details
	    return cancellation_details.reason
	    if cancellation_details.reason == speechsdk.CancellationReason.Error:
	    	return cancellation_details.error_details
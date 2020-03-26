# In this notebook, you will learn to convert an audio file of an English speaker to text using a Speech to Text API.
# Then you will translate the English version to a Spanish version using a Language Translator API.
# Note: You must obtain the API keys and enpoints to complete the lab.


# Speech to Text
# First we import SpeechToTextV1 from ibm_watson.For more information on the API, please click on this link
# https://cloud.ibm.com/apidocs/speech-to-text?code=python

from ibm_watson import SpeechToTextV1
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
from pathlib import Path  # python3 only
import os

env_path = Path('./resources/ibm-credentials-s2t.env')
print(env_path.absolute())
load_dotenv(dotenv_path=env_path)

url_s2t = os.getenv("SPEECH_TO_TEXT_URL")
iam_apikey_s2t = os.getenv("SPEECH_TO_TEXT_IAM_APIKEY")
print(url_s2t, iam_apikey_s2t)

# You create a Speech To Text Adapter object the parameters are the endpoint and API key.
# http://watson-developer-cloud.github.io/python-sdk/v0.25.0/apis/watson_developer_cloud.speech_to_text_v1.html
authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)

# the audio file that we will use to convert into text.
audioFilePath = './resources/PolynomialRegressionandPipelines.mp3'

# "rb" ,  this is similar to read mode, but it ensures the file is in binary mode.
# We use the method <code>recognize</code> to return the recognized text.
with open(audioFilePath, mode="rb") as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')

# The attribute result contains a dictionary that includes the translation:
print(response.result)

from pandas import json_normalize

json_normalize(response.result['results'], "alternatives")

# I think we should iterates on response.result['results'][i]
recognized_text = response.result['results'][0]["alternatives"][0]["transcript"]
print('recognized_text=', recognized_text)

# Language Translator
# First we import LanguageTranslatorV3 from ibm_watson. For more information on the API click here
# https://cloud.ibm.com/apidocs/language-translator?code=python
from ibm_watson import LanguageTranslatorV3

# The service endpoint is based on the location of the service instance, we store the information in the variable URL.
# To find out which URL to use, view the service credentials.

env_path = Path('./resources/ibm-credentials-translator.env')
print(env_path.absolute())
load_dotenv(dotenv_path=env_path)
url_lt = os.getenv("LANGUAGE_TRANSLATOR_URL")
apikey_lt = os.getenv("LANGUAGE_TRANSLATOR_APIKEY")

# API requests require a version parameter that takes a date in the format version=YYYY-MM-DD.
# This lab describes the current version of Language Translator, 2018-05-01
version_lt = '2018-05-01'

# we create a Language Translator object language_translator:
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt, authenticator=authenticator)
language_translator.set_service_url(url_lt)

# We can get a Lists the languages that the service can identify.
# The method Returns the language code. For example English (en) to Spanis (es) and name of each language.
print(language_translator.list_identifiable_languages().get_result())
json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")

# We can use the method translate this will translate the text.
# The parameter text is the text.
# Model_id is the type of model we would like to use use we use list the the langwich .
# In this case, we set it to 'en-es' or English to Spanish. We get a Detailed Response object translation_response
translation_response = language_translator.translate(text=recognized_text, model_id='en-es')
# The result is a dictionary.
print('translation_response=', translation_response)
translation = translation_response.get_result()
print('translation=', translation)

# We can obtain the actual translation as a string as follows:
spanish_translation = translation['translations'][0]['translation']
print("spanish_translation=", spanish_translation)

# We can translate back to English
translation_new = language_translator.translate(text=spanish_translation, model_id='es-en').get_result()
translation_eng = translation_new['translations'][0]['translation']
print("translation_eng=", translation_eng)

# We can convert it to french as well:
French_translation = language_translator.translate(text=translation_eng, model_id='en-fr').get_result()
translation_fr = French_translation['translations'][0]['translation']
print("translation_fr=", translation_fr)

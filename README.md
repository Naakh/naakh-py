# Naakh-py #

This is a python client that can be used to interact with the [Naakh API][https://www.naakh.in].

Here is some sample code that shows how you can use the API. 
<pre></code>
import time
import naakh
from pprint import pprint

from django.core.management.base import BaseCommand

from naakh.rest import ApiException


SAMPLE_OAUTH_CLIENT_ID = 'a59d3a19edb12a0efdcd'
SAMPLE_OAUTH_CLIENT_SECRET = '56d3c0c9776cdd683ca24435c12156e60fcb512e'
SAMPLE_USER_PASSWORD = 'password'
SAMPLE_USER_PHONE_NUMBER = '123451234'
SAMPLE_OAUTH_CONSUMER_KEY = 'e09444c4890dd0f234b3b7c624f362223767422d'
SAMPLE_TRANSLATION_REQUEST_UUID = 'rnkQQrnzmp4KQyYqAWHxxK'
SAMPLE_TRANSLATED_TEXT_UUID = 'CbC9oaUcrSNKT8fA8nJPYL'


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.api_client = naakh.ApiClient()
        self.test_access_token_creation()
        self.test_create_translation()
        self.test_update_translation()
        self.test_get_translation()
        self.test_get_all_languages()
        self.test_get_all_tones()
        self.test_get_all_topics()
        self.test_update_translated_text()
        self.test_get_translated_text()
        self.test_raising_api_exception()

    def test_access_token_creation(self):
        print "\n\n\n\n\n\n"
        print "Access Token Creation"
        access_token_creation_payload = naakh.AccessTokenCreationPayload()
        access_token_creation_payload.oauth_client_id = SAMPLE_OAUTH_CLIENT_ID
        access_token_creation_payload.oauth_client_secret = SAMPLE_OAUTH_CLIENT_SECRET
        access_token_creation_payload.password = SAMPLE_USER_PASSWORD
        access_token_creation_payload.phone_number = SAMPLE_USER_PHONE_NUMBER

        try:
            oauth2_api = naakh.OauthApi(self.api_client)
            data = oauth2_api.get_access_token(access_token_creation_payload, oauth_consumer_key=SAMPLE_OAUTH_CONSUMER_KEY)    
            pprint(data)
        except ApiException as e:
            print(e)

    def test_create_translation(self):
        print "\n\n\n\n\n\n"
        print "Create Translation"
        metadata = {'client_uuid': 'test_client_uuid'}
        translation_request_creation_payload = naakh.TranslationRequestCreationPayload()
        translation_request_creation_payload.cancel = False
        translation_request_creation_payload.instructions = "Simple test"
        translation_request_creation_payload.metadata = metadata
        translation_request_creation_payload.source_language = "en"
        translation_request_creation_payload.target_audience = "23-25"
        translation_request_creation_payload.target_languages = ["ml", "hi"]
        translation_request_creation_payload.text = "This is a test"
        translation_request_creation_payload.tone = "Formal"
        translation_request_creation_payload.topics = ["politics"]
        translation_request_creation_payload.web_url = "www.rohithsalim.com"

        try:
            translate_api = naakh.TranslateApi(self.api_client)
            response = translate_api.create(translation_request_creation_payload, oauth_consumer_key=SAMPLE_OAUTH_CONSUMER_KEY)    
            pprint(response)
        except ApiException as e:
            print(e)

    def test_update_translation(self):
        print "\n\n\n\n\n\n"
        print "Update Translation"

        uuid = SAMPLE_TRANSLATION_REQUEST_UUID  # Uuid
        metadata = {'key': 'value'}
        translation_request_creation_payload = naakh.TranslationRequestCreationPayload()
        translation_request_creation_payload.metadata = metadata
        try:
            translation_api = naakh.TranslationApi(self.api_client)
            response = translation_api.update_translation(uuid, translation_request_creation_payload, oauth_consumer_key=SAMPLE_OAUTH_CONSUMER_KEY)    
            pprint(response)
        except ApiException as e:
            print(e)

    def test_get_translation(self):
        print "\n\n\n\n\n\n"
        print "Get Translation"

        uuid = SAMPLE_TRANSLATION_REQUEST_UUID
        try:
            translation_api = naakh.TranslationApi(self.api_client)
            response = translation_api.get_translation(uuid, oauth_consumer_key=SAMPLE_OAUTH_CONSUMER_KEY)    
            pprint(response)
        except ApiException as e:
            print(e)

    def test_get_all_languages(self):
        print "\n\n\n\n\n\n"
        print "Get All Languages"

        try:
            langauges_api = naakh.LanguagesApi(self.api_client)
            response = langauges_api.get_all_languages(oauth_consumer_key=SAMPLE_OAUTH_CONSUMER_KEY)    
            pprint(response)
        except ApiException as e:
            print(e)

    def test_get_all_tones(self):
        print "\n\n\n\n\n\n"
        print "Get All Tones"

        try:
            tones_api = naakh.TonesApi(self.api_client)
            response = tones_api.get_all_tones(oauth_consumer_key=SAMPLE_OAUTH_CONSUMER_KEY)    
            pprint(response)
        except ApiException as e:
            print(e)

    def test_get_all_topics(self):
        print "\n\n\n\n\n\n"
        print "Get All Topics"

        try:
            topics_api = naakh.TopicsApi(self.api_client)
            response = topics_api.get_all_topics(oauth_consumer_key=SAMPLE_OAUTH_CONSUMER_KEY)
            pprint(response)
        except ApiException as e:
            print(e)

    def test_update_translated_text(self):
        print "\n\n\n\n\n\n"
        print "Update Translated Text"

        uuid = SAMPLE_TRANSLATED_TEXT_UUID  # Uuid
        metadata = {'key': 'value'}
        translated_text_update_payload = naakh.TranslatedTextUpdatePayload()
        translated_text_update_payload.metadata = metadata

        try:
            translatedtext_api = naakh.TranslatedtextApi(self.api_client)
            response = translatedtext_api.update_translated_text(uuid, translated_text_update_payload, oauth_consumer_key=SAMPLE_OAUTH_CONSUMER_KEY)    
            pprint(response)
        except ApiException as e:
            print(e)

    def test_get_translated_text(self):
        print "\n\n\n\n\n\n"
        print "Get Translated Text"

        uuid = SAMPLE_TRANSLATED_TEXT_UUID
        try:
            translatedtext_api = naakh.TranslatedtextApi(self.api_client)
            response = translatedtext_api.get_translated_text(uuid, oauth_consumer_key=SAMPLE_OAUTH_CONSUMER_KEY)
            pprint(response)
        except ApiException as e:
            print(e)

    def test_raising_api_exception(self):
        print "\n\n\n\n\n\n"
        print "Raising an error"
        access_token_creation_payload = naakh.AccessTokenCreationPayload()
        access_token_creation_payload.oauth_client_id = SAMPLE_OAUTH_CLIENT_ID
        access_token_creation_payload.oauth_client_secret = SAMPLE_OAUTH_CLIENT_SECRET
        access_token_creation_payload.password = SAMPLE_USER_PASSWORD
        access_token_creation_payload.phone_number = "INCORRECT_USERNAME"

        try:
            oauth2_api = naakh.OauthApi(self.api_client)
            data = oauth2_api.get_access_token(access_token_creation_payload, oauth_consumer_key=SAMPLE_OAUTH_CONSUMER_KEY)    
            pprint(data)
        except ApiException as e:
            print(e)
</code></pre>

Feel free to email rohitsalim@gmail.com if you have any questions at all. 
Django translations: Quick Guide
This is a short hint which is a smaller version of Django Translation Documentation

Step 1 – Setup
Make sure in settings.py you have the next settings:

USE_I18N = True
USE_L10N = True
LOCALE_PATHS = (
	os.path.join(os.path.dirname(__file__), "..", "locale"), # folder where locale files will sit
)
Step 2 – Prepare HTML templates
In all your templates (.html files) make sure you load i18n at the beginning of each file:

{% load i18n %}
Wrap all English text strings which are visualized into trans. E.g. if you had

<div class="item">Go Home</div>
It should become:

<div class="item">{% trans "Go Home" %}</div>
Step 3 – Prepare Python strings code
If somehow it happened that your strings located in python view files e.g. views.py (it happens 😉) then add import to the files:

from django.utils.translation import gettext as _
And wrap text strings into:

category = {
	'item': _('Red Snakes'), 
Better do it on top level of each view function, within dict or using several local variables. Gettext which used under the hook is pretty taugh to find it inside of some nested operators...
Step 4 – Generate text .po file for translators
Use the mange.py command to collect all text strings into .po file which will appear in locales folder (designed on step 1):

pipenv run django-admin makemessages -l ja
The commands generate files for one language. For several languages generate it multiple times with different -l argument.

Step 5 – Translate .po file
Basically, you need to type in an empty untranslated string under their English version to the target language

You might want to do it:

Try your multilingual capabilities and get your hands dirty by opening .po file in any text editor
Outsource to translators (some of them even know what is .po format)
Surrender to AI, you might like django-autotranslate
The last one could be a pretty interesting option to faster fulfill the translation for cheaper proofreaders.

Basically, after following the installation guide you could:

pipenv run python manage.py translate_messages --untranslated
And it will populate .po file using a translator of the Google Company.

However, you might easily connect to another service like Deepl:

AUTOTRANSLATE_TRANSLATOR_SERVICE = 'apps.yourapp.utils.DeeplTranslatorService'
The code of Service:

class DeeplTranslatorService(BaseTranslatorService):
	    BASE_URL = 'https://api.deepl.com/v2/translate'
	
	    def __init__(self):
	        pass
	    def translate_string(self, text, target_language, source_language='en', handle_xml=False):
	        print('[INFO][PAID] Doing deepl request')
	        conf = {
	            'auth_key': settings.DEEPL_TOKEN,
	            'text': text,
	            'source_lang': source_language.upper(),
	            'target_lang': target_language.upper(),
	        }
	        if handle_xml:
	            conf['tag_handling'] = 'xml'
	        resp = requests.get(self.BASE_URL, data = conf)
	        print("TRANSLATION", resp.text, resp.status_code)
	        text = json.loads(resp.text)['translations'][0]['text']
	        return text
	    def translate_strings(self, strings, target_language, source_language='en', optimized=True):
	        result = []
	        for s in strings:
	            text = self.translate_string(s, target_language, source_language)
	            result.append(text)
	        
	        return tuple(result)
Step 5 – Compile .po into binary .mo used by Django
pipenv run django-admin compilemessages
Step 6 – Activate the translation somehow
There are lot's of internal Django toolings to activate translations. For example by using sub-folder-based URLs parser like example.com/ja or subdomain-based like ja.example.com. Or depending on user's browser preference.

Here I will share the most flexible custom way.

Just create middleware and depending on any info from request (hostname/url/Geolocated IP) we can just call one function:

from django.utils.translation import activate
...
activate('ja')
Image for a hint

#Django

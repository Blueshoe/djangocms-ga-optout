# djangoCMS Opt-Out for Google Analytics
A djangoCMS Plugin that creates an Opt-Out link for Google Analytics.

## Installation
- Add `djangocms_ga_optout` to installed apps
- Run `python manage.py migrate djangocms_ga_optout`
- Add the string setting `GOOGLE_ANALYTICS_ID` to your settings file
- Load the plugins template tags in your `base.html`: `{% load djangocms_ga_optout %}`
- Include the opt-out JavaScript snippet **before** the normal Google Analytics snippet via the following template tag: `{% google_analytics_optout_js %}`

## Usage
- Add the CMS plugin 'Google Analytics Opt Out' to your privacy statement (tip: you can use the plugin from within the text editor).
- When the user clicks on the given link, no tracking events will be sent to Google Analytics (the opt-out is stored in a cookie, so when the user clears his cookies, GA tracking will enabled again).

## Troubleshooting
Error: `'djangocms_ga_optout' is not a valid tag library:`
Add the following to the TEMPLATE_LOADERS settings: `django.template.loaders.app_directories.load_template_source`


## Contributing
You're welcome to submit Pull Requests! :rocket:
Just take a look at the open issues.
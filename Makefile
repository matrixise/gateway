.PHONY: clean-pyc test docs docs-pdf
all: clean-pyc clean-tox test

test:
	python setup.py nosetests -s

tox-text:
	PYTHONDONTWRITEBYTECODE=tox

clean: clean-pyc clean-tox clean-doc
	rm -rf *.egg-info
	rm -rf dist

clean-pyc:
	find . -name "*.pyc" -or -name "*.pyo" -or -name "*~" | xargs rm -f

clean-tox:
	rm -rf .tox

clean-doc:
	rm -rf docs/_build	

i18n-extract:
	pybabel extract -F gateway/config/babel.cfg -k lazy_gettext -o gateway/translations/gateway.pot .

i18n-init: i18n-extract
	# example: ISO_CODE = fr_BE
	# pybabel init -i gateway/translations/gateway.pot -d gateway/translations -l ISO_CODE

i18n-update: i18n-extract
	pybabel update -i gateway/translations/gateway.pot -d gateway/translations

i18n-compile: 
	pybabel compile -d gateway/translations

docs:
	$(MAKE) -C docs html dirhtml latexpdf epub

docs-pdf:
	$(MAKE) -C docs latexpdf

upload-docs:
	$(MAKE) -C docs html dirhtml latex epub
	$(MAKE) -C docs/_build/latex all-pdf

	cd docs/_build/; mv html gateway-docs; zip -r gateway-docs.zip gateway-docs; mv gateway-docs html
	rsync -a docs/_build/dirhtml/ wirtel.be:/var/www/gateway.wirtel.be/docs/
	rsync -a docs/_build/latex/Flask.pdf wirtel.be:/var/www/gateway.wirtel.be/docs/gateway-docs.pdf
	rsync -a docs/_build/gateway-docs.zip wirtel.be:/var/www/gateway.wirtel.be/docs/gateway-docs.zip
	rsync -a docs/_build/epub/Flask.epub wirtel.be:/var/www/gateway.wirtel.be/docs/gateway-docs.epub

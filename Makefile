test:
	tox

docs:
	scripts/doc-build

rpm:
	git archive --output=oauth2client-rpm-src.tar.gz --prefix=oauth2client/ HEAD
	rpmbuild -bb oauth2client.spec \
		--define '_sourcedir $(shell pwd)' \
		--define 'major_version $(shell git describe --abbrev=0 | cut -c2-)' \
		--define 'minor_version $(subst -,.,$(shell git describe --long | cut -f2- -d-))'
	$(RM) oauth2client-rpm-src.tar.gz

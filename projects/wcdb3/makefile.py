all:
	make WCDB3.zip

clean:
	rm -f WCDB3.log
	rm -f WCDB3.zip
	rm -f *.pyc
	rm -rf html

turnin-list:
	turnin --list bendy cs373pj5

turnin-submit: WCDB3.zip
	turnin --submit bendy cs373pj5 WCDB3.zip

turnin-verify:
	turnin --verify bendy cs373pj5

# add other .py files

WCDB3.html: WCDB3.py
	pydoc -w WCDB3

WCDB3.log:
	git log > WCDB3.log

# add other .html and .py files

WCDB3.zip:            WCDB3.html WCDB3.log WCDB3.pdf WCDB3.py TestWCDB3.py
	zip -r WCDB3.zip  WCDB3.html WCDB3.log WCDB3.pdf WCDB3.py TestWCDB3.py

all:
	make Collatz.zip

clean:
	rm -f Collatz.html
	rm -f Collatz.log
	rm -f Collatz.zip
	rm -f *.pyc
	rm -f *.tmp

diff: RunCollatz.in RunCollatz.out RunCollatz.py
	RunCollatz.py < RunCollatz.in > RunCollatz.tmp
	diff RunCollatz.out RunCollatz.tmp
	rm RunCollatz.tmp

turnin-list:
	turnin --list bendy cs373pj1

turnin-submit: Collatz.zip
	turnin --submit bendy cs373pj1 Collatz.zip

turnin-verify:
	turnin --verify bendy cs373pj1

Collatz.html: Collatz.py
	pydoc -w Collatz

Collatz.log:
	git log > Collatz.log

Collatz.zip: Collatz.html Collatz.log Collatz.py        \
             RunCollatz.in RunCollatz.out RunCollatz.py \
             SphereCollatz.py                           \
             TestCollatz.py TestCollatz.out
	zip -r Collatz.zip                                \
           Collatz.html Collatz.log Collatz.py        \
           RunCollatz.in RunCollatz.out RunCollatz.py \
           SphereCollatz.py                           \
           TestCollatz.py TestCollatz.out

RunCollatz.out: RunCollatz.in RunCollatz.py
	RunCollatz.py < RunCollatz.in > RunCollatz.out

TestCollatz.out: TestCollatz.py
	TestCollatz.py > TestCollatz.out

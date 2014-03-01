INCODE?=oem.txt
RM?=rm -f

all: btkeytab.h

btkeytab.h: mkbtkeytab.py $(MAKEFILE_LIST)
	./$< <$(INCODE) >$@

.PHONY: clean
clean:
	$(RM) btkeytab.h

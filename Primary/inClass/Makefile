
#define the suffixes
.SUFFIXES:	.tex

#macro definitions
SHELL = /bin/sh
LATEX = pdflatex

.tex.aux:	
	$(LATEX) $<


LATEXFILES = 

all:	labManual.pdf

labManual.pdf: labManual.tex *.tex */*.tex
	$(LATEX) labManual

force:
	$(LATEX) labManual

view:	labManual.pdf
	/usr/bin/okular labManual.pdf &

testing.pdf:
	$(LATEX) testing

clean:
	rm -f *.aux *.nav *.snm *.toc *.log *.dvi *.out *~ functions/*.aux functions/*~ exponentials/*.aux exponentials/*~ trig/*.aux trig/*~ angles/*~ angles/*.aux



#define the suffixes
.SUFFIXES:	.tex

#macro definitions
SHELL = /bin/sh
LATEX = pdflatex

.tex.aux:	
	$(LATEX) $<


all:	labManual.pdf

labManual.pdf: labManual.tex *.tex
	$(LATEX) labManual

force:
	$(LATEX) labManual

view:	labManual.pdf
	/usr/bin/okular labManual.pdf &


clean:
	rm -f *.aux *.nav *.snm *.toc *.log *.dvi *.out *~ functions/*.aux functions/*~ exponentials/*.aux exponentials/*~ trig/*.aux trig/*~ angles/*~ angles/*.aux


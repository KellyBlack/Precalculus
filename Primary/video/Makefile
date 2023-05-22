
#define the suffixes
.SUFFIXES:	.tex

#macro definitions
SHELL = /bin/sh
LATEX = pdflatex

.tex.aux:	
	$(LATEX) $<


LATEXFILES = 

all:	videoManual.pdf

videoManual.pdf: videoManual.tex *.tex 
	$(LATEX) videoManual

force:
	$(LATEX) videoManual

view:	videoManual.pdf
	/usr/bin/okular videoManual.pdf &

testing.pdf:
	$(LATEX) testing

clean:
	rm -f *.aux *.nav *.snm *.toc *.log *.dvi *.out *~ 


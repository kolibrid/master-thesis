# LaTeX Makefile

FILENAME=main
PAPER=${FILENAME}.tex  # set the path to your TeX file here
SHELL=/bin/zsh   # for the while loop below

all:  ## Compile paper
	pdflatex $(PAPER)

clean:  ## Clean output files
	rm -f ${FILENAME}.{ps,log,aux,out,dvi,bbl,blg,toc,def}
	rm ${FILENAME}-blx.bib

bib:
	bibtex ${FILNAME}

watch:  ## Recompile on updates to the source file
	@while [ 1 ]; do; inotifywait $(PAPER); sleep 0.01; make all; done
	# for Bash users, replace the while loop with the following
	# @while true; do; inotifywait $(PAPER); sleep 0.01; make all; done

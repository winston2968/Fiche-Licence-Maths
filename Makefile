PDFLATEX = pdflatex
MAIN = main

compile: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex
	$(PDFLATEX) $(MAIN).tex
	$(PDFLATEX) $(MAIN).tex  # Deux fois pour bien générer les références

clean:
	rm -f $(MAIN).aux $(MAIN).log $(MAIN).out $(MAIN).toc $(MAIN).lof $(MAIN).lot $(MAIN).bbl $(MAIN).blg $(MAIN).maf $(MAIN).mtc* $(MAIN).thm $(MAIN).synctex.gz

cleanall: clean
	rm -f $(MAIN).pdf

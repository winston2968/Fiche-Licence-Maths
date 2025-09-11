# Configuration
LATEXMK = latexmk
MAIN = main

# Règle par défaut : génère le fichier PDF
compile: $(MAIN).pdf

# Compilation avec latexmk
$(MAIN).pdf: $(MAIN).tex
	$(LATEXMK) -pdf $(MAIN).tex  # Compile en PDF

# Nettoyage des fichiers temporaires générés par la compilation
clean:
	rm -f $(MAIN).aux $(MAIN).log $(MAIN).out $(MAIN).toc $(MAIN).lof $(MAIN).lot $(MAIN).bbl $(MAIN).blg $(MAIN).maf $(MAIN).mtc* $(MAIN).thm $(MAIN).synctex.gz $(MAIN).ptc* $(MAIN).fdb_latexmk $(MAIN).fls 

# Nettoyage complet : enlève le PDF et les fichiers temporaires
cleanall: clean
	rm -f $(MAIN).pdf

# Si tu veux utiliser latexmk en mode "continu" (pour recompiler automatiquement en cas de modification)
watch:
	$(LATEXMK) -pdf -pvc $(MAIN).tex

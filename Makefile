# Define tools 
PYTHON := python3 
LATEX := pdflatex 
TARGET := main_build.tex
FOLDER := build
SCRIPT := pybuild.py 

# Main rule 
all: run_python compile_latex

# Exec python script
pre_compile:
	$(PYTHON) $(SCRIPT)

# Compile latex file after python script
compile:
	cd $(FOLDER) && $(LATEX) $(TARGET)

# Double build for contents 
doucle_compile:
	cd $(FOLDER) && $(LATEX) $(TARGET) && $(LATEX) $(TARGET)

# Cleaning files 
clean:
	rm -f $(TARGET).aux $(TARGET).log $(TARGET).bbl $(TARGET).blg $(TARGET).out $(TARGET).toc
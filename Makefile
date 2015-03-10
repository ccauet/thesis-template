MAIN = main

LATEX = lualatex

FIGEXT = .pdf
MAINEXT= .pdf
BUILDCOMMAND=rm -f $(MAIN).aux && $(LATEX) $(MAIN) && biber $(MAIN) && $(LATEX) $(MAIN) && $(LATEX) $(MAIN)


# list of all source files
TEXSOURCES = $(wildcard *.tex) $(wildcard *.bib)
FIGSOURCES = $(wildcard figs/*$(FIGEXT))
SOURCES    = $(TEXSOURCES) $(FIGSOURCES)

# define output (could be making .ps instead)
OUTPUT = $(MAIN)$(MAINEXT)

# prescription how to make output (your favorite commands to process latex)
# do latex twice to make sure that all cross-references are updated 
$(OUTPUT): $(SOURCES) Makefile
	$(BUILDCOMMAND)

# just so we can say "make all" without knowing the output name
all: $(OUTPUT)

# remove temporary files (good idea to say "make clean" before putting things back into repository)
.PHONY : clean
clean:
	rm -f *~ *.aux *.log *.bbl *.blg *.dvi *.tmp *.out *.blg *.bbl *.fdb_latexmk *.fls *.idx *.ilg *.ind *.tdo *.toc *.bcf *.run.xml $(MAIN)$(MAINEXT) $(MAIN).ps

# remove output file
rmout: 
	rm  $(OUTPUT)

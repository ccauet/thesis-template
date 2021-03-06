MAIN = main

LATEX = lualatex
LATEX_OPTS=--shell-escape --interaction=batchmode
LATEX_PREFINAL_OPTS=--draftmode 
FIGEXT = .pdf
MAINEXT= .pdf
NUM_THREADS=8
BUILDCOMMAND=rm -f $(MAIN).aux && $(LATEX) $(LATEX_PREFINAL_OPTS) $(LATEX_OPTS) $(MAIN) && if [ -f "main.makefile" ]; then make -j $(NUM_THREADS) -f main.makefile; fi && biber $(MAIN) && $(LATEX) $(LATEX_PREFINAL_OPTS) $(LATEX_OPTS) $(MAIN) && $(LATEX) $(LATEX_OPTS) $(MAIN)

# list of all source files
TEXSOURCES = $(shell find common -type f -name "*.tex") $(shell find -L private -type f -name "*.tex") $(shell find common -type f -name "*.bib") $(shell find -L private -type f -name "*.bib")
FIGSOURCES = $(wildcard figs/*$(FIGEXT))
SOURCES    = $(TEXSOURCES) $(FIGSOURCES)

# define output (could be making .ps instead)
OUTPUT = $(MAIN)$(MAINEXT)

# prescription how to make output (your favorite commands to process latex)
# do latex twice to make sure that all cross-references are updated 
$(OUTPUT): $(SOURCES) Makefile
	$(BUILDCOMMAND) || ( $(LATEX) $(MAIN) && biber $(MAIN) )

# just so we can say "make all" without knowing the output name
all: $(OUTPUT)

# remove temporary files (good idea to say "make clean" before putting things back into repository)
.PHONY : clean
clean:
	./cleanup.sh
	rm -f $(MAIN)$(MAINEXT) $(MAIN).ps

# non-silent lualatex run for warnings etc.
loud:
	$(LATEX) $(MAIN)

# prettify all plots
prettify:
	common/scripts/prettify_all.py && common/scripts/prettify_all.py && common/scripts/prettify_all.py && common/scripts/prettify_all.py

# remove output file
rmout: 
	rm  $(OUTPUT)

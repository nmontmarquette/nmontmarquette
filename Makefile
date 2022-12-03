GENERATED_DIR=generator

.PHONY : all
all : $(GENERATED_DIR)/project_list.md

# Using Python tests as current way to generate files
$(GENERATED_DIR)/project_list.md: fr_ca/projects.xml
	@make spellcheck
	@./generate_project_summaries --input_data_file $<

.PHONY: spellcheck
spellcheck:
	@echo "Checking spelling..."
	@if [ $$(cat fr_ca/projects.xml | aspell --lang fr --personal=./aspell.fr_CA.pws --repl=./aspell.fr_CA.prepl --add-filter sgml list | wc -l) -ne 0 ]; then \
		cat fr_ca/projects.xml | aspell --lang fr --personal=./aspell.fr_CA.pws --repl=./aspell.fr_CA.prepl --add-filter sgml list \
		echo "Found one of more spelling mistakes."; \
		exit 1; \
	fi;\

.PHONY: clean
clean:
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -delete
	@rm -f    generated/*.md

.PHONY: test
test: spellcheck
	python3 -m unittest --verbose generator.tests.test_xml
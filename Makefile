GENERATED_DIR=generator

.PHONY : all
all : project_pages \
	$(GENERATED_DIR)/project_list.md \
	$(GENERATED_DIR)/project_summary.md \
	$(GENERATED_DIR)/projects_summary_3_cols.md \
	$(GENERATED_DIR)/projects_summary_3_cols_with_details.md

$(GENERATED_DIR)/projects_summary_3_cols.md: fr_ca/projects.xml
	@make spellcheck-ni
	@echo "Regenerating '$@' ..."
	@./generate_project_summaries --three_cols --input_data_file $< --output_file projects_summary_3_cols.md

$(GENERATED_DIR)/projects_summary_3_cols_with_details.md: fr_ca/projects.xml
	@make spellcheck-ni
	@echo "Regenerating '$@' ..."
	@./generate_project_summaries --three_cols --details --input_data_file $< --output_file projects_summary_3_cols_with_details.md

$(GENERATED_DIR)/project_summary.md: fr_ca/projects.xml
	@make spellcheck-ni
	@echo "Regenerating '$@' ..."
	@./generate_project_summaries --input_data_file $< --output_file project_summary.md

$(GENERATED_DIR)/project_list.md: fr_ca/projects.xml
	@make spellcheck-ni
	@echo "Regenerating '$@' ..."
	@./generate_project_list --input_data_file $<

.PHONY : project_pages
project_pages: fr_ca/projects.xml
	@make spellcheck-ni
	@echo "Regenerating pages ..."
	@./generate_project_pages --input_data_file $< --output_dir fr_ca --details

# Interractive spellcheck
.PHONY: spellcheck
spellcheck:
	aspell --lang fr --personal=./aspell.fr_CA.pws --repl=./aspell.fr_CA.prepl --add-filter sgml check fr_ca/projects.xml

# Non-interractive spellchecker
.PHONY: spellcheck-ni
spellcheck-ni:
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
test: spellcheck-ni
	python3 -m unittest --verbose generator.tests.test_xml
import nbformat

# Lista de notebooks que serão mesclados
notebooks = ["Notebooks/Dataset_Crise.ipynb", "Notebooks/Analise-Covid.ipynb"]
output_notebook = "notebook_final.ipynb"

# Criar um novo notebook vazio
merged_notebook = nbformat.v4.new_notebook()

for nb_file in notebooks:
    with open(nb_file, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
        merged_notebook.cells.extend(nb.cells)  # Adicionar células ao notebook final

# Salvar o notebook mesclado
with open(output_notebook, "w", encoding="utf-8") as f:
    nbformat.write(merged_notebook, f)

print(f"Notebooks combinados com sucesso em {output_notebook}")

from pathlib import Path

def listar_diretorio(caminho, nivel=0):
    root = Path(caminho)
    indent = "│   " * (nivel) + "├── "
    
    try:
        for item in sorted(root.iterdir()):
            if item.is_dir():
                print(f"{indent}{item.name}/")
                listar_diretorio(item, nivel + 1)
            else:
                print(f"{indent}{item.name}")
    except PermissionError:
        print(f"{indent} [permissão negada]")
import os

def collect_source_files(root_dir: str, extensions=None, skip_dirs=None):
    if extensions is None:
        extensions = {'.py', '.js', '.ts', '.java', '.c', '.cpp', '.cs', '.go', '.rs'}
    if skip_dirs is None:
        skip_dirs = {'.git', '.github', 'node_modules', '__pycache__', '.venv'}

    source_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Modify dirnames in-place to skip certain folders
        dirnames[:] = [d for d in dirnames if d not in skip_dirs]
        for file in filenames:
            if any(file.endswith(ext) for ext in extensions):
                full_path = os.path.join(dirpath, file)
                source_files.append(full_path)
    return source_files

def read_files(file_paths: list[str]) -> list[dict]:
    """Read file content into a list of dicts with path and code."""
    contents = []
    for path in file_paths:
        with open(path, 'r', encoding='utf-8') as f:
            contents.append({'path': path, 'code': f.read()})
    return contents
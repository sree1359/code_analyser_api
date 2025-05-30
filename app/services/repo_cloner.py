import os, shutil, subprocess, stat

def handle_remove_readonly(func, path, _):
    os.chmod(path, stat.S_IWRITE)
    func(path)

def clone_repo(git_url: str) -> str:
    temp_dir = "S:/code_analyser_temp"
    os.makedirs(temp_dir, exist_ok=True)
    for item in os.listdir(temp_dir):
        path = os.path.join(temp_dir, item)
        try:
            if os.path.isdir(path):
                shutil.rmtree(path, onerror=handle_remove_readonly)
            else:
                os.remove(path)
        except Exception as e:
            print(f"[⚠️] Skipped '{path}': {e}")
    subprocess.run(["git", "clone", git_url, temp_dir], check=True)
    return temp_dir
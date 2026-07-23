import subprocess

def update_config():
    # run generate_nav.py
    nav_yaml = subprocess.check_output(["python", "scripts/generate_nav.py"], text=True)
    
    with open("mkdocs.yml", "r", encoding="utf-8") as f:
        config = f.read()
        
    # Find where nav: starts
    nav_idx = config.find("\nnav:\n")
    if nav_idx == -1:
        # Maybe it's at the start of the file or doesn't exist
        nav_idx = config.find("nav:\n")
        if nav_idx == -1:
            base_config = config + "\n"
        else:
            base_config = config[:nav_idx]
    else:
        base_config = config[:nav_idx + 1]
        
    new_config = base_config + nav_yaml
    
    with open("mkdocs.yml", "w", encoding="utf-8") as f:
        f.write(new_config)
        
    print("mkdocs.yml updated successfully.")

if __name__ == "__main__":
    update_config()

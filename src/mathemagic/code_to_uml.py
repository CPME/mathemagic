import os
import subprocess
from pathlib import Path

def generate_uml_diagram():
    """
    Generate a UML class diagram in Mermaid format from the codebase using pyreverse.
    """
    # Get the project root directory
    current_dir = Path(__file__).parent
    project_root = current_dir.parent.parent
    
    # Create output directory if it doesn't exist
    output_dir = project_root
    os.makedirs(output_dir, exist_ok=True)
    
    # Run pyreverse to generate dot files
    subprocess.run([
        "pyreverse", 
        "-o", "dot",
        "-p", "mathemagic",
        str(current_dir)
    ], check=True)
    
    # Convert dot file to mermaid format
    dot_file = "classes_mathemagic.dot"
    mermaid_file = output_dir / "mathemagic.mmd"
    
    if not os.path.exists(dot_file):
        raise FileNotFoundError(f"Dot file not found: {dot_file}")
    
    # Parse dot file and convert to mermaid format
    with open(dot_file, 'r') as f:
        dot_content = f.read()
    
    # Basic conversion from dot to mermaid
    mermaid_content = "classDiagram\n"
    
    # Extract class definitions
    import re
    
    # Extract nodes (classes)
    node_pattern = r'"([^"]+)" \[label="{([^}]+)}"'
    nodes = re.findall(node_pattern, dot_content)
    
    for node_id, label in nodes:
        # Process label to extract class name and members
        parts = label.split('|')
        class_name = parts[0].strip()
        
        mermaid_content += f"    class {class_name}\n"
        
        # Add methods and attributes if available
        if len(parts) > 1:
            attributes = parts[1].split('\\l')
            for attr in attributes:
                attr = attr.strip()
                if attr:
                    mermaid_content += f"    {class_name} : {attr}\n"
                    
        if len(parts) > 2:
            methods = parts[2].split('\\l')
            for method in methods:
                method = method.strip()
                if method:
                    mermaid_content += f"    {class_name} : {method}()\n"
    
    # Extract relationships
    edge_pattern = r'"([^"]+)" -> "([^"]+)" \[.*label="([^"]*)"'
    edges = re.findall(edge_pattern, dot_content)
    
    for source, target, label in edges:
        # Find class names from node IDs
        source_class = next((name for id, name in nodes if id == source), source)
        source_class = source_class.split('|')[0].strip()
        
        target_class = next((name for id, name in nodes if id == target), target)
        target_class = target_class.split('|')[0].strip()
        
        if "inherit" in label.lower():
            mermaid_content += f"    {target_class} <|-- {source_class}\n"
        else:
            mermaid_content += f"    {source_class} --> {target_class}\n"
    
    # Write mermaid content to file
    with open(mermaid_file, 'w') as f:
        f.write(mermaid_content)
    
    # Clean up dot files
    os.remove(dot_file)
    os.remove("packages_mathemagic.dot")
    
    print(f"UML diagram generated: {mermaid_file}")

if __name__ == "__main__":
    generate_uml_diagram()

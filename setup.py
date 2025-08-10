from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """Read requirements from file, excluding editable installs and comments."""
    requirements = []
    
    try:
        with open(file_path, 'r') as file_obj:
            for line in file_obj:
                req = line.strip()  # Remove all whitespace
                
                # Skip empty lines, comments, and any line containing '-e'
                if req and not req.startswith('#') and '-e' not in req:
                    requirements.append(req)
                    
    except FileNotFoundError:
        print(f"Warning: {file_path} not found")
        return []
    
    return requirements

setup(
    name='end_to_end_project',
    version='0.0.1',
    author='Ranjan Vernekar',
    author_email='ranjanvernekar45@gmail.com',
    description='An end to end project for data analysis and machine learning',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

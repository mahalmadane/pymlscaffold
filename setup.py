from setuptools import setup, find_packages

setup(
    name='PyMLScaffold',  # Nom de ton package
    version='0.1',
    packages=find_packages(),  # Trouve tous les sous-packages
    install_requires=[],  # Ajouter ici les dépendances nécessaires
    description="Une bibliothèque pour générer des structures de projet ML prêtes à l'emploi",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Ton Nom",
    author_email="touremahalmadane250@gmail.com",
    url="https://github.com/mahalmadane",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

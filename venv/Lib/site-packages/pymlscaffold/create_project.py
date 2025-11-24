import os

def create_project_structure(project_name):
    # Définir la structure des dossiers
    structure = {
        "__init__.py": "",
        "README.md": "# " + project_name + "\n\nExplication du projet.",
        "requirements.txt": "# Liste des dépendances",
        "setup.py": """# setup.py
from setuptools import setup, find_packages

setup(
    name='{}',
    version='0.1',
    packages=find_packages(),
    install_requires=[]  # Ajoutez les dépendances ici
)
""".format(project_name),
        ".gitignore": """# Fichiers à ignorer par Git
*.pyc
__pycache__/
*.log
*.csv
*.sqlite
""",
        "data/raw": [],
        "data/interim": [],
        "data/processed": [],
        "notebooks": [
            "01_exploration.ipynb",
            "02_preprocessing.ipynb",
            "03_model_training.ipynb"
        ],
        "src": {
            "__init__.py": "",
            "data": {
                "load_data.py": "# Code pour charger les données",
                "preprocess.py": "# Code pour prétraiter ,les données",
                "strategie_univarie.py": "# Stratégie univariée de traitement des données",
                "strategie_multivarie.py": "# Stratégie multivariée de traitement des données",
                "strategie_bivarie.py": "# Stratégie bivariée de traitement des données"
            },
            "features": {
                "__init__.py": "",
                "build_features.py": "# Code pour l'ingénierie des features"
            },
            "models": {
                "__init__.py": "",
                "train_model.py": "# Code pour entraîner le modèle",
                "evaluate.py": "# Code pour évaluer le modèle",
                "predict.py": "# Code pour faire des prédictions"
            },
            "utils": {
                "__init__.py": "",
                "helpers.py": "# Fonctions utilitaires"
            },
            "pipelines": {
                "__init__.py": "",
                "steps": {
                    "__init__.py": "",
                    "function_load_step.py": "# Étape pour charger les données",
                    "function_train_step.py": "# Étape pour entraîner le modèle",
                    "function_eval_step.py": "# Étape pour évaluer le modèle",
                    "function_predict_step.py": "# Étape pour faire des prédictions",
                    "function_outlier_step.py": "# Étape pour détecter les valeurs aberrantes",
                    "function_missing_step.py": "# Étape pour gérer les valeurs manquantes",
                    "function_scaling_step.py": "# Étape pour normaliser/standardiser les données"
                },
                "preprocessing_steps": {
                    "__init__.py": "",
                    "class_missing_step.py": "# Étape pour gérer les valeurs manquantes",
                    "class_outlier_step.py": "# Étape pour détecter les valeurs aberrantes",
                    "class_scaling_step.py": "# Étape pour normaliser/standardiser les données"
                }
            }
        },
        "tests": [
            "__init__.py",
            "test_data.py",
            "test_model.py"
        ],
        "reports": {
            "figures": [],
            "metrics.json": "{}"
        },
        "configs": {
            "config.yaml": "# Fichier de configuration générale",
            "model_params.yaml": "# Hyperparamètres du modèle",
            "pipeline_config.yaml": "# Configurations pour ZenML/MLflow"
        },
        "api": {
            "__init__.py": "",
            "api.py": "# Code de l'API"
        },
        "scripts": [
            "run_pipeline.py",
            "train_local.py",
            "deploy_model.py"
        ]
    }

    # Fonction récursive pour créer les dossiers et fichiers
    def create_files_and_folders(base_path, structure):
        for name, value in structure.items():
            path = os.path.join(base_path, name)
            if isinstance(value, dict):
                # Créer un dossier et appeler la fonction récursivement
                os.makedirs(path, exist_ok=True)
                create_files_and_folders(path, value)
            elif isinstance(value, list):
                # Créer les fichiers dans le dossier
                os.makedirs(path, exist_ok=True)
                for file_name in value:
                    with open(os.path.join(path, file_name), 'w') as f:
                        f.write("# " + file_name)
            else:
                # Créer un fichier avec le contenu spécifié
                with open(path, 'w') as f:
                    f.write(value)
    
    # Créer le projet à la racine
    os.makedirs(project_name, exist_ok=True)
    create_files_and_folders(project_name, structure)
    print(f"Le projet {project_name} a été créé avec succès !")

# Exemple d'utilisation
create_project_structure("my_ml_project")

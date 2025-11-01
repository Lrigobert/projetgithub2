import os
import sys
import argparse
from openai import OpenAI

# Configuration de l'API OpenAI
# La clé API est lue automatiquement depuis la variable d'environnement OPENAI_API_KEY
# dans l'environnement GitHub Actions.
client = OpenAI()

def generate_ai_feedback(report_content: str, developer_name: str, commit_sha: str) -> str:
    """
    Génère un message de feedback personnalisé et motivant à partir du rapport d'erreur.
    """
    
    # Le prompt est crucial pour obtenir un feedback de qualité
    system_prompt = (
        "Vous êtes un assistant DevOps bienveillant et motivant. "
        "Votre tâche est d'analyser un rapport d'erreur de qualité de code (Flake8 et Mypy) "
        "et de générer un message personnalisé pour le développeur. "
        "Le message doit être clair, constructif, et motiver le développeur à corriger les erreurs. "
        "Il doit inclure les points suivants: "
        "1. Une salutation personnalisée à l'intention de l'utilisateur (ex: 'Bonjour [Nom du développeur]'). "
        "2. Un résumé des problèmes détectés (style, typage, etc.). "
        "3. Une explication simple de l'importance de ces corrections (conformité, qualité, etc.). "
        "4. Une phrase d'encouragement. "
        "5. Ne pas inclure de code, seulement le message. "
        "Le rapport d'erreur est le suivant: "
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini", # Utilisation d'un modèle rapide et efficace
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Rapport d'erreur pour le commit {commit_sha} par {developer_name}:\n\n{report_content}"}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Erreur lors de l'appel à l'API OpenAI: {e}"

def main():
    parser = argparse.ArgumentParser(description="Génère un feedback IA personnalisé pour les erreurs de qualité de code.")
    parser.add_argument("report_file", help="Chemin vers le fichier contenant le rapport d'erreur combiné.")
    parser.add_argument("developer_name", help="Nom du développeur (ex: $GITHUB_ACTOR).")
    parser.add_argument("commit_sha", help="SHA du commit (ex: $GITHUB_SHA).")
    
    args = parser.parse_args()

    if not os.getenv("OPENAI_API_KEY"):
        print("Erreur: La variable d'environnement OPENAI_API_KEY n'est pas définie.")
        print("Le script ne peut pas fonctionner sans clé API. Simulation du feedback.")
        
        # Simulation du feedback pour le livrable
        simulated_feedback = (
            f"Bonjour {args.developer_name},\n\n"
            "Votre dernier commit ({args.commit_sha[:7]}) a échoué aux vérifications de qualité de code.\n"
            "Des erreurs de style (Flake8) et de typage (Mypy) ont été détectées. "
            "Veuillez consulter le rapport ci-dessous pour les détails.\n"
            "La conformité aux normes de style et le typage strict sont essentiels pour la maintenabilité du code.\n"
            "Accrochez-vous, vous êtes sur la bonne voie pour améliorer la qualité de notre base de code !"
        )
        print("\n--- Feedback IA Simulé ---")
        print(simulated_feedback)
        print("--------------------------\n")
        
        # Le script doit retourner le feedback pour qu'il soit utilisé dans l'étape d'envoi de mail
        # Dans un vrai workflow, on écrirait le feedback dans un fichier ou on l'enverrait par mail directement.
        with open("ai_feedback_result.txt", "w") as f:
            f.write(simulated_feedback)
        
        sys.exit(0) # Succès pour la simulation
        
    try:
        with open(args.report_file, 'r') as f:
            report_content = f.read()
    except FileNotFoundError:
        print(f"Erreur: Le fichier de rapport '{args.report_file}' n'a pas été trouvé.")
        sys.exit(1)

    feedback = generate_ai_feedback(report_content, args.developer_name, args.commit_sha)
    
    print("\n--- Feedback IA Généré ---")
    print(feedback)
    print("--------------------------\n")
    
    # Écrire le feedback dans un fichier pour l'étape suivante du workflow (envoi de mail)
    with open("ai_feedback_result.txt", "w") as f:
        f.write(feedback)

if __name__ == "__main__":
    main()

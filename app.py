from flask import Flask, render_template, request, jsonify
import pandas as pd
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

# Créer le dossier uploads s'il n'existe pas
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'xlsx', 'xls'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def parse_note(value):
    """Convertir une note en float pour le tri"""
    if pd.isna(value):
        return None
    value = str(value).strip()
    # Remplacer les virgules par des points
    value = value.replace(',', '.').replace(' ', '')
    try:
        return float(value)
    except ValueError:
        return None

def process_excel(filepath):
    """Traiter le fichier Excel et retourner les données formatées"""
    df = pd.read_excel(filepath)

    # Renommer les colonnes pour simplifier
    column_mapping = {
        'Nom': 'nom',
        'Prénom': 'prenom',
        'Pseudo': 'pseudo',
        'Email': 'email',
        'Quelle note avez vous obtenue en UE 1': 'ue1',
        'Quelle note avez vous obtenue en UE 2': 'ue2',
        'Quelle note avez vous obtenue en UE 3.1': 'ue3',
        'Quelle note avez vous obtenue en UE 4': 'ue4',
        'Quel est votre rang général': 'rang'
    }

    # Trouver les colonnes correspondantes (recherche partielle)
    rename_dict = {}
    for col in df.columns:
        for key, value in column_mapping.items():
            if key.lower() in col.lower():
                rename_dict[col] = value
                break

    df = df.rename(columns=rename_dict)

    # Sélectionner les colonnes pertinentes
    columns_to_keep = ['nom', 'prenom', 'pseudo', 'email', 'ue1', 'ue2', 'ue3', 'ue4', 'rang']
    available_columns = [col for col in columns_to_keep if col in df.columns]
    df = df[available_columns]

    # Ajouter des colonnes numériques pour le tri
    for col in ['ue1', 'ue2', 'ue3', 'ue4']:
        if col in df.columns:
            df[f'{col}_num'] = df[col].apply(parse_note)

    # Calculer la moyenne si toutes les UE sont présentes
    ue_cols = ['ue1_num', 'ue2_num', 'ue3_num', 'ue4_num']
    if all(col in df.columns for col in ue_cols):
        df['moyenne'] = df[ue_cols].mean(axis=1, skipna=True)

    return df

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Aucun fichier sélectionné'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'Aucun fichier sélectionné'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            df = process_excel(filepath)
            # Convertir en liste de dictionnaires pour JSON
            data = df.to_dict(orient='records')
            # Remplacer NaN par None pour JSON
            for row in data:
                for key, value in row.items():
                    if pd.isna(value):
                        row[key] = None
            return jsonify({'success': True, 'data': data})
        except Exception as e:
            return jsonify({'error': f'Erreur lors du traitement: {str(e)}'}), 400

    return jsonify({'error': 'Type de fichier non autorisé. Utilisez .xlsx ou .xls'}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

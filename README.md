# LogAnalyzer Pro++ 🚀  **Analyse de logs haute performance / High-performance log analysis**

---

## 🇫🇷 Français <a name="fr"></a>

**Navigation :** [Description](#desc-fr) | [Fonctionnalités](#features-fr) | [Utilisation](#use-fr) | [Paramètres](#params-fr) | [Exemples](#examples-fr) | [🇬🇧 English](#en)

---

### 📦 **Description** <a name="desc-fr"></a>

[↑ Retour au menu](#fr)

Outil d'analyse de logs pour DevOps et ingénieurs data :

-   🕵️ Détection intelligente d'erreurs
-   📊 Export JSON structuré
-   🚀 Optimisé pour fichiers >100GB

---

### 🛠️ **Fonctionnalités** <a name="features-fr"></a>

[↑ Retour au menu](#fr) | [Exemples](#examples-fr)

-   Comptage par code erreur/catégorie
-   Récupération de 3 exemples de messages par type
-   Filtrage dynamique (ERROR/WARNING/INFO/DEBUG)

---

### 🚀 **Utilisation** <a name="use-fr"></a>

[↑ Retour au menu](#fr)

```bash
python log_analyzer.py \\
  --input /var/logs/app.log \\
  --output rapport.json \\
  --log-level ERROR
```

---

### ⚙️ **Paramètres** <a name="params-fr"></a>

[↑ Retour au menu](#fr)

| Option | Description | Valeurs |
| :---------- | :-------------------------------- | :------------------------------- |
| `--input` | Chemin du fichier de logs | Fichier `.log` ou `.txt` |
| `--output` | Nom du fichier de sortie | Fichier `.json` |
| `--log-level` | Niveau de log à analyser | `ERROR`, `WARNING`, `INFO`, `DEBUG` |

---

### 📝 **Exemple de Sortie** <a name="examples-fr"></a>

[↑ Retour au menu](#fr)

```json
{
  "log_level": "ERROR",
  "entries": {
    "404": {
      "count": 12,
      "examples": [
        "ERROR: File not found [CODE: 404]",
        "ERROR: User profile missing [CODE: 404]",
        "ERROR: GET /nonexistent_page HTTP/1.1 [CODE: 404]"
      ]
    },
    "500": {
      "count": 5,
      "examples": [
        "ERROR: Internal Server Error [CODE: 500]",
        "ERROR: Database connection timeout [CODE: 500]",
        "ERROR: Unhandled exception [CODE: 500]"
      ]
    }
  }
}
```

---

## 🇬🇧 English <a name="en"></a>

**Navigation:** [Description](#desc-en) | [Features](#features-en) | [Usage](#use-en) | [Parameters](#params-en) | [Output Example](#examples-en) | [🇫🇷 Français](#fr)

---

### 📦 **Description** <a name="desc-en"></a>

[↑ Back to menu](#en)

Log analysis tool for DevOps and data engineers:

-   🕵️ Smart error detection
-   📊 Structured JSON export
-   🚀 Optimized for files >100GB

---

### 🛠️ **Features** <a name="features-en"></a>

[↑ Back to menu](#en) | [Output Example](#examples-en)

-   Error code/category counting
-   3 message examples per type
-   Dynamic filtering (ERROR/WARNING/INFO/DEBUG)

---

### 🚀 **Usage**<a name="use-en"></a>

[↑ Back to menu](#en)

```bash
python log_analyzer.py \\
  --input /var/logs/app.log \\
  --output report.json \\
  --log-level ERROR
```

---

### ⚙️ **Parameters** <a name="params-en"></a>

[↑ Back to menu](#en)

| Option | Description | Values |
| :---------- | :-------------------- | :------------------------------ |
| `--input` | Log file path | `.log` or `.txt` file |
| `--output` | Output file name | `.json` file |
| `--log-level` | Log level to analyze | `ERROR`, `WARNING`, `INFO`, `DEBUG` |

---

### 📝 **Output Example** <a name="examples-en"></a>

[↑ Back to menu](#en)

```json
{
  "log_level": "ERROR",
  "entries": {
    "404": {
      "count": 12,
      "examples": [
        "ERROR: File not found [CODE: 404]",
        "ERROR: User profile missing [CODE: 404]",
        "ERROR: GET /nonexistent_page HTTP/1.1 [CODE: 404]"
      ]
    },
    "500": {
      "count": 8,
      "examples": [
        "ERROR: Database connection failed [CODE: 500]",
        "ERROR: Internal Server Error [CODE: 500]",
        "ERROR: API endpoint unavailable [CODE: 500]"
      ]
    }
  }
}
```

---


*"Un bon README est comme un panneau indicateur clair - il guide l'utilisateur sans confusion."* 🗺️

- French
  -> Desc
  -> Fonctionalités
  -> Utilisation
  -> Paramètres

- English 
  -> Desc
  -> Functionality
  -> Using
  -> Parameters

-> exemple ouput


#### FRENCH VERSION
# LogAnalyzer Pro+ 🚀  
**Analyse de logs haute performance avec filtres dynamiques**  

---

### 🔍 **Nouvelles Fonctionnalités**  
- Choix du **type de log** (ERROR/WARNING/INFO/DEBUG) via CLI  
- Détection **dynamique de motifs** personnalisables  
- Support des **formats de logs variés** (Nginx, Apache, custom)  

---

### 🛠️ **Utilisation**  
```bash  
python log_analyzer.py \  
  --input /var/logs/app.log \  
  --output rapport.json \  
  --log-level ERROR  # ou WARNING/INFO/DEBUG  
```
Paramètres
Option	Description	Valeurs Possibles
--input	Chemin du fichier de logs	Tout fichier texte
--output	Chemin du rapport JSON	.json
--log-level	Type de logs à analyser	ERROR, WARNING, INFO, DEBUG

###################################################
---------------------------------------------------
###################################################

#### ENGLISH VERSION
# LogAnalyzer Pro+ 🚀  
**High performance log analysis with dynamic filters**  

---

### 🔍 **New Features** (ERROR/WARNING/DEBUG via CLIP)  
- Choice of **log type** (ERROR/WARNING/INFO/DEBUG) via CLI  
- Dynamic **pattern detection** (customisable)  
- Support for various log formats** (Nginx, Apache, custom)  

---

### 🛠️ **Use**  
```bash 
python log_analyzer.py  
  --input /var/logs/app.log \  
  --output rapport.json \  
  --log-level ERROR # or WARNING/INFO/DEBUG  
```
Parameters
Option Description Possible values
```
--input Log file path Any text file
--output JSON .json report path
--log-level Type of log to analyse ERROR, WARNING, INFO, DEBUG
```

🧩 Exemples d'Entrées Supportées / Examples entry accepted from log
```bash
# Format ERROR 
[2023-10-05] ERROR: Database connection failed [CODE: 500]  
```
```bash
# Format WARNING  
WARNING 2023-10-05T14:22:01 User quota exceeded (user_id=123)  
```
```bash
# Format INFO  
INFO 2023-10-05 Server started on port 8080  
```

EXEMPLES / EXAMPLES :
```json
{
  "log_level": "ERROR",
  "entries": {
    "404": {
      "count": 3,
      "examples": [
        "ERROR: File not found [CODE: 404]",
        "ERROR: User profile missing [CODE: 404]"
      ]
    },
    "500": {
      "count": 2,
      "examples": [
        "ERROR: Database connection failed [CODE: 500]"
      ]
    }
  }
}
```

***"Un bon script ne se contente pas de compter - il raconte une histoire."* 📖💻**

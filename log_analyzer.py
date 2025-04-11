"""
LogAnalyzer Pro++ - Analyse de logs avec récupération des messages
Nouveautés : Comptage + liste des messages uniques avec exemples
"""
import re
from typing import Dict, Generator, List
from pathlib import Path
import json
from functools import lru_cache
import argparse
from collections import defaultdict

class LogAnalyzer:
    def __init__(self, log_path: Path, log_level: str = "ERROR"):
        self.log_path = log_path
        self.log_level = log_level.upper()
        # Regex dynamique selon le niveau de log
        if self.log_level == "ERROR":
            self.log_pattern = re.compile(r"ERROR: (.*?) \[CODE: (\d{3})\]")  # Capture message + code
        else:
            self.log_pattern = re.compile(rf"{self.log_level}:?\s(.*?)(?=\s\(|$)")  # Capture message seul

    @lru_cache(maxsize=128)
    def _compile_regex(self, pattern: str) -> re.Pattern:
        return re.compile(pattern)

    def _stream_logs(self) -> Generator[str, None, None]:
        with self.log_path.open('r', encoding='utf-8') as f:
            for line in f:
                yield line.strip()

    def analyze(self) -> Dict[str, Dict]:
        counts = defaultdict(lambda: {'count': 0, 'examples': []})
        for line in self._stream_logs():
            if match := self.log_pattern.search(line):
                # Extraction des composants
                if self.log_level == "ERROR":
                    message, code = match.groups()
                    key = code
                else:
                    message = match.group(1).strip()
                    key = message.split('(')[0].strip()  # Nettoyage des paramètres

                # Mise à jour du comptage et des exemples
                counts[key]['count'] += 1
                if len(counts[key]['examples']) < 3:  # Garde 3 exemples max
                    counts[key]['examples'].append(message)
        return dict(counts)

    def save_report(self, output_path: Path) -> None:
        report = {
            'log_level': self.log_level,
            'entries': self.analyze(),
            '_meta': 'Généré par LogAnalyzer Pro++ (github.com/votre_user)'
        }
        with output_path.open('w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analyseur de logs pro++')
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path, default=Path('report.json'))
    parser.add_argument('--log-level', type=str, 
                       choices=['ERROR', 'WARNING', 'INFO', 'DEBUG'], 
                       default='ERROR')
    args = parser.parse_args()

    if not args.input.exists():
        raise FileNotFoundError(f"Fichier {args.input} introuvable")

    analyzer = LogAnalyzer(args.input, args.log_level)
    analyzer.save_report(args.output)
    print(f"Rapport {args.log_level} généré : {args.output}")

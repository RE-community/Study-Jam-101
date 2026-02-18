
"""
Formatter CSV Glosarium ke Tabel Markdown
Dibuat untuk mengotomatisasi pembuatan tabel glosarium yang rapi dan terurut.
"""

import csv
import sys
import argparse

def csv_to_markdown(csv_file, output_file=None, sort_ignore_case=True):
    """
    Membaca file CSV dengan kolom 'Term' dan 'Definition',
    mengurutkan berdasarkan Term, lalu menghasilkan tabel Markdown.

    Args:
        csv_file (str): Path ke file CSV.
        output_file (str, optional): Jika diberikan, tabel ditulis ke file ini.
        sort_ignore_case (bool): Jika True, mengabaikan huruf besar/kecil saat sorting.

    Returns:
        str: String tabel Markdown.
    """
    try:
        with open(csv_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f, skipinitialspace=True)

            if 'Term' not in reader.fieldnames or 'Definition' not in reader.fieldnames:
                raise ValueError("CSV harus memiliki kolom 'Term' dan 'Definition'")
            rows = list(reader)
    except Exception as e:
        print(f"Error membaca file CSV: {e}", file=sys.stderr)
        sys.exit(1)

    if sort_ignore_case:
        rows.sort(key=lambda x: x['Term'].lower())
    else:
        rows.sort(key=lambda x: x['Term'])

    lines = ["| Term | Definition |", "|------|------------|"]
    for row in rows:
        term = row['Term'].replace('|', '\\|')  
        definition = row['Definition'].replace('|', '\\|')
        lines.append(f"| {term} | {definition} |")

    markdown = '\n'.join(lines)

    if output_file:
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(markdown)
            print(f"Tabel berhasil disimpan ke: {output_file}")
        except Exception as e:
            print(f"Error menulis file output: {e}", file=sys.stderr)
            sys.exit(1)

    return markdown

def main():
    parser = argparse.ArgumentParser(description="Ubah CSV glosarium menjadi tabel Markdown.")
    parser.add_argument('csv_file', help="File CSV input (dengan kolom Term, Definition)")
    parser.add_argument('-o', '--output', help="File output untuk tabel Markdown (opsional)")
    parser.add_argument('--case-sensitive', action='store_true',
                        help="Gunakan sorting case-sensitive (default: case-insensitive)")
    args = parser.parse_args()

    markdown = csv_to_markdown(
        args.csv_file,
        output_file=args.output,
        sort_ignore_case=not args.case_sensitive
    )

    if not args.output:
        print("\n--- Tabel Markdown ---\n")
        print(markdown)

    with open("glossary.md", "w", encoding="utf-8") as f:
        f.write(markdown)
        print("Tabel Markdown juga disimpan ke: glossary.md")

if __name__ == "__main__":
    main()
"""Read or search packaged source data. No network or file writes."""
from pathlib import Path
import argparse
import json


def records():
    path = Path(__file__).resolve().with_name("source-corpus.jsonl")
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            yield json.loads(line)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--id", help="video- followed by the original video ID")
    parser.add_argument("--query", help="Literal text search, not semantic ranking")
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--length", type=int, default=3500)
    parser.add_argument("--limit", type=int, default=8)
    args = parser.parse_args()
    if not args.id and not args.query:
        parser.error("Use --id or --query")
    if args.start < 0 or not 1 <= args.length <= 6000 or not 1 <= args.limit <= 30:
        parser.error("start >= 0; length 1..6000; limit 1..30")
    found = 0
    for record in records():
        if args.id:
            if record["source_id"] != args.id:
                continue
            full = record.pop("text")
            record.update(start=args.start, end=min(len(full), args.start + args.length),
                          characters=len(full), has_more=args.start + args.length < len(full),
                          text=full[args.start:args.start + args.length])
            print(json.dumps(record, ensure_ascii=False, indent=2))
            return
        haystack = record["title"] + "\n" + record["text"]
        if args.query.casefold() not in haystack.casefold():
            continue
        offset = record["text"].casefold().find(args.query.casefold())
        print(json.dumps({"source_id": record["source_id"], "date": record["date"],
                          "title": record["title"], "match_start": max(0, offset),
                          "excerpt": record["text"][max(0, offset - 80):max(0, offset) + 240]},
                         ensure_ascii=False))
        found += 1
        if found >= args.limit:
            return
    if args.id:
        raise SystemExit("No readable source with this ID")
    if not found:
        print("No literal match. This does not prove the topic is absent.")


if __name__ == "__main__":
    main()

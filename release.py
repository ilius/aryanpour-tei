#!/usr/bin/env python3
import argparse
import datetime
import gzip
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))


def run(cmd):
    print("+ " + " ".join(cmd), file=sys.stderr)
    subprocess.run(cmd, check=True)


def capture(cmd):
    return subprocess.run(
        cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL
    )


def last_release_tag():
    proc = capture(["gh", "release", "view", "--json", "tagName", "--jq", ".tagName"])
    return proc.stdout.strip() if proc.returncode == 0 else ""


def release_exists(tag):
    if capture(["git", "rev-parse", "-q", "--verify", f"refs/tags/{tag}"]).returncode == 0:
        return True
    return capture(["gh", "release", "view", tag]).returncode == 0


def remote_has_commit(sha):
    proc = capture(["gh", "api", f"repos/{{owner}}/{{repo}}/commits/{sha}"])
    return proc.returncode == 0


def next_tag():
    base = datetime.datetime.now(datetime.timezone.utc).strftime("%Y.%m.%d")
    tag = base
    n = 1
    while release_exists(tag):
        n += 1
        tag = f"{base}-{n}"
    return tag


def main():
    parser = argparse.ArgumentParser(
        description="Build aryanpour.tei.gz and publish a GitHub release."
    )
    parser.add_argument("--indir", default="aryanpour.parts")
    parser.add_argument("--output", default="aryanpour.tei")
    parser.add_argument("--dry-run", action="store_true", help="build but do not release")
    parser.add_argument("--force", action="store_true", help="release even without changes")
    parser.add_argument(
        "--allow-dirty", action="store_true", help="allow releasing with uncommitted changes"
    )
    args = parser.parse_args()

    os.chdir(ROOT)

    if shutil.which("gh") is None:
        raise SystemExit("gh CLI is required: https://cli.github.com/")

    if not args.allow_dirty and capture(["git", "status", "--porcelain"]).stdout.strip():
        raise SystemExit("working tree is dirty; commit changes or use --allow-dirty")

    head = capture(["git", "rev-parse", "HEAD"]).stdout.strip()

    if not args.dry_run and not remote_has_commit(head):
        raise SystemExit(
            f"HEAD {head} is not on GitHub; push the branch before releasing "
            "(e.g. git push origin main)"
        )

    last_tag = last_release_tag()
    if last_tag:
        commits = capture(["git", "rev-list", "--count", f"{last_tag}..HEAD"]).stdout.strip()
        changed = int(commits or 0) > 0
    else:
        changed = True

    if not changed and not args.force:
        print(f"No changes since {last_tag}; nothing to release.")
        return

    run([sys.executable, "combine_tei.py", "--indir", args.indir, "--output", args.output])

    gz_path = args.output + ".gz"
    with open(args.output, "rb") as src, gzip.open(gz_path, "wb", compresslevel=9) as dst:
        shutil.copyfileobj(src, dst)

    tag = next_tag()

    if args.dry_run:
        print(f"Built {gz_path}; would create release {tag} at {head}.")
        return

    notes = f"Weekly snapshot built from {head}."
    if last_tag:
        notes += f"\n\nChanges since {last_tag}."

    run(
        [
            "gh",
            "release",
            "create",
            tag,
            gz_path,
            "--title",
            tag,
            "--notes",
            notes,
            "--target",
            head,
        ]
    )


if __name__ == "__main__":
    main()

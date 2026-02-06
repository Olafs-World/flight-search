# AGENTS.md

Instructions for AI agents working on this repository.

## Overview

**flight-search** is a CLI tool for searching Google Flights. Built on [fast-flights](https://github.com/AWeirdDev/flights).

## Development

### Setup

```bash
git clone https://github.com/Olafs-World/flight-search.git
cd flight-search
uv sync
```

### Running Tests

```bash
uv run pytest
uv run ruff check .
```

### Testing Locally

```bash
uv run flight-search DEN LAX --date 2025-03-01
```

## Project Structure

```
flight_search/
├── __init__.py      # Package exports
├── cli.py           # CLI entry point (argparse)
├── search.py        # Core search logic (wraps fast-flights)
tests/
├── test_cli.py      # CLI tests
├── test_search.py   # Search function tests
```

## Making a Release

1. **Bump version** in `pyproject.toml`
2. **Update CHANGELOG.md** with changes under new version header
3. **Commit**: `git commit -am "Bump version to X.Y.Z"`
4. **Tag**: `git tag vX.Y.Z`
5. **Push**: `git push && git push --tags`

CI will automatically publish to PyPI when the tag is pushed.

## Code Style

- Use `ruff` for linting
- Follow existing patterns in the codebase
- Keep CLI output user-friendly with emoji
- Support both `--output text` and `--output json`

## Dependencies

- `fast-flights` - Google Flights scraper (core dependency)
- `pytest` - Testing (dev)
- `ruff` - Linting (dev)

## Git Conventions

- Commit messages: imperative mood ("Add feature" not "Added feature")
- Co-author AI contributions: `Co-authored-by: olaf-s-app[bot] <259723076+olaf-s-app[bot]@users.noreply.github.com>`

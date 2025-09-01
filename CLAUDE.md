# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an IThome Ironman web scraper written in Python that crawls topics, titles, and links from the IThome Ironman competition and stores results in a SQLite database.

## Development Environment

- **Python Version**: 3.13 (specified in `.python-version`)
- **Package Manager**: uv (preferred over pip)
- **Dependencies**: Currently none in `pyproject.toml`, but README mentions requests, Playwright(Headless), and sqlite3

## Key Commands

### Setup and Installation
```bash
uv sync  # Install dependencies when they're added to pyproject.toml
```

### Running the Application
```bash
python main.py  # Run the main scraper
# or
uv run main.py  # Run with uv
```

## Architecture Notes

- **Entry Point**: `main.py` - Currently contains minimal boilerplate
- **Target Dependencies**: The scraper will need requests for HTTP requests, Playwright(Headless) for HTML parsing, and sqlite3 for database operations
- **Data Storage**: Results intended to be stored in SQLite format
- **Target Website**: IThome Ironman competition (https://ithelp.ithome.com.tw/2025ironman?page=)

## Current State

The project is in early initialization phase with basic project structure in place but core scraping functionality not yet implemented.
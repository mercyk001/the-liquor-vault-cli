# The Liquor Vault CLI

A command-line interface (CLI) application for browsing, selecting, and ordering fine wines and spirits from The Liquor Vault. This app manages user authentication, inventory browsing, cart management, and order placement, all from your terminal.

## Features

- User registration and login
- Browse and search the liquor collection
- Add, update, or remove items from your cart
- Place orders with delivery details
- Persistent shopping cart and user state (per session)
- Debug mode for developers

## Project Structure
- `lib/` — Main application logic and CLI modules
- `migrations/` — Database migrations (likely Alembic)
- `liquor_vault.db` — SQLite database (local app data)
- `alembic.ini` — Alembic configuration for migrations
- `Pipfile` / `Pipfile.lock` — Python dependencies


### Prerequisites

- Python 3.8+
- pip
- (Recommended) Virtual Environment



## License

MIT License. 

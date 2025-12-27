# 🚀 Hackathon II - AI-Powered Todo App (Phase I)

A sophisticated, modular todo application featuring natural language processing capabilities and persistent storage, built with Python and designed for the WSL environment.

## 🏗️ Architecture

This application follows a clean, modular architecture with distinct layers:

- **Models** (`src/models/`): Contains the `Task` data model defining the structure of todo items
- **Services** (`src/services/`): Business logic layer with `TaskManager` for CRUD operations and `StorageManager` for data persistence
- **UI** (`src/ui/`): User interface layer with `CLIInterface` for user interaction
- **Agent** (`src/agent/`): Intelligence layer with `TodoAgent` for natural language processing

## 🧠 The Intelligence Skill

The `TodoAgent` module is the core intelligence of this application, featuring:

- **Natural Language Command Parsing**: Understands commands like `add Buy groceries`, `list tasks`, `done 1`, `remove 2`
- **No External LLM Calls**: All processing happens locally using regex patterns and string matching
- **Smart Command Recognition**: Supports various command formats and provides helpful feedback

## 💾 Data Persistence

The `StorageManager` handles data persistence using JSON files:

- **JSON Storage**: Tasks are saved to and loaded from `data/tasks.json`
- **WSL Environment Optimized**: Designed specifically for WSL2/Linux environments
- **Automatic Recovery**: Loads existing tasks on application startup

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Environment**: WSL2 (Linux)
- **Development Framework**: Multi-Agent System (Spec-Kit) with specialized agents
- **Server**: MCP GitHub Server

## ▶️ How to Run

1. Clone the repository
2. Navigate to the project directory
3. Run the application:

```bash
python3 -m src.todo_app
```

## 🏗️ Development Process

This project was built using a **Multi-Agent Development System** powered by Spec-Kit:

- **Specialized Agents**: Used dedicated agents for business logic and persistence
- **Spec-Driven Development**: Followed structured specifications throughout development
- **Modular Design**: Implemented clean separation of concerns between components
- **AI-Assisted Development**: Leveraged intelligent agents for code generation and maintenance

## 📁 Project Structure

```
src/
├── todo_app.py          # Main application entry point
├── agent/               # Intelligence layer
│   └── todo_agent.py    # Natural language command processor
├── models/              # Data models
│   └── task.py          # Task data model
├── services/            # Business logic
│   ├── task_manager.py  # Task CRUD operations
│   └── storage_manager.py # Data persistence
└── ui/                  # User interface
    └── cli_interface.py # Command-line interface
```

## 🎯 Features

- ✅ Add, update, delete, and mark tasks as complete
- ✅ Natural language command processing
- ✅ Persistent storage in JSON format
- ✅ Clean, intuitive command-line interface
- ✅ Modular, extensible architecture

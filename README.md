# AI Coding Agent

A command-line AI coding agent built with Python as part of the [Boot.dev](https://www.boot.dev/) Backend Developer learning path.

The project explores how Large Language Models (LLMs) can interact with a local codebase through function calling, allowing an AI agent to inspect files, execute Python scripts, modify code, and complete multi-step tasks.

Instead of simply generating text responses, the agent can select and execute tools, process their results, and continue working toward the user's request.

## Features

* **LLM Integration:** Connects to language models through the OpenRouter API using the OpenAI Python SDK.
* **Tool / Function Calling:** Allows the model to select and execute predefined functions.
* **File System Exploration:** Lists files and directories within a designated working directory.
* **File Reading:** Reads source code and other files to understand the project.
* **Python Execution:** Runs Python scripts and captures their output.
* **File Modification:** Creates or updates files based on the requested task.
* **Multi-Step Agent Loop:** Supports multiple tool calls within a single user request.
* **Context Management:** Maintains conversation history, including tool calls and their results.
* **Verbose Mode:** Provides additional information about tool execution for debugging.

## Tech Stack

| Technology              | Purpose                                                         |
| ----------------------- | --------------------------------------------------------------- |
| Python                  | Core application logic                                          |
| OpenRouter API          | Access to LLMs                                                  |
| OpenAI Python SDK       | Model communication and tool calling                            |
| python-dotenv           | Environment variable management                                 |
| Python Standard Library | File operations, subprocess execution, and CLI argument parsing |

## How It Works

The agent follows an iterative execution process:

1. The user submits a task through the command line.
2. The application sends the request and system instructions to the language model.
3. The model determines whether it needs to use an available tool.
4. If a tool is requested, the application executes the corresponding Python function.
5. The tool result is added to the conversation history and sent back to the model.
6. The process continues until the model produces a final response or the maximum iteration limit is reached.

The agent supports up to 20 iterations per request.

### Agent Workflow

```text
           User Request
                |
                v
         AI Agent (CLI)
                |
                v
          LLM via API
                |
                v
         Tool Required?
           /       \
         Yes        No
          |          |
          v          v
     Execute Tool   Final Response
          |
          v
     Collect Result
          |
          v
    Update Conversation
          |
          +------> LLM
```

## Available Tools

The agent provides four tools that the language model can call.

| Tool               | Description                                               |
| ------------------ | --------------------------------------------------------- |
| `get_files_info`   | Lists files and directories within the working directory. |
| `get_file_content` | Reads the contents of a specified file.                   |
| `run_python_file`  | Executes a Python file and returns its output.            |
| `write_file`       | Creates a new file or overwrites an existing file.        |

These tools allow the agent to interact with a local Python project rather than relying exclusively on the model's existing knowledge.

### Working Directory

The agent is currently configured to operate within the `calculator` directory.

Tool implementations include path validation to restrict file access and execution to the configured working directory.

The execution environment should still be treated as trusted development space because the agent can run Python code and modify files.

## Getting Started

### Prerequisites

Before running the project, make sure you have:

* Python 3.14 or later
* Git
* An OpenRouter API key
* An internet connection for API requests

### 1. Clone the Repository

```bash
git clone https://github.com/Tladadweh/ai-agent.git

cd ai-agent
```

### 2. Install Dependencies

This project uses `pyproject.toml` to define its Python dependencies.

Using `uv`:

```bash
uv sync
```

Alternatively, create a virtual environment and install the dependencies using pip:

```bash
python -m venv .venv
```

Activate the virtual environment.

Windows:

```powershell
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install .
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

Replace the placeholder with your own OpenRouter API key.

The application loads this variable using `python-dotenv`.

**Security:** Never commit your actual API key or `.env` file to GitHub.

### 4. Run the Agent

The current implementation operates on the local `calculator` directory.

Make sure this directory exists and contains the Python project you want the agent to work with.

Run the application by passing a task as a command-line argument:

```bash
python main.py "Explain how the calculator works"
```

To enable verbose output:

```bash
python main.py "Explain how the calculator works" --verbose
```

Verbose mode displays additional information about the tools being called and their results.

## Example Use Cases

The agent can be used to explore and work with a local Python project.

**Understanding a codebase**

```bash
python main.py "Explain how the calculator works"
```

**Inspecting project files**

```bash
python main.py "List the files in this project and explain their purpose"
```

**Running Python code**

```bash
python main.py "Run main.py and explain the output"
```

**Modifying a Python project**

```bash
python main.py "Add a new function to the calculator"
```

These examples illustrate the agent's intended capabilities. Actual results depend on the model's generated tool calls and the contents of the working directory.

## Project Structure

```text
ai-agent/
|
|-- main.py
|-- prompts.py
|-- call_function.py
|-- pyproject.toml
|
|-- functions/
|   |-- get_files_info.py
|   |-- get_file_content.py
|   |-- run_python_file.py
|   |-- write_file.py
|
|-- calculator/
|   |-- ... Python project files
|
|-- .env
```

**Main components:**

* `main.py`: Entry point responsible for CLI arguments, API communication, conversation history, and the agent execution loop.
* `prompts.py`: Defines the system instructions and available tool descriptions.
* `call_function.py`: Maps model-requested function calls to their corresponding Python implementations.
* `functions/`: Contains the individual tool implementations.
* `calculator/`: Serves as the agent's configured working directory.
* `pyproject.toml`: Defines project metadata and Python dependencies.
* `.env`: Stores the API key locally and should not be committed to version control.

## Key Learning Outcomes

Building this project provided hands-on experience with:

* Integrating LLM APIs into Python applications.
* Designing and implementing function-calling workflows.
* Managing conversation context across multiple interactions.
* Connecting language models to local tools and external functionality.
* Implementing iterative agent execution.
* Handling file operations and subprocess execution.
* Working with environment variables and API credentials.
* Understanding the importance of execution boundaries when allowing AI agents to interact with local files.

## Project Background

This project was developed as part of the **Build an AI Agent in Python** guided project in the Boot.dev Backend Developer learning path.

It demonstrates how a language model can be integrated with application-level tools to perform tasks beyond generating text.

The project is intended for learning and experimentation rather than production deployment.

## Author

**Tariq Ladadweh**

GitHub: [@Tladadweh](https://github.com/Tladadweh)

## Acknowledgments

Built as part of the [Boot.dev Backend Developer learning path](https://www.boot.dev/).

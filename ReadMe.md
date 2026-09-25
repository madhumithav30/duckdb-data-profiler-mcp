# Local Data Profiler & Analytics MCP Server 

A Model Context Protocol (**MCP**) server that allows Large Language Models (like Claude Desktop or Cursor) to profile local datasets and run high-speed vectorized analytical SQL using **DuckDB** over **STDIO** — 100% locally with zero cloud or API costs.

---

## Tools Exposed

1. **`profile_dataset(file_path: str)`**: Computes statistical summaries on any local `.parquet` or `.csv` file (null percentages, column types, min, max, and unique counts).
2. **`run_sql(query: str)`**: Executes analytical SQL directly against files using DuckDB's in-process vectorized engine without loading them into an external database.

---

## Quickstart

### 1. Clone & Set Up Virtual Environment

```bash
git clone https://github.com/<YOUR_GITHUB_USERNAME>/local-data-mcp.git
cd local-data-mcp

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Generate Sample Data

```bash
python generate_data.py
```

### 3. Validate with MCP Inspector

Test the tools interactively over STDIO:

```bash
npx @modelcontextprotocol/inspector .venv/bin/python server.py
```

Open the URL displayed (`http://localhost:5173`) in your browser to run queries and profile datasets.

---

## Connecting to Claude Desktop

Add the server to your Claude Desktop config file:

* **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
* **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

### 💡 Quick Tip (macOS / Linux)
Run this command in your terminal inside the project directory to output your exact, copy-pasteable JSON block:

```bash
echo "{\"mcpServers\": {\"local-data-profiler\": {\"command\": \"$(pwd)/.venv/bin/python\", \"args\": [\"$(pwd)/server.py\"]}}}"
```

### Manual Configuration

**macOS / Linux:**
```json
{
  "mcpServers": {
    "local-data-profiler": {
      "command": "<ABSOLUTE_PATH_TO_REPO>/.venv/bin/python",
      "args": ["<ABSOLUTE_PATH_TO_REPO>/server.py"]
    }
  }
}
```

**Windows:**
```json
{
  "mcpServers": {
    "local-data-profiler": {
      "command": "C:\\path\\to\\local-data-mcp\\.venv\\Scripts\\python.exe",
      "args": ["C:\\path\\to\\local-data-mcp\\server.py"]
    }
  }
}
```

Restart Claude Desktop, and you will see the 🔨 icon.

---

## 💡 Example Prompts to Try in Claude

* *"Profile `sample_orders.parquet` and explain the distribution of order amounts."*
* *"Write and execute a SQL query to calculate total revenue grouped by order status."*
* *"Are there any null values in `sample_orders.parquet`?"*

---

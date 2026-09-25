import duckdb
# MCP 2.x import
from mcp.server.mcpserver import MCPServer

# Initialize with MCPServer instead of FastMCP
mcp = MCPServer("Local Data Profiler")

@mcp.tool()
async def profile_dataset(file_path: str) -> str:
    """
    Profiles a local Parquet or CSV file and returns column statistics, 
    null counts, data types, and min/max values.
    """
    try:
        con = duckdb.connect()
        df_summary = con.execute(f"SUMMARIZE SELECT * FROM '{file_path}'").df()
        filtered = df_summary[["column_name", "column_type", "null_percentage", "min", "max", "approx_unique"]]
        return f"Data Profile for: {file_path}\n\n" + filtered.to_string(index=False)
    except Exception as e:
        return f"❌ Error profiling file: {str(e)}"

@mcp.tool()
async def run_sql(query: str) -> str:
    """
    Executes analytical SQL on local files using DuckDB.
    """
    try:
        con = duckdb.connect()
        result_df = con.execute(query).df()
        if len(result_df) > 50:
            preview = result_df.head(50).to_string(index=False)
            return f"Query returned {len(result_df)} rows. Showing first 50:\n\n{preview}"
        return result_df.to_string(index=False)
    except Exception as e:
        return f"❌ SQL Error: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
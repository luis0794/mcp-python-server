import os
import subprocess
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("terminal")
DEFAULT_WORKSPACE = os.path.expanduser("~/mcp/servers/mcp-python-server")

@mcp.tool()
async def run_command(command: str) -> str:
    """Run a command in the terminal
    
    Args:
        command: The command to run in the terminal

    Returns:
        The output of the command or an error message if the command fails
    """
    result = subprocess.run(command, shell=True, cwd=DEFAULT_WORKSPACE, capture_output=True, text=True)
    return result.stdout

if __name__ == "__main__":
    mcp.run(transport="stdio")
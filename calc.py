from mcp.server.fastmcp import FastMCP
mcp = FastMCP("calc-mcp")
@mcp.tool()
def add(a: int|float, b: int|float) -> int|float:
    """Add two numbers."""
    return a + b
@mcp.tool()
def subtract(a: int|float, b: int|float) -> int|float:
    """Subtract two numbers."""
    return a - b    
@mcp.tool()
def multiply(a: int|float, b: int|float) -> int|float:
    """Multiply two numbers."""
    return a * b    
@mcp.tool()
def divide(a: int|float, b: int|float) -> float:
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b   
@mcp.resource(uri="data://operations")     
def operations() -> list[str]:
    """List of available operations."""
    return ["add", "subtract", "multiply", "divide"]    
if __name__ == "__main__":
    mcp.run(transport="stdio")   
from mcp.server.fastmcp import FastMCP
#creating a server
mcp=FastMCP("hello-mcp")
@mcp.tool()
def add(a:int|float,b:int|float)->int|float:
    """
   this metho adds two numbers
    args:
    a(int|float): first number
    b(int|float): second number
    returns:
    int|float: sum of two numbers
    """
    return a+b
if __name__ == "__main__":
 mcp.run(transport="stdio")

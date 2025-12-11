from starlette.applications import Starlette
from starlette.routing import Mount,Host
from mcp.server.fastmcp import FastMCP
mcp=FastMCP("sse-demo")
@mcp.tool()
def add(x:int,y:int)->int:
    """
    Docstring for add
    
    :param x: Description
    :type x: int
    :param y: Description
    :type y: int
    :return: Description
    :rtype: int
    """
    return x+y
@mcp.tool()
def echo(message:str)->str:
    """
    Docstring for echo
    
    :param message: Description
    :type message: str
    :return: Description
    :rtype: str
    """
    return f"you said: {message}"

app=Starlette(routes=[
    Mount("/",app=mcp.sse_app())

])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="localhost",port=8000)

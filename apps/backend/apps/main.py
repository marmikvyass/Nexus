from fastapi import FastAPI
from pydantic import BaseModel

from apps.execution.executor import execute_tool

app = FastAPI(
    title='Nexus',
    description='Personal AI Operating System',
    version='0.1.0'
)


class ToolRequest(BaseModel):
    tool: str
    arguments:dict = {}


@app.get('/')
async def root():
    return {
        'name' : 'NEXUS',
        'message' : 'Personal AI Operating System',
        'status' : 'Online',
        'version' : '0.1.0'
    }

@app.get('/health')
async def health():
    return{
        'status' : 'Healthy'
    }

@app.post('/tools/execute')
async def execute(request: ToolRequest):
    return execute_tool(
        request.tool,
        request.arguments,
    )
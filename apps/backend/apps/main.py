from fastapi import FastAPI

app = FastAPI(
    title='Nexus',
    description='Personal AI Operating System',
    version='0.1.0'
)

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
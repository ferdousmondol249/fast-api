from fastapi import FastAPI

app=FastAPI()


@app.get('/')

def root():
    return {
        'data':{
            'name':'nitish',
            'age':18,
            'occupation': 'student'
        }
    }


@app.get('/about')
def about():
    return {
        'data':{
            'This is simply about page '
        }
    }


import requests


BASE_URL = (
    "http://127.0.0.1:8000"
)

def ask_question(
        session_id,
        query
):

    response = requests.get(

        f"{BASE_URL}/chat/",

        params={

            "session_id":
            session_id,

            "query":
            query
        }
    )

    return response.json()

def get_history(
        session_id
):

    response = requests.get(

        f"{BASE_URL}/history/",

        params={
            "session_id":
            session_id
        }
    )

    return response.json()

def upload_pdf(
        uploaded_file,
        session_id
):
    print("UPLOAD SESSION ID:", session_id)

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file,
            "application/pdf"
        )
    }

    response = requests.post(
        f"{BASE_URL}/upload/",
        files=files,
        data={
            "session_id": session_id
        }
    )
    print("Status:", response.status_code)
    print("Response:", response.text)

    if response.status_code != 200:

        return {
            "error": response.text
        }


    return response.json()

def get_sessions():
    response = requests.get(
        f"{BASE_URL}/history/sessions"
    )
    return response.json()

def stream_answer(
        session_id,
        query
):

    response = requests.get(
        f"{BASE_URL}/chat/stream",
        params={
            "session_id": session_id,
            "query": query
        },
        stream=True
    )

    return response

def create_session(
        session_id
):

    requests.post(

        f"{BASE_URL}/history/create",

        params={

            "session_id":
            session_id
        }
    )

def rename_chat(
        session_id,
        title
):

    requests.put(

        f"{BASE_URL}/history/rename",

        params={

            "session_id":
            session_id,

            "title":
            title
        }
    )
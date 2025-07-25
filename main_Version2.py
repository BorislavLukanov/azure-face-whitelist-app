import os
import requests
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

AZURE_FACE_ENDPOINT = os.getenv("AZURE_FACE_ENDPOINT")
AZURE_FACE_KEY = os.getenv("AZURE_FACE_KEY")
PERSON_GROUP_ID = "whitelist-group"

app = FastAPI(title="Azure Face Recognition Whitelist App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def detect_face(image_bytes):
    url = f"{AZURE_FACE_ENDPOINT}/face/v1.0/detect"
    headers = {
        'Ocp-Apim-Subscription-Key': AZURE_FACE_KEY,
        'Content-Type': 'application/octet-stream'
    }
    params = {'returnFaceId': 'true'}
    response = requests.post(url, params=params, headers=headers, data=image_bytes)
    response.raise_for_status()
    faces = response.json()
    if faces:
        return faces[0]['faceId']
    return None

def identify_face(face_id):
    url = f"{AZURE_FACE_ENDPOINT}/face/v1.0/identify"
    headers = {
        'Ocp-Apim-Subscription-Key': AZURE_FACE_KEY,
        'Content-Type': 'application/json'
    }
    json_data = {
        'personGroupId': PERSON_GROUP_ID,
        'faceIds': [face_id],
        'maxNumOfCandidatesReturned': 1,
        'confidenceThreshold': 0.7
    }
    response = requests.post(url, headers=headers, json=json_data)
    response.raise_for_status()
    results = response.json()
    if results and results[0]['candidates']:
        return True
    return False

@app.post("/recognize")
async def recognize(file: UploadFile = File(...)):
    image_bytes = await file.read()
    face_id = detect_face(image_bytes)
    if not face_id:
        return {"result": "disapproved", "reason": "No face detected"}
    is_approved = identify_face(face_id)
    return {"result": "approved" if is_approved else "disapproved"}

# Placeholder for enrollment endpoint (add face to whitelist)
@app.post("/enroll")
async def enroll(file: UploadFile = File(...), person_name: str = "Person"):
    """Enroll a new face into the whitelist person group."""
    # See README for full enrollment instructions (Azure Face API person group management)
    return {"status": "enrollment endpoint not fully implemented"}
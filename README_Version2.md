# Azure Face Recognition Whitelist App

## Overview

This app allows you to upload ("enroll") images of approved faces to a whitelist. It recognizes faces from smart home camera images, and returns "approved" if the face matches the whitelist, "disapproved" otherwise.

Runs as a FastAPI backend, designed for Azure (App Service/Functions), leveraging Azure Face API.

---

## Features

- **Whitelist Enrollment**: Add faces of approved individuals.
- **Recognition Endpoint**: Receives new camera images and checks for whitelist match.
- **Azure Face API Integration**: Uses Microsoft Cognitive Services for recognition.

---

## How It Works

1. **Enroll Faces**:
   - Upload images of allowed persons (prepare via API or Azure Portal).
   - Images are stored in Azure Blob Storage and registered in Azure Face API as a "Person Group".

2. **Recognition**:
   - Cameras send images to `/recognize` endpoint.
   - App checks with Azure Face API if any detected face matches the whitelist.
   - Returns JSON: `{ "result": "approved" }` or `{ "result": "disapproved" }`.

---

## Setup

### Prerequisites

- Azure subscription
- Azure Cognitive Services (Face API) resource
- Azure Blob Storage (for storing whitelist images)
- Python 3.8+
- `fastapi`, `uvicorn`, `requests`

### Install

```bash
pip install fastapi uvicorn requests
```

### Environment Variables

Set these in your deployment environment:

- `AZURE_FACE_ENDPOINT` – Example: `https://<your-region>.api.cognitive.microsoft.com`
- `AZURE_FACE_KEY` – Your Face API key

### Running Locally

```bash
uvicorn main:app --reload
```

---

## API Endpoints

### POST `/recognize`

Checks if an uploaded face matches the whitelist.

**Request**:
- `file`: Image file (form-data)

**Response**:
```json
{ "result": "approved" }
```
or
```json
{ "result": "disapproved" }
```

### POST `/enroll` (placeholder)

Designed for enrolling new whitelist faces (see below for Azure setup).

---

## Person Group Management

- Create a Person Group in Azure Face API (e.g., "whitelist-group").
- Enroll faces using Azure Face API's `/persongroups` and `/persons` endpoints, or extend the `/enroll` endpoint in this app.

See [Azure Face API docs](https://learn.microsoft.com/en-us/azure/cognitive-services/face/) for managing person groups and persons.

---

## Smart Home Camera Integration

- If your camera supports HTTP POST, configure it to send snapshots to `/recognize`.
- For RTSP streams, use a separate service (e.g., ffmpeg, OpenCV Python script) to periodically extract frames and POST them to `/recognize`.

---

## Security

- Protect endpoints with authentication in production (API keys, OAuth2, etc.)
- Restrict CORS origins to trusted sources.

---

## Our Conversation (Prompt History)

> **User:** can you build computer vision apps?  
> **Assistant:** Yes, I can help you design and build computer vision applications! ...  
> **User:** I want an app which can be loaded with photoes of faces which recognizes and approves while all others disapproves.  
> **Assistant:** Great idea! ...  
> **User:** I want it to run in azure and connect with smart home cameras  
> **Assistant:** Excellent! Here’s a plan tailored for your needs: ...  
> **User:** can you upload the code in new repository and document it including this prompts?  
> **Assistant:** Yes, I can prepare the code and documentation ...  
> **User:** do it  
> **Assistant:** Here’s how I’ll proceed...

---

## Next Steps

- Complete `/enroll` endpoint for direct whitelist management.
- Add authentication.
- Optionally build a React dashboard for face/person management.

---

## License

MIT

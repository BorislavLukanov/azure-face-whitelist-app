# Project Conversation & Prompt History

This file documents the original project idea, requirements, and the step-by-step conversation between the user and GitHub Copilot regarding this repository and its purpose.

---

## Project Idea & Requirements

- Build a face recognition app that:
  - Loads ("enrolls") photos of approved faces ("whitelist").
  - When a new face appears (via photo or camera), checks if it matches any enrolled face.
  - If match: "approved"; if not: "disapproved".
- App should run on Azure and connect with smart home cameras.

---

## Conversation History

**User:**  
can you build computer vision apps?  

**Copilot:**  
Yes, I can help you design and build computer vision applications! ...  

**User:**  
I want an app which can be loaded with photoes of faces which recognizes and approves while all others disapproves.

**Copilot:**  
Great idea! You want a face recognition app that works as follows:
- You load (enroll) photos of approved faces into the app ("whitelist").
- When a new face appears (via photo or camera), the app checks if it matches any enrolled face.
- If it matches: "approved".  
- If it doesn't match: "disapproved".

Could you clarify a few things to tailor the solution for you:
1. **Platform**: Do you want a web app, desktop app, or mobile app (Android/iOS)?
2. **Photos Source**: Should it work with live camera, uploaded images, or both?
3. **Tech Preferences**: Any preferred programming language or framework? (e.g., Python, JavaScript, React, etc.)
4. **Offline/Online**: Should it work without internet (offline)?

Once you answer, I can generate a project structure and a starter code for your face recognition app!

---

**User:**  
I want it to run in azure and connect with smart home cameras

**Copilot:**  
Excellent! Here’s a plan tailored for your needs:

**Goal:**  
A face recognition app running on Azure that connects with smart home cameras and approves/denies entry based on a whitelist of face photos.

**Architecture Overview:**  
- Azure App Service or Azure Functions for backend  
- Azure Blob Storage for storing whitelist face images  
- Azure Face API (Cognitive Services) for face detection/recognition  
- Integration with smart home cameras  
- Admin uploads whitelist faces via dashboard/API  
- Recognition endpoint returns "approved" or "disapproved"

Sample code and detailed workflow described...

---

**User:**  
can you upload the code in new repository and document it including this prompts?

**Copilot:**  
Yes, I can prepare the code and documentation for your face recognition app, including these prompts, and upload it to a new GitHub repository under your account (BorislavLukanov).

**User:**  
do it

**Copilot:**  
Here’s how I’ll proceed... (sample FastAPI app and README.md provided)

---

**User:**  
create the new repository and load the files there

**Copilot:**  
I don’t have permission to directly create a new repository in your GitHub account or upload files automatically. However, I can provide you with the exact files you need. Here’s how you can proceed:  
(instructions for uploading files and setting up the repo)

---

**User:**  
how I can download it?

**Copilot:**  
To download and use the files I provided, follow these simple steps:  
(instructions for copying/saving files, uploading, and using Git)

---

**User:**  
I've created the repository but now I 't see the upload files button

**Copilot:**  
No problem! If you’ve just created a new repository on GitHub and don’t see the "Upload files" button, it’s usually because the repository is empty and you’re looking at the quick setup page. Here’s what to do:  
(instructions for uploading files via web or Git)

---

**User:**  
how do I deploy in azure so it can be operational?

**Copilot:**  
Here’s a step-by-step guide to deploy your FastAPI app (with Azure Face API integration) to Azure and make it operational:  
(detailed Azure deployment instructions)

---

**User:**  
create a file from this prompt to upload it in the repo

**Copilot:**  
(You are reading that file now!)

---

This file serves as a transparent, chronological record of the project’s requirements and solution process.
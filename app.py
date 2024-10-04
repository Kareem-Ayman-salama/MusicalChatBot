from fastapi import FastAPI, UploadFile, HTTPException
import os

@app.post("/ask-question/")
async def ask_question(file: UploadFile):
    try:
        # Print some file information for debugging
        print(f"File name: {file.filename}")
        print(f"File content type: {file.content_type}")

        # Ensure the directory exists
        os.makedirs("/tmp", exist_ok=True)

        # Define the file location
        file_location = f"/tmp/{file.filename}"
        with open(file_location, "wb") as f:
            f.write(await file.read())

        # Process the question from the audio file
        answer, audio_response = process_audio_question(file_location)

        return {"text_answer": answer, "audio_response": audio_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

import subprocess

# Install python-multipart using subprocess
subprocess.check_call(["pip", "install", "nest_asyncio"])

import subprocess


subprocess.check_call(["pip", "install", "pydub"])

import nest_asyncio

if __name__ == "__main__":
    # Apply the patch
    nest_asyncio.apply()

    # Run the FastAPI app within the existing event loop
    uvicorn.run(app, host="0.0.0.0", port=8000)
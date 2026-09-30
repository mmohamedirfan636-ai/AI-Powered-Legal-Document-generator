from fastapi import APIRouter
from pydantic import BaseModel
from ai_core.gemini_generator import GeminiDocumentgenerator

router = APIRouter()

class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    dates: str

generator = GeminiDocumentgenerator()

@router.post("/generate")
def generate_document(request: documentRequest):
    generate_text = generator.generate_document(
    request.document_type,
    request.parties,
    request.terms,
    request.dates
    )

    return {
        "document":generated_text
    }
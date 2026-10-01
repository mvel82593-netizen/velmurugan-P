from fastapi import APIRouter, HTTPException

from backend.schemas import DocumentRequest, DocumentResponse
from backend.gemini_generator import GeminiDocumentGenerator


router = APIRouter()

generator = GeminiDocumentGenerator()


@router.post(
    "/generate",
    response_model=DocumentResponse
)
def generate_document(request: DocumentRequest):
    try:
        result = generator.generate_document(request)

        return DocumentResponse(
            document_type=request.document_type,
            content=result["content"],
            ai_generated=result["ai_generated"],
            model=result["model"]
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/documents")
def get_documents():
    return {
        "message": "Documents endpoint is working"
    }


@router.get("/health")
def health():
    return {
        "status": "ok"
    }
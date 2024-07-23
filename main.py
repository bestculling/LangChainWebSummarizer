import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain.schema import StrOutputParser
from langchain.schema.prompt_template import format_document
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import langchain 
# langchain.debug = True 
# langchain.verbose = True

load_dotenv()

# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    top_p=0.85,
    google_api_key=os.environ['GOOGLE_API_KEY']
)

# Create Prompt Templates
doc_prompt = PromptTemplate.from_template("{page_content}")
# Few-shot prompting x Role prompting
# Few-shot prompting: ตัวอย่าง prompt มีการให้ตัวอย่าง input และ output ที่ต้องการ ซึ่งเป็นลักษณะของ few-shot prompting ที่ช่วยให้โมเดลเข้าใจรูปแบบและผลลัพธ์ที่คาดหวังได้ดีขึ้น
# Role prompting: prompt นี้กำหนดบทบาทให้กับโมเดลภาษา ("ในฐานะที่คุณเป็น Prompt Engineer") เพื่อให้โมเดลเข้าใจบริบทและตอบสนองในลักษณะที่สอดคล้องกับบทบาทนั้น
# llm_prompt_template = """Write a concise summary of the following:
# "{text}"
# CONCISE SUMMARY:"""
llm_prompt_template = """
Summarize the following text concisely, focusing on the key points and main ideas:
"{text}"
CONCISE SUMMARY:
"""
llm_prompt = PromptTemplate.from_template(llm_prompt_template)

# Create Chain
stuff_chain = (
    {
        "text": lambda docs: "\n\n".join(
            format_document(doc, doc_prompt) for doc in docs
        )
    }
    | llm_prompt  
    | llm
    | StrOutputParser()
)

class SummarizeRequest(BaseModel):
    url: str
    language: str  # เพิ่ม field สำหรับภาษา

# FastAPI App
app = FastAPI()

@app.post("/summarize")
async def summarize_document(request_data: SummarizeRequest):  # รับ input เพิ่มเติม
    try:
        loader = WebBaseLoader(request_data.url)
        docs = loader.load()
        
        # ใช้ภาษาที่ผู้ใช้เลือก
        language = request_data.language  # รับภาษาจาก request

        # สรุปเนื้อหา (ปรับ Prompt ตามภาษาที่เลือก)
        if language == "th":
            llm_prompt_template = """
            สรุปข้อความต่อไปนี้อย่างกระชับ โดยเน้นที่ประเด็นสำคัญและแนวคิดหลัก:
            "{text}"
            สรุปโดยย่อ:
            """
        elif language == "en":  # หรือภาษาอื่น ๆ ที่คุณต้องการรองรับ
            llm_prompt_template = """
            Summarize the following text concisely, focusing on the key points and main ideas:
            "{text}"
            CONCISE SUMMARY:
            """
        else:
            return JSONResponse({"error": "Unsupported language"}, status_code=400)

        llm_prompt = PromptTemplate.from_template(llm_prompt_template)
        
        stuff_chain = (
            {
                "text": lambda docs: "\n\n".join(
                    format_document(doc, doc_prompt) for doc in docs
                )
            }
            | llm_prompt  
            | llm
            | StrOutputParser()
        )

        summary = stuff_chain.invoke(docs)

        return JSONResponse({"summary": summary}) 

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

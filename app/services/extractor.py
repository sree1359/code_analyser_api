from app.templates.prompt_template import template
from app.core.config import get_llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

llm = get_llm()
prompt = PromptTemplate(input_variables=["code"], template=template)
parser = JsonOutputParser()
chain = prompt | llm | parser

def extract_insights(code_chunk: str) -> dict:
    try:
        return chain.invoke({"code": code_chunk})
    except Exception as e:
        return {"error": str(e)}

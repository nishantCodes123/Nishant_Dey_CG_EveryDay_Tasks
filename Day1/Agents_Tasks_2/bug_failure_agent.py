from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from llm_config import chat_model

bug_report_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a QA Bug Reporting Specialist.
Structure the bug report using the following standard template:

1. **Summary / Title**: A clear, descriptive one-line summary of the bug.
2. **Environment & Pre-conditions**: What state the system and user must be in.
3. **Steps to Reproduce**: Detailed, numbered step-by-step instructions.
4. **Expected Result**: What should happen according to the requirements.
5. **Actual Result**: What actually happened in the defect.
6. **Severity & Priority**: Assessment of the bug impact.
7. **Evidence / Logs**: Any calculation discrepancies or error messages
"""
    ),
    (
        "human",
        "Requirement Context:\n{requirement}\n\nDefect Information:\n{defect}"
    )
])

bug_report_chain = bug_report_prompt | chat_model 


